import matplotlib.pyplot as plt
import numpy as np

#создаем массивы данных
x = np.linspace(0, 10, 50) #массив значений по оси х
y = np.sin(x) #массив значений по оси y

#создаём график
plt.plot(x, y)

#настрлйка параметров графика
plt.title('Синусоидальная функция')
plt.xlabel('x')
plt.ylabel('sin(x)')

plt.grid(True)

#Выводим график на экран
plt.show()