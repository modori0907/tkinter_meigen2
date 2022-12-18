





"""
# # 初期に実行する
# con = sqlite3.connect(('mycompany.db'))
# cObj = con.cursor()
# 
# # 一度だけ実行する。テーブル作るため
# # cObj.execute("CREATE TABLE employees(id INTEGER PRIMARY KEY, name TEXT, salary REAL, department TEXT, position TEXT)")
# # # con.commit()
# # cObj.execute("INSERT INTO employees VALUES (?,?,?,?,?)", (3, 'soma', 17500, 'Python','Developer'))
# # con.commit()
# cObj.execute("SELECT name FROM employees WHERE salary > 7500")
# result = cObj.fetchall()
# 
# for item in result:
#     print(item)
# 
# cObj.close()
# con.close()
"""