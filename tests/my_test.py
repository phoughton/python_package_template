import pytest
from myproj import myclass


@pytest.mark.parametrize("a, b, answer", [
        ( 1, 1, 2 ),
        ( 2, 2, 4 ),
        ( 10, 10, 20 )
    ])
def test_myclass(a, b, answer):
    my_obj = myclass.MyClass()
    assert my_obj.add(a,b) == answer
