import base64
from email import header
import requests 
from src.utils.constants import CLIENT_ID
from src.utils.constants import CLIENT_SECRET
from src.utils.constants import CERTIFICADO
from src.utils.constants import URL_HOM
import json,pyqrcode
from PIL import Image
from io import BytesIO
from fastapi.responses import FileResponse
class PixModel():

    def get_token(self):
        auth = base64.b64encode(
            (f'{CLIENT_ID}:{CLIENT_SECRET}').encode()
        ).decode()
        headers = {
            'Authorization':f"Basic {auth}",
            'Content-Type':'application/json'
        }
        payload = {'grant_type':'client_credentials'}
        response = requests.post(f'{URL_HOM}/oauth/token', headers=headers,data=json.dumps(payload), cert= CERTIFICADO)
        return json.loads(response.content)
    def create_qrcode(self, location_id):
        response = requests.get(f'{URL_HOM}/v2/loc/{location_id}/qrcode',headers=self._get_headers(),cert=CERTIFICADO)
        return json.loads(response.content)
    
    def create_order(self,txid,payload):
        response = requests.put(f'{URL_HOM}/v2/cob/{txid}',data=json.dumps(payload), headers=self._get_headers(),cert=CERTIFICADO)
        print(response.content)
        if response.status_code == 201:
            return json.loads(response.content)
        return {}
    def _get_headers(self):
        return {
            'Authorization':f"Bearer {self.get_token()['access_token']}",
            'Content-Type':'application/json'
        }
    
    def qrcode_generator(self,location_id):
        qrcode = self.create_qrcode(location_id)
        data_qrcode = qrcode['qrcode']
        url = pyqrcode.QRCode(data_qrcode,error='H')
        url.png('qrcode.jpg',scale=10)
        im = Image.open('qrcode.jpg')
        im = im.convert('RGBA')
        img_io = BytesIO()
        im.save(img_io,'PNG',quality=100)
        img_io.seek(0)
        return FileResponse('qrcode.jpg',media_type='image/jpeg',filename='image-qrcode.jpeg')

    def create_charge(self,txid,payload):
        location_id = self.create_order(txid,payload).get('loc').get('id')
        qr_code = self.qrcode_generator(location_id)

        return qr_code
