"""Anidacion de if en bucle while """

x = 0

while x <= 30 :
     
     x += 1

     if x == 15: #If para romper el while
      print("Se rompió la ejecución del bucle cuando x valía", x)
      break

     if x == 4: #condicionamos el valor 4
        
       print("se salto el valor  4  de x")
       continue
       
     if x == 6:#condicionamos el valor 6
           
       print("se salto el valor  6 de x")
       continue

     if x == 10:#condicionamos el valor 10
       
       print("se salto el valor  10 de x")
       continue
     print("El valor de x es: ", x) 
