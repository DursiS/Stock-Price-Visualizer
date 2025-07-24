""" Outside Modules """
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import yfinance as yf
import time
from functools import partial

""" Inside Modules """
import Dataset
from Dataset import update
import Preferences
from Tickers import ticker_list


""" Calling Upon Initial Data """
ticker = Preferences.ticker(ticker_list)
interval = Preferences.interval()
period = Preferences.period()

latest = Dataset.latest_price(ticker, interval, period)
data = Dataset.price_data(ticker, interval, period)
symbol = ticker.ticker

close_prices = data["Close"].to_numpy() # X-axis: price
times = data.index.to_pydatetime()      # Y-axis: time



""" Pyplot Settings """
global ax
fig, ax = plt.subplots(figsize=(10, 5))

fig.patch.set_facecolor('#1e1e1e') #Background
ax.set_facecolor('#2c2c2c') # Plot Area

ax.spines['bottom'].set_color('white')
ax.spines['left'].set_color('white')
ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='white')
ax.set_title(f"Ticker: {symbol}", color='white')
ax.set_ylabel("Price ($)", color='white')
ax.set_xlabel(f"Timeframe ({interval})", color='white')
ax.plot(times, close_prices, linewidth=0.5, c="green")


""" Plots & Auto-Updates """
update_partialed = partial(update,  # Sets propositional arguments for update
    close_prices=close_prices,
    times=times,
    fig=fig,
    ax=ax,
    latest=latest
    )

ani = animation.FuncAnimation(  # Applies the update function to the graph every 60sec
    fig, 
    update_partialed,
    interval=60000, 
    cache_frame_data=False
    )

plt.show()









