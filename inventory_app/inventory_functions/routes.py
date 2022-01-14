from flask import request, redirect, flash, render_template, Blueprint
from sqlalchemy import text

from inventory_app import db
from inventory_app.inventory_functions.utils import create_sample_data
from inventory_app.models.models import Inventory

inventory_functions = Blueprint('inventory_functions', __name__)


@inventory_functions.route('/add', methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        add_data(request.form['add-search-id'], request.form['add-search-name'], request.form['add-search-location'],
                 request.form['add-search-amount'])
    return redirect('/')


# helper function for add()
def add_data(id, name, location, amount):
    if all(v is not None for v in [id, name, location, amount]):
        flash('All information is needed to create an item')
        return redirect('/')
    try:
        inventory = Inventory(id, name, location, amount)
        db.session.add(inventory)
        db.session.commit()
        return redirect('/')
    except:
        flash('There was a problem when adding information')


@inventory_functions.route('/delete', methods=['GET', 'POST'])
def delete():
    for id in request.form.getlist('single_checkbox'):
        item_to_delete = db.session.query(Inventory).filter(Inventory.id == id).first()
        try:
            db.session.delete(item_to_delete)
            db.session.commit()
        except:
            flash('There was a problem when deleting information')
    return redirect('/')


@inventory_functions.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        item_id = request.form['id'].split()[0]
        col = request.form['id'].split()[1]
        new_val = request.form['value']
        try:
            db.session.query(Inventory).filter(Inventory.id == int(item_id)).update({col: new_val})
            db.session.commit()
        except:
            flash('There was a problem when updating information')
        return new_val


@inventory_functions.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        searched_items = search_items(request.form['add-search-id'], request.form['add-search-name'],
                                      request.form['add-search-location'], request.form['add-search-amount'])
        return render_template('index.html', items=searched_items)
    return render_template('/')


# helper function for search
def search_items(id, name, location, amount):
    searched_items = []
    stat = text(
        "SELECT * FROM inventory WHERE (id=:id OR :id = '') AND (name=:name OR :name = '') and (location=:location OR :location = '') AND (amount=:amount OR :amount = '')")
    try:
        searched_items = db.engine.execute(stat,
                                           {'id': id, 'name': name, 'location': location, 'amount': amount}).fetchall()
    except:
        flash('There was a problem when fetching the result')
        redirect('/')
    return searched_items


# create sample data to the database
@inventory_functions.route('/sample', methods=['GET', 'POST'])
def sample():
    if request.method == 'POST':
        create_sample_data()
    return redirect('/')
