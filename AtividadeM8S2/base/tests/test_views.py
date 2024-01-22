from pytest_django.asserts import assertTemplateUsed
import pytest

@pytest.mark.django_db
def test_reserva_view_deve_retorna_template(client):
     response = client.get('/reserva')
     assert response.status_code == 200
     assertTemplateUsed(response, 'reserva.html')


def test_agendamento_view_deve_retorna_template(client):
     response = client.get('/agendamento')
     assert response.status_code == 200
     assertTemplateUsed(response, 'agendamento.html')
  

def test_contato_view_deve_retorna_template(client):
     response = client.get('/contato')
     assert response.status_code == 200
     assertTemplateUsed(response, 'contato.html')


def test_categoria_view_deve_retorna_template(client):
     response = client.get('/categoria')
     assert response.status_code == 200
     assertTemplateUsed(response, 'categoria.html')