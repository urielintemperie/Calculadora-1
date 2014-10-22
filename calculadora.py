# calculadora. py
# =================================================.
# por Barlan, con ayuda de la comunidad Underc0de  |
# underc0de.org                                    |
# =================================================.

import os, sys # Importamos estas librerias relacionadas con la consola de Windows.
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

def Hipotenusa(a, b):	# Esta función sirve para calcular el lado mayor del triangulo.
	# c^2 = a^2 + b^2
	return sqrt((a * a) + (b * b))

def Cateto(a, b):	# Y con esta función calculamos uno de los 2 lados.
	# El lado a calcular, es la resta del cuadrado de la hipotenusa menos el cuadrado del otro cateto.
	return sqrt((a * a) - (b * b))

def Ecuacion_2Grado(X, Y, Z): # Función (eso espero xD) para resolver Ecuaciónes cuadrácticas
	# x = [ -b ± √(b2-4ac) ] / 2a
	try:
		n1 =(-Y + sqrt((Y ** 2) - ((4 * X) * Z)) / (2 * X))
		n2 =(-Y - sqrt((Y ** 2) - ((4 * X) * Z)) / (2 * X))
		return ("(+) = " + str(n1) + " (-) = " + str(n2))
	except:
		print("La ecuacion no tiene solucion.")

os.system("TITLE Calculadora v1.0 por Barlan")
os.system("color 1f")
while True:
	os.system("cls") # Limpiamos la consola para "ver mejor" xD
	print("""
# Calculadora v1.5
# por Barlan
# Creada el 9 de Octubre del 2014
# Revision #1: 20 de Octubre del 2014, a las 12:44 am
# Revision #2: 20 de Octubre del 2014, a las 10 pm
== Menu ==

Opciones:
[1] Sumar
[2] Restar
[3] Multiplicar
[4] Dividir
[5] Teorema de Pitagoras
[6] Ecuacion Cuadratica (o de segundo grado)
		""")
	try:
		op = int(input("\nElige una opcion escribiendo su inciso, 0 para salir:\n>> "))
		if op == 0:	# Funcion para salir
			input("Gracias por usar mi calculadora!")
			os.system("cls")
			sys.exit(1)

		elif op == 1:
			os.system("cls")
			print ("== SUMA ==\n")
			num1 = int(input("Ingresa el primer entero:>> "))
			num2 = int(input("Ingresa el segundo entero:>> "))
			resul = suma(num1, num2)
			print ("\nLa suma de las 2 variables es: ", resul)

		elif op == 2:
			os.system("cls")
			print ("== RESTA ==\n")
			num1 = int(input("Ingresa el primer entero:>> "))
			num2 = int(input("Ingresa el segundo entero:>> "))
			resul = resta(num1, num2)
			print ("\nLa resta de las 2 variables es: ", resul)

		elif op == 3:
			os.system("cls")
			print ("== MULTIPLICACION ==\n")
			num1 = int(input("Ingresa el primer entero:>> "))
			num2 = int(input("Ingresa el segundo entero:>> "))
			resul = multiplicacion(num1, num2)
			print ("\nLa multiplicacion de las 2 variables es: ", resul)

		elif op == 4:
			os.system("cls")
			print ("== DIVISION ==\n")
			num1 = int(input("Ingresa el primer entero:>> "))
			num2 = int(input("Ingresa el segundo entero:>> "))
			resul = division(num1, num2)
			print ("\nLa division de las 2 variables es: ", resul)
		elif op == 5:
			os.system("cls")
			print ("== TEOREMA DE PITAGORAS ==\n")
			print ("a ** 2 + b ** 2 = c ** 2\n")
			print ("""
1) Hallar valor de un cateto
2) Hallar valor de hipotenusa
				""")
			try:
				opcion = int(input(">> "))
				if opcion == 1:
					a = int(input("Ingresa el valor de la hipotenusa: "))
					b = int(input("Ingresa el valor del lado b: "))
					resul = Cateto(a, b)
					print ("El valor del cateto es: ", resul)
				else:
					a = int(input("Ingresa el valor del primer cateto: "))
					b = int(input("Ingresa el valor del segundo cateto: "))
					resul = Hipotenusa(a, b)
					print ("El valor de la hipotenusa es: ", resul)
			except ValueError:
				print ("Ingresa un valor valido")
			finally: # Probablemente ese pedazo de código puede eliminarse. xd
				os.system("pause>nul")

		elif op == 6:
			os.system("cls")
			# Al parecer, contiene errores al calcular todo, pero para soluciones futuras, lo dejo.
			print ("== ECUACION DE SEGUNDO GRADO O CUADRATICA ==\n")
			print ("Ecuacion:\n")
			X = int(input("X >> "))
			Y = int(input("Y >> "))
			Z = int(input("Z >> "))
			print (Ecuacion_2Grado(X, Y, Z))
			os.system("pause>nul")
		else: # En caso de que se ingrese un numero (opcion) que no hay.
			print ("No hay opciones mas alla del #6, intenta con un numero menor a ese, ok?")
			os.system("pause>nul")
	except ValueError: # En caso de que no se ingrese un numero.
		print ("Ingresa un valor correcto.")
		os.system("pause>nul")
