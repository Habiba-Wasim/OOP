class Book:
    total_books = 0  

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1  

    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.increment_book_count()  
        
book1 = Book("Python 101", "Coder")
book2 = Book("Advanced Python", "Habiba")

print("Total books added:", Book.total_books)