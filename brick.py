import shared


# https://iq.opengenus.org/odd-even-sort/
def sort(array):
    history = [array.copy()]

    sorted = False
    while not sorted:
        sorted = True

        (array, history, sorted) = loop(0, array, history, sorted)  # Odd
        (array, history, sorted) = loop(1, array, history, sorted)  # Even

    return (array, history)


def loop(start, array, history, sorted):
    for i in range(start, len(array) - 1, 2):
        if array[i + 1] < array[i]:
            array[i + 1], array[i] = array[i], array[i + 1]
            history.append(array.copy())
            sorted = False

    return (array, history, sorted)


shared.unit_test(sort)
shared.visualize(sort([4, 2, 5, 1, 15, 1, 3, 4, 8])[1])
