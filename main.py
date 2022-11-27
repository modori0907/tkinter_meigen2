# import tkinter
# import tkinter.filedialog
import time
from tkinter import *


# ---------------------------- 関数作成 ---------------------------- #

# --- 名言をサイクルさせる処理
# 名言を取得する処理:

# --仮、最終的にはDBにする

meigen_list = ["list_test1", "list_teest2", "list_teest3", "list_teest4", "teest5"]

not_stop = 0
def display_meigen():
    while not_stop == 0:
        for number, meigen in enumerate(meigen_list):
            yield meigen_label.config(text=meigen_list[number])


c = display_meigen()
def update():
    meigen_label.config(text=next(c))
    meigen_label.after(10000, update)



# ---------------------------- UI Setup ---------------------------- #

# 初期設定
window =Tk()
# root = tkinter.Tk()
window.title("You have my support")

# root.iconbitmap('') # 利用するのであれば
window.geometry('500x100')  # ウインドウのサイズ
window.resizable(0, 0)  # ウインドウサイズの変更。許可しない


#　名言ラベル
meigen_label = Label(text="TEST")
meigen_label.grid(column=0, row=0)
meigen_label.after(1000, update)

window.mainloop()