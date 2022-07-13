import pygame
pygame.init()

screen = pygame.display.set_mode([1000, 1000])

colors = {
    'red': (255, 0, 0)
}

# (x, y, z, color)
circles = []
current_demo = 'square'

def do_square_of_circles(x, z, size=2, radius=25):
    result = []

    if size < 2:
        return []
    
    current_x = -(radius * size) + x
    current_z = -(radius * size) + z

    i = 0
    j = 0
    rendering = True
    while rendering:
        if j == size:
            break
        if j == 0 or j == size-1:
            result.append((current_x, 0, current_z, colors['red']))
        else:
            if i == 0 or i == size-1:
                result.append((current_x, 0, current_z, colors['red']))
        current_x += radius * 3
        i += 1
        if i == size:
            current_x = -(radius * size) + x
            current_z += radius * 3
            i = 0
            j += 1

    return result

def generate_circles_by_demo_name(demo_name):
    result = []
    if demo_name == 'square':
        result += do_square_of_circles(0, 0)
        result += do_square_of_circles(-25, -25, 4)
        result += do_square_of_circles(-50, -50, 6)
        result += do_square_of_circles(-75, -75, 8)
    return result

running = True
circles = generate_circles_by_demo_name('square')

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
    for x, y, z, color in circles:
        pygame.draw.circle(screen, color, (x + 300, z + 300), 25)

    pygame.display.flip()

pygame.quit()
