import firstFile
import user_login
from firstFile import Books, edit_copies, show_all_books
from user_login import User, borrow_books, return_books, show_borrowed_books, load_users
import adminlogin
from adminlogin import admins

print("THIS PROJECT WILL HELP YOU TO UNDERSTAND HOW A LIBRARY MANAGEMENT SYSTEM WORKS")
print("")
print("DONE BY GROUP NO-7 (NAVJOT SINGH, LAVDEEP SINGH, MANVI GAJRANI)")
print("TOPIC: LIBRARY MANAGEMENT SYSTEM")
print("")

Books.refresh_data()
load_users()

while True:
    print("\nMAIN MENU")
    print("Enter the desired option:")
    print('---------------------------------------------------------')
    print("1. USER LOGIN\n")
    print("2. ADMIN LOGIN\n")
    print("3. EXIT\n")
    print('---------------------------------------------------------')

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            user_id = input("Enter your User ID: ")

            if user_id in User.users_data:
                user = User.users_data[user_id]
                print(f"Welcome, {user.name}!")

                while True:
                    print("\nUSER MENU")
                    print("1. SEARCH A SPECIFIC BOOK")
                    print("2. BORROW A BOOK")
                    print("3. RETURN A BOOK")
                    print("4. VIEW ALL BOOKS")
                    print("5. SHOW MY BORROWED BOOKS")
                    print("6. EXIT TO MAIN MENU")

                    try:
                        user_choice = int(input("Enter your choice: "))

                        if user_choice == 1:
                            print("\nSEARCH MENU")
                            print("1. View books by author name")
                            print("2. View books by genre")
                            print("3. View books by title")
                            print("4. Exit search menu")

                            try:
                                search_choice = int(input("Enter your choice: "))

                                if search_choice == 1:
                                    author = input("Enter the author's name: ")
                                    books = Books.get_books_by_author(author)
                                    if books:
                                        print(f"Books by {author}: {', '.join(books)}")
                                    else:
                                        print("No books found for this author.")

                                elif search_choice == 2:
                                    genre = input("Enter the genre: ")
                                    if genre in Books.genres:
                                        books = [book.title for book in Books.genres[genre].all_books]
                                        print(f"Books in {genre}: {', '.join(books) if books else 'No books found.'}")
                                    else:
                                        print("Invalid genre.")

                                elif search_choice == 3:
                                    title = input("Enter the book title: ")
                                    author = Books.get_author_by_title(title)
                                    if author:
                                        print(f"The book '{title}' is written by {author}.")
                                    else:
                                        print("Book not found.")

                                elif search_choice == 4:
                                    break
                                else:
                                    print("Invalid choice. Please enter a number between 1 and 4.")

                            except ValueError:
                                print("Invalid input. Please enter a number.")

                        elif user_choice == 2:
                            book_title = input("Enter the title of the book to borrow: ")
                            result = borrow_books(user_id, book_title)
                            print(result)

                        elif user_choice == 3:
                            book_title = input("Enter the title of the book to return: ")
                            result = return_books(user_id, book_title)
                            print(result)

                        elif user_choice == 4:
                            print("\nAvailable books:")
                            show_all_books()

                        elif user_choice == 5:
                            result = show_borrowed_books(user_id)
                            print(result)

                        elif user_choice == 6:
                            print("Returning to the main menu...")
                            break

                        else:
                            print("Invalid choice. Please enter a number between 1 and 6.")

                    except ValueError:
                        print("Invalid input. Please enter a number.")

            else:
                print("Invalid User ID. Please try again.")

        elif choice == 2:
            print("Admin Login")
            username = input("Enter admin username: ")
            password = input("Enter admin password: ")

            if username in admins and admins[username] == password:
                print("Login successful!")
                while True:
                    print("\nADMIN MENU")
                    print("1. ADD A NEW BOOK")
                    print("2. RESTOCK A BOOK")
                    print("3. LOGOUT")

                    try:
                        admin_choice = int(input("Enter your choice: "))
                        if admin_choice == 1:
                            print("Add Books")
                            book_title = input("Enter book title: ")
                            book_author = input("Enter book author: ")
                            book_genre = input("Enter book genre: ")
                            try:
                                book_quantity = int(input("Enter quantity: "))
                                if book_title.lower() in Books.books_title:
                                    print("Book already exists. Use restock to add more copies.")
                                else:
                                    Books(book_title, book_author, book_genre, book_quantity)
                                    Books.save_to_file()
                                    print(f"Book '{book_title}' added successfully!")
                            except ValueError:
                                print("Invalid input for quantity. Please enter a number.")
                        elif admin_choice == 2:
                            print("Restock Books")
                            book_title = input("Enter the title of the book to restock: ")
                            if book_title.lower() in Books.books_title:
                                try:
                                    additional_copies = int(input("Enter the number of copies to add: "))
                                    book = Books.books_title[book_title.lower()]
                                    book.copies += additional_copies
                                    Books.save_to_file()
                                    print(f"{additional_copies} copies added to '{book_title}'.")
                                except ValueError:
                                    print("Invalid input for copies. Please enter a number.")
                            else:
                                print("No such book is available.")
                        elif admin_choice == 3:
                            print("Logging out...")
                            break
                        else:
                            print("Invalid choice. Please enter 1, 2, or 3.")
                    except ValueError:
                        print("Invalid input. Please enter a number.")
            else:
                print("Invalid credentials.")
        elif choice == 3:
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")
    except ValueError:
        print("Invalid input. Please enter a number.")