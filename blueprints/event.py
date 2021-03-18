from flask import current_app, Blueprint, render_template

event_blueprint = Blueprint('event', __name__)

@event_blueprint.route('/event')
def event():

    return render_template("event.html")