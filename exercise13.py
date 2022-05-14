number_of_tickets = int(input("Введите кол-во билетов: "))
sum = 0
for visitor in range (number_of_tickets):
    visitor+=1
    age = int(input(f"Введите возраст {visitor}-го посетителя: "))
    if age < 18:
        print("Билет бесплатный")
    elif age <= 18:
        print("Билет стоит 990 рублей")
        sum += 990
    elif age <= 25:
        print("Билет стоит 990 рублей")
        sum += 990
    else:
        print("Билет стоит 1390 рублей")
        sum += 1390
if visitor > 3:
    print("Сумма к оплате с учëтом скидки 10%: ", sum - sum / 100 * 10)
else:
    print("Сумма к оплате:", float(sum))