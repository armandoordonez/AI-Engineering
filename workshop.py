# Función Lambda para calcular el cuadrado de un número
# square = lambda x: x ** 2
# print(square(3)) # Resultado: 9

# Funcion tradicional para calcular el cuadrado de un numero
# def square1(num):
#   return num ** 2

# print(square1(5)) # Resultado: 25


mi_dicc = {"A": 1, "B": 2, "C": 3}
res = lambda x: mi_dicc[x]%3
print(res(mi_dicc))

sorted(mi_dicc, key=lambda x: mi_dicc[x]%3)

 # Retorna ['C', 'A', 'B']