from flask import Flask
#from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
#db = SQLAlchemy(app)

@app.route('/')
def index():
    return 'Hello World'


if __name__ == '__main__':
    app.run(debug=True)