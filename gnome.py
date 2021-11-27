import shared


# https://www.geeksforgeeks.org/gnome-sort-a-stupid-one/
def sort(array):
    history = [array.copy()]

    i = 0
    while i < len(array):
        if i == 0:
            i += 1
        if array[i] >= array[i - 1]:
            i += 1
        else:
            # XOR-swapping to avoid temp variable
            array[i] ^= array[i - 1]
            array[i - 1] ^= array[i]
            array[i] ^= array[i - 1]
            history.append(array.copy())
            i -= 1

    return (array, history)


shared.unit_test(sort)
shared.visualize(sort([4, 2, 5, 1, 15, 1, 3, 4, 8])[1])
