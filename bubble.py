import shared


def sort(array):
    history = [(array.copy(), [])]

    sorted = False
    while not sorted:
        sorted = True

        for i in range(0, len(array) - 1):
            if array[i + 1] < array[i]:
                array[i + 1], array[i] = array[i], array[i + 1]
                history.append((array.copy(), [i, i + 1]))
                sorted = False

    return (array, history)


shared.unit_test(sort)
shared.visualize(sort([4, 2, 5, 1, 15, 1, 3, 4, 8])[1])
