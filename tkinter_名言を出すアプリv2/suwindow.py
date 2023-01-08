"""
UDEMYの講義をもとに作成
ツリービューの動きなどを理解するため
"""
# TODO 最終的にデータベースからデータを加工できるようにする

# db
import sqlite3

import tkinter
import tkinter.ttk as ttk

# ウィンドウの作成
root = tkinter.Tk()
root.title('test')
root.geometry('700x350')
root.resizable(0, 0)

# DATABSE_FILE = 'money_database.csv'
DATA = []
category_list = ["励まし", "落ち着く", "向上心"]

# DB作成
con = sqlite3.connect('meigens.db')
cursorObj = con.cursor()

cursorObj.execute(
    "CREATE TABLE IF NOT EXISTS meigens(id INTEGER PRIMARY KEY, category TEXT, sub category TEXT, meigen TEXT, author TEXT)")
con.commit()


# 関数の作成
def insert_date(row_data):
    tree.insert('', 'end', values=(row_data[0], row_data[1], row_data[2], row_data[3]))


def delete():
    #
    selected_ids = tree.selection()  # 選択しているIDを取得する
    # DBの削除処理。表示内容を実施しないと対象のidsがなくなるのでエラーになってしまう
    for n in range(len(selected_ids)):
        selected_item_ids = tree.selection()[n]  # 選択しているIDを取得する
        values = tuple(tree.item(selected_item_ids)['values'])[0]  # 取得したアイテムの１番目(DBのプリマリキー）を取得
        cursorObj.execute("DELETE FROM meigens WHERE id=?", (values,))  # idで削除
        con.commit()

    # # DBを更新する処理
    # print(len(selected_ids))
    # selected_item_ids = tree.selection()[0] # 選択しているIDを取得する
    # values = tuple(tree.item(selected_item_ids)['values'])[0]
    # print(values)

    # 表示内容を更新する処理
    for item_id in selected_ids:
        tree.delete(item_id)

    # 選択したアイテムから値を取得する処理
    # URL:https://www.web-dev-qa-db-ja.com/ja/python/treeviewtkinter%E3%81%AE%E3%82%A2%E3%82%A4%E3%83%86%E3%83%A0%E3%82%92%E5%89%8A%E9%99%A4%E3%81%8A%E3%82%88%E3%81%B3%E7%B7%A8%E9%9B%86%E3%81%99%E3%82%8B/1055640459/
    # selected_ids = tree.selection()[0] # 選択しているIDを取得する
    # values = tuple(tree.item(selected_ids)['values'])
    # print(values)
    # (10, '落ち着く', 'マイクラ')
    # (8, '落ち着く', '思考にきをつけなさい、それは言葉になるから')
    # # for item_id in selected_ids:
    #     tree.delete(item_id)
    #     print(item_id)
    #
    # update_db()


# データベースの中身をツリービューに表示する関数
def reflect_database():
    #
    cursorObj.execute("SELECT * FROM meigens")
    meigens_list = cursorObj.fetchall()
    for meigen in meigens_list:
        DATA.append(meigen[0])
        DATA.append(meigen[1])
        DATA.append(meigen[3])
        DATA.append(meigen[4])
        insert_date(DATA)
        DATA.clear()

    # with open(DATABSE_FILE, 'r', encoding='utf-8-sig', errors='ignore') as f:  # エラーが出た時無視する
    #     data_list = list(csv.reader(f)) # csvファイルをリスト形式で取得している
    #
    #     for data in data_list:
    #         insert_date(data)


# ツリービューにデータを追加する関数
def add():
    add_window()
    add_button.config(state='disabled')  # 追加ボタンを押下後に編集ボタンを無効にする処理
    edit_button.config(state='disabled')  # 追加ボタンを押下後に編集ボタンを無効にする処理
    delete_button.config(state='disabled')  # 上と同じ


# 追加ウインドウを作成する関数
def add_window():
    global data_category, data_content, data_author, add_subwindow
    add_subwindow = tkinter.Toplevel()
    add_subwindow.geometry("400x400")
    add_subwindow.title("データ追加")

    date_category_label = tkinter.Label(add_subwindow, text="カテゴリー")
    data_category = ttk.Combobox(add_subwindow, values=category_list)
    date_category_label.grid(row=0, column=0, padx=10, pady=20)
    data_category.grid(row=0, column=1, padx=10, pady=20)

    date_content_label = tkinter.Label(add_subwindow, text="内容")
    data_content = tkinter.Entry(add_subwindow)
    date_content_label.grid(row=1, column=0, padx=10, pady=20)
    data_content.grid(row=1, column=1, padx=10, pady=20)

    date_author_label = tkinter.Label(add_subwindow, text="著者")
    data_author = tkinter.Entry(add_subwindow)
    date_author_label.grid(row=2, column=0, padx=10, pady=20)
    data_author.grid(row=2, column=1, padx=10, pady=20)

    save_button = tkinter.Button(add_subwindow, text='保存', command=add_row)
    save_button.grid(row=3, column=0, columnspan=2)


# 行を追加する処理
def add_row():
    new_category = data_category.get()
    new_content = data_content.get()
    new_author = data_author.get()
    # new_date =[99, new_category, new_content, new_author]
    # insert_date(new_date)
    cursorObj.execute("INSERT INTO meigens(category,meigen,author) VALUES(?, ?, ?)",
                      (new_category, new_content, new_author))
    con.commit()
    reflect_database() # 追加したデータを一覧に反映させる処理
    add_subwindow.destroy()  # サブウィンドウを閉じる処理

    add_button.config(state='normal')
    edit_button.config(state='normal')
    delete_button.config(state='normal')



# フレームの作成
output_frame = tkinter.Frame(root)
button_frame = tkinter.Frame(root)
output_frame.pack()
button_frame.pack()

# ツリービューの作成
tree = ttk.Treeview(output_frame)
tree['columns'] = (1, 2, 3, 4)
tree['show'] = 'headings'  # 自分の見出しのみを表示。一番左にデフォルトで表示される階層は出さないようにする

# カラムの幅の設定
tree.column(1, width=50)
tree.column(2, width=80)
tree.column(3, width=400)
tree.column(4, width=100)

# カラムの見出し設定
tree.heading(1, text='ID')
tree.heading(2, text='カテゴリー')
tree.heading(3, text='内容')
tree.heading(4, text='著者')

reflect_database()

tree.pack(pady=20)

# テーブルデータ編集に関するボタンの作成
add_button = tkinter.Button(button_frame, text='追加', borderwidth=2, command=add)
edit_button = tkinter.Button(button_frame, text='編集', borderwidth=2)
delete_button = tkinter.Button(button_frame, text='削除', borderwidth=2, command=delete)

add_button.grid(row=0, column=0, padx=5, pady=15, ipadx=5)
edit_button.grid(row=0, column=1, padx=5, pady=15, ipadx=5)
delete_button.grid(row=0, column=2, padx=5, pady=15, ipadx=5)

# ループ処理
root.mainloop()
