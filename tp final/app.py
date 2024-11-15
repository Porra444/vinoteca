# from flask import Flask, jsonify, request
# from vinoteca import Vinoteca

# app = Flask(__name__)

# Vinoteca.inicializar()

# @app.route('/api/bodegas/<id>', methods=['GET'])
# def get_bodega(id):
#     bodega = Vinoteca.buscarBodega(id)
#     if bodega:
#         return jsonify(bodega.convertirAJSONFull()), 200
#     return jsonify({"error": "Bodega no encontrada"}), 404

# @app.route('/api/cepas/<id>', methods=['GET'])
# def get_cepa(id):
#     cepa = Vinoteca.buscarCepa(id)
#     if cepa:
#         return jsonify(cepa.convertirAJSONFull()), 200
#     return jsonify({"error": "Cepa no encontrada"}), 404

# @app.route('/api/vinos/<id>', methods=['GET'])
# def get_vino(id):
#     vino = Vinoteca.buscarVino(id)
#     if vino:
#         return jsonify(vino.convertirAJSONFull()), 200
#     return jsonify({"error": "Vino no encontrado"}), 404

# @app.route('/api/vinos', methods=['GET'])
# def get_vinos():
#     anio = request.args.get('anio', type=int)
#     orden = request.args.get('orden', type=str)
#     reverso = request.args.get('reverso', 'no')
#     vinos = Vinoteca.obtenerVinos(anio, orden, reverso)
#     return jsonify([vino.convertirAJSON() for vino in vinos]), 200

# if __name__ == '__main__':
#     app.run(debug=True)

# bodega.py
from entidadvineria import EntidadVineria

class Bodega(EntidadVineria):
    def __init__(self, id, nombre: str, vinos=None, cepas=None):
        super().__init__(id, nombre)
        self.vinos = vinos or []
        self.cepas = cepas or []

    def obtenerVinos(self):
        return self.vinos

    def obtenerCepas(self):
        return self.cepas

    def convertirAJSON(self):
        return {
            'id': self.id,
            'nombre': self.nombre
        }
    
    def convertirAJSONFull(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'cepas': [cepa.obtenerNombre() for cepa in self.obtenerCepas()],
            'vinos': [vino.obtenerNombre() for vino in self.obtenerVinos()]
        }
        
# cepa.py
from entidadvineria import EntidadVineria

class Cepa(EntidadVineria):
    def __init__(self, id, nombre: str, vinos=None, bodegas=None):
        super().__init__(id, nombre)
        self.vinos = vinos or []
        self.bodegas = bodegas or []

    def obtenerVinos(self):
        return self.vinos

    def obtenerBodegas(self):
        return self.bodegas

    def convertirAJSON(self):
        return {
            'id': self.id,
            'nombre': self.nombre
        }
    
    def convertirAJSONFull(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'vinos': [vino.obtenerNombre() for vino in self.obtenerVinos()],
            'bodegas': [bodega.obtenerNombre() for bodega in self.obtenerBodegas()]
        }
        
# vino.py
from entidadvineria import EntidadVineria

class Vino(EntidadVineria):
    def __init__(self, id, nombre: str, bodega: str, cepas=None, partidas=None):
        super().__init__(id, nombre)
        self.bodega = bodega
        self.cepas = cepas or []
        self.partidas = partidas or []

    def obtenerBodega(self):
        return self.bodega

    def obtenerCepas(self):
        return self.cepas

    def obtenerPartidas(self):
        return self.partidas

    def convertirAJSON(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'bodega': self.bodega,
            'cepas': self.cepas,
            'partidas': self.partidas
        }

    def convertirAJSONFull(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'bodega': self.obtenerBodega(),
            'cepas': [cepa.obtenerNombre() for cepa in self.obtenerCepas()],
            'partidas': self.partidas
        }


# app.py
from flask import Flask, jsonify, request
from vinoteca import Vinoteca

app = Flask(__name__)

# Inicializa la base de datos (vinoteca.json)
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
