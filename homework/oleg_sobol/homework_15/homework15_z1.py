import mysql.connector as mysql

db = mysql.connect(
    user="st-onl",
    password="AVNS_tegPDkI5BlB2lW5eASC",
    host="db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com",
    port=25060,
    database="st-onl"
)
cursor = db.cursor()

cursor.execute("INSERT INTO students (name, second_name) VALUES (%s, %s)",
               ("Oleg ee", "Sobol ee"))
student_id = cursor.lastrowid

cursor.execute("INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)",
               ("Group A ee", "2024-09-01 ee", "2025-05-31 ee"))
group_id = cursor.lastrowid

cursor.execute("UPDATE students SET group_id = %s WHERE id = %s",
               (group_id, student_id))

cursor.execute("INSERT INTO subjets (title) VALUES (%s)",
               ("Mathematics ee",))
subject_id_math = cursor.lastrowid
cursor.execute("INSERT INTO subjets (title) VALUES (%s)",
               ("Literature ee",))
subject_id_lit = cursor.lastrowid

cursor.execute("INSERT INTO lessons (title, subject_id) VALUES (%s, %s)",
               ("Lesson 1  Math ee", subject_id_math))
lesson_id_math1 = cursor.lastrowid
cursor.execute("INSERT INTO lessons (title, subject_id) VALUES (%s, %s)",
               ("Lesson 2  Math ee", subject_id_math))
lesson_id_math2 = cursor.lastrowid

cursor.execute("INSERT INTO lessons (title, subject_id) VALUES (%s, %s)",
               ("Lesson 1  Literature ee", subject_id_lit))
lesson_id_lit1 = cursor.lastrowid
cursor.execute("INSERT INTO lessons (title, subject_id) VALUES (%s, %s)",
               ("Lesson 2  Literature ee", subject_id_lit))
lesson_id_lit2 = cursor.lastrowid

cursor.execute("INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)",
               ("Databases ee", student_id))
cursor.execute("INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)",
               ("SQL ee", student_id))

cursor.execute("INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)",
               ("9", lesson_id_math1, student_id))
cursor.execute("INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)",
               ("8", lesson_id_math2, student_id))
cursor.execute("INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)",
               ("7", lesson_id_lit1, student_id))
cursor.execute("INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)",
               ("6", lesson_id_lit2, student_id))

db.commit()

cursor.execute("SELECT value FROM marks WHERE student_id = %s",
               (student_id,))
marks = cursor.fetchall()
print(marks)

cursor.execute("SELECT title FROM books WHERE taken_by_student_id = %s",
               (student_id,))
books = cursor.fetchall()
print(books)

cursor.execute("""SELECT
    s.name AS 'Имя',
    s.second_name AS 'Фамилия',
    g.title AS 'Группа',
    g.start_date AS 'Начало',
    g.end_date AS 'Конец',
    b.title AS 'Книги',
    m.value AS 'Оценки',
    l.title AS 'Занятия',
    subj.title AS 'Предметы'
FROM
    students s
LEFT JOIN
    `groups` g ON s.group_id = g.id
LEFT JOIN
    books b ON s.id = b.taken_by_student_id
LEFT JOIN
    marks m ON s.id = m.student_id
LEFT JOIN
    lessons l ON m.lesson_id = l.id
LEFT JOIN
    subjets subj ON l.subject_id = subj.id
WHERE
    s.id = %s
""", (student_id,))

info = cursor.fetchall()
print(info)

cursor.close()
db.close()
