# -Ejemplo:
#
# como siempre >>

lista = []

for numero in range (0,10):
  lista.append(numero**2)
print (lista)

# con LC >>

lista = [numero**2 for numero in range (0,10)]
print(lista)


# -Otro Ejemplo:

# como siempre >>

lista = []
for numero in range(0,11):
  if numero % 2 == 0:
    lista.append(numero)
print(lista)

# con LC >>

lista = [ numero for numero in range(0,11) if numero % 2 == 0]
