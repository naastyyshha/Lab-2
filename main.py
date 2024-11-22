import csv
import random
import xml.etree.ElementTree as ET


"Задание 1"
count = 0
with open('books.csv', 'r', encoding='windows-1251') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    for row in reader:
        if len((row['Название'])) > 30:
            count += 1
print(f'Количество книг, у которых в поле ```Название``` строка длиннее 30 символов: {count}')


"Задание 2"
def search_books(search):
    flag = 0
    with open('books-en.csv', 'r', encoding='windows-1251') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
            lower_case_title = row[2].lower()
            index = lower_case_title.find(search.lower())
            if index != -1 and int(row[3]) >= 2018:
                print(row[1])
                flag += 1
    return flag


while True:
    search = input('Enter the author: ')
    if search.lower() == 'stop':
        break

    results_count = search_books(search)

    if results_count == 0:
        print('Nothing is found')
    else:
        print(f'Found {results_count} books.')


"Задание 3"
with open('books-en.csv', 'r', encoding='windows-1251') as csvfile:
    file = list(csv.reader(csvfile, delimiter=';'))

random_rows = random.sample(file, 20)

with open('biography.txt', 'w') as output:
    for i, row in enumerate(random_rows, start=1):
        output.write(f'{i}. {row[2]}. {row[1]} - {row[3]}\n')



"Задание 4"
tree = ET.parse('currency.xml')
root = tree.getroot()
dict_charcode = {}
for valute in root.findall('Valute'):
    name = valute.find('Name').text
    charcode = valute.find('CharCode').text
    dict_charcode[name] = charcode
print("Словарь 'Name - CharCode':")
for name, charcode in dict_charcode.items():
    print(f"{name}: {charcode}")