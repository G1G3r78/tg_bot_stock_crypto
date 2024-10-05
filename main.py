import os
#import sys

#print(sys.path)

from meme_flask import get_price, get_crypto

from flask import (Flask,
    #redirect,
    #url_for,
                   render_template,
    #session,
                   request
                   )

folder = os.getcwd()
app = Flask(__name__, template_folder=folder)


@app.route("/submit", methods=["POST"])
def submit():
    try:
        try:
            input_str = request.form["input_text"]
            print(input_str)
        except:
            input_str = " "
        try:
            input_crypto = request.form["input_crypto"]
            print(input_crypto)
        except:
            input_crypto = " "
        get_price_ = get_price(input_str.upper())
        get_crypto_ = get_crypto(input_crypto.upper())
        if get_price_ is not None:
            ticker = f"Цена покупки {get_price_[1]} на данный момент: {get_price_[0]} рублей"
            graph_json = get_price_[2]
        else:
            ticker = f"ты ввёл говно или ничё не ввёл"
            graph_json = None
        if get_crypto_ is not None:
            ticker2 = f"Цена покупки {get_crypto_[1]} на данный момент: {get_crypto_[0]} USDT"
        else:
            ticker2 = f"ты ввёл говно или ничё не ввёл"
        print(ticker, "ticker")
        print(ticker2, "ticker2")
        return render_template("index.html",
                               ticker=ticker,
                               ticker2=ticker2,
                               graph_json=graph_json
                               )
    except:
        return render_template("index.html",
                               ticker=f"ты ввёл говно",
                               graph_json=None
                               )


@app.route("/")
def main():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, use_reloader=Flask, debug=True)
