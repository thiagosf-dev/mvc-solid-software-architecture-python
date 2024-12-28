from abc import ABC, abstractmethod
from typing import List
from ..entities.pets import PetsTable


class PetsRepositoryInterface(ABC):
    @abstractmethod
    def delete_pet(self, name: str) -> None: pass

    @abstractmethod
    def list_pets(self) -> List[PetsTable]: pass
