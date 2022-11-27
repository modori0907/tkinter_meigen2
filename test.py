i = 0
meigen_list = ["test1", "teest2", "teest3"]
def display_meigen():
    while i == 0:
        for number, meigen in enumerate(meigen_list):
            yield meigen_list[number]

c = display_meigen()
i = 0

for i in range(0,3):
    print(next(c))
    print(f"{i}回目")
    i += 1

