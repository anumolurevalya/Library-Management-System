
books = []

def add_book(title):
    books.append(title)
    print("Book added:", title)

def display_books():
    print("\nAvailable Books:")
    for book in books:
        print(book)

def search_book(title):
    if title in books:
        print("Book found:", title)
    else:
        print("Book not found:", title)

add_book("Python Programming")
add_book("Java Programming")
display_books()
search_book("Python Programming")
