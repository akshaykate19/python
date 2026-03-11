books=[]
while True:
    print("-- e-Library---")
    print("1:AddBooks\n2:ShowBooks\n3:UpdateBook\n4:DeleteBook\n5:Exit")
    choice=int(input("Enter Choice Number :"))
    if choice==1:
        title=input("Enter books title : ").lower()
        if title not in books:
           books.append(title)
           print(f"{title} Books added successfully !")
        else:
             print(f"{title} Book is already exists so add another book!!")
    elif choice==2:
        if len(books)==0:
            print("No books available try again")
        else:
            print("Available books are :",books)
    elif choice==3:
        if len(books)>0:
            old_book_tittle=input("Enter book tittle to update:").capitalize()
            if old_book_tittle in books:
                new_title=input("Enter book new title to update :").capitalize()
                books[books.index(old_book_tittle)]=new_title.capitalize()
                print(f"{old_book_tittle} Book title updated successfully!!")
            else:
                print(f"{old_book_tittle} Book title not found try again !!")
        else:
            print("No Books Available so first add the books!!")
    elif choice==4:
            if len(books)>0:
                old_book_tittle=input("Enter book tittle to remove:").capitalize()
                if old_book_tittle in books:
                    books.remove(old_book_tittle.capitalize())
                    print(f"{old_book_tittle}Book removed successfully !!")
                else:
                    print(f"{old_book_tittle} Book title not found try again !!")
            else:
                print("No Books Available so first add the books!!")
    elif choice==5:
        print("Thanks for using our services!!")
        break