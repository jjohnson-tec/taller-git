from taller.main import greet


def test_greet_default():
    assert greet() == "Hola, mundo!"


def test_greet_name():
    assert greet("Ana") == "Hola, Ana!"
