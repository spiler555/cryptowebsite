from flask import current_app, Blueprint, render_template
import json
from flask import request
from urllib.request import urlopen
from binance.client import Client
from time import strftime

searchcoin_blueprint = Blueprint('searchcoin', __name__)

EX_RATE_URL = 'https://api.exchangeratesapi.io/latest?base=USD&symbols=THB'
BITKUB_URL = 'https://api.bitkub.com/api/market/ticker'

@searchcoin_blueprint.route('/searchcoin')
def searchcoin():
    coin = request.args.get('coin')
    if not coin:
        coin = 'BTC'

    coin_data = get_coin(coin)
    time = get_time()
    return render_template("searchcoin.html",coin_data=coin_data, time=time,coin=coin)


def get_coin(coin):
    api_key = 'YOUR_BINANCE_API_KEY'
    api_secret = 'YOUR_BINANCE_API_SECRET'
    client = Client(api_key, api_secret)

    depth = client.get_order_book(symbol='BTCUSDT')
    prices = client.get_all_tickers()
    coin = coin.upper()
    thb_rate = get_thb()

    for p in prices:
        symbol = coin + 'USDT'

        if p['symbol'] == symbol:
            
            pc = float(p['price'])
            cal = "{:0,.2f}".format((pc * thb_rate))
            coin_data = 'เหรียญ: {} ราคา: {} บาท'.format(coin,cal)
            return(coin_data)



def get_thb():
    try:
        data = urlopen(EX_RATE_URL).read()
        parsed = json.loads(data)
        thb = parsed['rates']['THB']
        return thb
    except:
        thb = 30.5
        return coin_data

def get_time():
    
    time = strftime('%I:%M:%S %p {0} %d {1} %m {2} %Y').format('วันที่','เดือน','ปี')

    return time