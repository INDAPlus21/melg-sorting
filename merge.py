import shared


def sort(array):
    return sort_internal(array)


def sort_internal(array):
    history = [array.copy()]

    if len(array) == 1:
        return (array, history)

    middle = len(array)//2
    left = array[:middle]
    right = array[middle:]

    left = sort_internal(left)[0]
    right = sort_internal(right)[0]

    return (merge(left, right), history)


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
