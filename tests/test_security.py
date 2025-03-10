from http import HTTPStatus

from jwt import decode

from fast_api_do_zero.security import create_access_token, settings


def test_jwt():
    data = {'sub': 'test@tes.com'}
    token = create_access_token(data)

    decoded = decode(
        token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
    )

    assert decoded['sub'] == data['sub']
    assert decoded['exp']


def test_jwt_invalid_token(client):
    response = client.delete(
        'users/1',
        headers={'Authorization': 'Bearer token-invalido'},
    )

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {'detail': 'Could not validate credentials'}
