import pytest

@pytest.fixture(scope="session")
def browser():
    print("Браузер!")
    pass

    yield

    print("Закрываем браузер!")


@pytest.fixture
def login_page(browser):
    print("Логин пейдж!")
    pass



@pytest.fixture
def user():
    print("Юзер!")
    return "username", "password"