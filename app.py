from fastapi import FastAPI
from src.instance import Server

app = FastAPI(
    title='API PIX GERENCIA NET',
    description='API para gerar pagamentos dinamicos.',
)
Server.app = app
import src.controllers
