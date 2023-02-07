import os

def choose_option(options: list) -> int:
    """
    Описание ситуации где происходит выбор
    Принимает Список вариантов
    Спросить пользователя какой вариант
    Проверяет есть ли вариант пользователя в возможных вариантах
    Если есть, возращяет вариант пользователя
    """

    option = input("\nВведите номер варианта и нажимите Enter ")
    try: # что пробуем сделать?
        option = int(option)
    except ValueError: # сработает если try с ошибкой
        print("Эй, вводите целое неотрицательное число!")
    else: # выполниться если try без ошибки
        if option < len(options) and option > -1:
            return option 
        else:
            print("Такой выбор невозможен!")


def show_options(options: list):
    for num, options in enumerate(options, 1):
        print(f"{num}) {options}.")

def show_menu():
    print("Библиотека деревни Гадюкино")
    options = [
        "Показать все книги",
        "Добавить книгу",
        "Удалить книгу",
        "Найти книгу по номеру",
        "Найти книгу по названию",
        "Найти книгу по автору",
        "Найти книгу по году",
        "Выход"
    ]
    show_options(options)
    option = input("\nВведите номер варианта и нажимите Enter ")
    if option == "1":
        return show_books()
    if option == "2":
        return add_book()
    if option == "3":
        return remove_book()
    if option == "4":
        return search_by_number()
    if option == "5":
        return search_book_by_key('Название')
    if option == "6":
        return search_book_by_key('Автор')
    if option == "7":
        return search_book_by_key('Год выпуска')
    if option == "8":
        return leave() 



library = [
    {
        "Название": "Введение в python. Том 1",
        "Автор": "Лутц Марк",
        "Год выпуска": 2019
    },
    {
        "Название": "Введение в python. Том 2",
        "Автор": "Лутц Марк",
        "Год выпуска": 2019
    },
    {
        "Название": "Литература 7 класс",
        "Автор": "Минпросвещение",
        "Год выпуска": 2017
    },
    {
        "Название": "Mags Life",
        "Автор": "mag",
        "Год выпуска": 2023
    }

]

def show_books():
    if not library:
        print("Библиотека пуста!")
        return
    for num, book in enumerate(library, 1):
        print("Номер на полке:", num)
        print('Название:', book["Название"])
        print('Автор:', book["Автор"])
        print('Год выпуска:', book["Год выпуска"])
        print("")


def add_book() -> None:
    title = input("Введите название книги: ")
    if not title:
        print("Ошибка! Нет автора")
        return
    author = input("Введите имя Автора: ")
    if not author:
        print("Ошибка! Нет года издания")
        return
    year = input("Введите год издания: ")
    if year.isdigit():
        year = int(year)
    else:
        print("Год должен быть целым числом")
        print("")
        return
    print("")

    book = {
        "Название": title,
        "Автор": author,
        "Год выпуска": year,
    }

    if book in library:
        print("Не плагиать книги! Такая уже есть")
        return
    library.append(book)
    print(f"Книга {book['Название']} добавлена!")
    show_books()



def remove_book():
    """
    Удаляет книгу по номеру
    спрашивает, есть ли книги?
    """

    if not library:
        print("Библиотека пуста!")
        return

    num = input("Введите порядковый номер книги для удаления: ")
    if num.isdigit():
        num = int(num)
    else:
        print("Номер должен быть больше 1")         

    idx = num - 1   

    if idx < 0 or idx >= len(library):
        print("Ошибка! Нет такой книги")
        return    

    
    print(f"Книга {library[idx]['Название']} удалена")
    library.pop(idx)
    show_books()
       

def search_by_number():
    if not library:
        print("Библиотека пуста!")
        return

    num = input("Введите номер книги: ")

    if not num.isdigit():
       print("Номер должен быть числом")
       return

    num = int(num)
    idx = num - 1

    if idx < 0:
        print("Число должно быть положительным!") 
        return

    if idx >= len(library):
        print("Номер слишком большой!")
        return

    book = library[idx]

    print("Номер на полке:", num)
    print('Название:', book["Название"])
    print('Автор:', book["Автор"])
    print('Год выпуска:', book["Год выпуска"])
    print("")



def search_book_by_key(user_key: str) -> None:
    """ 
    Показывает на экране книгу, если находит её по номеру 
    """
    if not library:
        print("Библиотека пуста!")
        return

    user_value = input(f"Введите {user_key}: ")

    if user_key == "год" and user_value.isdigit():
        user_value = int(user_value)

    if not user_value:
        print("Нет данных для поиска!")
        os.system("cls")
        return show_menu()

    if user_key == "Год выпуска":
        if user_value.isdigit():
            user_value = int(user_value)       

    for book in library:
        if book[user_key] == user_value:
            print("Номер на полке:", {library.index(book) + 1})
            print('Название:', book["Название"])
            print('Автор:', book["Автор"])
            print('Год выпуска:', book["Год выпуска"])
            print("")
            
    return show_menu()


def leave():
    print(" ")
    print("Выходим...")
    print(" ")
    print("Выходим..")
    print(" ")
    print("Выходим...")
    print(" ")
    pass



show_menu()