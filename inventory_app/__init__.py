from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'Get the offer!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'
db = SQLAlchemy(app)
db.init_app(app)
engines = create_engine('sqlite:///../inventory.db')

from inventory_app.inventory_functions.routes import inventory_functions
from inventory_app.main.routes import main

app.register_blueprint(inventory_functions)
app.register_blueprint(main)

db.create_all()
