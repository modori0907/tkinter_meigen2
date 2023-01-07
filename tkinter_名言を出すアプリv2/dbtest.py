import sqlite3
import tkinter.ttk as ttk
from tkinter import *
from tkinter import messagebox

# TODO　ソートして表示する処理
# TODO  検索して表示する処理
# TODO ENTERで実行処理

# Tkinter 事前処理
meigens = Tk()

# ------- 変数 ------- #
# カテゴリー選択時に表示される
category_list = ["励まし", "落ち着く", "向上心"]

con = sqlite3.connect('meigens.db')
cursorObj = con.cursor()

# DB作成
cursorObj.execute(
    "CREATE TABLE IF NOT EXISTS meigens(id INTEGER PRIMARY KEY, category TEXT, sub category TEXT, meigen TEXT, author TEXT)")
con.commit()


# 何かの操作（追加など）をしたときにリセットする処理
def reset():
    for cell in meigens.winfo_children():
        cell.destroy()

    make_window()
    my_meigen()

# ソートする処理
def sorted_colum():
    pass


def my_meigen():
    cursorObj.execute("SELECT * FROM meigens")
    # 全データを取得する。
    meigens_list = cursorObj.fetchall()

    # 名言のデータベースカラム更新用

    def delete_meigen():

        if len(cursorObj.execute("SELECT * FROM meigens WHERE id=?", (meigen_delete.get(),)).fetchall()) == 0:
            messagebox.showinfo("Delet", "該当データがありません")

        else:
            cursorObj.execute("DELETE FROM meigens WHERE id=?", (meigen_delete.get(),))
            messagebox.showinfo("Delete", "名言を削除しました")

        reset()

    def insert_meigen():
        if meigen_category_add.get() == "" or meigen_content_add.get() == "":
            messagebox.showinfo("Insert", "値を入力してください")

        else:
            cursorObj.execute("INSERT INTO meigens(category,meigen,author) VALUES(?, ?, ?)", (meigen_up.get(),
                                                                                    meigen_content_add.get(), meigen_author_add.get()))
            con.commit()

            messagebox.showinfo("Insert", "名言を追加しました")

        reset()

    def update_meigen():

        if meigen_update_id.get() == "":
            messagebox.showinfo("Insert", "値を入力してください")

        else:
            if len(cursorObj.execute("SELECT * FROM meigens WHERE id=?", (meigen_update_id.get(),)).fetchall()) == 0:
                messagebox.showinfo("Delet", "該当データがありません")
            else:
                cursorObj.execute("UPDATE meigens SET category=?,meigen=?,author=? WHERE id=?", (meigen_category_update.get(),
                                                                                        meigen_content_update.get(), meigen_author_update.get(), meigen_update_id.get()))
                con.commit()

                messagebox.showinfo("Insert", "更新しました")

        reset()





    meigen_row = 1




    for meigen in meigens_list:
        meigen_id = Label(meigens, text=meigen[0])
        meigen_id.grid(row=meigen_row, column=0, sticky=N + S + E + W)

        meigen_category = Label(meigens, text=meigen[1])
        meigen_category.grid(row=meigen_row, column=1, sticky=N + S + E + W)

        meigen_content = Label(meigens, text=meigen[3])
        meigen_content.grid(row=meigen_row, column=2, sticky="nw")

        author_content = Label(meigens, text=meigen[4])
        author_content.grid(row=meigen_row, column=3, sticky=N + S + E + W)

        meigen_row += 1

    # 名言のリストを追加する処理のボタン

    meigen_category_add = ttk.Combobox(meigens, values=category_list)
    meigen_category_add.grid(row=meigen_row + 1, column=1)

    meigen_content_add = Entry(meigens, borderwidth=2, relief="groove")
    meigen_content_add.grid(row=meigen_row + 1, column=2, sticky=N + S + E + W)

    meigen_author_add = Entry(meigens, borderwidth=2, relief="groove")
    meigen_author_add.grid(row=meigen_row + 1, column=3, sticky=N + S + E + W)

    meigen_add_button = Button(meigens, text="追加", command=insert_meigen)
    meigen_add_button.grid(row=meigen_row + 1, column=4)

    meigen_add_button.bind("<Return>", lambda event: insert_meigen())
    # url:https://teratail.com/questions/248497

    # 名言を更新する処理

    meigen_update_id = Entry(meigens, borderwidth=2, relief="groove")
    meigen_update_id.grid(row=meigen_row + 2, column=0)

    meigen_category_update = ttk.Combobox(meigens, values=category_list)
    meigen_category_update.grid(row=meigen_row + 2, column=1)

    meigen_content_update = Entry(meigens, borderwidth=2, relief="groove")
    meigen_content_update.grid(row=meigen_row + 2, column=2, sticky=N + S + E + W)

    meigen_author_update = Entry(meigens, borderwidth=2, relief="groove")
    meigen_author_update.grid(row=meigen_row + 2, column=3, sticky=N + S + E + W)

    meigen_update_button = Button(meigens, text="更新", command=update_meigen)
    meigen_update_button.grid(row=meigen_row + 2, column=4)

    meigen_update_button.bind("<Return>", lambda event: update_meigen())


    # 名言のリストを削除する処理のボタン
    meigen_delete = Entry(meigens, borderwidth=2, relief="groove")
    meigen_delete.grid(row=meigen_row + 3, column=0)

    meigen_delete_button = Button(meigens, text="名言削除", bg="#142E54", command=delete_meigen)
    meigen_delete_button.grid(row=meigen_row + 3, column=4, sticky=N + S + E + W)

    meigen_delete_button.bind("<Return>", lambda event: delete_meigen())





