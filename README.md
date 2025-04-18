🐍 FastAPI do Zero:

Este repositório contém todo o conteúdo desenvolvido no curso FastAPI do Zero, ministrado por Eduardo Mendes (Dunossauro). O objetivo do curso é oferecer uma experiência prática e completa no uso do FastAPI, cobrindo desde a criação de APIs RESTful até o deploy da aplicação.

📚 Sobre o Curso:

O curso foi criado para quem deseja aprender FastAPI do início ao fim, explorando as boas práticas modernas de desenvolvimento com Python. O projeto principal será um gerenciador de tarefas (to-do list) com autenticação de usuários e todas as operações CRUD.

Ferramentas utilizadas:
- FastAPI 0.115+
- Pydantic 2.0+
- SQLAlchemy ORM 2.0+
- Alembic para migrações
- Python 3.11+ (desenvolvido com a versão 3.13.2)
- Pytest para testes
- Docker para conteinerização
- Fly.io para deploy

🧠 O que você vai aprender?

✅ Configuração de Ambiente
Uso do Poetry para gerenciar o projeto
Boas práticas com ferramentas de análise estática e formatação de código

✅ Fundamentos do FastAPI
Criação de rotas e endpoints
Operações CRUD
Injeção de dependência
Criação de schemas

✅ Modelagem de Dados
Modelos com Pydantic e SQLAlchemy
Migrações com Alembic

✅ Autenticação e Autorização
Sistema completo de login e proteção de rotas
Tokens de acesso e autenticação robusta

✅ Testes Automatizados
Testes com pytest
Cobertura de testes com coverage
Integração contínua com GitHub Actions

✅ Deploy
Conteinerização com Docker
Deploy com Fly.io

🧰 Ambiente de Desenvolvimento

Este projeto utiliza:
Python 3.13.2

Recomenda-se o uso do pyenv:

pyenv local 3.13.2

Poetry 2.1.2:

pipx install poetry==2.1.2

pipx inject poetry poetry-plugin-shell

poetry install

poetry shell

🛠️ Comandos com Taskipy

Todos os comandos são gerenciados com task:

task --list

Você pode visualizar o material gerado em:

📎 fastapidozero.dunossauro.com

 Acompanhe no canal do YouTube do Dunossauro.
