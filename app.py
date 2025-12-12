from flask import Flask, request, jsonify
from flaskext.mysql import MySQL
import pymysql
from pymysql.err import IntegrityError

app = Flask(__name__)
mysql = MySQL()

DB_CONFIG = {
    "host": "127.0.0.1",
    "user": "root",
    "password": "rudge21",
    "db": "api"
}





if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)


