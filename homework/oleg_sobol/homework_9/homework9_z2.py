def is_hot_days(value, temperatures):
    return list(filter(lambda temp: temp > value, temperatures))


def calculate_statistics(temps):
    if temps:
        max_temp = max(temps)
        min_temp = min(temps)
        avg_temp = sum(temps) / len(temps)
        return max_temp, min_temp, avg_temp
    return None, None, None


def main():
    temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29, 31, 33, 31, 30,
                    32, 30, 28, 24, 23]

    hot_days = is_hot_days(28, temperatures)
    max_temp, min_temp, avg_temp = calculate_statistics(hot_days)

    print(f"Самая высокая температура: {max_temp}")
    print(f"Самая низкая температура: {min_temp}")
    print(f"Средняя температура: {avg_temp:.2f}")


if __name__ == "__main__":
    main()
