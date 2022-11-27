# Дан список с заголовками и список списков с данными, где каждый отдельный
# список представляет собой строку для csv.
# Без использования модуля csv записать данные в файл output.csv.
#
# Реализовать функцию to_csv_file, которая будет записывать передаваемые ей данные в
# формате csv. Функция to_csv_file должна принимать следующие аргументы:
# filename - файл куда надо записывать
# headers - список заголовков
# rows список списков с данными
# delimiter - разделитель между значениями, по умолчанию ","
# new_line - разделитель строк, по умолчанию "\n".


OUTPUT_FILE = "output.csv"


def to_csv_file(filename, headers, rows, delimiter=',', new_line='\n'):
    with open(filename, 'w') as f:
        for head in headers:
            f.write(head)
            if head != headers[-1]:
                f.write(delimiter)
        f.write(new_line)
        for line_ in rows:
            for element in line_:
                f.write(element)
                if element != line_[-1]:
                    f.write(delimiter)
            f.write(new_line)  # TODO реализовать функцию to_csv_file


headers_list = ['longitude', 'latitude', 'housing_median_age', 'total_rooms', 'total_bedrooms', 'population', 'households', 'median_income', 'median_house_value']
data = [
    ['-122.050000', '37.370000', '27.000000', '3885.000000', '661.000000', '1537.000000', '606.000000', '6.608500', '344700.000000'],
    ['-118.300000', '34.260000', '43.000000', '1510.000000', '310.000000', '809.000000', '277.000000', '3.599000', '176500.000000'],
    ['-117.810000', '33.780000', '27.000000', '3589.000000', '507.000000', '1484.000000', '495.000000', '5.793400', '270500.000000'],
    ['-118.360000', '33.820000', '28.000000', '67.000000', '15.000000', '49.000000', '11.000000', '6.135900', '330000.000000'],
]

to_csv_file(OUTPUT_FILE, headers_list, data)  # TODO вызвать функцию to_csv_file и записать данные в файл

with open(OUTPUT_FILE) as output_f:
    for line in output_f:
        print(line, end="")
