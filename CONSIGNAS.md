# Sistema de Gestión de Productos

**Preentrega – Curso de Python**

## 1. Descripción del proyecto

Desarrollar un sistema básico de gestión de productos utilizando Python y los conceptos aprendidos durante el curso.

El programa funcionará mediante una **interfaz interactiva en la terminal**, desde la cual el usuario podrá agregar, consultar, buscar y eliminar productos.

No se requiere implementar una base de datos ni una interfaz gráfica.

## 2. Menú principal

El programa deberá presentar un menú interactivo con las siguientes opciones:

| Opción | Funcionalidad |
|:---:|---|
| 1 | Agregar un producto |
| 2 | Mostrar todos los productos |
| 3 | Buscar productos por nombre |
| 4 | Eliminar un producto |
| 5 | Salir del programa |

El menú deberá mostrarse repetidamente hasta que el usuario seleccione la **opción 5**, que finalizará la ejecución del programa.

## 3. Estructura de los datos

La información se almacenará en una **lista de listas**. Cada producto estará representado por una sublista que contendrá exactamente tres elementos:

- **Nombre:** cadena de texto.
- **Categoría:** cadena de texto.
- **Precio:** número entero, sin centavos.

Ejemplo de la estructura en Python:

```python
productos = [
    ["Teclado", "Informática", 15000],
    ["Mouse", "Informática", 8000],
    ["Cuaderno", "Librería", 3500]
]
```

No es necesario utilizar diccionarios, clases ni otras estructuras de datos más complejas.

## 4. Funcionalidades del sistema

### 4.1. Agregar un producto

Permitir al usuario registrar un nuevo producto mediante el ingreso de los siguientes datos:

- Nombre del producto.
- Categoría a la que pertenece.
- Precio expresado como número entero.

El programa deberá validar los datos ingresados antes de almacenar el producto como una nueva sublista.

### 4.2. Mostrar todos los productos

Recorrer la lista y mostrar todos los productos registrados de manera ordenada y legible.

Cada producto deberá incluir:

- Número de producto.
- Nombre.
- Categoría.
- Precio.

### 4.3. Buscar productos por nombre

Solicitar al usuario el nombre del producto que desea encontrar.

El programa deberá recorrer la lista y mostrar la información completa de todos los productos que coincidan con el criterio de búsqueda.

Si no se encuentran coincidencias, deberá informar al usuario mediante un mensaje.

### 4.4. Eliminar un producto

Permitir al usuario eliminar un producto utilizando su número o posición dentro de la lista.

El sistema deberá identificar el producto seleccionado y comprobar que la posición ingresada sea válida antes de proceder con la eliminación.

### 4.5. Salir del programa

Finalizar la ejecución del programa cuando el usuario seleccione la opción 5 del menú principal.

## 5. Conceptos de Python que se deben utilizar

| Concepto | Aplicación |
|---|---|
| Listas | Almacenar, consultar y eliminar productos. |
| Bucle `while` | Mantener el menú activo hasta que el usuario decida salir. |
| Bucle `for` | Recorrer los productos al mostrarlos o buscarlos. |
| Condicionales `if`, `elif` y `else` | Gestionar las opciones del menú y validar los datos. |
| Función `input()` | Recibir los datos y las opciones ingresadas por el usuario. |

## 6. Validación de datos

El programa deberá contemplar las siguientes validaciones para evitar errores durante su ejecución:

- [ ] Impedir el registro de productos con campos vacíos.
- [ ] Verificar que el precio ingresado sea un número entero válido.
- [ ] Comprobar que el producto seleccionado para su eliminación exista.
- [ ] Controlar las opciones ingresadas en el menú principal.

## 7. Resultado esperado

Al finalizar el proyecto, el programa deberá permitir administrar una lista de productos desde la terminal mediante un menú interactivo.

Todas las operaciones deberán realizarse sobre una lista de listas, respetando la estructura de datos establecida y utilizando los conceptos fundamentales de Python aprendidos durante el curso.

## 8. Progreso del proyecto

### Desarrollo
- [ ] Crear la estructura de datos.
- [ ] Implementar el menú principal.
- [ ] Agregar productos.
- [ ] Mostrar todos los productos.
- [ ] Buscar productos por nombre.
- [ ] Eliminar productos.
- [ ] Implementar la opción para salir del programa.

### Validaciones
- [ ] Evitar que se ingresen campos vacíos.
- [ ] Verificar que el precio sea un número entero válido.
- [ ] Comprobar que el producto exista antes de eliminarlo.
- [ ] Controlar las opciones incorrectas del menú.

### Pruebas
- [ ] Probar todas las opciones del menú.
- [ ] Probar el ingreso de datos incorrectos.
- [ ] Verificar que los productos se almacenen correctamente.
- [ ] Comprobar que el programa finalice correctamente.
