from urllib import response
from src.instance import Server
from src.models.pix import PixModel
app = Server.app

@app.post('/token')
def token():
    pix_model = PixModel()
    response = pix_model.get_token()
    return response