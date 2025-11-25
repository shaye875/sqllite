import csv
from sqllite1 import *
def create_table_cor():
    conn = create_db_add_conected()
    cursor = conn.cursor()
    cursor.execute("create table courses(id integer primary key autoincrement,name varchar(100),city varchar(100),address varchar(100),course varchar(100),district varchar(100),telephone integer,email varchar(100))")
    conn.commit()

def insert_cor(name,city,address,course,district,telephone,email):
    conn = create_db_add_conected()
    cursor = conn.cursor()
    cursor.execute(f"insert into courses(name,city,address,course,district,telephone,email)values('{name}','{city}','{address}','{course}','{district}',{telephone},'{email}')")
    conn.commit()

def select_cor():
    conn = create_db_add_conected()
    cursor = conn.cursor()
    cursor.execute("select * from courses")
    print(cursor.fetchall())

def import_csv():
    conn = create_db_add_conected()
    cursor = conn.cursor()
    with open("courses.csv",encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
             cursor.execute("insert into courses(name,city,address,course,district,telephone,email) values (?,?,?,?,?,?,?)",row)
             conn.commit()

def inner_join():
    conn = create_db_add_conected()
    cursor = conn.cursor()
    cursor.execute("select students.id,courses.name from students full join courses on students.id = courses.id")
    print(cursor.fetchall())

# create_table_cor()
# import_csv()

# insert_cor("shaye","bab","pardo","fullstack","not",33,"rrr")
# select_cor()
inner_join()