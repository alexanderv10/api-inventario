import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.json == {"message": "Bienvenido a la API de Inventario. Visita /producto para más información."}

def test_get_producto(client):
    response = client.get('/producto/1')
    assert response.status_code == 200
    assert response.json == {"nombre": "Producto A", "cantidad": 50}

def test_get_producto_not_found(client):
    response = client.get('/producto/999')
    assert response.status_code == 404
    assert response.json == {"error": "Producto no encontrado."}

def test_post_producto(client):
    response = client.post('/producto', json={"id_producto": 3, "cantidad": 10})
    assert response.status_code == 200
    assert response.json == {"message": "Producto agregado exitosamente."}

def test_put_producto(client):
    response = client.put('/producto/1', json={"nueva_cantidad": 100})
    assert response.status_code == 200
    assert response.json == {"message": "Stock actualizado exitosamente."}
