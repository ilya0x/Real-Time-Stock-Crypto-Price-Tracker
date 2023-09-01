import yfinance as yf
from flask import Flask, render_template, request, jsonify

# for charts
import pandas as pd
import numpy as np
import plotly.express as px

app = Flask(__name__, template_folder='templates')


# Rendering the index.html page
@app.route('/')
def index():
    return render_template('index.html')

# Getting stock / crypto data from Yahoo Finance
@app.route('/get_stock_data', methods=['POST'])
def get_stock_data():
    ticker = request.get_json()['ticker']
    data = yf.Ticker(ticker).history(period='1y')
    return jsonify({'currentPrice': data.iloc[-1].Close,
                    'openPrice': data.iloc[-1].Open})

'''
ADD: CHARTS:
1. Stock Price Charts - last 12 months & 10 years

@app.route('/get_stock_price_chart', methods=['POST'])
def get_stock_price_chart():
    ticker = request.get_json()['ticker']
    data = yf.Ticker(ticker).history(period='1y') # change to data-1y when adding data-10y
    # data-10y = yf.Ticker(ticker).history(period='10y')
    df = pd.DataFrame(data, columns=['Date', 'Close'])
    df['Date'] = pd.to_datetime(df['Date'])
    fig = px.line(df, x='Date', y='Close')
    return fig.to_json()
'''

if __name__ == '__main__':
    app.run(debug=True)

