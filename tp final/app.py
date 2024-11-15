from flask import Flask, jsonify, request
from vinoteca import Vinoteca

app = Flask(__name__)

Vinoteca.inicializar()

@app.route('/api/bodegas/<id>', methods=['GET'])
def get_bodega(id):
    bodega = Vinoteca.buscarBodega(id)
    if bodega:
        return jsonify(bodega.convertirAJSONFull()), 200
    return jsonify({"error": "Bodega no encontrada"}), 404

@app.route('/api/cepas/<id>', methods=['GET'])
def get_cepa(id):
    cepa = Vinoteca.buscarCepa(id)
    if cepa:
        return jsonify(cepa.convertirAJSONFull()), 200
    return jsonify({"error": "Cepa no encontrada"}), 404

@app.route('/api/vinos/<id>', methods=['GET'])
def get_vino(id):
    vino = Vinoteca.buscarVino(id)
    if vino:
        return jsonify(vino.convertirAJSONFull()), 200
    return jsonify({"error": "Vino no encontrado"}), 404

@app.route('/api/vinos', methods=['GET'])
def get_vinos():
    anio = request.args.get('anio', type=int)
    orden = request.args.get('orden', type=str)
    reverso = request.args.get('reverso', 'no')
    vinos = Vinoteca.obtenerVinos(anio, orden, reverso)
    return jsonify([vino.convertirAJSON() for vino in vinos]), 200

if __name__ == '__main__':
    app.run(debug=True)