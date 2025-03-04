from flask import Flask, jsonify
import os
import shutil

app = Flask(__name__)

# Rutas dentro del contenedor
BACKUP_DIR = "/app/almacenamiento/backups/"
CLIENTES_DIR = "/app/clientes/clientes/"  # Ajuste de la ruta

# Crear las carpetas si no existen
os.makedirs(BACKUP_DIR, exist_ok=True)
os.makedirs(CLIENTES_DIR, exist_ok=True)

@app.route("/backup", methods=["GET"])
def generar_respaldo():
    if not os.path.exists(CLIENTES_DIR):
        return jsonify({"error": "La carpeta de clientes no existe"}), 500

    archivos = os.listdir(CLIENTES_DIR)

    for archivo in archivos:
        shutil.copy(os.path.join(CLIENTES_DIR, archivo), BACKUP_DIR)

    return jsonify({"mensaje": "Respaldo generado exitosamente en almacenamiento"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)

