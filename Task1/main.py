import re
import chardet
import csv





def get_data():
    data = {'Изготовитель системы': [],
            'Название ОС': [],
            'Код продукта': [],
            'Тип системы': []}

    with open(r'C:\Users\cryst\OneDrive\Рабочий стол\HomeWork8\Task1\info_1.txt') as f:
        for line in f:
            match = re.match(r'^(.*?):\s*(.*)\s*$', line)
            if match:
                key = match.group(1)
                value = match.group(2)
                if key in data:
                    data[key].append(value)

    with open(r'C:\Users\cryst\OneDrive\Рабочий стол\HomeWork8\Task1\info_2.txt') as f:
        for line in f:
            match = re.match(r'^(.*?):\s*(.*)\s*$', line)
            if match:
                key = match.group(1)
                value = match.group(2)
                if key in data:
                    data[key].append(value)

    with open(r'C:\Users\cryst\OneDrive\Рабочий стол\HomeWork8\Task1\info_3.txt') as f:
        for line in f:
            match = re.match(r'^(.*?):\s*(.*)\s*$', line)
            if match:
                key = match.group(1)
                value = match.group(2)
                if key in data:
                    data[key].append(value)

    main_data = [['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']]
    for i in range(len(data['Изготовитель системы'])):
        row = [data['Изготовитель системы'][i], data['Название ОС'][i], data['Код продукта'][i], data['Тип системы'][i]]
        main_data.append(row)

    return main_data


def write_to_csv(file_path):
    # Получаем данные через вызов функции get_data()
    data = get_data()

    # Создаем список заголовков столбцов
    headers = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']

    # Создаем список значений для каждого заголовка
    values = []

    for row_index in range(1, len(data)):
        row = []
        for header in headers:
            col_index = headers.index(header)
            value = data[row_index][col_index] if col_index < len(data[row_index]) else ''
            row.append(value)
        values.append(row)

    # Записываем данные в CSV-файл
    with open(file_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(data[1:])


write_to_csv('data.csv')