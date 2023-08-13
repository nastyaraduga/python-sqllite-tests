import sqlite3
from sqlite3 import Error

def create_database(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)
   
def truncate_table(conn, truncate_table_sql):
    try:
        c = conn.cursor()
        c.execute(truncate_table_sql)
    except Error as e:
        print(e)
   
def create_client(conn, client):
    sql = ''' INSERT INTO client (name, change_date)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql,  client)
    conn.commit()
    return cur.lastrowid

def select_client(conn, client):
    sql = 'SELECT * FROM client WHERE id=?'
    cur = conn.cursor()
    cur.execute(sql, client)
    rows = cur.fetchall()
    return rows

def update_client(conn, client):
    sql = ''' UPDATE client
              SET name = ? ,
                  change_date = ? 
              WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql, client)
    conn.commit()
    
def delete_client(conn, client):
    sql = 'DELETE FROM client WHERE id=?'
    cur = conn.cursor()
    cur.execute(sql, client)
    conn.commit()


