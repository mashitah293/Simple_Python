
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
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book2 = Book("Pride and Prejudice", "Jane Austen")

# Step 2: Print the information of each book using the get_info method
print(book1.get_info())  # Expected Output: Title: The Great Gatsby, Author: F. Scott Fitzgerald
print(book2.get_info())  # Expected Output: Title: Pride and Prejudice, Author: Jane Austen

# Step 3: Use the static method to check if a book title is valid
valid_title_check1 = Book.is_valid_title("The Catcher in the Rye")
valid_title_check2 = Book.is_valid_title("")

print(f"Is 'The Catcher in the Rye' a valid title? {valid_title_check1}")  # Expected Output: True
print(f"Is '' a valid title? {valid_title_check2}")                        # Expected Output: False

# Step 4: Print the total number of books created using the class method
print(f"Total number of books created: {Book.get_total_books()}")  # Expected Output: 2
