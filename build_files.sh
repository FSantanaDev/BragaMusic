#!/bin/bash

# Instala as dependências do projeto Django a partir do arquivo requirements.txt
python3 -m pip install -r requirements.txt

# Verifica se a variável de ambiente PROD está vazia ou não definida
if [ -z "$PROD" ]; then

    # Se PROD não estiver definida (ambiente local), executa as migrações e coleta os arquivos estáticos
    python3 manage.py migrate
    python3 manage.py collectstatic --noinput

fi # Fim do bloco if