# TESTES DE INTEGRAÇÃO

import pytest
from .pets_repository import PetsRepository
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
