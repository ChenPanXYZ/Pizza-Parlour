from PizzaParlour import app

def test_pizza():
    response = app.test_client().get('/pizza')

    assert response.status_code == 200
    assert response.data == b'Welcome to Pizza Planet!'

def test_answer():
    data = [1, 2, 3]

    assert sum(data) == 5