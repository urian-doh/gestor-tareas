tareas = []

def agregar_tarea(titulo):
    if not titulo.strip():
        raise ValueError("Titulo vacío")
    tareas.append(titulo.strip())

def listar_tareas():
    return tareas