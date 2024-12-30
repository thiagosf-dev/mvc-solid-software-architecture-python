from ...models.sqlite.settings.connection import db_connection_handler
from ...models.sqlite.repositories.pets_repository import PetsRepository
from ...controllers.pet_deleter_controller import PetDeleterController
from ...views.pet_deleter_view import PetDeleterView


def pet_deleter_composer():
    model = PetsRepository(db_connection_handler)
    controller = PetDeleterController(model)
    view = PetDeleterView(controller)
    return view
