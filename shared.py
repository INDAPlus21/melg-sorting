import pygame


# Unit test (gives error if fails)
def unit_test(sort_function):
    assert sort_function([2, 3, 2])[0] == [2, 2, 3]
    assert sort_function([5, 10])[0] == [5, 10]
    assert sort_function([25, 15, 13, 35, 12, 29, 81, 54])[
        0] == [12, 13, 15, 25, 29, 35, 54, 81]
    assert sort_function([222, 2, 2222, 22])[0] == [2, 22, 222, 2222]
    assert sort_function([500, 1, 300, 2])[0] == [1, 2, 300, 500]
    assert sort_function([7, 14, 9, 12, 8])[0] == [7, 8, 9, 12, 14]
    assert sort_function([5, 4, 3, 2, 1])[0] == [1, 2, 3, 4, 5]


# History is a list of pairs of the array at that state and the time
def visualize(history):
    # Initialize
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("Visualisering Sorteringsalgoritmen")

    # Calculate width and height of bars
    bar_width = 500 / len(history[0])
    max_height = 0

    for item in history[0]:
        max_height = max(max_height, item)

    running = True
    current_state = 0
    while running:
        # Check for exit button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))

        # Draw bars
        for i in range(0, len(history[current_state])):
            bar = history[current_state][i]
            height = (bar / max_height) * 500 - 20
            y_position = 500 - height - 10
            pygame.draw.rect(screen, (0, 0, 0), (i * bar_width + 10,
                             y_position, bar_width - 20, height))

        pygame.display.flip()
        pygame.time.wait(500)

        if current_state < len(history) - 1:
            current_state += 1

    pygame.quit()
