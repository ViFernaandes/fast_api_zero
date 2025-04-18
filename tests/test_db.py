from dataclasses import asdict

from sqlalchemy import select

from fast_api_do_zero.models import Todo, TodoState, User


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
        'todos': [],
    }


def test_create_todo(session, user, mock_db_time):
    with mock_db_time(model=Todo) as time:
        todo = Todo(
            title='Test Todo',
            description='Test Desc',
            state=TodoState.draft,
            user_id=user.id,
        )

        session.add(todo)
        session.commit()

        todo = session.scalar(select(Todo))

    assert asdict(todo) == {
        'description': 'Test Desc',
        'id': 1,
        'state': 'draft',
        'title': 'Test Todo',
        'user_id': 1,
        'created_at': time,
        'updated_at': time,
    }


def test_user_todo_relationship(session, user):
    todo = Todo(
        title='Test Todo',
        description='Test Desc',
        state=TodoState.draft,
        user_id=user.id,
    )

    session.add(todo)
    session.commit()
    session.refresh(user)

    user = session.scalar(select(User).where(User.id == user.id))

    assert user.todos == [todo]
