from model_bakery import baker
from base.models import Reserva, Agendamento, Contato, Categoria
from datetime import date
import pytest


def test_config():
     assert 1 == 1

@pytest.mark.django_db
def test_str_de_reserva_deve_retornar_a_string_formatada():
     guarda_data = date(2024, 1, 14)
     reserva = baker.make(Reserva, data = guarda_data, nome_do_pet = 'claudio')
     assert str(reserva)== 'Reserva criada claudio, 2024-01-14'

@pytest.mark.django_db
def test_str_de_agendamento_deve_retornar_a_string_formatada():
     guarda_data = date(2024, 1, 20)
     agendamento = baker.make(Agendamento, data = guarda_data, nome = 'samuca', email = 'samucadelaxx@gamil.com', nome_do_pet = 'pedro')
     assert str(agendamento)=='Agendamento criado samuca, samucadelaxx@gamil.com, pedro, 2024-01-20'

@pytest.mark.django_db
def test_str_de_contato_deve_retornar_a_string_formatada():
     contato = baker.make(Contato, nome = 'samuca', email = 'samucadelaxx@gmail.com')
     assert str(contato)=='Contato criado samuca, samucadelaxx@gmail.com'

@pytest.mark.django_db
def test_str_de_categoria_deve_retornar_a_string_formatada():
     categoria = baker.make(Categoria, tamanho = 'pequeno', tipo = 'gato')
     assert str(categoria)=='Tamanho pequeno'

