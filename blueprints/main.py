from flask import current_app, Blueprint, render_template
from flask import request
from urllib.request import urlopen
import json

main = Blueprint('main', __name__)

COIN_GECKO_URL = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=50'
EX_RATE_URL = 'https://api.exchangeratesapi.io/latest?base=USD&symbols=THB'
COIN_GECKO_MAKETCAP_URL = 'https://api.coingecko.com/api/v3/global'

@main.route('/')
def home():

    data = urlopen(COIN_GECKO_URL).read()
    parsed = json.loads(data)

    coinList = parsed
    thb = get_thb()
    marketcap = get_marketcap()


    return render_template("home.html", coinList=coinList, thb=thb, marketcap=marketcap)

def get_thb():
    try:
        data = urlopen(EX_RATE_URL).read()
        parsed = json.loads(data)
        thb = parsed['rates']['THB']
        return thb
    except:
        thb = 30.5
        return thb

def get_marketcap():
    try:
        data = urlopen(COIN_GECKO_MAKETCAP_URL).read()
        parsed = json.loads(data)
        marketcap = parsed
        return marketcap
    except:
        marketcap = 0
        return marketcap

