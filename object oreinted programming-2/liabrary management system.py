class Library:
    def __init__(self, list, name):
        self.bookslist = list
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        print(f"Welcome to the {self.name} library. Here is the list of books available:")
        for book in self.bookslist:
            print(book)

    def lendBook(self, user, book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Lender-Book database has been updated. You can take the book now.")
        else:
            print(f"Book is already being used by {self.lendDict[book]}")
            
    def addBook(self, book):
        self.bookslist.append(book)
        print("Book has been added to the list.")   

    def returnBook(self, book):
        self.lendDict.pop(book)
if __name__ == "__main__":

         books = Library(["Python", "C++", "Java", "JavaScript", "C#"], "Let's Upskill")

         while True:
                print(f"Welcome to the {books.name} library. Enter your choice:")
                print("1. Display books")
                print("2. Lend a book")
                print("3. Add a book")
                print("4. Return a book")
                user_choice = input()
                if user_choice not in ["1", "2", "3", "4"]:
                   print("Invalid choice. Please try again.")
                   continue
                else:
                  user_choice = int(user_choice)

                if user_choice == 1:
                    books.displayBooks()
                elif user_choice == 2:
                    book = input("Enter the name of the book you want to lend: ")
                    user = input("Enter your name: ")
                    books.lendBook(user, book)
                elif user_choice == 3:
                    book = input("Enter the name of the book you want to add: ")
                    books.addBook(book)
                elif user_choice == 4:
                    book = input("Enter the name of the book you want to return: ")
                    books.returnBook(book)
                else:
                    print("Invalid choice. Please try again.")    
                
                print("Press q to quit and c to continue")
                user_choice2 = ""
                while (user_choice2 != "c" and user_choice2!= "q"):
                    user_choice2 = input()
                    if user_choice2 == "q":
                        exit()

                    elif user_choice2 == "c":
                        continue  


        