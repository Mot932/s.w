library = [
    {
    "название": "Введение в Python. Том 1",
    "автор": "Марк Лутц",
    "год": 2022
    },
    {
    "название": "Введение в Python. Том 2",
    "автор": "Марк Лутц",
    "год": 2023
    }

]


def show_all_books():
    for num, book in enumerate(library, 1):
        print("номер на полке", num)
        print("название", book["название"])
        print("автор", book["автор"])
        print("год", book["год"])
        print("")


def add_book():
   title = input("Введите название книги:")
   if not title:
       print("НЕТ НАЗВАНИЯ!")
       return
   author = input("Введите имя автора:")
   if not author:
       print("НЕТ АВТОРА!")
       return
   year = input("Введите год издания:")
   if not year:
       print("НЕТ ГОДА ИЗДАНИЯ!")
   if year.isdigit():
       year = int(year)
   else:
       print("Вводите цифры!")
       return

   book = {
    "название": title,
    "автор": author,
    "год": year,
   }
   if book in library:
       print("")
       print("такая книга уже есть!")
       print("")
       return


   library.append(book)

add_book()

show_all_books()
