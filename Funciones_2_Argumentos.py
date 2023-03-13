""" Funciones 2 Argumentos"""

#Ejercicio 1
def colores(*args):
	pass

colores('rojo', 'azul', 'verde', 'amarillo') #4 Argumentos
colores('lila', 'negro', 'rojo')#3 Argumentos
colores('rosa')#1 Argumentos
colores('marrón', 'naranja')#2 Argumentos

#ejercicio 2
def colores(*args):
	print('El color', args[1], 'es mi favorito.', 'El color', args[0], 'tampoco está mal.')

colores("Azul", "Negro")#Damos valor a los colores

#Ejercicio 3
def suma(*args):
	val = args[0] + args[1] + args[2] + args[3] + args[4] #Creamos 4 argumentos iniciando por el 0
	print('La suma es de:', val)#imprimimos la suma

suma(25, 47, 785, 6434, 1155, 1)#llamamos a la funcion y le damos valores
