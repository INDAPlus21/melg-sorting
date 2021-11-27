import visulization


def sort(array):
    i = 1
    history = [array]

    while i < len(array):
        x = array[i]
        j = i - 1

        while j >= 0 and array[j] > x:
            array[j + 1] = array[j]
            history.append(array.copy())  # Save state
            j -= 1

        array[j + 1] = x
        history.append(array.copy())  # Save state
        i += 1

    return (array, history)


# Unit test (gives error if fails)
assert sort([2, 3, 2])[0] == [2, 2, 3]
assert sort([5, 10])[0] == [5, 10]
assert sort([25, 15, 13, 35, 12, 29, 81, 54])[
    0] == [12, 13, 15, 25, 29, 35, 54, 81]
assert sort([222, 2, 2222, 22])[0] == [2, 22, 222, 2222]
assert sort([500, 1, 300, 2])[0] == [1, 2, 300, 500]
assert sort([7, 14, 9, 12, 8])[0] == [7, 8, 9, 12, 14]
assert sort([5, 4, 3, 2, 1])[0] == [1, 2, 3, 4, 5]

# Visualize example
visulization.visualize(sort([4, 2, 5, 1, 15, 1, 3, 4, 8])[1])
