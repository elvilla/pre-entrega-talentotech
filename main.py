#Introduccion Aplicacion
print("\nBienvenido a EPIC Bikes\n")

##Lista Bicicletas por Uso, Marca, Modelo, Valor.
lista_bicicletas = [
    ["Specialized", "Diverge 4 Pro", 17100000],
    ["Specialized", "Diverge 4 Expert", 10600001],
    ["Specialized", "Crux 5 Comp", 7814250],
    ["Specialized", "Diverge 4 Comp Carbon", 7000000],
    ["Specialized", "Crux Comp", 5400000],
    ["Specialized", "Diverge 4 Comp Alloy", 4644001],
]

##Menu Usuario
##| 1 | Agregar un producto |
##| 2 | Mostrar todos los productos |
##| 3 | Buscar productos por nombre |
##| 4 | Eliminar un producto |
##| 5 | Salir del programa |

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
        case 1:
            print("Para agregar un producto es necesario completar la siguiente informacion")
            while True:
                marca = input("Ingrese la marca: ")
                modelo = input("Ingrese el modelo: ")
                valor = input("ingrese el valor: ")
                bicicleta = [marca, modelo, valor]
                lista_bicicletas.append(bicicleta)
                #Agregar otro producto
                agregar_otro = input("Desea agregar otro producto? (Y/N): ")
                if agregar_otro != "Y":
                    break


        case 2:
            print("Listar todos los productos")
            for bicicleta in lista_bicicletas:
                print(f"Marca: {bicicleta[0]} | Modelo: {bicicleta[1]} | Precio: {bicicleta[2]}")
        
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
                   for bicicleta in lista_marca_elegida:
                        print(f"Marca: {bicicleta[0]} | Modelo: {bicicleta[1]} | Precio: {bicicleta[2]}")
                else:
                    print(f"{eleccion_marca} no se encuentra en la lista.")
                otra_busqueda = input("Desea hacer otra busqueda? (Y/N): ")
                if otra_busqueda != "Y":
                    break

        case 4:
            print("Menu para eliminar productos por numero de orden")
            while True:
                # Mostrar la lista actual (se actualiza en cada vuelta)
                for i in range(len(lista_bicicletas)):
                    bicicleta = lista_bicicletas[i]
                    print(f"{i+1}. Marca: {bicicleta[0]} | Modelo: {bicicleta[1]} | Precio: {bicicleta[2]}")

                print("Que producto desea eliminar? ")
                producto_a_eliminar = int(input(">> "))

                if producto_a_eliminar >= 1 and producto_a_eliminar <= len(lista_bicicletas):
                    lista_bicicletas.pop(producto_a_eliminar - 1)
                    print("Producto eliminado correctamente.")
                else:
                    print("El valor seleccionado es incorrecto")

                eliminar_otro = input("Desea eliminar otro producto? (Y/N): ")
                if eliminar_otro != "Y":
                    break

            # Lista final al terminar
            print("\nLista final de bicicletas:")
            for i in range(len(lista_bicicletas)):
                bicicleta = lista_bicicletas[i]
                print(f"{i+1}.Marca: {bicicleta[0]} | Modelo: {bicicleta[1]} | Precio: {bicicleta[2]}")

        case 5:
            print("Abandonando la aplicacion.")
            break
        case _:
            print("Ingreso una opcion incorrecta.")

