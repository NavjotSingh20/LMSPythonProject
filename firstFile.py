class Books:
    books_title = {}
    books_author = {}
    
    def __init__(self, title, author, genre, copies):
        self.title = title
        self.author =  author
        self.genre = genre
        self.copies = copies

        Books.books_title[title] = self
        Books.books_author[author] = self

    @classmethod
    def get_author_by_title(cls, title):
        book = cls.books_title.get(title)
        if book:
            return book.author
        else:
            return "Book not found"

    @classmethod
    def get_title_by_author(cls, author):
        book = cls.books_author.get(author)
        if book:
            return book.title
        else:
            return "Book not found"

#Sub class for genres can be added for further advancement

book1 = Books("Test Title", "Test Author", "Tech", 500)
book2 = Books("Test Title 2", "Test Author", "horror", 500)
a = input("Enter author name: ")
print(Books.get_title_by_author(a))