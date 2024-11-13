import math

salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев
increase = 0.03  # Ежемесячный рост цен


total_needed = 0

for month in range(months):
    deficit = spend - salary
    if deficit > 0:
        total_needed += deficit
    spend *= (1 + increase)
money_capital = math.ceil(total_needed)
print("Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital)
