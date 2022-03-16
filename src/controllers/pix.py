import requests
import uuid
from src.instance import Server
from pydantic import  BaseModel
from typing import Dict
from src.models.pix import PixModel
import json
app = Server.app
from src.utils.constants import *

class Calendario(BaseModel):
    expiracao:int = 3600

class Devedor(BaseModel):
    cpf:str = "12345678909"
    nome:str =  "Francisco da Silva"


class Valor(BaseModel):
    original:str = "1.10"


class Order(BaseModel):
    txtid :str = "ASLKDFHAJKSDBNFKJASBD12JH43232"
    calendario:Calendario
    devedor:Devedor
    valor:Valor 
    chave:str ="71cdf9ba-c695-4e3c-b010-abb521a3f1be"
    solicitacaoPagador:str = "Prestaçao de serviços"


class WebHook(BaseModel):
    webhookUrl :str

@app.post('/orders')
async def create_order(order : Order ):
    payload = order.dict()
    txtid = payload.pop('txtid')
    pixmodel = PixModel()
    response = pixmodel.create_charge(txtid,payload)
    return response

@app.put('/webhook')
async def put_webhook(webhook : WebHook,chave:str ='71cdf9ba-c695-4e3c-b010-abb521a3f1be'):
    pix = PixModel()
    token = pix.get_token().get('access_token')
    headers = {
        'Authorization':f'Bearer {token}',
        'Content-Type':'application/json',
        'Accept':'*/*',
        'Accept-Encoding':'gzip,deflat,br',
        'x-skip-mtls-checking':'True'
    }
    response = requests.put(URL_HOM+'/v2/webhook/'+chave,headers=headers,data=json.dumps(webhook.dict()),cert=CERTIFICADO)
   
    return response.content
    
