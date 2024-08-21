def operation_decorator(func):
    def wrapper(first, second, operation=None):
        if first == second:
            operation = '+'
        elif first < 0 or second < 0:
            operation = '*'
        elif second > first:
            operation = '/'
        elif first > second:
            operation = '-'
        return func(first, second, operation)
    return wrapper


@operation_decorator
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '*':
        return first * second
    elif operation == '/':
        return first / second
    elif operation == '-':
        return first - second


def main():
    first = int(input("Введите первое число: "))
    second = int(input("Введите второе число: "))
    result = calc(first, second, operation=None)
    print(f"Результат: {result}")


if __name__ == "__main__":
    main()
