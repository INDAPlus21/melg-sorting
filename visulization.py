import pygame


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
