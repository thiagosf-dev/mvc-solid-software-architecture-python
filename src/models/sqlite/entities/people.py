from sqlalchemy import BIGINT, Column, ForeignKey, String
from ....models.sqlite.settings.base import Base


class PeopleTable(Base):
    __tablename__ = 'people'

    id = Column(BIGINT, primary_key=True)

    first_name = Column(String, nullable=False)

    last_name = Column(String, nullable=False)

    age = Column(BIGINT, nullable=False)

    pet_id = Column(BIGINT, ForeignKey('pets.id'))

    def __repr__(self):
        return (
            f"People [id={self.id}, first_name={self.first_name}, "
            f"last_name={self.last_name}, age={
                self.age}, pets_id={self.pets_id}]"
        )
