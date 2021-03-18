from flask import Flask, render_template
from blueprints.main import main
from blueprints.news import news_blueprint
from blueprints.searchcoin import searchcoin_blueprint
from blueprints.event import event_blueprint
from blueprints.tradingview import tv_blueprint
from flask_sqlalchemy import SQLAlchemy
from models import db,Student

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///student.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.before_first_request
def create_table():
    db.create_all()


app.register_blueprint(main)
app.register_blueprint(news_blueprint)
app.register_blueprint(searchcoin_blueprint)
app.register_blueprint(event_blueprint)
app.register_blueprint(tv_blueprint)

@app.route('/about')
def about():
    student = Student.query.all()
    return render_template('about.html', student=student)

if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=8000)