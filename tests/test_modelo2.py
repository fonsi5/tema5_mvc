from modelo import ModeloTareas

def test_agregar_tarea():
    tar = ModeloTareas()
    tar.agregar_tarea("Tarea de Prueba")
    tar_updated = tar.obtener_tareas()
    assert tar_updated == ["Tarea de Prueba"]