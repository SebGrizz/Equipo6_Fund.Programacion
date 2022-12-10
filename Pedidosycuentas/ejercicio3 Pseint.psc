Algoritmo Pedidosycuentas
	// Paso 1: escoger una opciòn

	Escribir "(1)Ceviche"
	Escribir "(2)Arrozconmariscos" 
	Escribir "(3)Parihuela" 
	Escribir "(4)Causaacevichada"
	Escribir "ordenar tu pedido"
	Leer Opcion
	Escribir "(1)confirmar, (2)cancelar"
	Leer decision
	Si decision=1 Entonces
		Escribir "Ahora lo atendemos"
	SiNo
		Escribir "Vuelva a elegir una opcion"
	Fin Si 
	// Paso 2: pedir cuenta
	precioceviche<-30
	precioarrozconmarismo<-25
	precioparihuela<-35
	preciocausaacevichada<-35 
	Si Opcion=1 Entonces
		Escribir "su pedido sale un total de",precioceviche,"soles, gracias por su compra"
	Fin Si
	Si Opcion=2 Entonces
		Escribir "su pedido sale un total de",precioarrozconmarismo,"soles, gracias por su compra"
	Fin Si
	Si Opcion=3 Entonces
		Escribir "su pedido sale un total de",precioparihuela,"soles, gracias por su compra"
	Fin Si
	Si Opcion=4 Entonces
		Escribir "su pedido sale un total de",preciocausaacevichada,"soles, gracias por su compra"
	Fin Si
	
	
	
	
	
	
	
FinAlgoritmo
	