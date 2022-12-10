print(("digite el primer plato que desea ordenar"))
plato1 = input()
print(("digite el segundo plato que desea ordenar"))
plato2 = input()
print(("digite el tercer plato que desea ordenar"))
plato3 = input()
print(("digite el cuarto plato que desea ordenar"))
plato4 = input()
n = 4
arreglo = [str() for ind0 in range(n)]
arreglo[0] = plato1
arreglo[1] = plato2
arreglo[2] = plato3
arreglo[3] = plato4
print(("el orden en el que seran atendidos los platos son :"))
for i in range(4,0,-1):
		print((arreglo[i-1]))

