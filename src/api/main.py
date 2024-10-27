from flask import Flask
from flask_cors import CORS
from flask import jsonify,request
from config import config
from models import db,Empleado,Departamento,Mision,Viaje,Jefe_departamento

def create_app(enviroment):
	app = Flask(__name__)
	app.config['JSON_AS_ASCII'] = False
	app.config.from_object(enviroment)
	with app.app_context():
		db.init_app(app)
		db.create_all()
	return app

# Accedemos a la clase config del archivo config.py
enviroment = config['development']
app = create_app(enviroment)
CORS(app)

#rutas empleado
@app.route('/empleados', methods=['POST'])
def crear_empleado():

    request_body = request.json
    empleado.append(request_body)

    return "Ingresado OK", 200

@app.route('/empleados', methods=['GET'])
def get_empleado():

    empleados = [emp.json() for emp in Empleado.query.all()]
    print(Empleado.query.all())
    return jsonify({'empleados': empleados})
    

@app.route('/empleados/<id>', methods=['REMOVE'])
def delete_empleado(id):

    empleado = Empleado.query.filter_by(id=id).first()
    empleado.delete()
    return jsonify({'mensaje':'empleado borrado'})

##----------------------------------------------------------------------------
#rutas departamento

@app.route('/departamento', methods=['POST'])
def crear_departamento():

    request_body = request.json
    departamento.append(request_body)

    return "Ingresado OK"

@app.route('/departamento', methods=['GET'])
def get_departamento():

    departamento = [dep.json() for dep in Departamento.query.all()]
    return jsonify(departamento)


@app.route('/departamento/<id>', methods=['REMOVE'])
def delete_departamento(id):

    departamento = Departamento.query.filter_by(id=id).first()
    departamento.delete()
    return jsonify({'mensaje':'departamento borrado'})

##----------------------------------------------------------------------------
#rutas jefe de departamento

@app.route('/jefe', methods=['POST'])
def crear_jefe():

    request_body = request.json
    jefe.append(request_body)

    return "Ingresado OK"

@app.route('/jefe', methods=['GET'])
def get_jefe():

    jefe = [dep.json() for jef in Jefe_departamento.query.all()]
    return jsonify(jefe)


@app.route('/jefe/<id>', methods=['REMOVE'])
def delete_jefe(id):

    jefe = Jefe_departamento.query.filter_by(id=id).first()
    jefe.delete()
    return jsonify({'mensaje':'jefe borrado'})


##----------------------------------------------------------------------------
#rutas viaje

@app.route('/viaje', methods=['POST'])
def crear_viaje():

    request_body = request.json
    viaje.append(request_body)

    return "Ingresado OK"

@app.route('/viaje', methods=['GET'])
def get_viaje():

    viaje = [dep.json() for viaj in Viaje.query.all()]
    return jsonify(viaje)


@app.route('/viaje/<id>', methods=['REMOVE'])
def delete_viaje(id):

    viaje = Viaje.query.filter_by(id=id).first()
    viaje.delete()
    return jsonify({'mensaje':'viaje borrado'})

##----------------------------------------------------------------------------
#rutas mision

@app.route('/mision', methods=['POST'])
def crear_mision():

    request_body = request.json
    mision.append(request_body)

    return "Ingresado OK"

@app.route('/mision', methods=['GET'])
def get_mision():

    mision = [dep.json() for misi in Mision.query.all()]
    return jsonify(mision)


@app.route('/mision/<id>', methods=['REMOVE'])
def delete_mision(id):

    mision = Viaje.query.filter_by(id=id).first()
    mision.delete()
    return jsonify({'mensaje':'mision borrada'})

#Inicar API
if __name__ == '__main__':
	app.run(debug=True)### AYUDA ª