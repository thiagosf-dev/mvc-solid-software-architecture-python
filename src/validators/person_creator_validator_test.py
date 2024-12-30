from .person_creator_validator import person_creator_validator


class MockRequest:
    def __init__(self, body) -> None:
        self.body = body


def test_person_creator_valiator():
    request = MockRequest(
        body={
            "first_name": "first",
            "last_name": "last",
            "age": 99,
            "pet_id": 99
        }
    )
    person_creator_validator(request)
