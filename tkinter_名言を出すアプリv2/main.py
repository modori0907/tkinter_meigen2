from tkinter import *
import math

# --------------------------- CONSTANTS --------------------------- #
PINK = "#e2979c"
RED = "#e7385b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
BROWN = "#735F32"
FONT_NAMA = "Courier"
timer = None

# -------------------------- Meigen --------------------------- #
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
# --------------------------- FUNCTIONS --------------------------- #

# --- start --- #
def start_timer():
    display_meigen(0)
    count_up(0)

def display_meigen(count):
    if len(meigen_list) == count:
        window.after(5000, display_meigen, 0) # 繰り返し処理用。カウントを0にする
    canvas.itemconfig(meigen_text, text=meigen_list[count])
    global timer
    timer = window.after(5000, display_meigen, count + 1)

# --- count --- #

def count_up(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    global timer
    timer = window.after(1000,count_up, count +1)

def stop_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    canvas.itemconfig(meigen_text, text="")


# --------------------------- CONSTANTS --------------------------- #

window = Tk()
window.title("MediModori4")
window.config(padx=0, pady=0, bg=YELLOW)
window.attributes("-topmost", True) # メインウインドウを最前面に出す処理

# キャンバスを作成
canvas = Canvas(width=600, height=100, bg=YELLOW, highlightthickness=0)  # キャンバスのサイズ
icon_img = PhotoImage(file="plant.png")  # キャンバスに画像オブジェクト
canvas.create_image(40, 40, image=icon_img)  # 画像を配置する配置、うまく納めるために調整する
meigen_text = canvas.create_text(90, 20, text="", fill="Green", font=("Times", 20, "bold"), width=450, anchor="nw")
timer_text = canvas.create_text(40,70, text="00:00",fill=BROWN, font=("Times", 20, "bold"))
# canvas.pack()
canvas.grid(row=0, column=0)

start_button = Button(text="開始", highlightthickness=0, font=(FONT_NAMA, 15, "bold"), fg=GREEN, command=start_timer)
start_button_img = PhotoImage()
start_button.place(x=550, y=20)
reset_botton = Button(text="停止", highlightthickness=0, font=(FONT_NAMA, 15, "bold"), fg=GREEN,command=stop_timer)
reset_botton.place(x=550, y=50)

window.mainloop()
