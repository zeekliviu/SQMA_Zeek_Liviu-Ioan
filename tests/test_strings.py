def shout(s: str) -> str:
    return s.upper() + "!"

def test_shout_basic():
    assert shout("hello") == "HELLO!"

def test_shout_empty():
    assert shout("") == "!"
