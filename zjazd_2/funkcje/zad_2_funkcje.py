# from .zad_2 import wiecej_niz

# if __name__ == "__main"

def wiecej_niz(napis, prog):
    return {znak for znak in napis if napis.lower().count(znak) > prog}



def test_wiecej_niz_dla_pustego_napis():
    assert wiecej_niz("", 0) == set()


def test_wiecej_niz_dla_niepustego_napisu():
    assert wiecej_niz("aaaaaabbbbcccddd", 2) == {'a', 'b'}

