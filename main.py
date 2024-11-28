import pygame
import random
import math

WIDTH = 800
HEIGHT = 600

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True
dt = 0

number_balls = random.randint(1, 3)
number_balls = 5
circles = []

def checkCircleCircleCollision(circle1, circle2):
    radius_distance = circle1['r'] + circle2['r']
    x_distance = abs(circle2['x_pos'] - circle1['x_pos'])
    y_distance = abs(circle2['y_pos'] - circle1['y_pos'])
    center_distance = math.sqrt(math.pow(x_distance, 2) + math.pow(y_distance, 2))
    if radius_distance >= center_distance:
        print(center_distance)
        return True
    return False                                                                                                                                                                                                                                                                                                                          
def checkCircleWallCollision(circle):                                                                                                                            
    if circle['x_pos'] + circle['r'] > WIDTH or circle['x_pos'] - circle['r'] < 0 or circle['y_pos'] + circle['r'] > HEIGHT or circle['y_pos'] - circle['r'] < 0 :                                                                                                                                                                
        return True                                                                                                                                             
    return False

for i in range(number_balls):
    x_position = random.randint(31, 769)
    y_position = random.randint(31, 569)
    x_velocity = random.randint(-80, 80)
    y_velocity = random.randint(-80, 80)
    radius = random.randint(5, 40)
    circles.append({'id': i,'x_pos': x_position, 'y_pos': y_position, 'r': radius,'x_vel': x_velocity, 'y_vel': y_velocity})

while running:
    for event in pygame.event.get():
        if  event.type == pygame.QUIT:
            running = False

    screen.fill("white")

    for circle in circles:
        circle['x_pos'] += circle['x_vel']*dt
        circle['y_pos'] += circle['y_vel']*dt
        pygame.draw.circle(screen, "blue", (circle['x_pos'], circle['y_pos']), circle['r'])

    for circle1 in circles:
        checkCircleWallCollision(circle)
        for circle2 in circles:
            if circle1['id'] != circle2['id']:
                checkCircleCircleCollision(circle1, circle2)

    pygame.display.flip()
    clock.tick(60)
    dt = clock.tick(60) / 1000

pygame.quit()


    

