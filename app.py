import os

from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)


def database_status():
    connection = mysql.connector.connect(
        host=os.getenv("DB_HOST", "mysql"),
        port=int(os.getenv("DB_PORT", "3306")),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", "example"),
        database=os.getenv("DB_NAME", "appdb"),
    )
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT 1")
        return cursor.fetchone()[0]
    finally:
        connection.close()


def get_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "mysql"),
        port=int(os.getenv("DB_PORT", "3306")),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", "example"),
        database=os.getenv("DB_NAME", "appdb"),
    )


@app.route("/")
def hello_world():
    try:
        database_status()
        return "<p>Hello, World! Database connected.</p>"
    except Exception as error:
        app.logger.exception("Database connection failed")
        return f"<p>Hello, World! Database unavailable: {type(error).__name__}</p>", 503


@app.route("/health")
def health():
    try:
        database_status()
        return jsonify(status="ok")
    except Exception:
        return jsonify(status="error"), 503


@app.route("/clients")
def clients():
    connection = get_connection()
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT id, name FROM clients ORDER BY id")
        return jsonify(cursor.fetchall())
    finally:
        connection.close()


if __name__ == "__main__":
    app.run("0.0.0.0", port=int(os.getenv("PORT", "5000")))
