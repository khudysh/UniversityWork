import numpy as np
import matplotlib.pylab as plt

# Объявление и ввод переменных:
a = float(input("Нижний предел интегрирования: "))
b = float(input("Верхний предел интегрирования: "))
c = float(input("Верхний предел для X: "))
d = float(input("Нижний предел для X: "))
N = int(input("Кол-во разбиений: "))
h = (b-a)/N
k = 21  # кол-во сравниваемых точек

# Подынтегральное выражение:
f = lambda x, t: 1/((x+t)*t**2)

# Метод трапеций
def trapez(x):
    sumOfInter = 0.5 * (f(x, a) + f(x, b))
    for i in range(1, N):
        sumOfInter += f(x, a + i * h)
    return sumOfInter * h

# Точное вычисление
def exactIntegral(xPoints):
    return np.log(xPoints[i]+2)/xPoints[i]**2-(np.log(xPoints[i]+1)-xPoints[i])/xPoints[i]**2-1/(2*xPoints[i])-np.log(2)/xPoints[i]**2

# Создание точек
xPoints = [c + i*(d-c)/20 for i in range(k)]
xPoints = np.array(xPoints)

for i in range (k):
    if xPoints[i] == 0:
        xPoints[i] = 0.000001

# Точное значение:
yPoints = []
yExactPoints = []
for i in range (k):
    yExactPoints.append(exactIntegral(xPoints))

# Приближённое значение:
yPoints = trapez(xPoints)

# Размер ошибки:
error = 0.0
for i in range(k):
    if abs(yPoints[i] - yExactPoints[i]) > error:
        error = abs(yPoints[i] - yExactPoints[i])
print("Максимальная ошибка = ", error)

# Построение графика:
plt.title("График\n\n Максимальная ошибка = {}\n".format(error))
plt.ylabel("Значение определенного интеграла")
plt.xlabel("Значение переменной x")
plt.plot(xPoints, yExactPoints, "sr-", label="Приближенное")
plt.plot(xPoints, yPoints, "sc-" , label="Точное")
plt.legend()
plt.grid(True)
plt.minorticks_on()
plt.grid(which='minor', color='gray', linestyle='-', linewidth=0.5)
plt.show()
