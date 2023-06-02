
def ejecutar():
    sistema = Sistema()
    while True:
        option = input("ingrese la opcion: ")

        if option == "1":
            sistema.registrar_usuario()
            pass
        elif option == "2":
            print("Seleccionaste la opción 2 y saliste del sistema")
            break
        else:
            print("Opción inválida. Por favor, ingresa una opción válida.")
if __name__ =="__main__":
    ejecutar()

