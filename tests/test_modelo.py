from modelo import ModeloTareas

def test_agregar_tarea():
    modelo = ModeloTareas()
    modelo.agregar_tarea("Tarea 1")
    assert modelo.obtener_tareas() == ["Tarea 1"]

def test_obtener_tareas_copia():
    modelo = ModeloTareas()
    modelo.agregar_tarea("Tarea 1")
    tareas = modelo.obtener_tareas()
    tareas.append("Tarea 2")
    # La lista interna no debe cambiar
    assert modelo.obtener_tareas() == ["Tarea 1"]

def test_eliminar_tarea_valida():
    modelo = ModeloTareas()
    modelo.agregar_tarea("Tarea 1")
    modelo.agregar_tarea("Tarea 2")
    tarea_eliminada = modelo.eliminar_tarea(0)
    assert tarea_eliminada == "Tarea 1"
    assert modelo.obtener_tareas() == ["Tarea 2"]

def test_eliminar_tarea_invalida():
    modelo = ModeloTareas()
    modelo.agregar_tarea("Tarea 1")
    tarea_eliminada = modelo.eliminar_tarea(5)  # índice fuera de rango
    assert tarea_eliminada is None
    assert modelo.obtener_tareas() == ["Tarea 1"]