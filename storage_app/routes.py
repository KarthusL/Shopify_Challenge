from flask import redirect, render_template, request, flash, Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text, engine, create_engine

from storage_app import db, app
from storage_app.database import create_sample_data
# from storage_app.models.inventory import Inventory




app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'Get the offer!'
engine = create_engine('sqlite:///Inventory.db')
db = SQLAlchemy(app)
db.init_app(app)

class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(50), nullable=False)
    # Date_created = db.Column(db.DateTime, default=datetime.utcnow)
    amount = db.Column(db.Integer, nullable=False, default=0)

    def __init__(self, id, name, location, amount):
        self.id = id
        self.name = name
        self.location = location
        # self.date_created = date_created
        self.amount = amount


@app.route('/')
def index():
    items = Inventory.query.order_by(Inventory.id).all()
    return render_template('index.html', items=items)


@app.route('/add', methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        add_data(request.form['add-search-id'], request.form['add-search-name'],
                 request.form['add-search-location'],
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
                                      request.form['add-search-location'],
                                      request.form['add-search-amount'])
        return render_template('index.html', items=searched_items)
    return render_template('/')


# helper function for search
def search_items(id, name, location, amount):
    searched_items = []
    stat = text(
        "SELECT * FROM Inventory where (id=:id or :id = '') and (name=:name or :name = '') and (location=:location or "
        ":location = '') and (amount=:amount or :amount = '')")
    # try:
    conn = engine.connect()
    # except:
    #     flash('There was a problem when connecting to database')

    try:
        searched_items = conn.execute(stat, {'id': id, 'name': name, 'location': location, 'amount': amount}).fetchall()
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


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
