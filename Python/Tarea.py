class Tareas:

    def __init__(self):
        self.listaTareas = []

    #Metodo para agregar una tarea a la lista de tareas
    def agregar_tarea(self, descripcion, fecha_limite):
        longitud = 0
        if self.listaTareas:
            longitud = len(self.listaTareas)
        #Generamos el objeto de tipo tarea
        nuevaTarea = {"Indice" : longitud, "Descripcion": descripcion, "Fecha_Limite": fecha_limite, "Estado": False}
        #Agregamos la tarea a la lista de tareas
        self.listaTareas.append(nuevaTarea)
        print("¡Tarea agregada con exíto!")

    #Metodo para listar las tareas de la lista de tareas
    def mostrar_tareas(self):
        if self.listaTareas:
            #Recorremos la lista de tareas y imprimimos la lista de tareas
            for objeto in self.listaTareas:
                #Validamos el estado de la tarea
                if objeto.get("Estado"):
                    mensaje = "Completada"
                else:
                    mensaje = "No completada"
                print(f"Indice : {objeto.get("Indice")} - Estado : {mensaje} - Descripcion : {objeto.get("Descripcion")} - Fecha limite : {objeto.get("Fecha_Limite")}")
        else:
            print("\nNo hay tareas aún")

    #Metodo para marcar tareas como completadas de la lista de tareas
    def marcar_tarea_completada(self, indice):
        mensaje = "No se ha encontrado la tarea :("
        iterador = 0
        for objeto in self.listaTareas:
            if objeto.get("Indice") == indice:
                self.listaTareas[iterador]["Estado"] = True
                mensaje = "¡Tarea marcada con exíto!"
                break
            iterador += 1
        print(mensaje)
        

    #Metodo para eliminar una tarea de la lista tareas 
    def eliminar_tarea(self, indice):
        mensaje = "No se ha encontrado la tarea :("
        iterador = 0
        for objeto in self.listaTareas:
            if objeto.get("Indice") == indice:
                self.listaTareas.pop(indice)
                mensaje= "¡Tarea eliminada con exíto!"
                break
            iterador += 1
        print(mensaje)

