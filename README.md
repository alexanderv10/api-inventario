# API de Inventario

## Descripción
Esta API permite realizar operaciones de inventario básicas como:
- Consultar productos.
- Agregar nuevos productos.
- Actualizar la cantidad de productos existentes.

La API está implementada con Flask y utiliza un inventario simulado en memoria.

## Requisitos
- Python 3.8 o superior.
- Flask (incluido en requirements.txt).

## Instalación
Sigue estos pasos para configurar y ejecutar la API:

- Clona este repositorio
- Crea un entorno virtual y actívalo:
    python -m venv venv
    venv\Scripts\activate
- Instala las dependencias:
    pip install -r requirements.txt

## Ejecución
- Ejecuta el servidor Flask:
    python app.py
- La API estará disponible en http://127.0.0.1:5000/.

## Endpoints
1. Consultar Producto
Método: GET
URL: /producto/{id_producto}
Validaciones:
    El ID debe ser un entero positivo.
    Devuelve error 404 si el producto no existe.

2. Agregar Producto
Método: POST
URL: /producto
Cuerpo (JSON):
{
    "id_producto": 3,
    "cantidad": 20
}
Validaciones:
id_producto y cantidad deben ser números enteros positivos.

3. Actualizar Producto
Método: PUT
URL: /producto/{id_producto}
Cuerpo (JSON):
{
    "nueva_cantidad": 100
}
Validaciones:
id_producto debe ser un entero positivo.
nueva_cantidad debe ser un entero no negativo.

## Pruebas
Pruebas realizadas con Postman, incluyendo casos válidos e inválidos:

Consulta de producto existente y no existente.
Agregar un producto nuevo.
Actualizar stock de un producto.
Validaciones para IDs negativos o no válidos.

Pruebas Unitarias

El archivo `test_app.py` incluye pruebas automatizadas para validar los endpoints de la API. Estas pruebas fueron ejecutadas usando `pytest` y cubren los siguientes casos:

1. Ruta Principal (`GET /`):
   - Validación del mensaje de bienvenida.

2. Consultar Producto (`GET /producto/{id_producto}`):
   - Caso válido: Producto encontrado.
   - Caso inválido: Producto no encontrado.

3. Agregar Producto (`POST /producto`):
   - Caso válido: Producto agregado exitosamente.
   - Caso inválido: Validación de datos incorrectos.

4. Actualizar Producto (`PUT /producto/{id_producto}`):
   - Caso válido: Stock actualizado exitosamente.
   - Caso inválido: Producto no encontrado o cantidad no válida.

Cómo ejecutar las pruebas
1. Asegúrese de que el entorno virtual esté activado.
2. Ejecute el comando:
   pytest
3. Verifique que todas las pruebas pasen exitosamente.