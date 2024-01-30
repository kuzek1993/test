import pytest
from fixture.app_contact import Appcontact
from fixture.application import Application



@pytest.fixture(scope="session")
def app(request):
    fixture = Appcontact()
    request.addfinalizer(fixture.destroy)
    return fixture

@pytest.fixture(scope="session")
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture