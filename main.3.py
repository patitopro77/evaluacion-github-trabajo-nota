def mostrar_menu():
    """Muestra las opciones disponibles en el sistema."""
    print("\n=== GESTOR DE TAREAS ===")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir")
    print("========================")

def agregar_tarea(tareas):
    """Agrega una nueva tarea con estado inicial pendiente."""
    descripcion = input("\nIngrese la descripción de la tarea: ").strip()
    if not descripcion:
        print("❌ Error: La descripción no puede estar vacía.")
        return
    
    nueva_tarea = {
        "descripcion": descripcion,
        "completada": False
    }
    tareas.append(nueva_tarea)
    print(f"✅ Tarea '{descripcion}' agregada con éxito.")
# Lista global para almacenar las tareas como diccionarios
tareas = []

def agregar_tarea():
    titulo = input("Ingrese el título de la tarea: ")
    # Cada tarea es un diccionario con titulo y estado
    nueva_tarea = {"titulo": titulo, "completada": False}
    tareas.append(nueva_tarea)
    print(f"Tarea '{titulo}' agregada con éxito.")

def listar_tareas():
    print("\n--- LISTA DE TAREAS ---")
    for i, tarea in enumerate(tareas, 1):
        estado = "Completada" if tarea["completada"] else "Pendiente"
        print(f"{i}. {tarea['titulo']} [{estado}]")

def mostrar_menu():
    print("\n--- GESTOR DE TAREAS ---")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            agregar_tarea()
        elif opcion == "2":
            listar_tareas()
        elif opcion == "3":
            print("Saliendo del programa... ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()

tareas = []

def agregar_tarea():
    titulo = input("Ingrese el título de la tarea: ")
    nueva_tarea = {"titulo": titulo, "completada": False}
    tareas.append(nueva_tarea)
    print(f"Tarea '{titulo}' agregada con éxito.")

def listar_tareas():
    print("\n--- LISTA DE TAREAS ---")
    for i, tarea in enumerate(tareas, 1):
        estado = "Completada" if tarea["completada"] else "Pendiente"
        print(f"{i}. {tarea['titulo']} [{estado}]")

def marcar_completada():
    listar_tareas()
    try:
        indice = int(input("Ingrese el número de la tarea a marcar como completada: ")) - 1
        tareas[indice]["completada"] = True
        print(f"Tarea '{tareas[indice]['titulo']}' marcada como completada.")
    except:
        print("Ocurrió un error al procesar el índice.")

def mostrar_menu():
    print("\n--- GESTOR DE TAREAS ---")
    print("1. Agregar tarea")
    print("2. Listar tareas")
    print("3. Marcar tarea como completada")  # Nueva opción
    print("4. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            agregar_tarea()
        elif opcion == "2":
            listar_tareas()
        elif opcion == "3":
            marcar_completada()
        elif opcion == "4":
            print("Saliendo del programa... ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if _name_ == "_main_":
    main()