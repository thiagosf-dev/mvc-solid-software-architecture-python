from ...models.sqlite.settings.connection import db_connection_handler
from ...models.sqlite.repositories.people_repository import PeopleRepository
from ...controllers.person_finder_controller import PersonFinderController
from ...views.person_finder_view import PersonFinderView


def person_finder_composer():
    model = PeopleRepository(db_connection_handler)
    controller = PersonFinderController(model)
    view = PersonFinderView(controller)
    return view
