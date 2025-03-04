from flask import Flask, request, jsonify
import os

app = Flask(__name__)
CLIENTES_DIR = "/app/clientes/"

@app.route("/servicio", methods=["POST"])
def agregar_servicio():
    data = request.json
    nombre = data.get("nombre")
    servicio = data.get("servicio")
    archivo = os.path.join(CLIENTES_DIR, f"{nombre}.txt")

    if not os.path.exists(archivo):
        return jsonify({"mensaje": "Cliente no encontrado"}), 404

    with open(archivo, "a") as f:
        f.write(f"- {servicio}\\n")

    return jsonify({"mensaje": "Servicio agregado"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)

