from flask import current_app, Blueprint, render_template

tv_blueprint = Blueprint('tv', __name__, url_prefix='/market')

@tv_blueprint.route('/<string:ticker>')
def tv(ticker):
    ticker = ticker
    return render_template("tv.html", ticker=ticker)

@tv_blueprint.route('/btc/<string:ticker>')
def tvbtc(ticker):
    ticker = ticker
    return render_template("tvbtc.html", ticker=ticker)