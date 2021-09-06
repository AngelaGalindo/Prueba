diccionario=dict()
usuario="1"
contrasena="2"

def promedio (*valor):
    longitud=len(valor)
    promedio=sum(valor)/longitud
    return round (promedio,2) 

def ultimo_peso():
    total=[]
    for val in diccionario.values():
        total.append(val[-1])
    return total    


while True:
    usu=input("Ingrese usuario:")
    cont=input("Ingrese contraseña: ")
    lista=[]
    if usu==usuario and cont==contrasena:
        print("Ha ingresado con exito")
        break
    else:
        print("La contraseña o el usuario son incorrectos, intente de nuevo")          
        
while True:
    try:
        print("")
        cla=input("Ingrese el codigo del animal:")
        p1=float(input("Ingrese el primer peso del animal : "))
        p2=float(input("Ingrese el segundo peso del animal : "))
        p3=float(input("Ingrese el tercer peso del animal : "))               
    except ValueError:
        print("Ingrese solo numeros enteros")
    else:
        vaca=0
        if p1<= 1300 and p2 <= 1300 and p3 <= 1300:
            val=(p1,p2,p3)
            diccionario[cla]=val
            vaca+=1 
            print(diccionario)
            print("")
            y=input("Desea seguir ingresando animales si/no: ")
            if y == 'no' or y == 'No'or y=='NO':
                break 
        else:
            print("Alguno de los pesos es imposible (mayor a 1300kg ), intente de nuevo")
while True:
    print("")
    print("Opcion 1.Ver lista de pesos y promedio de cada animal")
    print("Opcion 2.Promedio de pesos entre todos los animales")
    print("Opcion 3.Extremos de pesos")
    print("Opcion 4.Destete")
    print("opcion 5.Sacrificio")
    print("opcion 6.colsulta")
    print("opcion 7.Salir") 
    try:
        x=int(input("Ingrese una opcion:"))
    except ValueError:
        print("Ingrese solo un numero entre 1 y 6")
    else:
        if x == 1:
            print("")
            print("El codigo del animal con sus respectivos pesos:",diccionario)
            for cla,val in diccionario.items():
                print(f"El animal con el codigo {cla} y con pesos {val} tiene un peso promedio de {promedio(*val)}")  
        elif x == 2:
            total=ultimo_peso()
            print("")    
            print("El promedio de pesos en el ganado es:",promedio(*total))
        elif x == 3:
            pesos=[]
            for val in diccionario.values():
                pesos.append(val[-1])
            mayor_peso=max(pesos) 
            menor_peso=min(pesos)
            print("")  
            print("El codigo del animal con sus respectivos pesos:",diccionario)
            print(f"De los ultimos pesos ingresados el menor es: {menor_peso}")
            print(f"De los ultimos pesos ingresados el mayor es: {mayor_peso} ")
        elif x == 4:
            contador=0
            total=ultimo_peso()
            for des in total:
                if des >= 120 and des <= 135:
                    contador+=1 
            print("")        
            print("El numero de vacas (con un peso entre 120 y 135) para destete es:",contador)                
        elif x == 5:
            conta=0
            total=ultimo_peso()
            for sa in total:
                if sa >= 450:
                    conta+=1
            print("")        
            print("El numero de vacas (con un peso mayor a 450) para sacrifico es:",conta)
        elif x == 6:
            try:
                print("") 
                clav=input("Ingrese el codigo del animal que quiere buscar: ")
                print(f"El animal con el codigo {clav} y con peso {diccionario[clav]} tiene un peso promedio de {promedio(*diccionario[clav])}")
                print("") 
            except KeyError:
                    print("Ese codigo no existe o no fue encontrado")
                    print("")          
        elif x == 7:
            print("Se ha cerrado sesion")
            break