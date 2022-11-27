# Реализовать конвертер из csv в json формат:
#
# [{column -> value}, ... , {column -> value}]
# название столбца — значение (аналог DictReader из модуля csv).
# Для csv формата принять:
# разделитель между значениями, по умолчанию ","
# разделитель строк, по умолчанию "\n".
#
# Встроенным модулем csv пользоваться нельзя, json можно. В результате распечатать
# json строку с отступами равными 4.


import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(file) -> list[dict]:
    with open(file) as f:
        list_ = []
        for line in f:
            list_.append(line)
    lists = [element.split(',') for element in list_]
    dict_full = []
    for num_list in range(1, len(lists)):
        index = 0
        dict_ = {}
        for x in lists[0]:
            dict_[x.rstrip()] = lists[num_list][index].rstrip()
            index += 1
        dict_full.append(dict_)
    return dict_full  # TODO реализовать конвертер из csv в json


csv_to_list_dict(INPUT_FILE)
print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
