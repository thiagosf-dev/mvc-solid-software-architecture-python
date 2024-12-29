from src.controllers.interfaces.person_creator_controller import PersonCreatorControllerInterface
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.views.interfaces.view_interface import ViewInterface


class PersonCreatorView(ViewInterface):

    def __init__(self, controller: PersonCreatorControllerInterface) -> None:
        self.__controller = controller

    def handle(self, request: HttpRequest) -> HttpResponse:
        person_info = request.body
        body_response = self.__controller.create(person_info)
        return HttpResponse(body=body_response, status_code=201)