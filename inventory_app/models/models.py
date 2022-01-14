from inventory_app import db


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
