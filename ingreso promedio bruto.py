preciodeceviche = 30
precioarrozconmarismo = 25
precioparihuela = 35
preciocausaacevichada =35

n1 = float(input("ingrese el numero de pedidos del ceviche\n"))
n2 = float(input("ingrese el numero de pedidos del arroz con marisco\n"))
n3 = float(input("ingrese el numero de pedidos de parihuela\n"))
n4 = float(input("ingrese el numero de pedidos de causa acevichada\n"))

recau1 = n1*preciodeceviche
recau2 = n2*precioarrozconmarismo
recau3 = n3*precioparihuela
recau4 = n4*preciocausaacevichada

print ("lo recaudado de ceviche es", recau1)
print("lo recaudado de arroz con mariszo es", recau2)
print("lo recaudado de parihuela es", recau3)
print("lo recaudado de causa acevichada es", recau4)

sumatotal = recau1+recau2+recau3+recau4
print("el total recaudado del restaurant es", sumatotal)


