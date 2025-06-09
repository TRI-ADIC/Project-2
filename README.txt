====================================
Crypto Tracker for Beginners - README
====================================

------------------------------------
ABOUT THE PROJECT
------------------------------------
Crypto Tracker for Beginners is a simple, user-friendly web app that lets users:
- View current market data for popular cryptocurrencies
- Track historical price trends over time
- See global headquarters of major crypto exchanges on a map

The app uses the CoinGecko public API to retrieve live data, and Streamlit to build an interactive interface.

------------------------------------
REQUIREMENTS
------------------------------------
To run this app, you must have:

• Python 3.8 or newer  
• pip (Python package manager)  
• Internet connection (for API access)

Python Libraries used:
- streamlit
- pandas
- requests

To install them, run:
    pip install streamlit pandas requests

------------------------------------
HOW TO RUN THE APP
------------------------------------
1. Open a terminal or command prompt.
2. Navigate to the folder containing the app file (e.g., `crypto_app.py`).
3. Run the following command:

    streamlit run crypto_app.py

4. Your default browser will open the app automatically at:
    http://localhost:8501

------------------------------------
HOW TO CLOSE THE APP
------------------------------------
To shut down the app:

1. Return to the terminal window.
2. Press CTRL + C to stop the Streamlit server.
3. Close the terminal if desired.

------------------------------------
NOTES
------------------------------------
• API data is cached for 5 minutes to avoid hitting CoinGecko rate limits.
• If you see an error like "Rate limit exceeded," wait a few minutes before reloading.
• The map shows sample exchange locations for demonstration purposes only.