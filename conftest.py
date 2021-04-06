import pytest
from fixture.application import Application


# inicjalizator fikstury
@pytest.fixture(scope="session")
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture
