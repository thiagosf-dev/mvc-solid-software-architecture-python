# TESTES DE INTEGRAÇÃO

import pytest
from .pets_repository import PetsRepository
from .people_repository import PeopleRepository
from ....models.sqlite.settings.connection import db_connection_handler

# db_connection_handler.connect_to_db()


@pytest.mark.skip(reason="Interation with the database")  # pragma: no cover
def test_list_pets():
    repo = PetsRepository(db_connection_handler)
    repo.list_pets()


@pytest.mark.skip(reason="Interation with the database")  # pragma: no cover
def test_delete_pet():
    repo = PetsRepository(db_connection_handler)
    repo.delete_pet("belinha")


@pytest.mark.skip(reason="Interation with the database")  # pragma: no cover
def test_insert_person():
    first_name = "Test first name"
    last_name = "Test last name"
    age = 20
    pet_id = 2
    repo = PeopleRepository(db_connection_handler)
    repo.insert_person(first_name, last_name, age, pet_id)


@pytest.mark.skip(reason="Interation with the database")  # pragma: no cover
def test_get_person():
    person_id = 1
    repo = PeopleRepository(db_connection_handler)
    response = repo.get_person(person_id)
    print()
    print(response)
    print(response.first_name)
    print(response.pet_name)
