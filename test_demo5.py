#calling the argument in every testcase we need with Class
import pytest

@pytest.mark.usefixtures("tupset")
class Testcallfixture:
    def test_first_program(self):
        print("Test first program")
        msg = "Hello World"
        assert msg == "Hello World", "Test failed"

    def test_secondprogram(self):
        print("Test second program")
        a = 4
        b = 6
        assert a != b, "Test failed"