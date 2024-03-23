#!/bin/bash

# Entrando na pasta do backend
cd app/api_cb_viagens

# Criando um ambiente virtual para o backend e suas dependencias
python -m venv venv

# Ativando o ambiente virtual
venv/Scripts/activate

# Instalando as dependencias do backend
pip install -r requirements.txt

# Executando as migrações do banco de dados
python manage.py makemigrations
python manage.py migrate

# Iniciando o servidor do backend
python manage.py runserver 3000

# Entrando na pasta do frontend
cd ../front_cb_viagens

# Iniciando o servidor do frontend
npm run serve
