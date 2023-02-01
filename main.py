ticket_count = int(input("Введите количество билетов: "))
total_cost = 0

for i in range(ticket_count):
    age = int(input("Введите возраст посетителей: "))
    if age < 18:
        cost = 0
    elif age >= 18 and age <= 25:
        cost = 990
    else:
        cost = 1390
    total_cost += cost

if ticket_count > 3:
    total_cost = total_cost * 0.9

print("Общая стоимость:", total_cost, "рублей")
