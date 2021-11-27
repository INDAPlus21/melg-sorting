import shared


def sort(array):
    history = [array.copy()]

    for i in range(0, len(array) - 1):
        min_index = i
        j = i + 1

        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j

        if min_index != i:
            # XOR-swapping to avoid temp variable
            array[i] ^= array[min_index]
            array[min_index] ^= array[i]
            array[i] ^= array[min_index]
            history.append(array.copy())

    return (array, history)


shared.unit_test(sort)
shared.visualize(sort([4, 2, 5, 1, 15, 1, 3, 4, 8])[1])
