import pytest
@pytest.mark.usefixtures("dataload")
class TestExample:
    def test_editprofile(self,dataload):
        print(dataload)


def test_crossBrowser(crossBrowser):
    print(crossBrowser)