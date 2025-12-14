

# Final Project – CSE1

## Activity: Building a CRUD REST API with MySQL, Testing, and XML/JSON Output

This project is a **Flask-based CRUD REST API** developed as the **Final Project for CSE1**. The API connects to a **MySQL database** and allows clients to **Create, Read, Update, and Delete (CRUD)** records. It supports **JSON and XML output formats** and includes basic testing to ensure API functionality.

The API serves as an interface for any client that understands **HTTP**, **JSON**, or **XML**.

---

## 📌 Features

* CRUD operations (Create, Read, Update, Delete)
* RESTful API endpoints
* MySQL database integration
* JSON and XML response formats
* Tested API endpoints (manual or automated)
* Uses Flask virtual environment

---

## 🛠 Technologies Used

* Python 3
* Flask
* MySQL
* Flask-MySQL / PyMySQL / mysqlclient
* JSON & XML
* Postman (for API testing)

---

## 📂 Project Structure

```
final-project-cse1/
│── app.py
│── requirements.txt
│── .gitignore
│── README.md
│── tests/
│   └── test_api.py
```
---

## 🚀 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/final-project-cse1.git
cd final-project-cse1
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the virtual environment:

* **Windows**

```bash
venv\Scripts\activate
```

* **macOS/Linux**

```bash
source venv/bin/activate
```

> ⚠️ The virtual environment is ignored using `.gitignore` and is **not uploaded to GitHub**.

---

### 3. Install Required Libraries

```bash
pip install -r requirements.txt
```

Example `requirements.txt`:

```
flask
pymysql
mysqlclient
```

---

## ▶️ Running the Application

```bash
python app.py
```

The API will run at:

```
http://127.0.0.1:5000/
```

---

## 📡 API Endpoints (Sample)

| Method | Endpoint    | Description              |
| ------ | ----------- | ------------------------ |
| GET    | /items      | Retrieve all records     |
| GET    | /items/<id> | Retrieve a single record |
| POST   | /items      | Create a new record      |
| PUT    | /items/<id> | Update a record          |
| DELETE | /items/<id> | Delete a record          |


```

## 📌 Notes

* Ensure MySQL is running before starting the application
* Update database credentials inside `app.py`
* The project follows RESTful API design principles
