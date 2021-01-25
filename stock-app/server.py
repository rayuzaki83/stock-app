from flask import Flask
import requests

app = Flask(__name__)

API_URL = 'https://financialmodelingprep.com/api/v3/stock/real-time-price/{ticker}'

def fetch_price(ticker):
    data = requests.get(API_URL.format(ticker=ticker.upper()),
                                              params={'apikey':'8cf388916ee42fef9a4b07f87ec5c6b7'}).json()
    return data["price"]

# http://localhost:5000/stock/APPL

@app.route('/stock/<ticker>')
def stock(ticker):
    price = fetch_price(ticker)
    return "The price of {ticker} is {price}".format(ticker=ticker, price=price)

@app.route('/')
def home_page():
    return 'Try /stock/APPL'