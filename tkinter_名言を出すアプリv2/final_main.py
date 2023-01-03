import tkinter as tk
from tkinter import Canvas, PhotoImage
import tkinter.messagebox
import sqlite3

con = sqlite3.connect('meigens.db')
cursorObj = con.cursor()
cursorObj.execute("CREATE TABLE IF NOT EXISTS meigens(id INTEGER PRIMARY KEY, main_category TEXT, sub_category TEXT, meigen TEXT)")
con.commit()

cursorObj.execute("INSERT INTO meigens VALUES(1, '励まし')")

class Application(tk.Frame):
    # masterはTKINTERの全体オブジェクト。
    def __init__(self, meigens, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        self.running = False
        self.time = 0
        self.hours = 0
        self.mins = 0
        self.secs = 0
        self.build_interface()
# MODORI
        self.n = 0  # 名言をリストから表示させるための処理
        self.meigens = meigens # 名言リストの初期化

    def build_interface(self):

        self.meigen = tk.Label(self,text="")
        self.meigen.grid(row=0, column=1)

        # 　時間入力
        self.time_entry = tk.Entry(self)
        self.time_entry.grid(row=1, column=1)

        # 　残り時間
        self.clock = tk.Label(self, text="00:00:00", font=("Courier", 20), width=10)
        self.clock.grid(row=2, column=1, stick="S")

        # 　残り時間のラベル
        self.time_label = tk.Label(self, text="hour   min   sec", font=("Courier", 10), width=15)
        self.time_label.grid(row=3, column=1, sticky="N")

        # 開始ボタン
        # lambdaを入れないとエラーになる。selfを入れないとエラーになる
        # TODO なぜlambdaを使うのかを理解する
        self.power_button = tk.Button(self, text="Start", command=lambda: self.start())
        self.power_button.grid(row=4, column=0, sticky="NE")

        self.reset_button = tk.Button(self, text="Reset", command=lambda: self.reset())
        self.reset_button.grid(row=4, column=1, sticky="NW")

        self.quit_button = tk.Button(self, text="Quit", command=lambda: self.quit())
        self.quit_button.grid(row=4, column=3, sticky="NE")

        # self.pause_button = tk.Button(self, text="Pause", command=lambda: self.pause())
        # self.pause_button.grid(row=3, column=2, sticky="NW")

        # Enterキーを押下して　
        # master.bindはEnter入力でもスタート、ストップが動くようにするためのキー
        # master.bindは全体としての動きを与えるので、Enterはstop,startを繰り返すようにする。
        # master.bindの初期値はstart(次のEnterはstar関数でstopに変換.
        # vは入力した値が入る（時刻を指定するところに）
        # xは多分
        self.master.bind("<Return>", lambda x: self.start())
        self.time_entry.bind("<Key>", lambda v: self.update())

    def calculate(self):
        """time calculation"""
        # 取得した値をsecを変換
        self.hours = self.time // 3600
        # 1時間（つまり60)を超えたminは23
        self.mins = (self.time // 60) % 60
        self.secs = self.time % 60
        # {:02d}とは。書式設定。dは整数。0は埋め。2は桁数を指定。:は前に入れる.入れないと更新されない
        return "{:02d}:{:02d}:{:02d}".format(self.hours, self.mins, self.secs)

    def update(self):
        """validation"""
        # int型で入力された値を取得する. 時間を指定
        self.time = int(self.time_entry.get())
        try:
            # int型で変更できるのであれば、計算する
            self.clock.configure(text=self.calculate())
        except:
            # int型で取得できなければ00:00:00と表示
            self.clock.configure(text="00:00:00")

    def timer(self):
        """display time"""
        # runningがtrueであることを確認
        # falseになる条件は,stop
        # start,pause,resume関数から呼び出される
        # startを押下するとtimerを呼び出す
        # 1秒間隔で秒数を下げる
        if self.running:
            if self.time <= 0:
                self.clock.configure(text="Time's up!")
                self.master.attributes("-topmost", True)  # メインウインドウを最前面に出す処理
            else:
                self.clock.configure(text=self.calculate())
                self.time -= 1
                self.after(1000, self.timer)

# MODORI4
    def meigen_timer(self):
        """display meigen"""
        # runningがtrueであることを確認
        # falseになる条件は,stop
        # start,pause,resume関数から呼び出される
        # startを押下するとtimerを呼び出す
        # 1秒間隔で秒数を下げる

        if self.running:
            self.meigen.configure(text=self.meigens[self.n], wraplength=200, anchor="e", justify="left")
            self.n += 1
            self.after(10000, self.meigen_timer)


    def start(self):
        """start timer"""

        # 秒数を入力するtime_entryから値をゲットする。int型にする
        # int型で入力しなければ、self.time = self.timeなので00:00:00がself.timeに入力される
        # exceptでself.timeを使わずにtimeにしてしまうと、start,stopがうまく動かない
        # まず、指定したい時刻を入力、スタートボタンを押すと空欄になる。つまり、ここからスタート、ストップを押しても
        # 常時、except処理が走るようになる。その時、self.timeはストップするタイミングでストップ時の値を保持している。
        # tryではtimeに値を入れて、その後deleteする。(Entryの中身を0文字目から最後の文字まで削除
        # runningをTrueにするとタイムカウントが始まる。

        try:
            self.time = int(self.time_entry.get())
            self.time_entry.delete(0, 'end')
        except:
            self.time = self.time

        # startを押した後にStopボタンに変換して、コマンドもstopにする
        self.power_button.configure(text="Stop", command=lambda: self.stop())
        # Enterで操作したときの動き
        self.master.bind("<Return>", lambda x: self.stop())
        self.running = True
        # timerを呼び出す。
        # timerは
        self.timer()
#MODORI4
        self.meigen_timer()

    def stop(self):
        """Stop timer"""
        # stopボタンを押下したら、startにボタン、機能を変換
        # stopボタンを押したらstartが開始するので、starメソッドを実行している。
        # runningをFalseにしている
        self.power_button.configure(text="Start", command=lambda: self.start())
        self.master.bind("<Return>", lambda x: self.start())
        self.running = False

    def reset(self):
        """Resets the timer to 0."""
        self.power_button.configure(text="Start", command=lambda: self.start())
        self.master.bind("<Return>", lambda x: self.start())
        self.running = False
        self.time = 0
        self.clock["text"] = "00:00:00"

    def quit(self):
        """quit the window"""
        if tk.messagebox.askokcancel("Quit", "Do you want to quit?"):
            root.destroy()

    # def pause(self):
    #     """Pause timer"""
    #     self.pause_button.configure(text="Resume", command=lambda: self.resume())
    #     self.master.bind("<Return>", lambda x: self.resume())
    #     if self.running == True:
    #         self.running = False
    #     # timerにポーズした時の値を入力する
    #     self.timer()
    #
    # def resume(self):
    #     """Resume timer"""
    #     self.pause_button.configure(text="Pause", command=lambda: self.pause())
    #     self.master.bind("<Return>", lambda x: self.pause())
    #     if self.running == False:
    #         self.running = True
    #     self.timer()




# この関数を直接読んだ場合、以下のコードを実行する。
if __name__ == "__main__":
    """Main loop of timer"""
# MODORI4
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
    root = tk.Tk()
    root.title("M4 Timer")

    # Application(root).pack(side="top", fill="both", expand=True)
    # MODORI4
    # 明示的に引数を指定することで
    Application(master=root, meigens=meigen_list).pack()
    # Application(master=root, meigens=meigen_list).pack(side="top", fill="both", expand=True)
    root.mainloop()
"""
参照
labelで改行しても左詰め
lbl = tkinter.Label(text=mes, bg='pink', width=30, anchor='e', justify='left')

"""
