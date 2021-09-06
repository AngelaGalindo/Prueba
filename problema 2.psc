Algoritmo Area
	Escribir 'escriba la hipotenusa de la figura'
	Leer hip
	Escribir 'escriba radio o cateto de la figura'
	Leer rad
	areasemicir <- (PI*rad^2)/2
	cat1 <- rc(hip^2-rad^2)
	areatri <- ((rad*2)*cat1)/2
	areafora <- (areasemicir+areatri)
	Escribir 'El area de la forma A es ',areafora
FinAlgoritmo
