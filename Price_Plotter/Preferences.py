import yfinance as yf
import pandas as pd


def interval():
    """ Prompts for interval """
    interval = 0
    intervals = ['1m', '2m', '5m', '15m', '30m', '60m', '90m', '1h', '1d', '5d', '1wk', '1mo', '3mo']
    while interval not in intervals:
        interval = input("Interval (1m<): ")
    return interval
    
    
def period():
    """ Prompts for period """
    period = 0
    periods = ['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd']
    while period not in periods:
        period = input("Period (1d<): ")
    return period
    

def ticker(ticker_list):
    """ Prompts for ticker & checks validility"""
    ticker = input("Ticker: ")
    while ticker not in ticker_list:
        ticker = input("Ticker: ")
    ticker = yf.Ticker(f"{ticker}")
    return ticker
    