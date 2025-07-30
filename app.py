import psycopg2
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from Hiatt in 3308'

@app.route('/db_test')
def test_db():
    conn = psycopg2.connect("postgresql://db_hello_user:7U1ktlvsCHdm5hlqJlSiahJpMo0IX3LV@dpg-d24qnqvgi27c73bb4tgg-a/db_hello")
    conn.close()
    return 'The database is connected'