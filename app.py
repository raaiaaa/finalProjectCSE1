from datetime import timedelta
from typing import Any, Dict, Tuple

from dicttoxml import dicttoxml
from flask import Flask, jsonify, make_response, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from flask_mysqldb import MySQL
from config import apply_mysql_config

app = Flask(__name__)
apply_mysql_config(app)
app.config["JWT_SECRET_KEY"] = "change-this-secret"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)

mysql = MySQL(app)
jwt = JWTManager(app)

EMPLOYEE_FIELDS = ("first_name", "last_name", "age", "address")

def get_response_format() -> str:
    fmt = request.args.get("format", "json").lower()
    if fmt not in {"json", "xml"}:
        raise ValueError("Invalid format. Use ?format=json or ?format=xml.")
    return fmt

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)


