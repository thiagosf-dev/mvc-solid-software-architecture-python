from abc import ABC, abstractmethod
from ..http_types.http_request import HttpRequest
from ..http_types.http_response import HttpResponse


class ViewInterface(ABC):

    @abstractmethod
    def handle(self, request: HttpRequest) -> HttpResponse: pass
