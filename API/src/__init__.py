from flask import Flask
from config import config

#database
from database.Database import db

#routes
from src.route import TareaRoutes

def init_app(configname):

    app = Flask(__name__)

    #Configuracion
    app.config.from_object(config[configname])

    #uso de orm
    db.init_app(app)

    #Blueprints
    app.register_blueprint(TareaRoutes.main, url_prefix='/tareas_blueprint')

    return app
