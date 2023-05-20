days = ("Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье")

num_of_weekends = int(input("Сколько выходных дней на неделе вы хотите? "))
weekends = days[-num_of_weekends:]
workdays = days[:-num_of_weekends]

print("Ваши выходные дни:", ", ".join(weekends))
print("Ваши рабочие дни:", ", ".join(workdays))