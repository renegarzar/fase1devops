from flask import Flask, request, jsonify
import os

app = Flask(__name__)
CLIENTES_DIR = "/home/rene/Documents/app/clientes/"

@app.route("/servicio", methods=["POST"])
def agregar_servicio():
    data = request.json
    nombre = data.get("nombre")
    servicio = data.get("servicio")
    archivo = os.path.join(CLIENTES_DIR, f"{nombre}.txt")
    
    if not os.path.exists(archivo):
        return jsonify({"mensaje": "Cliente no encontrado"}), 404
    
    with open(archivo, "a") as f:
        f.write(f"- {servicio}\n")
    return jsonify({"mensaje": "Servicio agregado"})

if __name__ == "__main__":
    app.run(debug=True, port=5001)
