import pygame
import sys

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 600, 400
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
ERASER = (255, 255, 255)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Paint App")

clock = pygame.time.Clock()

drawing = False
last_pos = None
color = BLACK
radius = 5

def draw_circle(pos):
    pygame.draw.circle(screen, color, pos, radius)

def draw_rectangle(start, end):
    rect = pygame.Rect(start, (end[0] - start[0], end[1] - start[1]))
    pygame.draw.rect(screen, color, rect, 2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                drawing = True
                last_pos = event.pos
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drawing = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                color = RED
            if event.key == pygame.K_b:
                color = BLUE
            if event.key == pygame.K_g:
                color = GREEN
            if event.key == pygame.K_e:
                color = ERASER
    if drawing:
        draw_circle(pygame.mouse.get_pos())
    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()