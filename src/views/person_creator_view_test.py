from src.views.http_types.http_request import HttpRequest
from src.views.person_creator_view import PersonCreatorView


class PersonCreatorControllerMock:
    def create(self, person_info: dict) -> dict:
        return person_info


def test_handler():
    controller = PersonCreatorControllerMock()
    view = PersonCreatorView(controller)
    person_info = view.handle(HttpRequest({
        "first_name": "Test first name",
        "last_name": "Test last name",
        "age": 99,
        "pet_id": 99
    }))
    body_response = controller.create(person_info.body)
    assert person_info.body == body_response
    assert person_info.status_code == 201
