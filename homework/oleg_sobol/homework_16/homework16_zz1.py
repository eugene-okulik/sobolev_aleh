import mysql.connector as mysql
import os
import csv
from dotenv import load_dotenv


load_dotenv()

db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
)

cursor = db.cursor(dictionary=True)

base_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
csv_file_path = os.path.join(
    base_path, 'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv'
)

with open(csv_file_path, newline='') as csv_file:
    file_data = csv.reader(csv_file)
    headers = next(file_data)
    csv_data = [row for row in file_data]
for row in csv_data:
    print(row)

missing_data = []

for row in csv_data:
    name, second_name, group_title, book_title, subject_title, lesson_title, mark_value = row

    query = """
    SELECT students.name, students.second_name, `groups`.title as group_title, books.title as book_title,
           subjets.title as subject_title, lessons.title as lesson_title, marks.value as mark_value
    FROM students
    JOIN `groups` ON students.group_id = `groups`.id
    LEFT JOIN books ON students.id = books.taken_by_student_id
    LEFT JOIN marks ON students.id = marks.student_id
    LEFT JOIN lessons ON marks.lesson_id = lessons.id
    LEFT JOIN subjets ON lessons.subject_id = subjets.id
    WHERE students.name = %s AND students.second_name = %s AND `groups`.title = %s
    AND books.title = %s AND subjets.title = %s AND lessons.title = %s AND marks.value = %s
    """

    cursor.execute(query, (name, second_name, group_title, book_title, subject_title, lesson_title, mark_value))
    result = cursor.fetchone()
    if not result:
        missing_data.append(row)

if missing_data:
    print("missing date:")
    for row in missing_data:
        print(row)
else:
    print("all date good!!!")

cursor.close()
db.close()
