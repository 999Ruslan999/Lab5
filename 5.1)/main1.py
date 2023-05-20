numbers = [10, 25, 33, 48, 52]
user_num = int(input("Введите число: "))
if user_num in numbers:
    print("Поздравляю, Вы угадали число!")
else:
    print("Нет такого числа!")
print("Исходный список:", numbers)
