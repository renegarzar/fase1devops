from flask import Flask, request, jsonify
import os

app = Flask(__name__)
CLIENTES_DIR = "/app/clientes/"
os.makedirs(CLIENTES_DIR, exist_ok=True)

@app.route("/cliente", methods=["POST"])
def registrar_cliente():
    data = request.json
    nombre = data.get("nombre")
    archivo = os.path.join(CLIENTES_DIR, f"{nombre}.txt")

    if os.path.exists(archivo):
        return jsonify({"mensaje": "Cliente ya registrado"}), 400

    with open(archivo, "w") as f:
        f.write(f"Nombre: {nombre}\\nServicios:\\n")

    return jsonify({"mensaje": "Cliente registrado"}), 201

@app.route("/cliente/<nombre>", methods=["GET"])
def obtener_cliente(nombre):
    archivo = os.path.join(CLIENTES_DIR, f"{nombre}.txt")

    if not os.path.exists(archivo):
        return jsonify({"mensaje": "Cliente no encontrado"}), 404

    with open(archivo, "r") as f:
        contenido = f.read()

    return jsonify({"datos": contenido})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

