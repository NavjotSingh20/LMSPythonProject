import firstFile
from firstFile import books_title
#dictionary to store admin credentials 
#dictionary to store admin credentials
admins={
    "admin1":"password1",
    "admin2":"password2"
}
def admin_login():
     print ("admin login")
username=input("enter admin username:")
password=input("enter admin password:")
if username in admins and admins[username]==paassword:
        print("login successful")
else:
        print("invalid credentials")

def add_new_book():
     print("add books")
     book_title=input("enter book title")
     book_author=input("enter book author")
     book_quantity=int(input("enter quantity"))
     if book_title in books_title:
         print ("book already exists ,use restock to add more books")
     else:
         print("added successfully")

def restock_book():
      print("restock books")
      book_title=input("enter title")
      if book_title in books_title:
           additional_copies=int(input("enter the number of copies"))
           book_title.copies+=additional_copies
      else:
           print("no such book is available")

def admin_menu():
     while True:
         print("1 : add new book")
         print("2 : restock book")
         print("3 : logout")

     choice=int(input("enter your choice"))
     if choice==1:
           add_new_book()
     elif choice==2:
           restock_book()
     elif choice==3:
           print("logging out")
     else:
           print("invalid choice")

def main():
        print("welcome")
