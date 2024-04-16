import csv
import re

with open('exceptions.txt', 'r') as file_txt:
    txt_domains = {row.strip() for row in file_txt}

with open('test.csv', 'r') as file_csv:
    reader = csv.DictReader(file_csv)
    
    # Проверяем наличие столбца 'Email' в заголовке CSV файла
    if 'Domain' not in reader.fieldnames:
        print("Столбец 'Domain' не найден в CSV файле.")
        exit(1)

    for row in reader:
        email = row['Domain']

        if email in txt_domains:
            print("Найдено точное совпадение:", email)
            with open('result.txt', 'a+') as result_file:
                result_file.write(f'{email}\n')
        else:
            match = re.search(r'@(.+)', email)
            if match:
                domain = match.group(1)

                if domain in txt_domains:
                    print("Найдено совпадение по домену:", email)
                    with open('result.txt', 'a+') as result_file:
                        result_file.write(f'{email}\n')
