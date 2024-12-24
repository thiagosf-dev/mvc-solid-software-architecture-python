import pytest
from .pets_repository import PetsRepository
from ....models.sqlite.settings.connection import db_connection_handler

db_connection_handler.connect_to_db()


@pytest.mark.skip(reason="Interation with the database")  # pragma: no cover
def test_list_pets():
    pets_repository = PetsRepository(db_connection_handler)
    pets = pets_repository.list_pets()
    print()
    print(pets)
