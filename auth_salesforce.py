# auth_salesforce.py

import time
import jwt
import requests
from dotenv import load_dotenv
import os

load_dotenv()

# ========== CONFIGURAÇÕES ==========
IS_SANDBOX = os.getenv('IS_SANDBOX', 'False') == 'True'
KEY_FILE = os.getenv('KEY_FILE')
ISSUER = os.getenv('ISSUER')
SUBJECT = os.getenv('SUBJECT')

def authenticate_salesforce():
    DOMAIN = 'test' if IS_SANDBOX else 'login'

    print('🔑 Lendo chave privada...')
    with open(KEY_FILE) as fd:
        private_key = fd.read()

    print('🔒 Gerando JWT...')
    claim = {
        'iss': ISSUER,
        'exp': int(time.time()) + 300,
        'aud': f'https://{DOMAIN}.salesforce.com',
        'sub': SUBJECT,
    }
    assertion = jwt.encode(claim, private_key, algorithm='RS256')

    print('🌐 Solicitando token de acesso...')
    r = requests.post(f'https://{DOMAIN}.salesforce.com/services/oauth2/token', data={
        'grant_type': 'urn:ietf:params:oauth:grant-type:jwt-bearer',
        'assertion': assertion,
    })

    if r.status_code != 200:
        print('❌ Falha na autenticação:', r.status_code, r.text)
        raise Exception('Falha na autenticação')

    response_data = r.json()
    access_token = response_data['access_token']
    instance_url = response_data['instance_url']

    print('✅ Autenticado com sucesso!')
    return access_token, instance_url

# Para teste direto:
if __name__ == "__main__":
    token, url = authenticate_salesforce()
    print('Access Token:', token)
    print('Instance URL:', url)
