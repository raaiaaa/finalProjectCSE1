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

def make_api_response(payload: Dict[str, Any], status_code: int = 200):
    try:
        fmt = get_response_format()
    except ValueError as err:
        payload = {"error": str(err)}
        status_code = 400
        fmt = "json"

    if fmt == "xml":
        xml_payload = dicttoxml(payload, custom_root="response", attr_type=False)
        response = make_response(xml_payload, status_code)
        response.headers["Content-Type"] = "application/xml"
        return response

    response = make_response(jsonify(payload), status_code)
    response.headers["Content-Type"] = "application/json"
    return response

def sanitize_employee_payload(payload: Dict[str, Any], partial: bool = False) -> Tuple[bool, Any]:
    if not isinstance(payload, dict):
        return False, "Request body must be a JSON object."

    sanitized: Dict[str, Any] = {}
    for key in payload.keys():
        if key not in EMPLOYEE_FIELDS:
            return False, f"Unsupported field: {key}"

    for key in EMPLOYEE_FIELDS:
        if key not in payload:
            continue

        value = payload[key]
        if key == "age":
            try:
                age_value = int(value)
            except (TypeError, ValueError):
                return False, "Age must be an integer."
            if not 16 <= age_value <= 100:
                return False, "Age must be between 16 and 100."
            sanitized[key] = age_value
            continue

        if not isinstance(value, str) or not value.strip():
            return False, f"{key.replace('_', ' ').title()} cannot be empty."
        sanitized[key] = value.strip()

    if not partial:
        missing = [field for field in EMPLOYEE_FIELDS if field not in sanitized]
        if missing:
            return False, "Missing fields: " + ", ".join(missing)
    elif not sanitized:
        return False, "Provide at least one field to update."

    return True, sanitized


def fetch_employee(employee_id: int) -> Dict[str, Any] | None:
    cursor = mysql.connection.cursor()
    cursor.execute(
        "SELECT id, first_name, last_name, age, address FROM employees WHERE id = %s",
        (employee_id,),
    )
    record = cursor.fetchone()
    cursor.close()
    return record

@app.get("/")
def index():
    return make_api_response({"message": "CSE1 Final Project API is running."})

@app.post("/login")
def login():
    credentials = request.get_json(silent=True) or {}
    username = (credentials.get("username") or "").strip()
    password = (credentials.get("password") or "").strip()

    if not username or not password:
        return make_api_response({"error": "Username and password are required."}, 400)

    if username != "admin" or password != "password123":
        return make_api_response({"error": "Invalid username or password."}, 401)

    token = create_access_token(identity=username)
    return make_api_response({"message": "Login successful.", "access_token": token})

@app.post("/employees")
@jwt_required()
def create_employee():
    payload = request.get_json(silent=True) or {}
    is_valid, sanitized = sanitize_employee_payload(payload)
    if not is_valid:
        return make_api_response({"error": sanitized}, 400)

    cursor = mysql.connection.cursor()
    try:
        cursor.execute(
            """
            INSERT INTO employees (first_name, last_name, age, address)
            VALUES (%s, %s, %s, %s)
            """,
            (
                sanitized["first_name"],
                sanitized["last_name"],
                sanitized["age"],
                sanitized["address"],
            ),
        )
        mysql.connection.commit()
        new_id = cursor.lastrowid
    except Exception as exc:
        mysql.connection.rollback()
        cursor.close()
        return make_api_response({"error": "Database error.", "details": str(exc)}, 500)

    cursor.close()
    employee = fetch_employee(new_id)
    return make_api_response({"message": "Employee created successfully.", "employee": employee}, 201)


@app.get("/employees")
@jwt_required()
def list_employees():
    cursor = mysql.connection.cursor()
    try:
        cursor.execute("SELECT id, first_name, last_name, age, address FROM employees ORDER BY id")
        employees = cursor.fetchall()
    except Exception as exc:
        cursor.close()
        return make_api_response({"error": "Database error.", "details": str(exc)}, 500)

    cursor.close()
    return make_api_response({"employees": employees, "count": len(employees)})


@app.get("/employees/<int:employee_id>")
@jwt_required()
def get_employee(employee_id: int):
    employee = fetch_employee(employee_id)
    if not employee:
        return make_api_response({"error": "Employee not found."}, 404)
    return make_api_response({"employee": employee})


@app.put("/employees/<int:employee_id>")
@jwt_required()
def update_employee(employee_id: int):
    payload = request.get_json(silent=True) or {}
    is_valid, sanitized = sanitize_employee_payload(payload, partial=True)
    if not is_valid:
        return make_api_response({"error": sanitized}, 400)

    assignments = ", ".join(f"{field} = %s" for field in sanitized.keys())
    values = list(sanitized.values()) + [employee_id]

    cursor = mysql.connection.cursor()
    try:
        cursor.execute(f"UPDATE employees SET {assignments} WHERE id = %s", values)
        mysql.connection.commit()
        if cursor.rowcount == 0:
            cursor.close()
            return make_api_response({"error": "Employee not found."}, 404)
    except Exception as exc:
        mysql.connection.rollback()
        cursor.close()
        return make_api_response({"error": "Database error.", "details": str(exc)}, 500)

    cursor.close()
    updated = fetch_employee(employee_id)
    return make_api_response({"message": "Employee updated successfully.", "employee": updated})


@app.delete("/employees/<int:employee_id>")
@jwt_required()
def delete_employee(employee_id: int):
    cursor = mysql.connection.cursor()
    try:
        cursor.execute("DELETE FROM employees WHERE id = %s", (employee_id,))
        mysql.connection.commit()
        if cursor.rowcount == 0:
            cursor.close()
            return make_api_response({"error": "Employee not found."}, 404)
    except Exception as exc:
        mysql.connection.rollback()
        cursor.close()
        return make_api_response({"error": "Database error.", "details": str(exc)}, 500)

    cursor.close()
    return make_api_response({"message": "Employee deleted successfully."})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)


