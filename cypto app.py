import streamlit as st
import pandas as pd
import requests
from datetime import datetime
import time

# --- Page Configuration ---
st.set_page_config(page_title="Crypto Tracker", layout="wide")

# --- Title ---
st.title("📈 Crypto Tracker for Beginners")
st.markdown("Track cryptocurrency prices, trends, and more — powered by CoinGecko API.")

# --- Sidebar ---
st.sidebar.header("Configuration")

@st.cache_data(ttl=300)  # cache for 5 minutes
# Fetch list of coins
@st.cache_data
def get_coin_list():
    url = "https://api.coingecko.com/api/v3/coins/list"
    time.sleep(1.5)  # Wait 1.5 seconds between calls
    response = requests.get(url)
    return response.json()

coins = get_coin_list()
# Text input to filter coins
search_term = st.sidebar.text_input("🔍 Search coin name")

# Filter coin list by search term
filtered_coins = [coin for coin in coins if search_term.lower() in coin['name'].lower()] if search_term else coins
coin_names = [coin['name'] for coin in filtered_coins]

# Select from filtered list
selected_coin_name = st.sidebar.selectbox("Select a Cryptocurrency", coin_names)

st.sidebar.caption(f"{len(coin_names)} result(s) found")

# Get coin ID for selected name
selected_coin = next((coin for coin in coins if coin['name'] == selected_coin_name), None)
coin_id = selected_coin['id'] if selected_coin else "bitcoin"

# --- Market Data ---
st.subheader(f"📊 Current Market Data for {selected_coin_name}")

@st.cache_data
def get_market_data(coin_id):
    url = f"https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "ids": coin_id
    }
    response = requests.get(url, params=params)
    return response.json()

market_data = get_market_data(coin_id)

if market_data:
    df = pd.DataFrame(market_data)
    desired_columns = ["name", "symbol", "current_price", "market_cap", "price_change_percentage_24h"]
    available_columns = [col for col in desired_columns if col in df.columns]
if available_columns:
    st.dataframe(df[available_columns])
    st.success("Market data loaded successfully!")
else:
    st.warning("The selected coin does not have the expected market data available.")

# --- Historical Chart ---
st.subheader("📉 Price Trend Over Time")

days = st.slider("Select number of days to display:", 1, 90, 30)

@st.cache_data
def get_price_history(coin_id, days):
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart"
    params = {
        "vs_currency": "usd",
        "days": days
    }
    response = requests.get(url, params=params)
    
    return response.json()

price_data = get_price_history(coin_id, days)

if "prices" in price_data and price_data["prices"]:
    prices = pd.DataFrame(price_data["prices"], columns=["timestamp", "price"])
    prices["date"] = pd.to_datetime(prices["timestamp"], unit="ms")
    prices.set_index("date", inplace=True)
    chart_type = st.radio("Select chart type:", ["Line Chart", "Area Chart", "Bar Chart"])
    if chart_type == "Line Chart":
        st.line_chart(prices["price"])
    elif chart_type == "Area Chart":
        st.area_chart(prices["price"])
    else:
        st.bar_chart(prices["price"])
    st.info("Price history chart generated.")
else:
    st.warning("Price data not available for this coin and time range.")
    
if st.button("🔄 Reload Data"):
    st.rerun()
    
# --- Extras ---
if st.checkbox("Show raw API response"):
    st.write(price_data)
    
    
# --- Map Section ---

# Sample data
data = {
    'Exchange': ['Binance', 'Coinbase', 'Kraken', 'Bitstamp', 'KuCoin',
                 'Huobi', 'OKX', 'Crypto.com', 'Gemini', 'Bitfinex'],
    'lat': [19.3133, 37.7749, 37.7749, 51.5074, -4.6796,
            39.9042, 37.3382, 1.3521, 40.7128, 22.3193],
    'lon': [-81.2546, -122.4194, -122.4194, -0.1278, 55.4920,
            116.4074, -121.8863, 103.8198, -74.0060, 114.1694]
}

df = pd.DataFrame(data)

# Display map
st.subheader("🌍 Crypto Exchange Headquarters")
st.map(df)