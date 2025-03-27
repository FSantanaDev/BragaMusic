#!/bin/bash

# Instala as dependências do projeto Django a partir do arquivo requirements.txt
python3 -m pip install -r requirements.txt

# Executa as migrações e coleta os arquivos estáticos
python3 manage.py migrate
python3 manage.py collectstatic --noinput