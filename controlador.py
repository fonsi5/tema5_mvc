from modelo import ModeloTareas
from vista import VistaConsola

class ControladorTareas:
    def __init__(self):
        self.modelo = ModeloTareas()
        self.vista = VistaConsola()
    
    def ejecutar(self):
        while True:
            opcion = self.vista.mostrar_menu()
            
            if opcion == "1":
                tareas = self.modelo.obtener_tareas()
                self.vista.mostrar_tareas(tareas)
            
            elif opcion == "2":
                nueva_tarea = self.vista.obtener_tarea()
                self.modelo.agregar_tarea(nueva_tarea)
            
            elif opcion == "3":
                indice = self.vista.obtener_indice()
                tarea_eliminada = self.modelo.eliminar_tarea(indice)
                if tarea_eliminada:
                    print(f"Eliminada: {tarea_eliminada}")
            
            elif opcion == "4":
                print("¡Hasta luego!")
                break
            
            else:
                print("Opción inválida")