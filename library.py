def borrow_book(self, patron_name, book_title):
    patron = next((p for p in self.patrons if p.name == patron_name), None)
    book = next((b for b in self.books if b.title == book_title), None)

    if patron and book:
        if book.available:
            book.available = False
            patron.borrowed_books.append(book)
            print(f"{patron_name} borrowed '{book_title}'.")
        else:
            print("Book is already borrowed.")
    else:
        print("Patron or book not found.")


def return_book(self, patron_name, book_title):
    patron = next((p for p in self.patrons if p.name == patron_name), None)

    if patron:
        for book in patron.borrowed_books:
            if book.title == book_title:
                book.available = True
                patron.borrowed_books.remove(book)
                print(f"{patron_name} returned '{book_title}'.")
                return

    print("Book or patron not found.")