import shared

# Global history variable as it makes things easier
history = []


def sort(array):
    history.clear(),
    sorted = sort_internal(array, array, 0)
    history.append((sorted, list(range(0, len(array)))))
    return (sorted, history)


def sort_internal(array, entire_array, index):
    if len(array) == 1:
        return array

    middle = len(array)//2
    left = array[:middle]
    right = array[middle:]

    left = sort_internal(left, entire_array, index)
    right = sort_internal(right, entire_array, index + middle)

    # Save to history
    entire_array[index:index+len(left)] = left
    entire_array[index+len(left):index+len(left)+len(right)] = right
    history.append((entire_array.copy(), list(
        range(index, index+len(left)+len(right)))))

    return merge(left, right)


def merge(a, b):
    c = []

    while len(a) > 0 and len(b) > 0:
        if a[0] > b[0]:
            c.append(b[0])
            del b[0]
        else:
            c.append(a[0])
            del a[0]

    while len(a) > 0:
        c.append(a[0])
        del a[0]
    while len(b) > 0:
        c.append(b[0])
        del b[0]

    return c


shared.unit_test(sort)
shared.visualize(sort([4, 2, 5, 1, 15, 1, 3, 4, 8])[1])
