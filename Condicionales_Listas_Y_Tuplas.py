"""Condicional If Elif Else"""
print("Adivina mi top 4 colores") # Titulo del programa
tupla =("Azul","Negro","Rojo","Verde") #CREACION DE TUPLA
dato= input("Ingresa tu eleccion de color\n") #Salto de linea para evitar datos amontonados

if dato in tupla[0] : #Buscamos entre los datos de la tupla
    
    print("El color Azul esta dentro de mis 4 favoritos")

elif dato in tupla[1] :#Buscamos entre los datos de la tupla
       
    print("El color Negro esta dentro de mis 4 favoritos")

elif dato in tupla[2] :#Buscamos entre los datos de la tupla
       
    print("El color Rojo esta dentro de mis 4 favoritos")

elif dato in tupla[3] :#Buscamos entre los datos de la tupla
       
    print("El color Verde esta dentro de mis 4 favoritos")

else :

    print("Este color no entra en mi top de favorito")
