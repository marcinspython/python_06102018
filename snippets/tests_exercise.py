from snippets.dodawanie import dodawanie

def test_dodawanie1():
    assert dodawanie(2, 3) == 5


def test_dodawanie2():
    assert dodawanie(2, 2) == 4
