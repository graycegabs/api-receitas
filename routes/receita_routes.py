from flask_restx import Namespace, Resource, fields
from flask import request
from modelos.models import Receita, ReceitaIngrediente, Ingrediente
from database.db import db

api = Namespace('Receitas', description='Operações relacionadas às receitas')

Ingrediente_input = api.model('IngredienteInput', {
    'ingrediente_id': fields.Integer(required=True),
    'quantidade': fields.Float(required=True),
})

Receita_input = api.model('ReceitaInput', {
    'nome': fields.String(required=True),
    'modo_preparo': fields.String(required=True),
    'ingredientes': fields.List(fields.Nested(Ingrediente_input), required=True)
})

@api.route('/')
class ReceitaList(Resource):
    @api.expect(Receita_input)
    def post(self):
        data = request.get_json()
        receita = Receita(nome=data['nome'], modo_preparo=data['modo_preparo'])
        db.session.add(receita)
        db.session.commit()

        for ing in data['ingredientes']:
            item = ReceitaIngrediente(
                receita_id=receita.id,
                ingrediente_id=ing['ingrediente_id'],
                quantidade=ing['quantidade']
            )
            db.session.add(item)
        db.session.commit()

        return {'id': receita.id, 'mensagem': 'Receita criada com sucesso'}, 201
    
    def get(self):
        receitas = Receita.query.all()
        resultado = []
        for r in receitas:
            ingredientes = []
            for ri in r.ingredientes:
                ingredientes.append({
                    'id': ri.ingrediente.id,
                    'nome': ri.ingrediente.nome,
                    'quantidade': ri.quantidade,
                    'unidade': ri.ingrediente.unidade
                })
            resultado.append({
                'id': r.id,
                'nome': r.nome,
                'mode_preparo': r.modo_preparo,
                'ingredientes': ingredientes
            })
        return resultado
    
@api.route('/<int:id>')
class ReceitaResource(Resource):
    def delete(self, id):
        receita = Receita.query.get_or_404(id)
        db.session.delete(receita)
        db.session.commit()
        return {'mensagem': 'Receita deletada com sucesso'}