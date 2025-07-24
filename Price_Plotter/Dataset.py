import yfinance as yf
import numpy as np



def price_data(ticker, interval, period):
    int_pref = interval
    pd_pref = period
    data = ticker.history(period=pd_pref, interval=int_pref)
    return data
    
    
def latest_price(ticker, interval, period):
    int_pref = interval
    pd_pref = period
    latest = ticker.history(period=pd_pref, interval=int_pref)["Close"].iloc[-1]
    return latest
    
    
def update(frame, close_prices, latest, ax, times, fig):
    line, = ax.plot([], [], linewidth=0.5, c="green")
    
    """ Re-draws & Ajusts """
    line.set_data(times, close_prices)
    ax.relim()
    ax.autoscale_view()
    fig.canvas.draw()
    
    """ Adds New Data """
    times = np.append(times, frame)
    close_prices = np.append(close_prices, latest) # Adds points to array for future use

    return line,