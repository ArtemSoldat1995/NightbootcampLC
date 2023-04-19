salary = int(input('Введите оклад: ' ))
calendar_days = int(input('Количество рабочих дней: '))
days_worked = int(input('Количество отработаных дней: '))
premium = int(input('Премии: '))
tax = int(input('Налог: '))
retention = int(input('Удержания: '))
salary_2 = (salary / calendar_days * days_worked + premium) * ((100 - tax) / 100) - retention
print(salary_2)