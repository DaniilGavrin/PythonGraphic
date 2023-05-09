import numpy as np
import matplotlib.pyplot as plt

дни = np.arange(1, 31)
выплаты = [1000, 0, 0, 0, 0, 500, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]

#Создание графика
fig, ax = plt.subplots()
ax.plot(дни, выплаты)

# Создание внешнего вида графика
ax.set_xlabel('День месяца')
ax.set_ylabel('Выплаты')
ax.set_title('График выплат сотрудникам по дням')

plt.show()