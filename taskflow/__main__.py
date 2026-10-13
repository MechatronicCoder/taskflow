"""Demo del proyecto. Ejecutar con: python -m taskflow"""
from taskflow import GestorTareas, __version__


def mostrar(tareas):
    for tarea in tareas:
        estado = "[x]" if tarea.completada else "[ ]"
        print(f"  {estado} #{tarea.id} {tarea.titulo} ({tarea.prioridad})")


def main():
    gestor = GestorTareas()
    gestor.agregar("Configurar el repositorio en GitHub", "alta")
    gestor.agregar("Escribir el README", "media")
    gestor.agregar("Repasar el material de la clase", "baja")
    gestor.agregar("Preparar demo", "alta")
    gestor.completar(1)
    gestor.completar(2)
    gestor.completar(3)

    print(f"TaskFlow v{__version__}")
    print("\nTodas las tareas:")
    mostrar(gestor.listar())

    print("\nFiltro por prioridad alta (TF-8):")
    mostrar(gestor.filtrar_por_prioridad("alta"))

    print('\nBusqueda de "readme" (TF-9):')
    mostrar(gestor.buscar_texto("readme"))

    r = gestor.resumen()
    print("\nResumen de avance (TF-10):")
    print(f"  {r['completadas']} de {r['total']} completadas, "
          f"{r['pendientes']} pendientes, avance {r['avance']} %")

    print("\nTitulo duplicado (TF-11):")
    try:
        gestor.agregar("  preparar DEMO ")
    except ValueError as error:
        print(f"  Rechazado: {error}")


if __name__ == "__main__":
    main()