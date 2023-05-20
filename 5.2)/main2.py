list = [1, 2, 3, 4, 5, 5]
for i in list:
    if list.count(i) > 1:
        print("Повторяющийся элемент:", i)
        break
else:
    print("Повторяющихся элементов нет")
