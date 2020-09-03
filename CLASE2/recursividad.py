#thinkpython.spa.pdf   pagina 53

#recursivo es como circular
#como describr una palabra con la misma palabra
#ciclo sin fin
#termina donde partimos
#la recursividad no es exactamente circular
#tiene un inicio y un fin
#es un remolino

#ejemplo

#objeter factirial de un numero
#0! = 1  por definicion. asi que termina ahi.
#n! = n.(n-1)!
#pregutna de entrevista



def factorial(numero):
    if numero == 0:  #el fin de la recursividad
        return 1
    else:
        print(f"soy el {numero}")
        recur = factorial (numero-1)   #vuelve a ejecutar la funcion, o sea que vuelve al principio
        da = recur * numero
        return da

print(factorial(5))


#5 es igual a 0? no. va al else y se ejecuta la funcion nuevbamente pero de un numero menor. hasta que llega a 0 y directamente sale con valor 1.


'''
factorial    n -> 5      recur -> 2   da -> 120 (24*5)  multiplicas por el factorial
factorial    n -> 4      recur -> 2   da -> 24 (6*4)
factorial    n -> 3      recur -> 2   da -> 6 (2*3)
factorial    n -> 2      recur -> 1   da -> 2 (1*2)
factorial    n -> 1      recur -> 0   da -> 1 (1*1)
factorial    n -> 0      da -> 1

'''

#recursion es una funcion/algoritmo que se llama a si misma n cantidad de veces
#no se aplica a cualquier problema
#se usa para factorial
#para figonachi


#ejemplo arbol genealogico
#usar funcion padres desde nosotros, despues de nuevo a nuestros papas, despyeus de nuevbo a abuelos, etc
#desgranamos un problema hasta llegar al origen

#diagrama de PILA
#ir apilando diferentes ejcuciones
#la primera que pongo es la ultima que se ejecuta.



#achicar la funcion


def factorial2(numero):
    if numero == 0:  #el fin de la recursividad
        return 1
    else:
        return factorial2 (numero-1) * numero

print(factorial2(5))



#otro ejemplo: fibonacci


#fibonacci de 0 = 1
#fibonacci de 1 = 1
#fibonacci de n es fibonacci (n-1) + fibonacci (n-2)
#SUELE SER PREG DE ENTREVISYTA

def fibonacci (n):
    if n == 0 or n == 1: #condicion base
        return 1
    else:
        return fibonacci(n-1) + fibonacci (n-2)

print(fibonacci(10))

#tratar de usar la menor cantidad e pasos


#OJO CONLOS CICLOS INFINITOS PORQUE SE CUELGA TODOOOOO, SE CUELGA LA COMPU
#se rompe TODOOOOO
