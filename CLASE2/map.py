#nos permite iterar y aplica runa funcional#sobre un elemento iterable como una lista
#esto e sun paradigma declarativo
#usamos una funcion que no sabemos como funca pero sabemos como usarla


def doblar (numero):
    return numero*2   #aca no iteramos porque se eso se encarga map()


numeros = [2,5,10,23,50,63]

map(doblar, numeros)   #le pasas la funcion y el iterable en este caso una lista

result1 = list(map(doblar, numeros))
print(result1)


result2 = list(map(lambda x: x*2, numeros))  #ejemplo con funcion anonima
print(result2)


#en ningun momento escribo un ciclo


#filter filtrar segun una condicion
#map transforma segun una cuenta
#ambos trabajan sobre elemetos iterables
