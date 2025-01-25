print("THIS PROJECT WILL HELP YOU TO UNDERSTAND HOW A LIBRARY MANAGEMENT SYSTEM WORKS ")
print("")
print("")
print("")
print("")
print("")
print("")
print("DONE BY GROUP  NO- 7 (NAVJOT SINGH, LAVDEEP SINGH, MANVI GAJRANI  ")
print("                TOPIC:-  LIBRARY MANAGEMENT SYSTEM       ")
while True:
    print("Enter the desired option:- ")
    print('---------------------------------------------------------------------')

    print('---------------------------------------------------------------------')
    print("")
    print("")
    print("1.USER LOGIN")
    print("")
    print("2.ADMIN LOGIN")
    print('---------------------------------------------------------------------')

    print('---------------------------------------------------------------------')
    choice = eval(input("Enter the choice from the above options:- "))

    if choice == 1:
        x= input("Enter your UserName:- ")
        y= input("Enter your Password:-  ")


        while True:
            print("1.SEARCH A SPECIFIC BOOK  ")

            print("2. BORROW A BOOK  ")

            print("3. RETURN A BOOK  ")

            print("4. VIEW ALL BOOKS  ")

            print("5. EXIT TO MAIN MENU  ")

            a=eval(input("Enter the choice from above menu:- "))

            if a==1:

                while True:
                    print("1. VIEW BOOK BY AUTHOR NAME ")

                    print("2. VIEW BOOK BY GENRE  ")

                    print("3. VIEW BOOK BY TITLE  ")

                    print("4. TO GO TO PREVIOUS MENU, PRESS ENTER ")

                    b=eval(input("Enter The Desired Option :- "))

                    if b ==1:

                        break

                    elif b ==2:

                        break

                    elif b==3:

                        break

                    else:

                        break

    elif choice ==2:
        u= input("Enter UserName:-  ")
        v = input("Enter Password:-   ")
