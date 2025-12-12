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

mysql.init_app(app)

def get_db_connection():
    return pymysql.connect()


def fetch_all_employees():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()
    cursor.close()
    conn.close()
    return employees

@app.route("/")
def home():
    return "Flask is running ✅"



if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)


