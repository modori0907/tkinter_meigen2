# i = 0
# meigen_list = ["test1", "teest2", "teest3"]
# def display_meigen():
#     while i == 0:
#         for number, meigen in enumerate(meigen_list):
#             yield meigen_list[number]
#
# c = display_meigen()
# i = 0
#
# for i in range(0,3):
#     print(next(c))
#     print(f"{i}回目")
#     i += 1


import time
import math

from tkinter import *

# timer = True
# count=0
# while timer:
#     count_min = math.floor(count / 60)
#     count_sec = count % 60
#     print(f"{count_min}:{count_sec}")
#     time.sleep(1)
#     count+=1

def count_down(count):
    print(count)
    window.after(1000, count_down, count-1)



window = Tk()
window.title("")


window.mainloop()