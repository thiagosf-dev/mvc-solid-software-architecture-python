from typing import List
from ..models.sqlite.entities.pets import PetsTable
from ..models.sqlite.interfaces.pets_repository import PetsRepositoryInterface


class PetListerController:
    def __init__(self, pet_repository: PetsRepositoryInterface) -> None:
        self.__pet_repository = pet_repository

    def list(self) -> dict:
        pets = self.__get_pets_in_db()
        response = self.__format_response(pets)
        return response

    def __get_pets_in_db(self) -> List[PetsTable]:
        pets = self.__pet_repository.list_pets()
        return pets

    def __format_response(self, pets: List[PetsTable]) -> dict:
        formated_pets = [{"name": pet.name, "type": pet.type} for pet in pets]
        return {
            "data": {
                "type": "Pets",
                "count": len(pets),
                "attributes": formated_pets
            }
        }
