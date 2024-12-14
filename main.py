# flask-login
# flask-sqlalchem
#

from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True) # automatically rerun the application after every change instead of doing this by myself
