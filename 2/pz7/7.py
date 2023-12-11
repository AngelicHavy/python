# 1) Написати Python-скрипт, який повинен:
# виконати пошук всіх CSV-файлів в поточному робочому каталозі;
# прочитати повний вміст кожного файла;
# записати зміст кожного файла без першого рядка (рядок заголовка) в
# CSV-файл з тим же ім’ям.

import csv
import os

# Створення каталогу для зберігання файлів без заголовків
output_directory = 'headerRemoved'
os.makedirs(output_directory, exist_ok=True)

# Цикл, що проходить кожний файл в поточній директорії
for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'):
        continue  # Пропускаємо файли, які не є CSV

    print('Removing header from ' + csvFilename + '...')

    # Зчитуємо CSV-файл (пропускаючи перший рядок).
    csvRows = []
    with open(csvFilename, 'r') as csvFileObj:
        readerObj = csv.reader(csvFileObj)
        csvRows = [row for idx, row in enumerate(readerObj) if idx != 0]

    # Записуємо дані в новий CSV-файл.
    with open(os.path.join(output_directory, csvFilename), 'w', newline='') as csvFileObj:
        csvWriter = csv.writer(csvFileObj)
        csvWriter.writerows(csvRows)

print('Header removal complete.')

# 2) Написати Python-скрипт, для формату даних XML який повинен:
# зчитати з консолі назву населеного пункту (на англійській мові);
# завантажує погодні дані в JSON-форматі з ресурсу openweathermap.org;
# перетворює JSON-об’єкт в Python-структуру даних;
# виводить прогноз погоди на сьогодні та на наступні два дні.

import csv
import os

os.makedirs('headerRemoved', exist_ok=True)

for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'):
        continue  # skip non-csv files

    print('Removing header from ' + csvFilename + '...')

    # Читаємо CSV-файл і видаляємо перший рядок (рядок заголовка).
    with open(csvFilename, 'r') as csvFileObj:
        csvReader = csv.reader(csvFileObj)
        csvRows = [row for idx, row in enumerate(csvReader) if idx != 0]

    # Записуємо дані в новий CSV-файл.
    with open(os.path.join('headerRemoved', csvFilename), 'w', newline='') as csvFileObj:
        csvWriter = csv.writer(csvFileObj)
        csvWriter.writerows(csvRows)

print('Header removal complete.')
