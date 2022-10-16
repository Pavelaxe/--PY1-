Нашей компании нужно сгруппировать клиентов для АБ-тестов. Алгоритм группировки очень простой - взять ID клиента 
(состоит из 5-7 цифр, например 7412567) и найти сумму всех его цифр. Получившееся число и является номером группы, в 
которую входит данный клиент.

Для того, чтобы понять, насколько хорош такой простой алгоритм, тебе нужно написать следующие диагностические функции:

Функция, которая подсчитывает число покупателей, попадающих в каждую группу, если нумерация ID сквозная и начинается с 0. 
На вход функция получает целое число n_customers (количество клиентов).

Функция, аналогичная первой, если ID начинается с произвольного числа. На вход функция получает целые числа: n_customers 
(количество клиентов) и n_first_id (первый ID в последовательности).

def count_groups_var_1(n_customers):
    groups = {}
    customers_id = -1
    for i in range(n_customers):
        customers_id += 1
        customers_id_for_sum = customers_id
        sum_ = 0    
        while customers_id_for_sum > 0:
            sum_ += customers_id_for_sum % 10
            customers_id_for_sum //= 10
        groups[sum_] = groups[sum_] + 1 if sum_ in groups else 1
    return groups

def count_groups_var_2(n_customers, n_first_id):
    groups = {}
    customers_id = n_first_id - 1
    for i in range(n_customers):
        customers_id += 1
        customers_id_for_sum = customers_id
        sum_ = 0    
        while customers_id_for_sum > 0:
            sum_ += customers_id_for_sum % 10
            customers_id_for_sum //= 10
        groups[sum_] = groups[sum_] + 1 if sum_ in groups else 1
    return groups
