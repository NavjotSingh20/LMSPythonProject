class Books:
    class Fiction:
        all_books = []

    class Educational:
        all_books = []

    class Technology:
        all_books = []

    class History:
        all_books = []

    genres = {
        "Fiction": Fiction,
        "Educational": Educational,
        "Technology": Technology,
        "History": History,
    }

    books_title = {}
    books_author = {}

    original_titles = {}
    original_authors = {}

    def __init__(self, title, author, genre, copies):

        self.title = title
        self.author = author
        self.copies = copies


        Books.original_titles[title.lower()] = title
        Books.original_authors[author.lower()] = author

        if genre in Books.genres:
            Books.genres[genre].all_books.append(self)
        else:
            print("Genre not recognized")

        Books.books_title[title.lower()] = self

        if author.lower() not in Books.books_author:
            Books.books_author[author.lower()] = []

        Books.books_author[author.lower()].append(self)

    @classmethod
    def get_author_by_title(cls, title):
        book = cls.books_title.get(title.lower())
        if book:
            return cls.original_authors.get(book.author.lower())
        else:
            return "Book not found"

    @classmethod
    def get_books_by_author(cls, author):
        author = author.lower()
        books = cls.books_author.get(author)
        if books:
            return [cls.original_titles.get(book.title.lower()) for book in books]
        else:
            return "Book not found"


bfile = open("library_data.txt", "r")
lines = bfile.readlines()


for line in lines[1:]:
    title, author, genre, copies = line.strip().split(",")
    Books(title, author, genre, int(copies))

bfile.close()


a = input("Enter author name: ").strip()
print(Books.get_books_by_author(a))
