book_we_want = input()

checked_books = 0

while True:
    current_search = input()
    if current_search == book_we_want:
        print(f"You checked {checked_books} books and found it.")
        break
    if current_search == "No More Books":
        print(f"The book you search is not here!")
        print(f"You checked {checked_books} books.")
        break
    checked_books += 1
