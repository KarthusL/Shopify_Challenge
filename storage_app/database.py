from flask import flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func

from .models.inventory import Inventory
# from .routes import Inventory
from storage_app import db


def create_sample_data():
    try:
        row = db.session.query(func.max(Inventory.id)).first()
    except:
        flash('There was a problem when creating sample data')
    if row is not None:
        index = row[0] if row[0] is not None else 0
    else:
        index = 0
    while True:
        index += 1
        item = Inventory(index, 'Macbook', 'NY', 1000)
        db.session.add(item)
        db.session.commit()
        if index % 5 == 0:
            break