from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get('/')
def read_root():
    return {'message': 'Primeira vez subindo no fastApi'}


@app.get('/resposta', status_code=HTTPStatus.OK, response_class=HTMLResponse)
def retorno_html():
    return """
    <html>
        <head>
            <title> Nosso olá mundo!</title>
        </head>
        <body>
            <h1>Olá Mundo </h1>
        </body>
        </html>"""
