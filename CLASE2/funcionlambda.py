#LAMBDA

# son funciones matematicas y anonimas
# no le tenes que poner nombre
# o usarla sin nombrarla
#si la funcion la vas a usar mucho, conviene nombrarla con def

#
# no funciona con funciones muy largas
# hay que reducirlas a una linea de codigo
# si requiere mas, yo no podemos usar lambda
#
# SIMPLIFICANDO

def doblar (num):  #asi lo veniamos haciendo
  resultado = num*2
  return resultado
#
print(doblar(2))
#
def doblar(num):
    return num*2
#
# #lambda num: num*2

doblar2 = lambda num: num*2
print(doblar2(2))


#LAMBDA nombredelparametro : lo que queremos devolver
