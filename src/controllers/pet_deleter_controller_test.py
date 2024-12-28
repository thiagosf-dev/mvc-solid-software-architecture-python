from .pet_deleter_controller import PetDeleterController


def test_delete_pet(mocker):
    mock_repository = mocker.Mock()  # faz um mock do repositório de pets
    controller = PetDeleterController(mock_repository)
    controller.delete("pet")

    mock_repository.delete_pet.assert_called_once_with("pet")
