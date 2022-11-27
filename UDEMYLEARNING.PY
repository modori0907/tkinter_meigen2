import sqlite3

# DBを作成する
con = sqlite3.connect('mycompany.db')
cObj = con.cursor()

# # テーブル、カラムを作成、作成するときに一度だけ実行。２回やるとエラーになってしまう。
cObj.execute(
    "CREATE TABLE IF NOT EXISTS employees(id INTEGER PRIMARY KEY , name TEXT, salary REAL, department TEXT,position TEXT)")
con.commit()


def insert_value(id, name, salary, department, position):
    cObj.execute("INSERT INTO employees VALUES (?,?,?,?,?)", (id, name, salary, department, position))
    con.commit()

def update_department(dep, id):
    cObj.execute("UPDATE employees SET department=? WHERE id=?", (dep,id))
    con.commit()

cObj.close()
con.close()
