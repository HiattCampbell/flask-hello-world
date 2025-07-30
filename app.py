import psycopg
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from Hiatt in 3308'

@app.route('/db_test')
def testing():
    conn = psycopg.connect("postgresql://db_hello_user:7U1ktlvsCHdm5hlqJlSiahJpMo0IX3LV@dpg-d24qnqvgi27c73bb4tgg-a/db_hello")
    conn.close()
    return 'The database is connected'

@app.route('/db_create')
def creeating():
    conn = psycopg.connect("postgresql://db_hello_user:7U1ktlvsCHdm5hlqJlSiahJpMo0IX3LV@dpg-d24qnqvgi27c73bb4tgg-a/db_hello")
    cur = con.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Basketball(
        First varchar(255),
        Last varchar(255),
        City varchar(255),
        Name varchar(255),
        Number int
        );
''')
    conn.commit()
    conn.close()
    return 'Basketball table successfully created'