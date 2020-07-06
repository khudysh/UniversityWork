from math import sqrt, log
from matplotlib import pyplot as plt

f = lambda t, x: (t**2)*sqrt(x**2 + t**2) #Подынтегральная функция

def F(t, x):
    """Первообразная функция"""
    t = t if t != 0 else 10E-20
    x = x if x != 0 else 10E-20
    return x*sqrt(t**2 + x**2)*(2*t**3+t*x**2)/abs(x)/8 - x**4*log(abs(x*sqrt(t**2+x**2)+t*abs(x)))/8


a = float(input("Введите a: "))
b = float(input("Введите b: "))
c = float(input("Введите c: "))
d = float(input("Введите d: "))
N = int(input("Введите N: "))
X = [c + i*(d-c)/20 for i in range(21)] #генерируем список значений x
h = (b-a)/N #объявим шаг переменной t
T = [a + i*h for i in range(N+1)] #генерируем список точек t с шагом h
maxError = 0 #инициализируем максимальную ошибку нулем
for x in X: #для каждого значения из X вычислим значение ошибки
    definite_integral_1 = sum([(f(T[i-1], x) + f(T[i], x))/2*h for i in range(1, N+1)]) #сгенерируем список частичных интегральных сумм и вычислим их сумму
    definite_integral_2 = F(T[-1], x) - F(T[0], x) #по формуле Ньютона-Лейбница вычислим значение интеграла
    maxError = max(maxError, abs(definite_integral_1 - definite_integral_2)) #вычислим значение ошибки
print("Максимальная ошибка:", maxError) #выведем значение max ошибки
x = X[len(X)//2] #выбираем значение x из середины списка X
partial_sums = [(f(T[i-1], x) + f(T[i], x))/2*h for i in range(N+1)] #генерируем список частичных сумм
approximate = [sum(partial_sums[0:i]) for i in range(N+1)] #генерируем список приближенных значений определенного интеграла
accurate = [F(T[i], x) - F(T[0], x) for i in range(N+1)] #генерируем список точных значений определенного интеграла
plt.title("Графики определенного интеграла при x={}".format(x))
plt.ylabel("Значение определенного интеграла")
plt.xlabel("Значение t")
plt.grid(True)
plt.plot(T, accurate, color="green", label="Точное")
plt.plot(T, approximate, color="red", label="Приближенное")
plt.legend()
plt.show()
