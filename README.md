# Real-time Bitcoin Price Tracker

A lightweight Flask application that streams live Bitcoin (BTC) price updates to your browser using Server-Sent Events (SSE). Get real-time cryptocurrency price data with a beautiful dark-themed interface.

## Features

- **Real-time Updates**: Bitcoin price refreshes automatically every second in the browser
- **Server-Sent Events (SSE)**: Efficient one-way data streaming from server to client
- **Dark Theme UI**: Modern, eye-friendly interface with custom styling
- **CoinGecko Integration**: Reliable price data from the CoinGecko public API
- **Lightweight**: Minimal dependencies, fast startup, and low resource usage
- **Background Polling**: Server fetches latest prices every 5 seconds in a separate thread

## Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

## Installation

### Clone the Repository

```bash
git clone <repository-url>
cd agent-example-20251205
```

### Install Dependencies

**On Windows (PowerShell):**
```powershell
python -m pip install -r .\requirements.txt
```

**On macOS/Linux:**
```bash
pip install -r requirements.txt
```

The application requires only two packages:
- `Flask>=2.0` - Web framework
- `requests>=2.0` - HTTP library for API calls

## Usage

### Start the Application

**On Windows (PowerShell):**
```powershell
python .\app.py
```

**On macOS/Linux:**
```bash
python app.py
```

### Access the Application

Once the server is running, open your web browser and navigate to:

```
http://localhost:5000
```

You should see a dark-themed card displaying the current Bitcoin price in USD, with automatic updates every second.

### Stop the Application

Press `Ctrl+C` in the terminal to stop the server.

## How It Works

### Architecture

1. **Background Thread**: A daemon thread continuously polls the CoinGecko API every 5 seconds to fetch the latest Bitcoin price
2. **Shared State**: The latest price and timestamp are stored in a shared dictionary accessible by all threads
3. **SSE Streaming**: When clients connect to `/stream`, they receive Server-Sent Events with price updates every second
4. **Client Updates**: The browser's EventSource API receives these events and updates the UI in real-time

### API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Main page with the Bitcoin price display |
| `/stream` | GET | Server-Sent Events endpoint for real-time price updates |

### External API

The application uses the CoinGecko public API:
- **Endpoint**: `https://api.coingecko.com/api/v3/simple/price`
- **Parameters**: `ids=bitcoin&vs_currencies=usd`
- **Rate Limiting**: 50 calls/minute (free tier)
- **No Authentication Required**

## Technical Details

### File Structure

```
agent-example-20251205/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── templates/
│   └── index.html     # Frontend HTML with embedded CSS and JavaScript
└── README.md          # This file
```

### Key Technologies

- **Flask**: Lightweight WSGI web application framework
- **Server-Sent Events (SSE)**: HTML5 standard for server-to-client streaming
- **Threading**: Python's threading module for concurrent price fetching
- **CoinGecko API**: Free cryptocurrency data API

### Configuration

The following parameters can be modified in `app.py`:

- **Fetch Interval**: `time.sleep(5)` in `fetch_price_loop()` (line 27)
- **Update Interval**: `time.sleep(1)` in `event_stream()` (line 34)
- **Host**: `host="0.0.0.0"` in `app.run()` (line 51)
- **Port**: `port=5000` in `app.run()` (line 51)

## Troubleshooting

### Port Already in Use

If you see an error like "Address already in use", another application is using port 5000. You can either:
- Stop the other application
- Change the port in `app.py` (line 51) to a different number, e.g., `port=5001`

### Connection Issues

If the browser shows "connection lost, retrying…":
- Check your internet connection (required for CoinGecko API)
- Verify the Flask server is running without errors
- Check if CoinGecko API is accessible: https://status.coingecko.com/

### Price Not Updating

If the price shows "—" or doesn't update:
- Wait up to 5 seconds for the first API fetch to complete
- Check server console for error messages
- Verify CoinGecko API is responding (might have rate limiting)

## Future Enhancements

Potential improvements for this application:

- Add support for multiple cryptocurrencies
- Implement WebSocket support as an alternative to SSE
- Add historical price charts
- Include price change indicators (up/down arrows)
- Add support for different fiat currencies (EUR, GBP, etc.)
- Implement caching to reduce API calls
- Add authentication for secure access
- Deploy to cloud platforms (Heroku, AWS, etc.)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is provided as-is for educational and demonstration purposes.

## Acknowledgments

- [CoinGecko](https://www.coingecko.com/) for providing free cryptocurrency price data
- Flask community for the excellent web framework
- Server-Sent Events specification for enabling real-time data streaming
