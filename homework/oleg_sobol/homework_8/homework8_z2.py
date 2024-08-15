import sys

sys.set_int_max_str_digits(100000)


def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def get_fibonacci_number(position, fib_gen):
    number = 0
    for _ in range(position):
        number = next(fib_gen)
    return number


def main():
    fib_gen = fibonacci_generator()
    fib_5 = get_fibonacci_number(5, fib_gen)
    fib_200 = get_fibonacci_number(200, fib_gen)
    fib_1000 = get_fibonacci_number(1000, fib_gen)
    fib_100000 = get_fibonacci_number(100000, fib_gen)

    print(f"5е число Фибоначчи: {fib_5}")
    print(f"200е число Фибоначчи: {fib_200}")
    print(f"1000е число Фибоначчи: {fib_1000}")
    print(f"100000е число Фибоначчи: {fib_100000}")


if __name__ == "__main__":
    main()
