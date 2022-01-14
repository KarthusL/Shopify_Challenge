from flask import render_template, request, Blueprint

from inventory_app import db
from inventory_app.models.models import Inventory

main = Blueprint('main', __name__)


@main.route('/')
@main.route('/index', methods=['POST', 'GET'])
def index():
    items = db.session.query(Inventory).order_by(Inventory.id).all()
    return render_template('index.html', items=items)


# Page for checking all data in database
@main.route('/database', methods=['POST', 'GET'])
def message_database():
    all_messages = Inventory.query.filter_by().all()
    return render_template('database.html', all_messages=all_messages)
