import pytest

@pytest.fixture(scope="class")
def tupset():
    print("I will be executing first")
    yield
    print("I will be executing at the last")

@pytest.fixture()
def dataload():
    print("User profile is being created")
    return ["Bandana","Limbu","bandanatigela04@gmail.com"]

@pytest.fixture(params=["chrome","Firefox","IE"])
def crossBrowser(request):
    return request.param


