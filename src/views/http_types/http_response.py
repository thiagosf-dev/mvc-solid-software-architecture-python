class HttpResponse:
    def __init__(self, status_code: int = 200, body: dict = None) -> None:
        self.status_code = status_code
        self.body = body
