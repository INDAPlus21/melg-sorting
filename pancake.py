import shared


def sort(array):
    history = [(array.copy(), [])]

    for i in range(len(array), 0, -1):
        max_index = array.index(max(array[:i]))
        sub_array = array[:max_index+1]
        array[:max_index+1] = sub_array[::-1]  # Flip to start
        sub_array = array[:i]
        array[:i] = sub_array[::-1]  # Flip entire
        history.append((array.copy(), list(range(0, i))))

    return (array, history)


shared.unit_test(sort)
shared.visualize(sort([4, 2, 5, 1, 15, 1, 3, 4, 8])[1])
