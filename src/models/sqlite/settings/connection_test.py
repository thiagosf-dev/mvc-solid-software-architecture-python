import pytest
from sqlalchemy import Engine
from .connection import db_connection_handler


@pytest.mark.skip(reason="Interation with database")
def test_connect_to_db():
    enginer = db_connection_handler.get_engine()
    assert enginer is None

    db_connection_handler.connect_to_db()
    enginer = db_connection_handler.get_engine()
    assert enginer is not None
    assert isinstance(enginer, Engine)
