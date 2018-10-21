def przytnij(data, start, stop):
    result = []

    for element in data:
        if start(element) and not stop(element):
            result.append(element)


    return result


def test_przytnij():
    assert przytnij(
        data=[1, 2, 3, 4, 5, 6, 7],
        start=lambda x: x > 3,
        stop=lambda x: x == 6,
    ) == [4, 5, 6]




# przytnij(
# data = [1,2,3,4,5,6,7]
# start = lambda x: x > 3,
# stop = lambda x: x == 6,
# )
