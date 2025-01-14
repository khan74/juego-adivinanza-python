
import random 

numero_secreto = random.randint(1,100) 
adivinado = False
intentos = 0
intentos_maximos = 7

print("Adiviná el número secreto")

while not adivinado and intentos < intentos_maximos:
    numero = int(input("Introduce un número del 1 al 99: "))
    if numero_secreto == numero: 
        adivinado = True 
        break
    elif numero < numero_secreto:
        print("El número es mayor al ingresado")
    else:
        print("El número es menor al ingresado")
    intentos += 1
    txt = "Te quedan {0} intentos"
    print(txt.format(intentos_maximos - intentos))

if adivinado:
    txt = "Adivinaste!!! El número era {0}"
    print(txt.format(numero_secreto)) 
    input("Presiona enter para salir, TIGRE")
else:
    txt = "No adivinaste piscui, el número era {0}, tenes el culo lleno de leche!!"
    print(txt.format(numero_secreto))
    input("Presiona enter para salir, CULORROTO")

