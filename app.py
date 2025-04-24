from flask import Flask
from flask_restx import Api
from config import config
from database.db import db

from routes.ingrediente_routes import api as ingrediente_ns
from routes.receita_routes import api as receita_ns

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)

    api = Api(app, version='1.0', title='API de Receitas', description='CRUD de ingredientes e receitas com Swagger')

    api.add_namespace(ingrediente_ns, path="/ingredientes")
    api.add_namespace(receita_ns, path="/receitas")

    with app.app_context():
        db.create_all()
    
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)