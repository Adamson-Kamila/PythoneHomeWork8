import json
import os

# None - функция ничего не возвращает или иначе возвращает нам что-то.

def delete(data_book: list) -> None:  # функция для удаления контакта
    """ Перед тем как удалить контакт, нам нужно найти контакт, который будем удалять,
    поэтому запускаем функцию в функции, отвечающую за поиск контактов 'find'
    """
    element = find(data_book)  # <--- вот она
    delete_element = input('Удалить? ')  # задаем уточняющий вопрос пользователю
    if delete_element.lower() == 'да':  # проверяем, если ответ (за  это отвечает переменная delete_element), да
        index = data_book.index(element)  # тогда контакт, находящийся под индексом удаляется
        del data_book[index]  # удаляем с помощью функции del


def update(data_book: list) -> None:  # вносим изменения в контакт
    """ Перед тем как обновить контакт, нам нужно найти контакт, который будем обновлять,
       поэтому запускаем функцию в функции, отвечающую за поиск контактов 'find'
       """
    element = find(data_book)  # <--- вот она
    key = input(f'{list(element.keys())} Укажите нужный ключ: ')  # показываем пользователю ключи контакта (имя, фамилия
    # номер телефона).
    element[key] = input('Введите изменения: ')  # предлагаем выбрать необходимый ключ для изменения.


def show_contacts(data_book: list) -> None:  # выводим контакты в консоль
    print('\n'.join(map(str, data_book)))  # выводим контакты в консоль.
    # Метод join() объединяет элементы списка в одну строку, разделяя их символом новой строки (\n).


def find(data_book: list) -> dict:  # ищем контакт
    """"Самый простой логичный поиск контакта, это поиск по номеру телефона, так как имена и фамилии могут совпадать,
    а номера телефонов уникальные"""
    phone = input('Введите номер телефона для поиска: ')  # предлагаем пользователю ввести номер телефона контакта,
    # который необходимо найти.
    found = list(filter(lambda el: el['phone'] == phone, data_book)) # используем lambda, которой передаем,
    # введенный пользователем, номер телефона. Filter будет фильтровать контакты в списке data_book. И если
    # введенный номер телефона совпадет с номером в data_book, то lambda вернет его нам с контактом
    return found[0] # логично, что поисковая функция, будет возвращать нам контакт.


def create(data_book: list) -> None:  # принимает список (либо с контактами, либо без) и создаем новый контакт
    """В этой функции создаем контакты. Функция будет принимать в себя список пустой или с контактами.
    Сам data_book представляет  собой список со сложенными словарями. Контакты находятся во вложенных словарях
    Ключами в словаре являются: name, first_name, phone"""
    data_dict = {
        'name': input('Введите имя: '),
        'first_name': input('Введите фамилию: '),
        'phone': input('Введите номер телефона: ')
    }
    data_book.append(data_dict)


def make_dump(data_book: list, path: str = 'phone_book.json') -> None:  # сохраняем контакты в файл
    """ Создает дамп справочника.
    :param data_book: Объект справочника, <class 'list'>.
    :param path: Путь к дампу справочника, <class 'str'>.
    :return: None
    """
    with open(path, 'w', encoding='UTF-8') as file:
        json.dump(data_book, file, ensure_ascii=False)


def get_dump(
        path: str = 'phone_book.json') -> list:  # загружаем контакты из файла, если они есть, иначе создаем новый список
    """ Функция загружает дамп справочника.
    :param path: Путь к дампу справочника, <class 'str'>.
    :return: Возвращает справочник, <class 'list'>.
    """

    if path in os.listdir(os.curdir) and os.stat(path).st_size:
        with open(path, 'r', encoding='UTF-8') as file:
            dump = json.load(file)
    else:
        dump = list()
    return dump


def main(): # главная функция, в которой вызываются выше написанные функции.
    menu = {
        'Создать': create,
        'Изменить': update,
        'Показать': show_contacts,
        'Найти': find,
        'Удалить': delete,
    }
    phone_book = get_dump()
    key = input(f'{list(menu.keys())} Выберите действие: ')
    menu[key](phone_book)
    make_dump(phone_book)


main()
