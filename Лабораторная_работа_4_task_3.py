# Реализовать функцию delete, принимающую список и индекс, по которому надо удалить элемент.
# По умолчанию удаляется последний элемент из списка.
#
# Результатом вернуть измененный список.
def delete(list_, index=None):
    if index is None:
        full_list = list_[:-1]
    else:
        if index >= 0:
            first_part = list_[:index]
            second_part = list_[index + 1:]
        else:
            first_part = list_[:index]
            pre_second_part = list_[-1:index:-1]
            second_part = pre_second_part[::-1]
        full_list = first_part + second_part
    return full_list


print(delete([0, 0, 1, 2], index=1))  # [0, 1, 2]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2, 3]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3, 4]
