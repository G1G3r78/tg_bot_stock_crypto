import apimoex

import requests

import plotly.graph_objects as go
import plotly.io as pio


def get_price(tick) -> tuple[float | int, str, str] | None:
    try:
        with requests.Session() as session:
            df = apimoex.get_market_candles(session,
                                              tick,
                                              start="2014-01-01",
                                              end=None,
                                              interval=24
            )
            dates = [candle['begin'] for candle in df]
            opens = [float(candle['open']) for candle in df]
            highs = [float(candle['high']) for candle in df]
            lows = [float(candle['low']) for candle in df]
            closes = [float(candle['close']) for candle in df]

            # Create candlestick figure
            fig = go.Figure(data=[go.Candlestick(x=dates,
                                                 open=opens,
                                                 high=highs,
                                                 low=lows,
                                                 close=closes)])
            fig.update_layout(title=f'{tick} Candlestick Chart',
                              xaxis_title='Date',
                              yaxis_title='Price',
                              xaxis_rangeslider_visible=False,
                              paper_bgcolor="rgba(0, 234, 255, .2)",  # Set paper background color
                              plot_bgcolor="rgba(255, 255, 255, .5)",
                              font=dict(family="Arial", size=18, color="white"),
            )   # Set plot area background color

            # Add rounded corners (border) to the figure
            fig.update_shapes(
                [
                dict(type="rect",
                     x0="2024-09-01",  # Start of the x-axis
                     x1=dates[-1],     # End of the x-axis
                     y0=min(lows),     # Minimum low price
                     y1=max(highs),    # Maximum high price
                     line=dict(color="rgba(255,255,255,0)"),  # Invisible border
                     fillcolor="rgba(0, 0, 0, 0.1)",  # Slightly transparent background
                     layer="below")
                ]
            )

            # Convert the figure to JSON
            graph_json = pio.to_json(fig)

        return df[-1]["close"], tick, graph_json
    except Exception as e:
        print(f"An error occurred: {e}")  # Log the error for debugging
        return None


def get_crypto(tick) -> tuple[float | int, str] | None:
    or_url = "https://api.binance.com/api/v3/ticker/price?symbol="
    or_url = or_url + tick + "USDT"
    try:
        responce = requests.get(or_url)
        responce.json()
        crypto = round(
            float(
                responce.json()["price"]
            ), 4
        )
        return crypto, tick
    except:
        return None
