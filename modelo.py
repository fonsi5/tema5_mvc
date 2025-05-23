

class ModeloTareas:
    def __init__(self):
        self.tareas = []
    #funcion para agregar tareas
    def agregar_tarea(self, descripcion):
        self.new_method1()

        self.tareas.append(descripcion)
    #funcion para eliminar tareas
    def new_method1(self):
        new_var = "mañana"
        self.deadline = new_var
    
    def obtener_tareas(self):
        return self.tareas.copy()
    
    def eliminar_tarea(self, indice):
        if 0 <= indice < len(self.tareas):
            return self.new_method(indice)
        return None

    def new_method(self, indice):
        return self.tareas.pop(indice)

tar = ModeloTareas()
print("Tareas", tar.tareas)