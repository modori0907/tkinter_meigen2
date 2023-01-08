"""
UDEMYの講義をもとに作成
ツリービューの動きなどを理解するため
"""
# TODO 最終的にデータベースからデータを加工できるようにする

import tkinter
import tkinter.ttk as ttk
import csv

# ウィンドウの作成
root = tkinter.Tk()
root.title('test')
root.geometry('500x350')
root.resizable(0, 0)

DATABSE_FILE='money_database.csv'


# 関数の作成
def insert_date(row_data):
    tree.insert('', 'end', values=(row_data[0], row_data[1], row_data[2]))

def delete():
    selected_ids = tree.selection() # 選択しているIDを取得する
    for item_id in selected_ids:
        tree.delete(item_id)

# データベースの中身をツリービューに表示する関数
def reflect_database():
    with open(DATABSE_FILE, 'r', encoding='utf-8-sig', errors='ignore') as f:  # エラーが出た時無視する
        data_list = list(csv.reader(f)) # csvファイルをリスト形式で取得している

        for data in data_list:
            insert_date(data)


# フレームの作成
output_frame = tkinter.Frame(root)
button_frame = tkinter.Frame(root)
output_frame.pack()
button_frame.pack()

# ツリービューの作成
tree = ttk.Treeview(output_frame)
tree['columns'] = (1, 2, 3)
tree['show'] = 'headings'  # 自分の見出しのみを表示。一番左にデフォルトで表示される階層は出さないようにする

# カラムの幅の設定
tree.column(1, width=130)
tree.column(2, width=130)
tree.column(3, width=130)

# カラムの見出し設定
tree.heading(1, text='カテゴリー')
tree.heading(2, text='内容')
tree.heading(3, text='著者')

# データの追加
# tree.insert('', 'end', values=('2022/1/1', 'food', '4000'))  # endでデータの末尾に追加していく処理になる
# tree.insert('', 'end', values=('2022/1/1', 'drink', '1000'))  # endでデータの末尾に追加していく処理になる
# tree.insert('', 'end', values=('2022/1/1', 'snack', '4000'))  # endでデータの末尾に追加していく処理になる

# insert_date(['2022/1/1', 'food', '4000'])
# insert_date(['2022/1/2', 'drinks', '4000'])
# insert_date(['2022/1/3', 'snack', '4000'])

reflect_database()


tree.pack(pady=20)

# テーブルデータ編集に関するボタンの作成
add_button = tkinter.Button(button_frame, text='追加', borderwidth=2)
edit_button = tkinter.Button(button_frame, text='編集', borderwidth=2)
delete_button = tkinter.Button(button_frame, text='削除', borderwidth=2, command=delete)

add_button.grid(row=0, column=0, padx=5, pady=15, ipadx=5)
edit_button.grid(row=0, column=1, padx=5, pady=15, ipadx=5)
delete_button.grid(row=0, column=2, padx=5, pady=15, ipadx=5)

# ループ処理
root.mainloop()