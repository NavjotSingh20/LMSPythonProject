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

    def __init__(self, title, author, genre, copies):
        self.title = title
        self.author = author
        self.copies = copies

        if genre in Books.genres:
            Books.genres[genre].all_books.append(self)
        else:
            print("Genre not recognized")

        Books.books_title[title] = self
        if author not in Books.books_author:
            Books.books_author[author] = []

        Books.books_author[author].append(self)

    @classmethod
    def get_author_by_title(cls, title):
        book = cls.books_title.get(title)
        if book:
            return book.author
        else:
            return "Book not found"

    @classmethod
    def get_books_by_author(cls, author):
        books = cls.books_author.get(author)
        if books:
            return [book.title for book in books]
        else:
            return "Book not found"


bfile = open("library_data.txt", "r")
lines = bfile.readlines()
for lines in lines[1:]:
    title, author, genre, copies = lines.strip().split(",")
    Books(title, author, genre, int(copies))

print(Books.Educational.all_books)

bfile.close()