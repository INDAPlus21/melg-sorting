import shared
import random


def sort(array):
    history = [(array.copy(), [])]

    while not sorted(array) == array:
        random.shuffle(array)
        history.append((array.copy(), list(range(0, len(array)))))

    return (array, history)


shared.visualize(sort([1, 3, 2, 10])[1])
