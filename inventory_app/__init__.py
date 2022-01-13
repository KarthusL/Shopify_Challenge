from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text, engine, create_engine, func

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'Get the offer!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'
db = SQLAlchemy(app)
db.init_app(app)
engines = create_engine('sqlite:///../inventory.db')
from inventory_app import routes

db.create_all()
