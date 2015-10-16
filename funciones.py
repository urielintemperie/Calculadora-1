# =================================================.
# funciones.py
# Funciones para:                                  |
# calculadora.py                                   |
# por Barlan, con ayuda de la comunidad Underc0de  |
# underc0de.org                                    |
# =================================================.
from math import sqrt # Importamos desde la librería math la función para raices cuadradas.

# Creamos funciones para resolver los problemas:
def suma(num1, num2):
	resultado = num1 + num2
	return resultado

def resta(num1, num2):
	resultado = num1 - num2
	return resultado

def multiplicacion(num1, num2):
	resultado = num1 * num2
	return resultado

def division(num1, num2):
	resultado = num1 / num2
	return resultado

#el primer numero se potencia segun el segundo
def potencia(num1, num2):
	resultado = num1 ** num2
	return resultado

#devuelve la raiz cuadrada del numero
def raizCuadrada(num1):
	resultado = sqrt(num1)
	return resultado

def Hipotenusa(a, b):	# Esta función sirve para calcular el lado mayor del triangulo.
	# c^2 = a^2 + b^2
	return sqrt((a * a) + (b * b))

def Cateto(a, b):	# Y con esta función calculamos uno de los 2 lados.
	# El lado a calcular, es la resta del cuadrado de la hipotenusa menos el cuadrado del otro cateto.
	return sqrt((a * a) - (b * b))

def Ecuacion_2Grado(a, b, c): # Función (eso espero xD) para resolver Ecuaciónes cuadrácticas
	# x = [ -b ± √(b2-4ac) ] / 2a
	try:
		x1 =(-b + sqrt((b ** 2) - ((4 * a) * c)) / (2 * a))
		x2 =(-b - sqrt((b ** 2) - ((4 * a) * c)) / (2 * a))
		return ("(+) = " + str(x1) + " (-) = " + str(x2))
	except:
		print("La ecuacion no tiene solucion.")
