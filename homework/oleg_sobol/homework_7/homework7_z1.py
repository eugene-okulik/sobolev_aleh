import random

random_number = random.randint(0, 9)
while True:
    number = int(input("угадай цифру: "))
    if number == random_number:
        print("Поздравляю! Вы угадали!")
        break
    else:
        print("попробуйте снова")
