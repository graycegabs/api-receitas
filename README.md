# 🍽️ API de Receitas

Este projeto é uma API simples de gerenciamento de receitas culinárias, desenvolvida em Python com Flask. A API permite criar, listar, atualizar e deletar ingredientes e receitas, além de fornecer documentação automática com Swagger.

---

## 🛠️ Tecnologias Utilizadas

- Python 3.10+
- Flask
- Flask-SQLAlchemy
- Flask-RESTX (para documentação Swagger)
- SQLite (banco de dados)

---

## Endpoints

- `POST /ingredientes`: Criar um ingrediente
- `GET /ingredientes`: Listar todos os ingredientes
- `PUT /ingredientes/{id}`: Atualizar um ingrediente
- `DELETE /ingredientes/{id}`: Deletar um ingrediente
- `POST /receitas`: Criar uma receita
- `GET /receitas`: Listar todas as receitas
- `DELETE /receitas/{id}`: Deletar uma receita

## Como rodar a API

### 1. Clone o repositório:
   ```bash
   git clone https://github.com/graycegabs/api-receitas.git
   ```

---
### 2. Crie um ambiente virtual (opcional, mas recomendado)
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```
---

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

---

### 4. Execute a aplicação

```bash
python app.py
```

A API estará disponível em: [http://localhost:5000](http://localhost:5000)

---

### 📚 Acessando a documentação Swagger

A documentação da API é gerada automaticamente pelo Flask-RESTX e estará disponível logo na rota raiz:

[http://localhost:5000](http://localhost:5000)

---

## 🧪 Exemplos de requisições no Postman
### ✅ Criar ingrediente (POST /ingredientes)
```json
{
  "nome": "Açúcar",
  "unidade": "gramas"
}
```

### 📃 Listar ingredientes (GET /ingredientes)
---
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
---
### ❌ Deletar receita (DELETE /receitas/{id})
