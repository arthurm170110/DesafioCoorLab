#!/bin/bash

# Entrando na pasta do backend
cd api_cb_viagens

# Criando um ambiente virtual para o backend e suas dependencias
python3 -m venv venv

# Ativando o ambiente virtual
source venv/bin/activate

# Instalando as dependencias do backend
pip install -r requirements.txt

# Executando as migrações do banco de dados
python manage.py makemigrations
python manage.py migrate

# Iniciando o servidor do backend
python manage.py runserver 3000 &

# Entrando na pasta do frontend
cd ../front_cb_viagens

echo "Instalando algumas dependencias, aguarde..."

# Instalando o vue/cli
npm install @vue/cli

# Iniciando o servidor do frontend
npm run serve &

# Esperando 5 segundos
sleep 5

# Abrindo o navegador
xdg-open http://localhost:8080