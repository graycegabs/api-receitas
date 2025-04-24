# 🍽️ API de Receitas com Flask

Este projeto é uma API simples de gerenciamento de receitas culinárias, desenvolvida em Python com Flask. A API permite criar, listar, atualizar e deletar ingredientes e receitas, além de fornecer documentação automática com Swagger.

---

## 🛠️ Tecnologias Utilizadas

- Python 3.x
- Flask
- Flask-SQLAlchemy
- Flask-RESTX (para documentação Swagger)
- SQLite (banco de dados leve embutido)

---

## 🗂️ Estrutura do Projeto

```
📁 api-receitas/
├── app.py                # Arquivo principal que inicia o app
├── requirements.txt      # Dependências do projeto
├── config.py             # Configurações da aplicação
├── models/               # Modelos do banco de dados
│   └── models.py
├── routes/               # Rotas organizadas por entidade
│   ├── ingrediente_routes.py
│   └── receita_routes.py
├── database/
│   └── db.py             # Banco de dados SQLite (criado automaticamente)      
├── instance/
│   └── receitas.db
```

---

## 📦 Configurando o ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

---

## 🚀 Instalando as dependências do projeto

```bash
pip install -r requirements.txt
```

---

## ▶️ Executando o projeto localmente

```bash
python app.py
```

A aplicação estará disponível em: [http://localhost:5000](http://localhost:5000)

---

## 📚 Acessando a documentação Swagger

A documentação da API é gerada automaticamente pelo Flask-RESTX e está disponível logo na rota raiz:

[http://localhost:5000](http://localhost:5000)

---

## 🧪 Testando a API com Postman

### ✅ Criar ingrediente (POST /ingredientes)
```json
{
  "nome": "Açúcar",
  "unidade": "gramas"
}
```

### 📃 Listar ingredientes (GET /ingredientes)
Retorna uma lista com todos os ingredientes cadastrados.

### ✅ Criar receita (POST /receitas)
```json
{
  "nome": "Bolo de Chocolate",
  "modo_preparo": "Misture tudo e asse por 40 minutos.",
  "ingredientes": [
    {
      "ingrediente_id": 1,
      "quantidade": 200
    },
    {
      "ingrediente_id": 2,
      "quantidade": 3
    }
  ]
}
```

### 📃 Listar receitas (GET /receitas)
Retorna todas as receitas com ingredientes detalhados.

### ❌ Deletar receita (DELETE /receitas/{id})
Exclui uma receita específica pelo seu ID.

---

## 📝 Licença

Este projeto está sob a licença MIT. Sinta-se à vontade para usá-lo e modificá-lo conforme necessário.
