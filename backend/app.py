from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host=os.getenv('DB_HOST', 'db'),
        database=os.getenv('DB_NAME', 'mydb'),
        user=os.getenv('DB_USER', 'myuser'),
        password=os.getenv('DB_PASS', 'mypassword')
    )
    return conn

@app.route('/')
def hello():
    return jsonify({"message": "Hola desde Flask!"})

@app.route('/items')
def items():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT id, name FROM items;')
    rows = cur.fetchall()
    cur.close()
    conn.close()
    result = [{"id": r[0], "name": r[1]} for r in rows]
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
