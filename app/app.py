from flask import Flask
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host="db",
        user="root",
        password="password",
        database="demo"
    )

@app.route("/")
def show_users():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, email FROM users")
    rows = cursor.fetchall()
    conn.close()

    html = "<h2>👥 Users Table</h2><table border='1'><tr><th>ID</th><th>Name</th><th>Email</th></tr>"
    for row in rows:
        html += f"<tr><td>{row[0]}</td><td>{row[1]}</td><td>{row[2]}</td></tr>"
    html += "</table>"
    return html

@app.route("/products")
def show_products():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, price, stock FROM products")
    rows = cursor.fetchall()
    conn.close()

    html = "<h2>🛍️ Products Table</h2><table border='1'><tr><th>ID</th><th>Name</th><th>Price</th><th>Stock</th></tr>"
    for row in rows:
        html += f"<tr><td>{row[0]}</td><td>{row[1]}</td><td>${row[2]}</td><td>{row[3]}</td></tr>"
    html += "</table>"
    return html

@app.route("/orders")
def show_orders():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT o.id, u.name AS user_name, p.name AS product_name, o.status, o.order_date
        FROM orders o
        JOIN users u ON o.user_id = u.id
        JOIN products p ON o.product_id = p.id
    """)
    rows = cursor.fetchall()
    conn.close()

    html = "<h2>📦 Orders Table</h2><table border='1'><tr><th>Order ID</th><th>User</th><th>Product</th><th>Status</th><th>Date</th></tr>"
    for row in rows:
        html += f"<tr><td>{row[0]}</td><td>{row[1]}</td><td>{row[2]}</td><td>{row[3]}</td><td>{row[4]}</td></tr>"
    html += "</table>"
    return html

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

