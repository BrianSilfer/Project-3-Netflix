from flask import Flask, jsonify
import psycopg2
app = Flask(__name__)
def connect_db():
    conn = psycopg2.connect(
        dbname='Project_3',
        user='postgres',
        password='bsilf6767',
        host='localhost',
        port='5432'
    )
    return conn
@app.route('/data', methods=['GET'])
def get_data():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('SELECT * FROM netflix_titles')
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(rows)
if __name__ == '__main__':
    app.run(debug=True) 