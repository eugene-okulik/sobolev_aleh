import random


def add_random_bonus(value):
    random_value = random.randint(500, 1000)
    return value + random_value


def get_total_salary(value, is_bonus):
    if is_bonus:
        return add_random_bonus(value)
    else:
        return value


def main():
    salary = int(input("Введите число: "))
    is_random_bonus: bool = bool(random.choice([True, False]))
    total_salary = get_total_salary(salary, is_random_bonus)

    print(f"{salary}, {is_random_bonus}, - '${total_salary}'")


if __name__ == "__main__":
    main()
