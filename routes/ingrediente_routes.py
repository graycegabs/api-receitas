from flask_restx import Namespace, Resource, fields
from flask import request
from modelos.models import Ingrediente
from database.db import db

api = Namespace('Ingredientes', description='Operações com ingredientes')

ingrediente_model = api.model('Ingrediente', {
    'id': fields.Integer(readOnly=True),
    'nome': fields.String(required=True),
    'unidade': fields.String(required=True)
})

@api.route('/')
class IngredienteLista(Resource):
    @api.marshal_list_with(ingrediente_model)
    def get(self):
        return Ingrediente.query.all()
    
    @api.expect(ingrediente_model)
    @api.marshal_with(ingrediente_model, code=201)
    def post(self):
        data = request.json
        ing = Ingrediente(nome=data['nome'], unidade=data['unidade'])
        db.session.add(ing)
        db.session.commit()
        return ing
    
@api.route('/<int:id>')
class IngredienteResource(Resource):
    @api.expect(ingrediente_model)
    def put(self, id):
        data = request.json
        ing = Ingrediente.query.get_or_404(id)
        ing.nome = data.get('nome', ing.nome)
        ing.unidade = data.get('unidade', ing.unidade)
        db.session.commit()
        return{'mensagem': 'Ingrediente atualizado com sucesso'}
    
    def delete(self, id):
        ing = Ingrediente.query.get_or_404(id)
        db.session.delete(ing)
        db.session.commit()
        return {'mensagem': 'Ingrediente deletado com sucesso'}
    