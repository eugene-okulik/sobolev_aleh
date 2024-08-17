from datetime import datetime


def parse_date(date_str):
    return datetime.strptime(date_str, "%b %d, %Y - %H:%M:%S")


def get_full_month_name(date_obj):
    return date_obj.strftime("%B")


def format_date(date_obj):
    return date_obj.strftime("%d.%m.%Y, %H:%M")


def main():
    date_str = "Jan 15, 2023 - 12:05:33"
    date_obj = parse_date(date_str)
    print(get_full_month_name(date_obj))
    print(format_date(date_obj))


if __name__ == "__main__":
    main()
