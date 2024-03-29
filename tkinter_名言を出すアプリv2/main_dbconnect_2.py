import csv
import datetime
# MODORI4
import sqlite3
import tkinter as tk
import tkinter.messagebox
import tkinter.ttk as ttk


# TODO(m4) サブウインドウを開いて、コメント、成果を入れる
# TODO(m4) 機械学習をいれる。コメントなどをみて。曜日も入れるか
# TODO(m4) アマゾンの予定と連携するようにしたい

class Application(tk.Frame):
    category_list = ["褒めてあげたい", "頑張った", "普通", "不満", "だめだ"]

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

        # M4
        self.n = 0  # 名言をリストから表示させるための処理
        self.meigens = meigens  # 名言リストの初期化
        self.start_time = ""  # 開始時間
        self.end_time = ""  # 終了時間
        self.impression = ""  # 感想
        self.comment = ""  # 終わった時の感想

    def build_interface(self):

        self.meigen = tk.Label(self, text="")
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
        self.power_button = tk.Button(self, text="Start", command=lambda: self.start())
        self.power_button.grid(row=4, column=0, sticky="NE")

        self.reset_button = tk.Button(self, text="Reset", command=lambda: self.reset())
        self.reset_button.grid(row=4, column=1, sticky="NW")

        # TODO なんか見た目がカッコ悪いので考える
        # MODORI4
        # # 対象の項目を選択
        # self.category_button = tk.ttk.Combobox(self, values=self.category_list, width=4)
        # self.category_button.grid(row=4, column=2, sticky="NW")

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

    # TODO: make subwindow

    def write_results(self):
        self.write_results = tkinter.Toplevel()
        self.write_results.geometry("300x100")
        # xボタンを無効化する処理（表示はされるが押しても有効にならない）
        # 参照URL: https://teratail.com/questions/139235
        self.write_results.protocol('WM_DELETE_WINDOW', (lambda: 'pass')())
        self.write_results.title("I've tried!")

        self.impression_label = tkinter.Label(self.write_results, text="感想")
        self.impression_label.grid(row=0, column=0, padx=2, pady=3)

        self.impression = tkinter.ttk.Combobox(self.write_results, values=self.category_list)
        self.impression.grid(row=0, column=1, padx=2, pady=2)

        self.comment_label = tkinter.Label(self.write_results, text="一言")
        self.comment_label.grid(row=1, column=0, padx=2, pady=3)

        self.comment = tkinter.Entry(self.write_results)
        self.comment.grid(row=1, column=1, padx=2, pady=3)

        self.save_button = tkinter.Button(self.write_results, text="保存", command=lambda: self.write_result_add())
        self.save_button.grid(row=2, column=0, padx=2, sticky="N")

        # end_time = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')

    def write_result_add(self):

        """
        結果をcsvファイルに出力する処理
        :return:
        """

        end_time = datetime.datetime.now()
        date = end_time.strftime('%Y/%m/%d')
        week_of_day = end_time.strftime('%a')

        self.difference_time = ((end_time - self.start_time).seconds) // 60

        with open('life_log.csv', 'a', newline="") as f:
            fwriter = csv.writer(f, delimiter=",")
            # datetimeの引き算はtimedeltaのオブジェクトになる。そのままだとmilsesecondsまで表示されてしまうので、
            # minuteのオプションをつけて、分のみ表示させるようにした。

            fwriter.writerow(
                [date, week_of_day, self.start_time.strftime('%H:%M:%S'),
                 end_time.strftime('%H:%M:%S'),
                 self.difference_time, self.impression.get(), self.comment.get()])

        # ウインドウを閉じる処理
        self.write_results.destroy()

        # ２回目にサブウィンドウを開こうとするとエラーになってしまう。
        # （TypeError: 'Toplevel' object is not callable)
        # これを防ぐため、一旦オブジェクトを削除することにした
        del self.write_results

    def calculate(self):
        """time calculation"""
        # 取得した値をsecを変換
        self.hours = self.time // 3600
        # 1時間（つまり60)を超えたminは23
        self.mins = (self.time // 60) % 60
        self.secs = self.time % 60
        # {:02d}とは。書式設定。dは整数。0は埋め。2は桁数を指定。:は前に入れる.入れないと更新されない
        # 開始時間の取得
        self.set_time = "{:02d}:{:02d}:{:02d}".format(self.hours, self.mins, self.secs)
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
                # self.master.attributes("-topmost", True)  # メインウインドウを最前面に出す処理
                self.write_results()

            else:
                self.clock.configure(text=self.calculate())
                self.time -= 1
                self.after(1000, self.timer)

    # MODORI4

    def display_meigen(self):
        """
        名言を表示させる処理
        :return:
        """
        self.meigen_list = []
        con = sqlite3.connect('meigens.db')
        cursorObj = con.cursor()
        cursorObj.execute("SELECT * FROM meigens")
        meigens = cursorObj.fetchall()
        con.commit()
        for meigen in meigens:
            meigen_list.append(meigen[3])

        self.meigen_timer()

    def meigen_timer(self):
        """display meigen"""
        # runningがtrueであることを確認
        # falseになる条件は,stop
        # start,pause,resume関数から呼び出される
        # startを押下するとtimerを呼び出す
        # 1秒間隔で秒数を下げる

        if self.running:
            if self.time <= 0:
                self.meigen.configure(text="")

            elif len(meigen_list) == self.n:
                self.n = 0
                self.after(10000, self.meigen_timer)
            else:
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
        self.master.attributes("-topmost", False)  # メインウインドウを最前面に出さない処理、終了時出すようにしているので。
        # Enterで操作したときの動き
        self.master.bind("<Return>", lambda x: self.stop())
        self.running = True
        # timerを呼び出す。
        self.timer()
        # M4
        self.meigen_timer()
        self.start_time = datetime.datetime.now()

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


# この関数を直接読んだ場合、以下のコードを実行する。
if __name__ == "__main__":
    """Main loop of timer"""
    # MODORI4
    # DB接続
    meigen_list = []
    con = sqlite3.connect('meigens.db')
    cursorObj = con.cursor()
    cursorObj.execute("SELECT * FROM meigens")
    meigens = cursorObj.fetchall()
    for meigen in meigens:
        meigen_list.append(meigen[3])

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
