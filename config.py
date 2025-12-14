from typing import Dict

MYSQL_CONFIG: Dict[str, object] = {
	"MYSQL_HOST": "localhost",
	"MYSQL_USER": "root",
	"MYSQL_PASSWORD": "root",
	"MYSQL_DB": "rudge",
	"MYSQL_PORT": 3306,
	"MYSQL_CURSORCLASS": "DictCursor",
}


def apply_mysql_config(app) -> None:
	for key, value in MYSQL_CONFIG.items():
		app.config[key] = value