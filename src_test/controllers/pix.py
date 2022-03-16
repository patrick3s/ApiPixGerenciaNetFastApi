from src_test.instance import client
import json
def test_create_qrcode_pix():
    import uuid
    payload = {
    "txtid":f"{str(uuid.uuid4()).replace('-','')}",
    "calendario": {
        "expiracao": 3600
        },
    "devedor": {
        "cpf": "12345678909",
        "nome": "Francisco da Silva"
        },
    "valor": {
        "original": "1.10"
        },
    "chave": "71cdf9ba-c695-4e3c-b010-abb521a3f1be",
    "solicitacaoPagador": "Informe o número ou identificador do pedido."
    }

    response = client.post('/orders',json=payload)
    assert response.status_code == 200

def test_create_weekhook():
    payload = {
        "webhookUrl":"https://exemplo-pix/webhook"
    }
    params = {'chave':'71cdf9ba-c695-4e3c-b010-abb521a3f1be'}
    
    response = client.put('/webhook',json=payload,params=params)

    assert response.status_code == 200

