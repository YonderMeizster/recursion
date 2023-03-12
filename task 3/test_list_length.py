from list_length import estimate_length


def test_1():
    for i in range(500):
        collec = [j for j in range(i)]
        collec_id = id(collec)
        collec_values = collec[:]

        assert estimate_length(collec) == len(collec)
        assert collec_id == id(collec)
        assert collec_values == collec
