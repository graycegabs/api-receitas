# 🍽️ API de Receitas

Este projeto é uma API simples de gerenciamento de receitas culinárias, desenvolvida em Python com Flask. A API permite criar, listar, atualizar e deletar ingredientes e receitas, além de fornecer documentação automática com Swagger.

---

## 🛠️ Tecnologias Utilizadas

- Python 3.x
- Flask
- Flask-SQLAlchemy
- Flask-RESTX (para documentação Swagger)
- SQLite (banco de dados leve embutido)

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
   git clone https://github.com/seu-usuario/api-receitas.git
   ```

---

### 2. 🚀 Instale as dependências do projeto

```bash
pip install -r requirements.txt
```

---

### 3. ▶️ Execute o projeto localmente

```bash
python app.py
```
---

A aplicação estará disponível em: [http://localhost:5000](http://localhost:5000)

---

## 📚 Acessando a documentação Swagger

A documentação da API é gerada automaticamente pelo Flask-RESTX e estará disponível logo na rota raiz:

[http://localhost:5000](http://localhost:5000)

---

## 📝 Licença

Este projeto está sob a licença MIT. Sinta-se à vontade para usá-lo e modificá-lo conforme necessário.