def make_window():
    meigen_id = Label(meigens, text="ID")
    meigen_id.grid(row=0, column=0, sticky=N + S + E + W)

    meigen_category = Label(meigens, text="Category")
    meigen_category.grid(row=0, column=1, sticky=N + S + E + W)

    meigen_content = Label(meigens, text="Meigen")
    meigen_content.grid(row=0, column=2, sticky=N + S + E + W)

    author_content = Label(meigens, text="Author")
    author_content.grid(row=0, column=3, sticky=N + S + E + W)



# TODO 削除はIDからリストを取得して選択できるようにする

# ------- 最終処理 ------- #

make_window()
my_meigen()
meigens.mainloop()
cursorObj.close()
con.close()

"""
学んだこと

mysqlはnullがデフォルトで許可されている
https://bituse.info/mysql/11#:~:text=NULL%E3%82%92%E8%A8%B1%E5%8F%AF%E3%81%99%E3%82%8B%E3%81%AB,%E3%81%AB%E8%A8%AD%E5%AE%9A%E3%81%99%E3%82%8B%E3%81%A8%E6%9C%89%E7%94%A8%E3%81%A7%E3%81%99%E3%80%82


# ------- insert処理 ------- #
cursorObj.execute("INSERT INTO meigens(category,meigen) VALUES('カテゴリーテスト', '名言テスト')")
con.commit()

# ------- update処理 ------- #

cursorObj.execute("UPDATE meigens SET category=?, meigen=? WHERE id=?", ("アップデートテスト", "アップデート名言", 1))
con.commit()

# ------- delete処理 ------- #
cursorObj.execute("DELETE FROM meigens WHERE id=?", (1,))
con.commit()



# -------- stickyの使い方 ------- #
sticky	pack の anchor と fill をあわせた属性です。 スペースに余裕がある場合、どこに配置するか、どのように引き伸ばすかを指定します。
指定できる値は anchor と同じ、Tk.CENTER, Tk.W, Tk.E, Tk.N, Tk.S, Tk.NW, Tk.NW, Tk.SW, Tk.SE です。 位置決めには値を単独で、引き伸ばす場合には値を '+' して指定します。
たとえば、左寄せは sticky=Tk.W, 上よせは sticky=Tk.N。
左右に引き伸ばすには sticky=Tk.W + Tk.E, 上下に引き伸ばすには sticky=Tk.N + Tk.S,
全体に引き伸ばすには sticky=Tk.W + Tk.E + Tk.N + Tk.S。


"""
