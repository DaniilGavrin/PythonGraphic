import matplotlib.pyplot as plt
import numpy as np

#Данные цен на товары в течении 2022 года
prices = [100, 180, 120, 200, 165, 150, 180, 132, 99, 150, 160, 180]

#Ось времени
months = range(1, len(prices) + 1)

#Построение графика
plt.plot(months, prices)

#настройка оис и заголовков
plt.title('Цена')
plt.xlabel('Дни')
plt.ylabel('Цены')

# Отображение графика
plt.show()