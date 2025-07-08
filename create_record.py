# create_record.py

import requests
from auth_salesforce import authenticate_salesforce

API_VERSION = '60.0'

def execute_composite(composite_body):
    """
    Executa um composite API genérico.
    Recebe o JSON pronto.
    """
    access_token, instance_url = authenticate_salesforce()
    composite_url = f"{instance_url}/services/data/v{API_VERSION}/composite"

    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }

    print(f'🚀 Executando Composite em: {composite_url}')
    print('🔹 Payload:', composite_body)

    response = requests.post(composite_url, headers=headers, json=composite_body)

    print('Status:', response.status_code)
    print('Resposta:', response.json())

    return response.json()
