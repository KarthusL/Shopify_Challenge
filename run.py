from inventory_app import app, db

if __name__ == '__main__':
    app.run(debug=True)
    # if you want to delete all data from database after stopping the app, release the code below
    # db.drop_all()
