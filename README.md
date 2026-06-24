# evaluacion-github-trabajo-nota
def mostrar_menu():
    print("/n----GESTOR DE TAREAS----")
    print("1.- agregar tarea")
    print("2.- listar tareas")
    print("3.- salir")

def main():
    while True:
        mostrar_menu()
        opcion = int(input("eliga una de las opciones >> "))
        if opcion == 1:
            print("(proximamente) agregar tarea")
        elif opcion ==2:
            print("(proximamente) Listar tarea")
        elif opcion ==3:
            print("saliendo del programa... hasta luego")
        else:
            print("opcion invalida, intentelo denuevo")
if_name_ == "_main_":
    main()
