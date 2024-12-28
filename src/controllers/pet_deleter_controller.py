from src.controllers.interfaces.pet_deleter_controller import PetDeleterControllerInterface
from ..models.sqlite.interfaces.pets_repository import PetsRepositoryInterface


class PetDeleterController(PetDeleterControllerInterface):
    def __init__(self, pet_repository: PetsRepositoryInterface) -> None:
        self.__pet_repository = pet_repository

    def delete(self, name: str) -> None:
        self.__pet_repository.delete_pet(name)
