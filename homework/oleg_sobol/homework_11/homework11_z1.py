class Book:
    material = "бумага"
    has_text = True
    has_exercises = True

    def __init__(self, title, author, pages, isbn, reserved=False):
        self.title = title
        self.author = author
        self.pages = pages
        self.isbn = isbn
        self.reserved = reserved

    def reserve(self):
        self.reserved = True

    def __str__(self):
        return (f"Название: {self.title}, Автор: {self.author}, страницы: {self.pages}, "
                f"материал: {self.material}"
                + (", зарезервирована" if self.reserved else ""))


class SchoolBook(Book):

    def __init__(self, title, author, pages, isbn, subject, grade, reserved=False):
        super().__init__(title, author, pages, isbn, reserved)
        self.subject = subject
        self.grade = grade

    def __str__(self):
        return (f"Название: {self.title}, Автор: {self.author}, страницы: {self.pages}, "
                f"предмет: {self.subject}, класс: {self.grade}"
                + (", зарезервирована" if self.reserved else ""))


book11 = SchoolBook("Алгебра", "Иван Иванов", 200, "1234567890", "Математика", 9)
book12 = SchoolBook("История", "Сергей Сергеев", 150, "0987654321", "История", 10)
book13 = SchoolBook("География", "Андрей Андреев", 300, "1122334455", "География", 8)

book12.reserve()

book1 = Book("Идиот", "Федор Достоевский", 500, "1234567890")
book2 = Book("Война и мир", "Лев Толстой", 1200, "0987654321")
book3 = Book("Преступление и наказание", "Федор Достоевский", 700, "1122334455")
book4 = Book("Гарри Поттер", "Дж. К. Роулинг", 400, "2233445566")
book5 = Book("Мастер и Маргарита", "Михаил Булгаков", 300, "6677889900")

book5.reserve()

books = [book1, book2, book3, book4, book5]
for book in books:
    print(book)

textbooks = [book11, book12, book13]
for textbook in textbooks:
    print(textbook)
