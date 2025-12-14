from datetime import timedelta
from typing import Any, Dict, Tuple

from dicttoxml import dicttoxml
from flask import Flask, jsonify, make_response, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from flask_mysqldb import MySQL

from config import apply_mysql_config

app = Flask(__name__)
apply_mysql_config(app)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)


