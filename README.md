# 📱 Agenda Telefônica com MongoDB

![Python](https://img.shields.io/badge/Python-3.6+-blue?logo=python)
![MongoDB](https://img.shields.io/badge/MongoDB-5.0+-green?logo=mongodb)
![License](https://img.shields.io/badge/License-MIT-yellow)

Um aplicativo CLI completo para gerenciar seus contatos telefônicos com armazenamento em MongoDB.

## 🚀 Recursos Principais

- **CRUD Completo** (Create, Read, Update, Delete)
- Pesquisa inteligente por nome/telefone
- Categorização de contatos
- Interface intuitiva via linha de comando
- Persistência em banco de dados NoSQL

## 🛠️ Tecnologias Utilizadas

- Python 3+
- PyMongo (Driver oficial do MongoDB para Python)
- MongoDB (Local ou Atlas)

## 📦 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/agenda-telefonica.git
cd agenda-telefonica

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

pip install -r requirements.txt

1. ➕ Adicionar Contato
2. 📋 Listar Contatos
3. ✏️ Atualizar Contato
4. ❌ Remover Contato
5. 🔍 Pesquisar Contato
6. 🚪 Sair

agenda-telefonica/
├── agenda_telefonica.py  # Código principal
├── README.md            # Este arquivo
└── requirements.txt     # Dependências