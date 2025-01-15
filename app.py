from flask import Flask, request, jsonify

app = Flask(__name__)

# Inventario simulado
inventario = {
    1: {"nombre": "Producto A", "cantidad": 50},
    2: {"nombre": "Producto B", "cantidad": 30},
}

# Ruta principal
@app.route("/")
def home():
    return jsonify({"message": "Bienvenido a la API de Inventario. Visita /producto para más información."})

# Ruta para manejar favicon.ico
@app.route("/favicon.ico")
def favicon():
    return "", 204

# Ruta para consultar un producto
@app.route("/producto/<id_producto>", methods=["GET"])
def get_producto(id_producto):
    try:
        # Convertimos manualmente el ID a entero
        id_producto = int(id_producto)
    except ValueError:
        # Si no es un número válido, devolvemos un error
        return jsonify({"error": "El ID del producto debe ser un entero válido."}), 400

    if id_producto <= 0:
        return jsonify({"error": "El ID del producto debe ser un entero positivo."}), 400

    producto = inventario.get(id_producto)
    if not producto:
        return jsonify({"error": "Producto no encontrado."}), 404

    return jsonify({"nombre": producto["nombre"], "cantidad": producto["cantidad"]})

# Ruta para agregar un nuevo producto
@app.route("/producto", methods=["POST"])
def post_producto():
    data = request.get_json()
    id_producto = data.get("id_producto")
    cantidad = data.get("cantidad")

    if not isinstance(id_producto, int) or id_producto <= 0:
        return jsonify({"error": "El ID del producto debe ser un entero positivo."}), 400
    if not isinstance(cantidad, int) or cantidad <= 0:
        return jsonify({"error": "La cantidad debe ser un entero positivo."}), 400

    if id_producto in inventario:
        inventario[id_producto]["cantidad"] += cantidad
    else:
        inventario[id_producto] = {"nombre": f"Producto {id_producto}", "cantidad": cantidad}

    return jsonify({"message": "Producto agregado exitosamente."})

# Ruta para actualizar el stock de un producto
@app.route("/producto/<int:id_producto>", methods=["PUT"])
def put_producto(id_producto):
    data = request.get_json()
    nueva_cantidad = data.get("nueva_cantidad")

    if not isinstance(nueva_cantidad, int) or nueva_cantidad < 0:
        return jsonify({"error": "La cantidad debe ser un entero no negativo."}), 400

    if id_producto not in inventario:
        return jsonify({"error": "Producto no encontrado."}), 404

    inventario[id_producto]["cantidad"] = nueva_cantidad
    return jsonify({"message": "Stock actualizado exitosamente."})

if __name__ == "__main__":
    app.run(debug=True)