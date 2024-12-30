from src.errors.error_types.http_bad_request import HttpBadRequestError
from src.errors.error_types.http_not_found import HttpNotFoundError
from src.errors.error_types.http_unprocessable_entity import HttpUnprocessableEntityError
from src.views.http_types.http_response import HttpResponse


def handle_errors(error: Exception) -> HttpResponse:
    if isinstance(error, (HttpBadRequestError, HttpUnprocessableEntityError, HttpNotFoundError)):
        return HttpResponse(
            status_code=error.status_code,
            body={"errors": [{
                "title": error.name,
                "detail": error.message
            }]}
        )
    return HttpResponse(
        status_code=500,
        body={
            "errors": [{
                "title": "InternalServerError",
                "detail": str(error)
            }]
        }
    )
