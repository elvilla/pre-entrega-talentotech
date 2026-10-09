# EPIC Bikes

**Gestión de Inventario de Bicicletas de EPIC Bikes**

**Proyecto – Preentrega del Curso de Python**

---

## 1. Descripción del proyecto

**EPIC Bikes** es una aplicación desarrollada en Python que permite
gestionar un inventario básico de bicicletas mediante una interfaz
interactiva en la terminal.

La aplicación no requiere bases de datos, interfaces gráficas ni
bibliotecas externas.

## 2. Funcionalidades

El sistema presenta un menú interactivo con cinco opciones:

| Opción | Funcionalidad | Descripción |
|:---:|---|---|
| 1 | Agregar un producto | Incorporar una bicicleta al inventario. |
| 2 | Mostrar productos | Visualizar los productos registrados. |
| 3 | Buscar productos | Buscar bicicletas dentro del inventario. |
| 4 | Eliminar un producto | Eliminar una bicicleta por su número de orden. |
| 5 | Salir | Finalizar la aplicación. |

El menú permanece activo hasta que el usuario selecciona la **opción 5**.

## 3. Tecnologías utilizadas

| Tecnología | Aplicación |
|---|---|
| Python 3.10+ | Lenguaje principal de desarrollo. |
| CLI | Interacción mediante la terminal. |
| Git | Control de versiones. |
| GitHub | Publicación del repositorio. |


## 4. Instalación y ejecución

### 4.1. Requisitos

Para ejecutar Epic Bikes es necesario contar con:

- Python 3.10 o superior.
- Una terminal compatible con Python.
- Git, únicamente para clonar el repositorio.

Verificar la versión instalada:

```bash
python3 --version
```

### 4.2. Clonar el repositorio

```bash
https://github.com/elvilla/pre-entrega-talentotech
```

Ingresar al directorio:

```bash
cd pre-entrega-talentotech
```

### 4.3. Ejecutar la aplicación

```bash
python3 main.py
```

No es necesario instalar dependencias adicionales.

## 5. Funcionamiento del sistema

### 5.1. Menú principal

Al iniciar la aplicación se presenta el siguiente menú:

```text
Bienvenido a Epic Bikes

Por favor elija una de las siguientes opciones:

| 1 | Agregar un producto
| 2 | Mostrar todos los productos
| 3 | Buscar productos por nombre
| 4 | Eliminar un producto
| 5 | Salir del programa
```

### 5.2. Gestión de productos

El usuario puede:

- Agregar bicicletas al inventario.
- Consultar los productos disponibles.
- Realizar búsquedas.
- Eliminar productos mediante su número de orden.

### 5.3. Almacenamiento de información

Los productos se almacenan mediante una **lista de listas**.

**Importante:** los datos se mantienen únicamente en memoria.
Las modificaciones realizadas durante una sesión no se conservan
después de cerrar la aplicación.

## 6. Estructura del proyecto

```text
pre-entrega-talentotech/
├── main.py        # Código principal
├── CONSIGNAS.md   # Requisitos del ejercicio
├── README.md      # Documentación del proyecto
```
