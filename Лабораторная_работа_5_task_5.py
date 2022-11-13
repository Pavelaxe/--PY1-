# Написать функцию для генерации случайных паролей заданной длины n
# (по умолчанию 8 символов). В качестве алфавита следует использовать:
#
# Буквы верхнего регистра: A - Z
# Буквы нижнего регистра: a - z
# Цифры: 0 - 9
# Для того чтобы сгенерировать случайную выборку, следует использовать функцию
# sample из модуля random.

import string
from random import choice
import random
length = 8


def get_random_password() -> str:
    str_with_password = []
    while len(str_with_password) != length:
        range_ = [string.ascii_uppercase, string.ascii_lowercase, string.digits]
        type_of_sym = choice(range_)
        str_with_password += random.sample(type_of_sym, 1)
    str_with_password = ''.join(str_with_password)
    return str_with_password  # TODO написать функцию генерации случайных паролей


print(get_random_password())
