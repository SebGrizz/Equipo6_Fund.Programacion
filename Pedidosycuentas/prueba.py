


if __name__ == '__main__':
	precioceviche = 30
	precioarrozconmarismo = 25
	precioparihuela = 35
	preciocausaacevichada = 35
	
	print("(1)Ceviche")
	print("(2)Arrozconmariscos")
	print("(3)Parihuela")
	print("(4)Causaacevichada")
	print("ordenar tu pedido")
	opcion = int(input())
	print("(1)confirmar, (2)cancelar")
	decision = int(input())
	if decision == 1:
		print("Ahora lo atendemos")
	else:
		print("Vuelva a elegir una opcion")

	
	if opcion==1:
		print("su pedido sale un total de",precioceviche,"soles, gracias por su compra")
	if opcion==2:
		print("su pedido sale un total de",precioarrozconmarismo,"soles, gracias por su compra")
	if opcion==3:
		print("su pedido sale un total de",precioparihuela,"soles, gracias por su compra")
	if opcion==4:
		print("su pedido sale un total de",preciocausaacevichada,"soles, gracias por su compra")

