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
    """
    Выводи на экран все книги
    """
    if not library:
        print("")
        print("Книг нету!")
        print("")
        return
    for num, book in enumerate(library, 1):
        print("номер на полке:", num)
        print("название:", book["название"])
        print("автор:", book["автор"])
        print("год:", book["год"])
        print("")


def add_book() -> None:

    """

    Добавляет уникальную книгу, если автор,название или год выпуска различаются иначе return

    """

    title = input("Введите название книги:")
    if not title:
       print("НЕТ НАЗВАНИЯ!")
       print("")
       return
    author = input("Введите имя автора:")
    if not author:
       print("НЕТ АВТОРА!")
       print("")
       return
    year = input("Введите год издания:")
    if year.isdigit():
       year = int(year)
    else:
       print("Вводите цифры!")
       print("")
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
    print("")
    print(f"Книга {book['название']} успешно добавлена")
    print("")

def remove_book() -> None:
    """
    удаляет книгу по номеру
    """
    if not library:
        print("библиотека пуста!")
        return

    num = input("Введите порядковый номер книги для удаления ")

    if num.isdigit():
        num = int(num)
    else:
        print("номер должен быть больше нуля!")
        return

    idx = num -1

    if idx < 0 or idx >= len(library):
        print("такой книги нет!")
        return


    print("")
    print(f"Книга {library[idx]['название']} удалена")
    print("")
    library.pop(idx)




remove_book()

show_all_books()

