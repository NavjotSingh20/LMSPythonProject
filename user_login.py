import firstFile
from firstFile import Books, edit_copies


class User:
    users_data = {}
    def __init__(self,user_id,name,books_borrowed,book1=None,book2=None,book3=None):
        self.user_id = user_id
        self.name = name
        self.books_borrowed = books_borrowed
        self.borrowed_books = [book1,book2,book3]

        User.users_data[user_id] = self

def load_users():
    userfile = open("user_data.txt", "r")
    lines = userfile.readlines()
    for line in lines[1:]:
        user_id, username, books_borrowed, book1, book2, book3 = line.strip().split(",")
        User(user_id, username, int(books_borrowed), book1, book2, book3)
    userfile.close()


def borrow_books(user_id, book_title):
    user = User.users_data.get(user_id)
    if not user:
        return "User not found."

    book = Books.books_title.get(book_title.lower())
    if not book:
        return "Book not found in library."
    if book.copies <= 0:
        return "No copies available."

    if user.books_borrowed >= 3:
        return "User has already borrowed the maximum number of books."

    if book_title in user.borrowed_books:
        return "User has already borrowed this book."

    user.borrowed_books[user.books_borrowed] = book_title
    user.books_borrowed += 1
    book.copies -= 1

    user_file = open("user_data.txt", "r")
    lines = user_file.readlines()
    user_file.close()

    updated_lines = []
    for line in lines:
        if line.startswith(user.user_id):
            updated_lines.append(
                f"{user.user_id},{user.name},{user.books_borrowed}," +
                f"{user.borrowed_books[0] or ''},{user.borrowed_books[1] or ''},{user.borrowed_books[2] or ''}\n"
            )
        else:
            updated_lines.append(line)

    user_file = open("user_data.txt", "w")
    user_file.writelines(updated_lines)
    user_file.close()

    edit_copies(book_title, book.copies)
    Books.refresh_data()

    return f"{book_title} successfully borrowed by {user.name}."

def return_books(user_id, book_title):
    user = User.users_data.get(user_id)
    if not user:
        return "User not found."

    if book_title not in user.borrowed_books:
        return "Book not found in the user's borrowed list."

    user.borrowed_books.remove(book_title)
    user.books_borrowed -= 1

    book = Books.books_title.get(book_title.lower())
    if book:
        book.copies += 1
    else:
        return "Error: Book not found in library data."

    user_file = open("user_data.txt", "r")
    lines = user_file.readlines()
    user_file.close()

    updated_lines = []
    for line in lines:
        if line.startswith(user.user_id):
            updated_lines.append(
                f"{user.user_id},{user.name},{user.books_borrowed}," +
                f"{user.borrowed_books[0] if len(user.borrowed_books) > 0 else ''}," +
                f"{user.borrowed_books[1] if len(user.borrowed_books) > 1 else ''}," +
                f"{user.borrowed_books[2] if len(user.borrowed_books) > 2 else ''}\n"
            )
        else:
            updated_lines.append(line)

    user_file = open("user_data.txt", "w")
    user_file.writelines(updated_lines)
    user_file.close()

    edit_copies(book_title, book.copies)
    Books.refresh_data()

    return f"{book_title} successfully returned by {user.name}."

def show_borrowed_books(user_id):
    user = User.users_data.get(user_id)
    if not user:
        return "User not found."

    borrowed_books = [book for book in user.borrowed_books if book]
    books_count = user.books_borrowed

    if books_count == 0:
        return f"{user.name} has not borrowed any books."
    else:
        return f"{user.name} has borrowed {books_count} books: {', '.join(borrowed_books)}."

