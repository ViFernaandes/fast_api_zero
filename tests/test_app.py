from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_api_do_zero.app import app


def test_root_deve_retornar_ok_e_primeira_vez_subindo_no_fastAPi():
    client = TestClient(app)  # Arrange (Organização)

    response = client.get('/')  # Fase que executa um bloco de código, Act.

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Primeira vez subindo no fastApi'}
