# import tkinter
# import tkinter.filedialog
import tkinter
from tkinter import *
import math
import time

# ---------------------------- 定数 ---------------------------- #
# 色
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
BRLUE = "#0072BC"
FONT_NAME = "Courier"

# ---------------------------- 関数作成 ---------------------------- #

# --- 名言をサイクルさせる処理
# 名言を取得する処理:

# --仮、最終的にはDBにする

meigen_list = ["悲しかったら鏡を見なさい 苦しかったら手を合わせなさい",
               "相手を許す。過去の怒りを手放す。これ以上苦しまないように、反応しないように努める。反応しないように努めるこれは、捨の心です。",
               "「自分が」「あの人が」という思いが〝心に刺さった矢〟であることに、人は気づかない。正しく見る者に、苦しみを繰り返すこだわり（自意識）は存在しない。",
               "よく注意して、落ち着きを保っている人は、怒りによって、行いが、言葉が、思いがざわつくことを、よく防いでいる。",
               "自分に強烈なスポットライトが当たっていれば、最前列さえ見えなくなるはずです",
               "腹がたったら自分にあたれ。悔しかったら自分を磨け",
               "大事なのは自分が生きているということに対して、そして周りにいる人々も自分と同じように生きているのだということに対して、注意深くなることだと思います。",
               "現実は続く。人生は続いていく。そうした日々の中にあって、せめて自分の中に苦しみを増やさない、「納得できる」生き方をしよう──そう考えるのです。",
               "他人の物事のために、自分のなすべきことを捨て去ってはならない。自分の物事を熟知して、自分のなすべきことに専念せよ。",
               "あの人（家族・世間）に認められたところで、それが一体なんなのだ？",
               "思考に気をつけなさいそれはいつか言葉になるから。言葉に気をつけなさいそれはいつか行動になるから。",
               "行動に気をつけなさいそれはいつか習慣になるから。習慣に気をつけなさいそれはいつか性格になるから。",
               "性格に気をつけなさいそれはいつか運命になるから。",
               "一番よいのは、怒りを管理しておくことです。怒らないようにすることです。怒りは「自己発火する不幸の原因」だと覚えておけばおさまると思います。",
               "自分の言葉に自分が尊敬を感じるような言葉をいっている",
               "その一言一語、その言葉のすべてが、人生に直接的に影響する暗示となる、という大事な宇宙真理を絶対に忘れない",
               "ニコニコして馬鹿にされるのなら、馬鹿にさせとけ",
               "自分の活き方が悪かったから、神がそれを教えるために与えて下された",
               "自分の尊い生命を守ってくれる心の王座には断然、恐怖というような悪魔は入れない"
               ]


not_stop = 0
def display_meigen():
    while not_stop == 0:
        for number, meigen in enumerate(meigen_list):
            yield meigen_label.config(text=meigen_list[number])


# ジェネレーターを利用して指定秒数単位で繰り返し名言を流す
c = display_meigen()
def update():
    meigen_label.config(text=next(c))
    meigen_label.after(10000, update)

timer = True

# def start_button():
#     meigen_label.after(1000, update)

def start_button():
    count = 0
    while timer:
        count_min = math.floor(count / 60)
        count_sec = count % 60
        timer_label.config(text=f"{count_min}:{count_sec}")
        count += 1







# ---------------------------- UI Setup ---------------------------- #

# 初期設定
window = Tk()
# root = tkinter.Tk()
window.title("You have my support")
window.config(padx=100, pady=10, bg=YELLOW)
window.attributes("-topmost", True) # メインウインドウを最前面に出す処理

# root.iconbitmap('') # 利用するのであれば
window.geometry('1000x70')  # ウインドウのサイズ
# window.resizable(0, 0)  # ウインドウサイズの変更。許可しない

# 　名言ラベル
meigen_label = Label(text="自分を励ますために", fg=BRLUE, bg=YELLOW, font=("ＭＳ ゴシック", 20),wraplength=800, anchor='e', justify='left')
meigen_label.grid(column=0, row=1)
# meigen_label.after(1000, update)

timer_label = Label(text="00:00", bg=YELLOW, fg=GREEN, font=("ＭＳ ゴシック", 20), anchor='e', justify='left')
timer_label.grid(column=0, row=0)

start_button = Button(text="Start", bg=YELLOW, fg=GREEN, highlightthickness=0, command=start_button)
start_button.grid(column=1, row=0)

window.mainloop()
