import json
import time
import threading
from flask import Flask, render_template, Response, request, redirect, url_for, session, flash
import requests

app = Flask(__name__)
app.secret_key = 'dev-secret-key-change-in-production'

# Shared state for latest price
latest = {"price": None, "time": None}

def fetch_price_loop():
    """Background thread: poll CoinGecko for BTC price every 5 seconds."""
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {"ids": "bitcoin", "vs_currencies": "usd"}
    while True:
        try:
            resp = requests.get(url, params=params, timeout=10)
            resp.raise_for_status()
            data = resp.json()
            price = data.get("bitcoin", {}).get("usd")
            latest["price"] = price
            latest["time"] = time.time()
        except Exception:
            # keep previous value if fetch fails
            pass
        time.sleep(5)

def event_stream():
    """Generator that yields Server-Sent Events with latest price every second."""
    while True:
        payload = {"price": latest["price"], "time": latest["time"]}
        yield f"data: {json.dumps(payload)}\n\n"
        time.sleep(1)


@app.route("/")
def index():
    if not session.get("authenticated"):
        return redirect(url_for("login"))
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        password = request.form.get("password")
        if password == "test":
            session["authenticated"] = True
            flash("Hooray!", "success")
            return redirect(url_for("index"))
        else:
            flash("Incorrect password", "error")
    return render_template("login.html")


@app.route("/stream")
def stream():
    if not session.get("authenticated"):
        return Response("Unauthorized", status=401)
    return Response(event_stream(), mimetype="text/event-stream")


if __name__ == "__main__":
    # start background fetcher
    t = threading.Thread(target=fetch_price_loop, daemon=True)
    t.start()
    app.run(host="0.0.0.0", port=5000, threaded=True)
