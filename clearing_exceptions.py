import csv

with open('test.csv', 'r') as file_csv:
    csv_data = {row['Domain'] for row in csv.DictReader(file_csv)}

with open('list_uns.txt', 'r') as file:
    for list_domain in file.readlines():
        lid = list_domain.strip()  

        if lid in csv_data:
            print("Нашел совпадение:", lid)
            with open('result.txt', 'a+') as result:
                res = result.write(f'{lid}\n')

