from flask import Blueprint, jsonify, request

from src.model.TareaModel import Tareas, tarea_schema, tareas_schema
from database.Database import db

main=Blueprint('tareas_blueprint', __name__)

#Ruta para llamar todas las tareas
@main.route('/tareas', methods=['GET'])
def get_tareas():
    all_tareas = Tareas.query.all()
    result = tareas_schema.dump(all_tareas)

    return jsonify(result)

#Ruta para llamar una tarea por ID
@main.route('/tareas/<id>', methods=['GET'])
def get_tarea(id):
    tarea = Tareas.query.filter_by(Id_Tarea=id).first_or_404()
    result = tarea_schema.dump(tarea)

    return jsonify(result)

#Ruta para crear una nueva tarea
@main.route('/tareas', methods=['POST'])
def create_tarea():
    tarea_data = request.get_json()
    tarea = Tareas(
            Id_Tarea = None,
            Nombre=tarea_data.get('Nombre'),
            Descripcion=tarea_data.get('Descripcion'),
            Fecha_max=tarea_data.get('Fecha_max'),
        )

    db.session.add(tarea)
    db.session.commit()

    result = tarea_schema.dump(tarea)
    return jsonify(result), 201

#Ruta para editar una tarea por ID
@main.route('/tareas/<id>', methods=['PUT'])
def editar_tarea(id):
    tarea = Tareas.query.filter_by(Id_Tarea=id).first_or_404()
    
    tarea.Nombre = request.json['Nombre']
    tarea.Descripcion = request.json['Descripcion']
    tarea.Fecha_max = request.json['Fecha_max']
    db.session.commit()

    result = tarea_schema.dump(tarea)
    
    return jsonify({"msg": "Dato modificado exitosamente", "tarea": result})

#Ruta para eliminar un contacto por ID
@main.route('/tareas/<id>', methods=['DELETE'])
def delete_contacto(id):
    tarea = Tareas.query.filter_by(Id_Tarea=id).first_or_404()
    
    db.session.delete(tarea)
    db.session.commit()
    
    return jsonify({"msg": "contacto eliminado exitosamente"})