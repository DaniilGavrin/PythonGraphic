import matplotlib.pyplot as plt
import numpy as np

# Создаём данные для графика
names = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']

employee1 = [0, 1, 0, 0, 0, 0, 0]
employee2 = [0, 0, 0, 0, 0, 0, 0]
employee3 = [0, 0, 0, 0, 0, 0, 0]

#Создаем график
fig, ax = plt.subplots()
bar_width = 0.25
opacity = 0.8
index = np.arange(len(names))

rects1 = plt.bar(index, employee1, bar_width, alpha=opacity, color='b', label = 'Даниил')
rects2 = plt.bar(index + bar_width, employee2, bar_width, alpha=opacity, color='g', label = 'Лера')
rects3 = plt.bar(index + bar_width *2, employee3, bar_width, alpha=opacity, color='r', label = 'Нет сотрудника')

plt.xlabel('День недели')
plt.ylabel('Часы работа')
plt.title('Время работы сотрудников по дням недели')
plt.xticks(index + bar_width, names)
plt.legend()

plt.tight_layout()
plt.show()