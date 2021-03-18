from flask import current_app, Blueprint, render_template

news_blueprint = Blueprint('news', __name__)

@news_blueprint.route('/crytonews')
def news():
    return render_template("news.html")