
# django-daraja

STK PUSH API

## Installation

set up venv

pip install -r requirements.txt

python manage.py migrate

## Start the server

python manage.py runserver

## URLs
127.0.0.1:8000/tests/stk-push/success - send prompt

127.0.0.1:8000/callback-data - retrieve callback data from models in py server

# Ngrok
ngrok http 8000

replace the generate url T stk_push_callback_url = 'x/stk_push/callback/'


