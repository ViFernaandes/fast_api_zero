from dataclasses import asdict

from sqlalchemy import select

from fast_api_do_zero.models import User


def test_create_user(session, mock_db_time):
    with mock_db_time(model=User) as time:
        novo_user = User(
            username='test',
            email='test@test.com',
            password='secret',
        )

        session.add(novo_user)
        session.commit()

        user = session.scalar(select(User).where(User.username == 'test'))

    assert asdict(user) == {
        'id': 1,
        'username': 'test',
        'email': 'test@test.com',
        'password': 'secret',
        'created_at': time,
    }
