from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:PG123@localhost/TareaDB'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)
class Tarea(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)  
    descripcion = db.Column(db.String(200), nullable=False)
    fecha = db.Column(db.Date, nullable=False)

    def __init__(self, name, description, due_date):
        self.name = name
        self.descripcion = description
        self.fecha = due_date


class TareaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Tarea
        load_instance = True
        fields = ('id', 'name', 'descripcion', 'fecha')  

Tarea_schema = TareaSchema()
Tareas_schema = TareaSchema(many=True)


@app.route('/tarea', methods=['POST'])
def add_Tarea():
    name = request.json['name']
    descript = request.json['descripcion']
    date = request.json['fecha']
    new_Tarea = Tarea(name,descript, date)
    db.session.add(new_Tarea)
    db.session.commit()
    return Tarea_schema.jsonify(new_Tarea)

@app.route('/tarea', methods=['GET'])
def get_Tareas():
    all_Tareas = Tarea.query.all()
    result = Tareas_schema.dump(all_Tareas)
    return jsonify(result)

@app.route('/tarea/<id>', methods=['GET'])
def get_Tarea(id):
    tarea = Tarea.query.get(id)
    return Tarea_schema.jsonify(tarea)

@app.route('/tarea/<id>', methods=['DELETE'])
def delete_Tarea(id):
    tarea = Tarea.query.get(id)
    db.session.delete(tarea)
    db.session.commit()
    return jsonify({'mensaje': 'Tarea eliminada'})

@app.route('/tarea/<id>', methods=['PUT'])
def update_task(id):
    tarea = Tarea.query.get(id)
    if not tarea:
        return jsonify({'mensaje': 'Tarea no encontrada'}), 404
    tarea.name = request.json.get('name', tarea.name)
    tarea.descripcion = request.json.get('descripcion', tarea.descripcion)
    tarea.fecha = request.json.get('fecha', tarea.fecha)
    db.session.commit()
    return Tarea_schema.jsonify(tarea)


if __name__ == '__main__':
    app.run(debug=True)
