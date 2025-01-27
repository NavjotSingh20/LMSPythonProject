import firstFile
from firstFile import Books

# dictionary to store admin credentials
admins = {
    "admin1": "password1",
    "admin2": "password2"
}


def admin_login():
    print("admin login")
    username = input("enter admin username:")
    password = input("enter admin password:")
    if username in admins and admins[username] == password:
        print("login successful")
        return True
    else:
        print("invalid credentials")
        return False


def add_new_book():
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    genre = input("Enter book genre: ")
    if genre not in Books.genres:
        return "Invalid genre."
    try:
        copies = int(input("Enter quantity: "))
        if title.lower() in Books.books_title:
            return "Book already exists. Use restock to add more copies."
        else:
            Books(title, author, genre, copies)
            Books.save_to_file()  # Save the new book to the file
            return "Book added successfully!"
    except ValueError:
        return "Invalid input for quantity."



def restock_book():
    title = input("Enter book title: ")
    if title.lower() in Books.books_title:
        try:
            additional_copies = int(input("Enter additional copies: "))
            book = Books.books_title[title.lower()]
            book.copies += additional_copies
            Books.save_to_file()  # Save the updated number of copies to the file
            return "Book restocked successfully!"
        except ValueError:
            return "Invalid input for additional copies."
    else:
        return "Book not found in library."


def admin_menu():
    while True:
        print("1 : add new book")
        print("2 : restock book")
        print("3 : logout")

        choice = int(input("enter your choice"))
        if choice == 1:
            add_new_book()
        elif choice == 2:
            restock_book()
        elif choice == 3:
            print("logging out")
            break
        else:
            print("invalid choice")


def main():
    print("welcome")

    while True:
        if admin_login():
            admin_menu()
            break
        else:
            retry = input("do you want to try again ? yes/no")
            if retry.lower() != "yes":
                print("exiting the system")
                break


if __name__ == "__main__":
    main()