contact_data = {'Фамилия': None, 'Имя': None, 'Отчество': None, 'Номер телефона': None}

# Для приведения в красивый формат
def form_table(a):
    word = ''
    for i in a:
        if i != '\n':
            i = '|{:^15}|'.format(str(i))
            word += i
    return word
# Запрос данных у пользователя
def ask_data():
    contact_data['Фамилия'] = input('Ведите фамилию: ')
    contact_data['Имя'] = input('Введите имя: ')
    contact_data['Отчество'] = input('Ведите отчество: ')
    contact_data['Номер телефона'] = input('Ведите номер телефона: ')
    return contact_data
# Добавление контакта
def add_new_contact():
    with open('phone_book.txt', 'a', encoding='utf-8') as file:
        file.writelines('%s;' % value for value in ask_data().values())
        file.write('\n')
    if True:
        print('Контакт успешно добавлен!')
    
# Поиск контакта
def find_contact():
    param = input('Для поиска контакта укажите, пожалуйста, один из следующих параметров:\nФамилия,\nИмя,\nОтчество,\nНомер телефона:\n>>').capitalize()
    with open('phone_book.txt', 'r', encoding='utf-8') as file:
        for count, line in enumerate(file):
            if param in line:
                lines = {}
                lines[count+1] = form_table(list(line.split(";")))
                for key, value in lines.items():
                    print(key, value)
    return 
    
# Удаление контакта    
def del_contact():
    find_contact()
    with open('phone_book.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
        num = int(input('Введите порядковый номер контакта для подтверждения удаления: '))
    with open('phone_book.txt', 'w', encoding='utf-8') as fd:
        for line in lines:
            if line != lines[num-1]:
                fd.write(line)
    return 'Контакт успешно удален.'

# Копирование контакта в новый файл
def copy_contact():
    find_contact()
    with open('phone_book.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
        num = int(input('Введите порядковый номер контакта для подтверждения копирования: '))
    with open('phone_book_new.txt', 'w', encoding='utf-8') as fd:
        for line in lines:
            if line == lines[num-1]:
                fd.write(line)
    return 'Контакт успешно скопирован в файл phone_book_new.txt'

# Вывод всей телефонной книги
def open_phonebook():
    title = ['ФАМИЛИЯ','ИМЯ','ОТЧЕСТВО','НОМЕР ТЕЛЕФОНА']
    with open('phone_book.txt', 'r', encoding='utf-8') as file:
        print(form_table(title))
        for line in file:
            print(form_table(list(line.split(";"))))
    
# Основное меню
def main():
    isStop = 10
    while isStop != 0: 
        print('Вам доступны следующие операции: \n 1 Найти контакт\n 2 Добавить новый контакт\n 3 Удалить\n 4 Открыть всю книгу\n 5 Копировать контакт \n 0 Выход')
        isStop = int(input('Введите, пожалуйста, интересующий вас пункт:'))
        if isStop == 1:
            find_contact()
        elif isStop == 2:
            add_new_contact()
        elif isStop == 3:
            del_contact()
        elif isStop == 4:
            open_phonebook()
        elif isStop == 5:
            copy_contact()
        input('Нажмите Enter чтобы продолжить.')
    return 'До новых встреч!'
main()
