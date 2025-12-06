# Real-time Bitcoin Price (Flask + SSE)

This small Flask app streams the current Bitcoin price (USD) to the browser using Server-Sent Events (SSE). It polls CoinGecko's public API every 5 seconds and the client receives updates in real time.

Quick start (PowerShell):

```powershell
python -m pip install -r .\requirements.txt
python .\app.py
```

Open `http://localhost:5000` in your browser.

Notes:
- Uses CoinGecko public API: `https://api.coingecko.com/api/v3/simple/price`
- SSE endpoint: `/stream`
- Poll interval: 5s (server-side)

If you want WebSockets instead, I can change the implementation to use `flask-socketio`.
