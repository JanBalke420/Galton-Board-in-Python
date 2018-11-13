import random
import pygame

resolution = (1280,720)

margin = 50
spacing = 10

num_layers = 50
distribution = [0]*(num_layers+1)

num_sims = 0

print(distribution)

def drawDistribution():
    max_value = 1
    for val in distribution:
        if val >= max_value:
            max_value = val
    h_scale = (resolution[1]-margin)/max_value

    y = resolution[1]
    w = (resolution[0]-2*margin-(num_layers)*spacing)/(num_layers+1)

    for i in range(num_layers+1):
        x = margin + i*w + i*spacing
        h = distribution[i]*h_scale
        pygame.draw.rect(display, (0,0,255),(x, y, w, -h))

def simulateBall():
    ball = num_layers/2
    for i in range(num_layers):
        direction = random.randint(0,1)
        direction = direction - 0.5
        ball += direction
    distribution[int(ball)] += 1

pygame.init()
display = pygame.display.set_mode(resolution)
clock = pygame.time.Clock()

running = True
while running:
    clock.tick(60)
    display.fill((255,255,255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    simulateBall()
    num_sims += 1
    if num_sims%500 == 0:
        print(num_sims, 'balls simulated')
        print(distribution)
    drawDistribution()

    pygame.display.flip()