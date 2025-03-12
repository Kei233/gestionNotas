
lista_notas = []
lista_estudiantes = {"nombre": "Juan", "notas": []}


def menu() -> str:
    print("\n=== Menú de opciones ===")
    print("1- Ingresar notas de estudiante")
    print("2- Mostrar notas del estudiante")
    print("3- Salir")
    opcion = int(input("> Ingrese una opción 🍨: "))
    return opcion


def ingresar_notas(nombre, lista_notas) -> list:
    for estudiante in lista_notas:
        if (lista_estudiantes["nombre"] == nombre):
            print("Ingresar notas")
            nota = float(input("Ingrese una nota: "))
            input("Presione Enter para continuar...")
            lista_notas[nombre].append(nota)
        else:
            print("Estudiante no encontrado... Creando estudiante")
            lista_notas[nombre] = {"nombre": nombre, "notas": []}
            print("Ingresar notas")
            lista_notas[nombre].append(nota)
            input("Presione Enter para continuar...")


def mostrar_notas(lista_notas) -> None:
    print("📠 Notas: 📠")
    i = 0
    for nota in lista_notas:
        i += 1
        print(f"{i}. ", nota)

    input("Presione Enter para continuar...")


def inicio() -> None:
    opcion = menu()
    while True:
        if opcion == 1:
            ingresar_notas(lista_notas)
        elif opcion == 2:
            mostrar_notas(lista_notas)
        elif opcion == 3:
            print("Hasta luego")
            break
        else:
            print("Opción inválida")
        opcion = menu()


inicio()
