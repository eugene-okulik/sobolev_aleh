results = [
    "результат операции: 42",
    "результат операции: 54",
    "результат работы программы: 209",
    "результат: 2"
]


def calc(numb):
    number = int(numb[numb.index(':') + 2:])
    return number + 10


for i in results:
    print(calc(i))
