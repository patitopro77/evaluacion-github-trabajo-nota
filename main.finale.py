
tareas = []

def agregar_tarea():
    titulo = input("\nIngrese el título de la tarea: ").strip()
    # Validación: evita cadenas vacías o espacios en blanco
    if not titulo:
        print("Error: El título de la tarea no puede estar vacío.")
        return
    
    nueva_tarea = {"titulo": titulo, "completada": False}
    tareas.append(nueva_tarea)
    print(f"Tarea '{titulo}' agregada con éxito.")

def listar_tareas():
    """Muestra en pantalla todas las tareas con su respectivo índice y estado."""
    if not tareas:
        print("\nInfo: No hay tareas registradas en el sistema.")
        return False
        
    print("\n================ LISTA DE TAREAS ================")
    for i, tarea in enumerate(tareas, 1):
        estado = " Completada" if tarea["completada"] else " Pendiente"
        print(f"[{i}] {tarea['titulo']} - Estado: {estado}")
    print("=================================================")
    return True

def marcar_completada():
    """Cambia el estado lógico del diccionario seleccionado a True."""
    if not listar_tareas():
        return
    try:
        indice = int(input("\nSeleccione el número de tarea completada: ")) - 1
        # Validación: Evita desbordamiento de índices (IndexError)
        if 0 <= indice < len(tareas):
            tareas[indice]["completada"] = True
            print(f"Tarea '{tareas[indice]['titulo']}' marcada como completada.")
        else:
            print("Error: El número ingresado está fuera de rango.")
    except ValueError:
        print("Error: Entrada inválida. Debe digitar un número entero.")

def eliminar_tarea():
    """Remueve de forma definitiva un elemento de la lista por su posición."""
    if not listar_tareas():
        return
    try:
        indice = int(input("\nSeleccione el número de tarea a eliminar: ")) - 1
        if 0 <= indice < len(tareas):
            # libera espacio de la memoria
            tarea_eliminada = tareas.pop(indice)
            print(f"Tarea '{tarea_eliminada['titulo']}' eliminada correctamente.")
        else:
            print("Error: El número ingresado está fuera de rango.")
    except ValueError:
        print("Error: Entrada inválida. Ingrese exclusivamente números.")

def mostrar_menu():
    """Imprime el menú de navegación del sistema."""
    print("\nMENÚ PRINCIPAL DEL SISTEMA")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir del programa")

def main():
    """Punto de entrada principal para la ejecución de la aplicación."""
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción (1-5): ").strip()
        
        if opcion == 1:
            agregar_tarea()
        elif opcion == 2:
            listar_tareas()
        elif opcion == 3:
            marcar_completada()
        elif opcion == 4:
            eliminar_tarea()
        elif opcion == 5:
            print("\nEjecución finalizada. Gracias por utilizar el sistema.")
            break
        else:
            print("Opción no válida. Por favor, marque una opción del 1 al 5.")

# Ejecución del programa
main()

