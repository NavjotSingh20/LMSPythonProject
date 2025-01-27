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
        self.genre = genre
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

    @classmethod
    def clear_all(cls):
        for genre in cls.genres.values():
            genre.all_books.clear()

        cls.books_title.clear()
        cls.books_author.clear()

    @classmethod
    def refresh_data(cls):
        Books.clear_all()

        bfile = open("library_data.txt", "r")
        lines = bfile.readlines()

        for line in lines[1:]:
            title, author, genre, copies = line.strip().split(",")
            Books(title, author, genre, int(copies))

        bfile.close()

    @classmethod
    def save_to_file(cls):
        with open("library_data.txt", "w") as file:
            file.write("Title,Author,Genre,Copies\n")
            for book in cls.books_title.values():
                file.write(f"{book.title},{book.author},{book.genre},{book.copies}\n")


def load_books():
    bfile2 = open("library_data.txt", "r")
    lines = bfile2.readlines()
    for line in lines[1:]:
        title, author, genre, copies = line.strip().split(",")
        Books(title, author, genre, int(copies))
    bfile2.close()


def edit_copies(title, new_copies):
    bfile3 = open("library_data.txt", "r")
    lines = bfile3.readlines()
    updated_lines = []
    book_found = False

    for line in lines:
        file_title, author, genre, copies = line.strip().split(",")
        if file_title.lower() == title.lower():
            book_found = True
            updated_lines.append(f"{file_title},{author},{genre},{new_copies}\n")
        else:
            updated_lines.append(line)

    bfile3.close()

    if not book_found:
        print("Error")
        return

    bfile4 = open("library_data.txt", "w")
    bfile4.writelines(updated_lines)
    bfile4.close()

    Books.refresh_data()


def show_all_books():
    # Collecting all books from all genres
    all_books = []
    for genre in Books.genres.values():
        all_books.extend(genre.all_books)

    if not all_books:
        print("No books available in the library.")
        return

    print("List of all books:")
    for book in all_books:
        print(f"'{book.title}' by {book.author}")
