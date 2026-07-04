class Library:
    print("="*40)
    print("      LIBRARY MANAGEMENT SYSTEM")
    print("="*40)

    def __init__(self):
        self.book=["Math","Phy","Chem"]

    def books(self):
          print("\nAvailable Books:")
          for i, book in enumerate(self.book, start=1):
            print(i, ".", book)

    def search(self):
        search_book=str(input("Enter search book name : "))

        if search_book in self.book:
            print("✓",search_book,"is avilable")

        else:
            print("❌ This book is unavailable")

    def issue(self):
        issue_book=str(input("Enter issue book name :"))

        if issue_book in self.book:
            print("✓ Book issued successfully")
            print("Your return date is 30 june")
            self.book.remove(issue_book)

        else:
            print("❌ This book is unavilable")  

    def return_book(self):
        returnn=str(input("Enter return book name : "))
        self.book.append(returnn)      
        print("✓ Book returned successfully")

    def add_book(self):
        add=str(input("Enter add book name : "))
        self.book.append(add)
        print("✓ Book added successfully")

    def exit(self):
        print("Thank you!")       

library=Library()

def menu():
    print("\n========== MENU ==========")
    print("1. View All Books")
    print("2. Search Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Add book")
    print("6. Exit")

while True:
    menu()
    choose=int(input("\nEnter your option : "))

    if choose==1:
        library.books()

    elif choose==2:  
        library.search()
        
    elif choose==3:
        library.issue()    

    elif choose==4:
        library.return_book()    

    elif choose==5:
        library.add_book()

    elif choose==6:
        print("Thank you!")    
        break

    else:
        print("❌ Invalid option")   