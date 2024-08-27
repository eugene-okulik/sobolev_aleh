import os
from datetime import datetime, timedelta


base_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
file_path = os.path.join(base_path, 'eugene_okulik', 'hw_13', 'data.txt')


def read_file():
    with open(file_path, 'r') as file:
        for line in file.readlines():
            yield line


lines = list(read_file())

date_1 = datetime.fromisoformat(lines[0].split(' - ')[0].split('. ')[1])
date_2 = datetime.fromisoformat(lines[1].split(' - ')[0].split('. ')[1])
date_3 = datetime.fromisoformat(lines[2].split(' - ')[0].split('. ')[1])

date_1_week_later = date_1 + timedelta(weeks=1)
day_of_week = date_2.strftime('%A')
days_ago = (datetime.now() - date_3).days

print(f"на неделю позже: {date_1_week_later}")
print(f"день недели: {day_of_week}")
print(f"дата была {days_ago} дней назад")
