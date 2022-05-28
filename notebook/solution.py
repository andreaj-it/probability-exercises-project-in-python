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

#import libraries
import random
import numpy as np

bolas = {}

for i in range(60):
    if i < 10:
        bolas[i] = 'White'
    elif i > 9 and i < 30:
        bolas[i] = 'Red'
    else:
        bolas[i] = 'Green'  
  
#print(bolas)        
#Initialize important variables

blancos_o_rojos=0
mismo_color=0

n_simulations=1000

for i in range(n_simulations):
    
    #make a list of the colors that we choose
    lista_de_colores=[]

    #armo lista con 5 bolas sacadas al azar
    for i in range(5):
        lista_de_colores.append(bolas[random.randint(0,59)])
    
    #Convert it to a numpy array
    lista_de_colores = np.array(lista_de_colores)

    #print(lista_de_colores)
   
    #veo cuantas bolas armo el random de cada color
    blanco = sum(lista_de_colores == 'White')
    rojo = sum(lista_de_colores == 'Red')
    verde = sum(lista_de_colores == 'Green')
    
    #print('Blanco : '+str(blanco)+' Rojo : '+str(rojo)+' Verde : '+str(verde)) 
    
    #Keep track if the combination met the criteria
    if blanco == 3 and rojo == 2:
        blancos_o_rojos += 1
    
    if rojo == 5 or blanco == 5 or verde ==5:
        mismo_color +=1
    
print('La probabilidad de 3 bolas blancas y 2 bolas rojas es : ', round(blancos_o_rojos/n_simulations*100,2),'%')
print('La probabilidad q sean todas del mismo color es : ', round(mismo_color/n_simulations*100,2),'%')    
    
#print 'the probability of 3 white and 2 red is' in percentage

#print 'the probability of all the same color is' in percentage   