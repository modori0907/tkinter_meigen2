import json

# coins = [
#     {
#         "symbol" : "BTC",
#         "amount_owned": 2,
#         "price_per_coin": 3200
#     },
#     {
#         "symbol": "BTS",
#         "amount_owned": 4,
#         "price_per_coin": 6200
#     }
# ]
#
# for coin in coins:
#     print(coin["price_per_coin"])


"""ジェネレーターの試験"""


# def power(values):
#     for value in values:
#         print('%sを供給' % value)
#         yield value

# def adder(values):
#     for value in values:
#         print('%sに値を追加' % value)
#         if value % 2 == 0:
#             yield value + 3
#         else:
#             yield value + 2
# elements = [1, 4, 7, 9, 12, 19]
# results = adder(power(elements))
#
# print(next(results))
# print(next(results))
# print(next(results))


# def psychologist():
#     print('Please your annoying?')
#     while True:
#         answer = (yield)
#         if answer is not None:
#             if answer.endswith('?'):
#                 print("Don't ask yourself a lots")
#             elif 'Good' in answer:
#                 print("It's good idea. Let's do it")
#             elif 'Bad' in answer:
#                 print("Don't think bad things")
#
# free = psychologist()
# next(free)
# free.send('Bad')
# free.send('I do not know?')


# クラス変数のテスト
#
class T(object):
    def __init__(self, meigens, *args, **kwargs):
        self.meigens = meigens
        print(self.meigens)
    def testprint(self):
        for meigen in self.meigens:
            print(meigen)

test = [1,2,3,4,5]
t = T(test)

t.testprint()


# class Person(object):
#     def
#
#
#         self.name = name
#         print(self.name)
#
#     def say_something(self):
#         print("hello")
#
#
# person = Person()
# person.say_something()
