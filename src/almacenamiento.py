from flask import Flask, jsonify
import os

app = Flask(__name__)
BACKUP_DIR = "/home/rene/Documents/app/backups/"
os.makedirs(BACKUP_DIR, exist_ok=True)

@app.route("/backup", methods=["GET"])
def generar_respaldo():
    archivos = os.listdir("/home/rene/Documents/app/clientes/")
    for archivo in archivos:
        os.system(f"cp /home/rene/Documents/app/clientes/{archivo} {BACKUP_DIR}")
    return jsonify({"mensaje": "Respaldo generado exitosamente"})

if __name__ == "__main__":
    app.run(debug=True, port=5002)
