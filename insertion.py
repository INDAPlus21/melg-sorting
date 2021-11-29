import shared


def sort(array):
    history = [(array.copy(), [])]

    for i in range(1, len(array)):
        x = array[i]
        j = i - 1

        while j >= 0 and array[j] > x:
            array[j + 1] = array[j]
            history.append((array.copy(), [j, j + 1]))  # Save state
            j -= 1

        array[j + 1] = x
        history.append((array.copy(), [j + 1]))  # Save state

    return (array, history)


shared.unit_test(sort)
shared.visualize(sort([4, 2, 5, 1, 15, 1, 3, 4, 8])[1])
