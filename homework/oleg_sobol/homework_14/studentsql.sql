INSERT INTO students (name, second_name, group_id)
VALUES ('Oleg', 'Sobol', NULL);

INSERT INTO books (title, taken_by_student_id)
VALUES ('Introduction to Databases 22', 2014),
       ('Advanced SQL 22', 2014);

INSERT INTO `groups` (title, start_date, end_date)
VALUES ('Group A 2014', '2024-09-01', '2025-06-01');

UPDATE students
SET group_id = (SELECT id FROM `groups` WHERE title = 'Group A 2014')
WHERE id = 2014;

INSERT INTO subjets (title)
VALUES ('Math 22'),
       ('Physics 22');

INSERT INTO lessons (title, subject_id)
VALUES ('Algebra 22', (SELECT id FROM subjets WHERE title = 'Math 22')),
       ('Geometry 22', (SELECT id FROM subjets WHERE title = 'Math 22')),
       ('Mechanics 22', (SELECT id FROM subjets WHERE title = 'Physics 22')),
       ('Optics 22', (SELECT id FROM subjets WHERE title = 'Physics 22'));

INSERT INTO marks (value, lesson_id, student_id)
VALUES ('9+', (SELECT id FROM lessons WHERE title = 'Algebra 22'), 2014),
       ('8+', (SELECT id FROM lessons WHERE title = 'Geometry 22'), 2014),
       ('7+', (SELECT id FROM lessons WHERE title = 'Mechanics 22'), 2014),
       ('6+', (SELECT id FROM lessons WHERE title = 'Optics 22'), 2014);

SELECT value
FROM marks
WHERE student_id = 2014;

SELECT title
FROM books
WHERE taken_by_student_id = 2014;

SELECT
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
    s.id = 2014;
