def wiecej_niz(napis, prog):
    licz
    return set()



def test_wiecej_niz_dla_pustego_napis():
    assert wiecej_niz("", 0) == set()


def test_wiecej_niz_dla_niepustego_napisu():
    assert wiecej_niz("aaaaaabbbbcccddd", 2) == {'a', 'b'}
