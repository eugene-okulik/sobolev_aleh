import requests
from time import sleep

url = "https://www.google.ru/"
max_requests = 30
request_count = 0
while True:
    response = requests.get(url)
    print(f"Статус {url}: {response.status_code}")
    request_count += 1
    if request_count >= max_requests:
        break
    sleep(1)

print("Достигнуто максимальное количество запросов. Завершение работы.")