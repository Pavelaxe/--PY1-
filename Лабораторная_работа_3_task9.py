salary = 5000  # зарплата
spend = 6000  # траты
months = 0  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

while months != 10:
    need_money += (spend-salary)
    spend *= 1.03
    months += 1
    # TODO Оформить решение

print(round(need_money))
