import pytest
from fixture.application import Application


fixture = None


# inicjalizator fikstury
@pytest.fixture
def app(request):
    global fixture
    if fixture is None:
        browser = request.config.getoption("--browser")
        fixture = Application(browser=browser)
    else:
        if not fixture.is_valid():
            fixture = Application()
    fixture.session.ensure_login(username="admin", password="secret")
    return fixture


# autouse=True sprawia, że dana fikstura wykonuje się automatycznie nawet jeśli nie jest wskazana
@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    # przekazywany bedzie parser wiersza polecen w ktorym jest metoda addoption
    parser.addoption("--browser", action="store", default="firefox")
