import sqlite3
def create_db_add_conected():
    conn = sqlite3.connect("students.db")
    # conn.row_factory = sqlite3.Row
    return conn


def create_table(table):
    conn = create_db_add_conected()
    cursor = conn.cursor()
    cursor.execute(f"create table {table}(id integer primary key autoincrement,name text,grade integer);")

def select():
    conn = create_db_add_conected()
    cursor = conn.cursor()
    cursor.execute("select * from students")
    return cursor.fetchall()

def inset(name,grade):
    conn = create_db_add_conected()
    cursor = conn.cursor()
    cursor.execute(f"insert into students(name,grade)values('{name}',{grade})")
    conn.commit()

def update(id,name,grade):
    conn = create_db_add_conected()
    cursor = conn.cursor()
    cursor.execute(f"update students set name = '{name}' where id = {id}")
    cursor.execute(f"update students set grade = {grade} where id = {id}")
    conn.commit()

def delete(id):
    conn = create_db_add_conected()
    cursor = conn.cursor()
    cursor.execute(f"delete from students where id = {id}")
    conn.commit()




