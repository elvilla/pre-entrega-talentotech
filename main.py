#Imports
import enum

#Introduccion Aplicacion
print("\nBienvenido a EPIC Bikes\n")

##Lista de Bicicletas (por Marca, Modelo, Valor)
lista_bicicletas = [
    ["Specialized", "Diverge 4 Pro", 17100000],
    ["Specialized", "Diverge 4 Expert", 10600001],
    ["Specialized", "Crux 5 Comp", 7814250],
    ["Specialized", "Diverge 4 Comp Carbon", 7000000],
    ["Specialized", "Crux Comp", 5400000],
    ["Specialized", "Diverge 4 Comp Alloy", 4644001],
]

#Menu Usuario
print("Por favor elija una de las siguientes opciones:")
while True:
    print("""
    | 1 | Agregar un producto
    | 2 | Mostrar todos los productos
    | 3 | Buscar productos por nombre
    | 4 | Eliminar un producto
    | 5 | Salir del programa
    """)
    seleccion_opcion_usuario = int(input(">> "))

    match seleccion_opcion_usuario:
        #Agregar Producto
        case 1:
            print("Para agregar un producto es necesario completar la siguiente informacion")
            while True:
                marca = input("Ingrese la marca: ")
                marca = marca.strip().capitalize()

                modelo = input("Ingrese el modelo: ")
                modelo = modelo.strip().capitalize()

                valor = input("ingrese el valor: ")
                valor = valor.strip().capitalize()

                bicicleta = [marca, modelo, valor]
                agregar_confirmacion = input(f"Confirma que desea agregar el producto: Marca: {marca} | Modelo: {modelo} | Precio: {valor}? (Y/N: )").upper()
                if agregar_confirmacion != "Y":
                    break
                else:
                    lista_bicicletas.append(bicicleta)
                
                #Agregar otro producto
                agregar_otro = input("Desea agregar otro producto? (Y/N): ").upper()
                if agregar_otro != "Y":
                    break

        #Lista Productos
        case 2:
            for i, (marca, modelo, valor) in enumerate(lista_bicicletas, start=1):
                print(f"{i}) Marca: {marca} | Modelo: {modelo} | Precio: ${valor}")
        
        #Buscador Productos
        case 3:
            print("Buscador de productos por marca")
            while True:
                print("Escriba la marca de el/los producto/s a mostrar: ")
                eleccion_marca = input(">> ")
                
                lista_marca_elegida = []

                for i in lista_bicicletas:
                    if eleccion_marca == i[0]:
                        lista_marca_elegida.append(i)
                
                if lista_marca_elegida:
                    for i, (marca, modelo, valor) in enumerate(lista_marca_elegida, start=1):
                        print(f"> Marca: {marca} | Modelo: {modelo} | Precio: ${valor}")
                
                else:
                    print(f"{eleccion_marca} no se encuentra en la lista.")
                otra_busqueda = input("Desea hacer otra busqueda? (Y/N): ").upper()
                if otra_busqueda != "Y":
                    break
        
        #Eliminar Productos
        case 4:
            print("Menu para eliminar productos por numero de orden")
            while True:
                # Mostrar la lista actual (se actualiza en cada vuelta)
                for i, (marca, modelo, valor) in enumerate(lista_bicicletas, start=1):
                    print(f"{i}) Marca: {marca} | Modelo: {modelo} | Precio: ${valor}")

                print("Que producto desea eliminar? ")
                producto_a_eliminar = int(input(">> "))
                if producto_a_eliminar >= 1 and producto_a_eliminar <= len(lista_bicicletas):
                    marca, modelo, valor = lista_bicicletas[producto_a_eliminar - 1]
                    eliminar_confirmacion = input(f"Confirma que desea eliminar: {marca} | {modelo}? (Y/N): ").upper()

                    if eliminar_confirmacion == "Y":
                        lista_bicicletas.pop(producto_a_eliminar - 1)
                        print("Producto eliminado")
                    else:
                        break

                else:
                    print("El valor seleccionado es incorrecto")

                eliminar_otro = input("Desea eliminar otro producto? (Y/N): ").upper()

                if eliminar_otro != "Y":
                    break

            # Lista final al terminar
            print("\nLista final de bicicletas:")
            for i, (marca, modelo, valor) in enumerate(lista_bicicletas, start=1):
                print(f"{i}) Marca: {marca} | Modelo: {modelo} | Precio: {valor}")
        
        #Cerrar Aplicacion
        case 5:
            print("Abandonando la aplicacion.")
            break
        case _:
            print("Ingreso una opcion incorrecta.")
