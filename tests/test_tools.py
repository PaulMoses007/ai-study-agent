from src.tools import calculator, keyword_search


def test_calculator():
    assert calculator("2 + 2") == "4"


def test_keyword_search():
    text = "Python is powerful"
    result = keyword_search(text, "Python")
    assert len(result) == 1
