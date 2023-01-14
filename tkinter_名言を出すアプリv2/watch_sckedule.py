# TODO(modori4) 最後に感想を入力するフィールドを設ける
# TODO(modori4) 実施した時間をメモる
# TODO(modori4) 開始時にやる内容を明記する
# TODO(modori4) 感想や得点を記載する。あとでまとめられるようにする

import sql



"""

時間は自動入力　開始、終了
得点は手動
コメントを残す

"""
import datetime
import csv


# with open('eggs.csv', 'w', newline='') as csvfile:
#     spamwriter = csv.writer(csvfile, delimiter='',
#                             quotechar='|', quoting=csv.QUOTE_MINIMAL)
#
#     spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
#     spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])

dt_now = datetime.datetime.now()
with open('test.csv', 'w+', newline="") as f:
    fwriter = csv.writer(f, delimiter=",")
    fwriter.writerow([dt_now, "Good", "強い気持ちで頑張りますね"])
