from flask import Flask, request, jsonify
from flaskext.mysql import MySQL
import pymysql
from pymysql.err import IntegrityError



if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)


