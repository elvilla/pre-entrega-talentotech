#Introduccion Aplicacion
print("\nBienvenido a Epic Bikes\n")

##Lista Bicicletas por Uso, Marca, Modelo, Valor.
lista_bicicletas = [
    ["Gravel", "Specialized", "Diverge 4 Pro", 17100000],
    ["Gravel", "Specialized", "Diverge 4 Expert", 10600001],
    ["Gravel", "Specialized", "Crux 5 Comp", 7814250],
    ["Gravel", "Specialized", "Diverge 4 Comp Carbon", 7000000],
    ["Gravel", "Specialized", "Crux Comp", 5400000],
    ["Gravel", "Specialized", "Diverge 4 Comp Alloy", 4644001],
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
                uso = input("Ingrese el tipo/uso de bicicleta: ")
                marca = input("Ingrese la marca: ")
                modelo = input("Ingrese el modelo: ")
                valor = input("ingrese el valor: ")
                bicicleta = [uso, marca, modelo, valor]
                lista_bicicletas.append(bicicleta)
                #Agregar otro producto
                agregar_otro = input("Desea agregar otro producto? (Y/N): ")
                if agregar_otro != "Y":
                    break


        case 2:
            print("Listar todos los productos")
            for bicicleta in lista_bicicletas:
                print(f"Uso: {bicicleta[0]} | Marca: {bicicleta[1]} | Modelo: {bicicleta[2]} | Precio: {bicicleta[3]}")
        
        case 3:
            print("Buscador de productos por marca")
            while True:
                print("Escriba la marca de el/los producto/s a mostrar: ")
                eleccion_marca = input(">> ")
                
                lista_marca_elegida = []

                for i in lista_bicicletas:
                    if eleccion_marca == i[1]:
                        lista_marca_elegida.append(i)
                if lista_marca_elegida:
                    for b in lista_marca_elegida:
                        print(f"Marca: {b[1]} | Modelo: {b[2]} | Precio: {b[3]}")
                else:
                    print(f"{eleccion_marca} no se encuentra en la lista.")
                otra_busqueda = input("Desea hacer otra busqueda? (Y/N): ")
                if otra_busqueda != "Y":
                    break


        case 4:
            print("Menu para eliminar productos por numero de orden")
            for i in range(len(lista_bicicletas)):
                print(lista_bicicletas)
            while True:
                print("Que producto desea eliminar? ")
                producto_a_eliminar = input(">> ")
                producto_a_eliminar = int(producto_a_eliminar)
                for x in range(len(lista_bicicletas)):
                    if producto_a_eliminar == x+1:
                        lista_bicicletas.pop(producto_a_eliminar-1)
                    else:
                        print("El valor seleccionado es incorrecto")
                        break


        case 5:
            print("Abandonando la aplicacion.")
            break
        case _:
            print("Ingreso una opcion incorrecta.")

