from tkinter import *

test

# --------------------------- CONSTANTS --------------------------- #
PINK = "#e2979c"
RED = "#e7385b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAMA = "Courier"

window = Tk()
window.title("You can do it")
window.config(padx=100, pady=10, bg=YELLOW)

# キャンバスを作成
canvas = Canvas(width=300, height=300) # キャンバスのサイズ
icon_img = PhotoImage(file="plant.png") # キャンバスに画像オブジェクト
canvas.create_image(40, 40, image=icon_img) # 画像を配置する配置、うまく納めるために調整する
canvas.create_text(50, 100, text="思考に気をつけなさい.テスト", fill="Green", font=(FONT_NAMA, 20, "bold"), width=200, anchor="nw")
canvas.pack()


window.mainloop()