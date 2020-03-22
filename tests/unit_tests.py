from PizzaParlour import app
def test_pizza():
    response = app.test_client().get('/pizza')

    assert response.status_code == 200
    assert response.data == b'Welcome to Pizza Planet!'

def test_new_order():
    data = {}
    response = app.test_client().post('/make-a-new-order', json = data)
    assert response == 4