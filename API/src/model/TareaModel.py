from database.Database import db
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class Tareas(db.Model):
    __tablename__ = 'Tareas'

    Id_Tarea = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String)
    Descripcion = db.Column(db.String)
    Fecha_max = db.Column(db.Date)

    def __init__(self, Id_Tarea, Nombre, Descripcion, Fecha_max):
        self.Id_Tarea = Id_Tarea
        self.Nombre = Nombre
        self.Descripcion = Descripcion
        self.Fecha_max = Fecha_max

class TareasSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Tareas
        load_instance = True

tarea_schema = TareasSchema()
tareas_schema = TareasSchema(many=True)
