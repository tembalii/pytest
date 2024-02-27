from book import Book
from member import Member

def main():
    book1 = Book("Harry Potter", "J.K. Rowling")
    book1.display_info()

    member1 = Member("John Doe", "12345")
    member1.display_info()

if __name__ == "__main__":
    main()
