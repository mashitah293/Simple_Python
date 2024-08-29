class Book:
    total_books = 0

    def __init__(self, title, author):
    
        self.title = title
        self.author = author
        Book.total_books += 1

    def get_info(self):
        
        return f"Title: {self.title}, Author: {self.author}"
    @classmethod
    def get_total_books(cls):
    
        return cls.total_books
    @staticmethod
    def is_valid_title(title):
        
        return isinstance(title, str) and bool(title.strip())

book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
book3 = Book("", "Unknown Author")

print(book1.get_info())  
print(book2.get_info()) 
print(Book.get_total_books())
print(Book.is_valid_title("1984"))  
print(Book.is_valid_title(""))      

