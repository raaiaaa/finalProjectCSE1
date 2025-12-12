from flask import Flask, request, jsonify
from flaskext.mysql import MySQL
import pymysql
from pymysql.err import IntegrityError

app = Flask(__name__)
mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'rudge21'
app.config['MYSQL_DATABASE_DB'] = 'api'
app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'

employee = [
    {"id": 1, "name": "John Doe", "age": "28", 'address': 'New York'},
]




if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)


