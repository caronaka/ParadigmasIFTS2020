#FILTER() Y MAP()

#Las funciones preferidas del paradigma funcional


#FILTER
#filtrar un iterable y nos devuelve una nueva coleccion

def multiple(num):
    if num % 5  == 0:
        return True

num = [2,5,10,23,25,33]

resultado = list(filter(multiple, num))

print(resultado)

#el primer parametro de filter es la condicion y segundo parametro num que es la lista

#si te devuelve filter objetct at 0x754654
#objeto de tipo filter y el numero es el espacio en la memoria
#tenes que pasarlo a lista con list()



resultado2 = list(filter(lambda numero : numero %5 == 0, num))
print(resultado2)

#ejemplo sin usar funcion multiple. usamos lambda.
#nombre del parametro.
