import random

trabajadores = ["Juan Pérez", "María García", "Carlos López", "Ana Martínez", "Pedro Rodríguez",
           "Laura Hernández", "Miguel Sánchez", "Isabel Gómez", "Francisco Díaz", "Elena Fernández"]

datos_trabajadores = []


def asignar_sueldos():
    for trabajador in trabajadores:
        sueldo = random.randrange(300000,2500000)
    
        datos_trabajadores.append({"nombre":trabajador, "sueldo": sueldo, "categoria":clasifica_sueldos(sueldo)})


def clasifica_sueldos(sueldo):
    if  sueldo < 800000:
        return "sueldos menores a $800.000"
    elif 800000 <= sueldo<= 2000000:
        return "sueldos entre $800.000 y $2.000.000"
    elif sueldo > 2000000:
        return "sueldos mayores a $2.000.000"
        
def estadisticas():
    sueldos = []
    for trabajador in datos_trabajadores:
        sueldos.append(trabajador["sueldo"])

    return max(sueldos), min(sueldos), (sum(sueldos)/len(sueldos))


def mostrarTrabajadores(rango):
    print(f"\nCATEGORIA : {rango}\n")
    for trabajador in datos_trabajadores:
        if trabajador["categoria"] == rango:
            print(f"\tnombre: {trabajador["nombre"]}, sueldo:{trabajador["sueldo"]}" )

asignar_sueldos()
 
while True:
    print("\n\n MENU PRINCIPAL\n\n")
    print("1. Asignar sueldos aleatorios")
    print("2. Clasificar sueldos")
    print("3. Ver estadisticas")
    print("4. reporte de sueldos")
    print("5. Salir")

    opcion = int(input("ingrese su opcion >>"))

    if opcion == 5:
        print("\n\n\tSaliendo ...")
        break
    elif opcion == 1:
        print ("sueldos creados") 

    elif opcion == 2:
        print("\n\n\tMENU MOSTRAR TRABAJDORES POR CATEGORIA")
        mostrarTrabajadores("sueldos menores a $800.000")
        mostrarTrabajadores("sueldos entre $800.000 y $2.000.000")
        mostrarTrabajadores("sueldos mayores a $2.000.000")
        input("\n\n\t >> PRESIONE ENTER PARA CONTINUAR <<")

    elif opcion == 3:
        print("\n\n\tMENU MOSTRAR ESTADISTICAS")
        maximo, minimo, promedio = estadisticas()
        print(f"\n\tsueldo maximo : ${maximo}\n\tsueldo minimo: ${minimo}\n\tPromedio: ${promedio}")
        input("\n\n\t >> PRESIONE ENTER PARA CONTINUAR <<")

  
