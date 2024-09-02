from Tarea import Tareas
import time

tarea = Tareas()

print(f"Bienvenido a tu lista de tareas (To Do List)")
while True:
    print(f"\n1. Ingresar una tarea \n2. Ver Tareas")
    print(f"3. Marcar tarea como completada \n4. Eliminar tarea \n5. Salir")

    opcion = int(input("\nDigite una opcion: "))

    if opcion == 1:
        descripcion = input("Ingrese la descripción de la tarea: ")
        fecha_limite = input("Ingrese la fecha limite de la tarea (DD-MM-AAAA): ")
        tarea.agregar_tarea(descripcion, fecha_limite)
    elif opcion == 2:
        tarea.mostrar_tareas()
    elif opcion == 3:
        tarea.mostrar_tareas()
        indice= int(input("Ingrese el indice asignado a la tarea: "))
        tarea.marcar_tarea_completada(indice)
        time.sleep(1)
    elif opcion == 4:
        tarea.mostrar_tareas()
        indice= int(input("Ingrese el indice asignado a la tarea: "))
        tarea.eliminar_tarea(indice)
        time.sleep(1)
    elif opcion == 5:
        print("Vete al carajo xddd")
        break
    
    time.sleep(1)

