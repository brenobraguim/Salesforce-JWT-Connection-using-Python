# run.py

from create_record import execute_composite
from mapper import mapper
from mapping_utils import apply_mapper
from incoming_json import json_plataforma

# 🎯 JSON recebido
incoming_json = json_plataforma

# 🔹 Aplica o mapper
mapped_data = apply_mapper(incoming_json, mapper)

contact_data = mapped_data.get('Contact', {})
account_data = mapped_data.get('Account', {})

print("🔍 Contact:", contact_data)
print("🔍 Account:", account_data)

# ✅ Monta Composite
composite_body = {
    "allOrNone": True,
    "compositeRequest": [
        {
            "method": "POST",
            "url": "/services/data/v60.0/sobjects/Account",
            "referenceId": "NewAccount",
            "body": account_data
        },
        {
            "method": "POST",
            "url": "/services/data/v60.0/sobjects/Contact",
            "referenceId": "NewContact",
            "body": {
                **contact_data,
                "AccountId": "@{NewAccount.id}"
            }
        }
    ]
}

# 🚀 Executa Composite
result = execute_composite(composite_body)

print('✅ Resultado final:', result)
