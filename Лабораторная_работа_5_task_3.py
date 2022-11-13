# Написать функцию, которая возвращает список, заполненный случайными целыми
# числами. Числа в списке должны быть уникальными.
#
# Диапазон случайных чисел от -10 до 10 включительно. Размер списка 15 чисел.

import random
def get_unique_list_numbers() -> list[int]:
    list_ = []
    while len(list_) != 15:
        random_d = random.randint(-10, 10)
        if random_d not in list_:
            list_.append(random_d)
    return list_  # TODO написать функцию для получения списка уникальных целых чисел


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
