from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/promedio', methods=['POST'])
def calcular_promedio():
    datos = request.get_json()
    if not datos or 'calificaciones' not in datos:
        return jsonify({"error": "Faltan datos o calificaciones"}), 400
        
    nombre = datos.get('nombre', 'Estudiante')
    calificaciones = datos['calificaciones']
    promedio = sum(calificaciones) / len(calificaciones)
    
    return jsonify({
        "nombre": nombre,
        "promedio": promedio
    })

if __name__ == '__main__':
    app.run(debug=True)
