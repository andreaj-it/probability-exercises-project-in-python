### Exercise 1 

#import libraries
import random

iterations=1000
num_of_items=0

#Funtion to roll the dice.
for i in range(iterations):
    dado1=random.randint(1,6)#numeros del dato
    dado2=random.randint(1,6)#numeros del dato

    suma = dado1 + dado2

    if(suma > 7) or (suma%2 ==0): #la usma es mayor a 7 o es un numero par
        num_of_items +=1

probabilidad = round((num_of_items/iterations)*100,2)

print('Seguimiento : '+str(probabilidad)+'%')

### Exercise 2

