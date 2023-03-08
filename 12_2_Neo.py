import re
from pprint import pprint


# читаем адресную книгу в формате CSV в список contacts_list
import csv
with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

pprint(contacts_list)

contacts_list_res = []


for i in contacts_list:
    print(i)
    i = ','.join(i)
    # print(i)

    # Поиск 8 и замена на +7
    pat_1 = r"(?<![0-9])8"
    i = re.sub(pat_1, "+7", i)
    # print(i)

    # Поиск 10 подряд и замена на +7(ххх)-хх-хх
    pat_2 = r"(\+7)(\d{3})(\d{3})(\d{2})(\d{2})"
    subst_2 = r"+7(\2)\3-\4-\5"
    i = re.sub(pat_2, subst_2, i)
    # print(i)

    # Поиск +7 495-913-0168 и замена на - -
    pat_3 = r"(\+7|8)\s*(\d+)[-\s]*(\d+)[-\s]*(\d{2})(\d{2})"
    subst_3 = r"+7(\2)\3-\4-\5"
    i = re.sub(pat_3, subst_3, i)
    # print(i)

    # замена на +7(999)999-99-99
    pat_4 = r"(\+7)?\s*\((\d+)\)\s*(\d+)[-\s]*(\d+)[-\s]*(\d+)"
    subst_4 = r"+7(\2)\3-\4-\5"
    i = re.sub(pat_4, subst_4, i)
    # print(i)

    # замена на +7(999)999-99-99 доб.9999;
    pat_5 = r"(\s*|\s*\()доб\.\s*(\d{4})(\s*\)|\s*)"
    subst_5 = r" доб.\2"
    i = re.sub(pat_5, subst_5, i)
    # print(i)

    # Пооиск Ф И О,,
    pat_6 = r"([А-Я]+\w+)\s+([А-Я]+\w+)\s+([А-Я]+\w+),,"
    subst_6 = r"\1,\2,\3"
    i = re.sub(pat_6, subst_6, i)
    # print(i)

    # Пооиск И О,,
    pat_7 = r"([А-Я]+\w+)\s+([А-Я]+\w+),"
    subst_7 = r"\1,\2"
    i = re.sub(pat_7, subst_7, i)
    # print(i)

    j = i.split(',')

    # print(j)

    contacts_list_res.append(j)

# Список дублирующих строк:
double_counter = []


for i in range(len(contacts_list_res) - 1):
    # print(i, contacts_list_res[i][0])
    for j in range(i + 1, len(contacts_list_res)):
        if contacts_list_res[i][0] == contacts_list_res[j][0]:
            double_counter.append(j)
            # print(contacts_list_res[i][0])
            # print(len(contacts_list_res[i]))
            for k in range(1, len(contacts_list_res[i])):
                if contacts_list_res[i][k] < contacts_list_res[j][k]:
                    contacts_list_res[i][k] = contacts_list_res[j][k]
                    # print(type(contacts_list_res[j][k]))

print()
print('Список дублирующих строк:', *double_counter)
# Реверс списка, чтобы было проще удалить дубли с конца списка
double_counter.sort(reverse=True)

# удаление дублей с конца списка
for i in double_counter:
    contacts_list_res.pop(i)

print()
for i in contacts_list_res:
    print(i)


# код для записи файла в формате CSV
with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(contacts_list_res)

