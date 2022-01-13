from flask import redirect, render_template, request, flash
from sqlalchemy import text, func

from inventory_app import app, db
from inventory_app.database_function import create_sample_data
from inventory_app.models import Inventory


@app.route('/')
@app.route('/index', methods=['POST', 'GET'])
def index():
    items = db.session.query(Inventory).order_by(Inventory.id).all()
    return render_template('index.html', items=items)


@app.route('/add', methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        add_data(request.form['add-search-id'], request.form['add-search-name'], request.form['add-search-location'],
                 request.form['add-search-amount'])
    return redirect('/')


# helper function for add()
def add_data(id, name, location, amount):
    inventory = Inventory(id, name, location, amount)
    try:
        db.session.add(inventory)
        db.session.commit()
        return redirect('/')
    except:
        flash('There was a problem when adding information')


@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method == 'POST':
        for id in request.form.getlist('single_checkbox'):
            item_to_delete = db.session.query(Inventory).filter(Inventory.id == id).first()
            try:
                db.session.delete(item_to_delete)
                db.session.commit()
            except:
                flash('There was a problem when deleting information')
    return redirect('/')


@app.route('/update', methods=['GET', 'POST'])
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


@app.route('/search', methods=['GET', 'POST'])
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
        "SELECT * FROM inventory where (id= :id or :id = '') and (name=:name or :name = '') and (location=:location or "
        ":location = '') and (amount=:amount or :amount = '')")

    try:
        searched_items = db.engine.execute(stat,
                                           {'id': id, 'name': name, 'location': location, 'amount': amount}).fetchall()
    except:
        flash('There was a problem when fetching the result')
        redirect('/')
    return searched_items


@app.route('/sample', methods=['GET', 'POST'])
def sample():
    if request.method == 'POST':
        create_sample_data()
    return redirect('/')


@app.route('/database', methods=['POST', 'GET'])
def message_database():
    all_messages = Inventory.query.filter_by().all()
    return render_template('database.html', all_messages=all_messages)


