import pygame
import time
import random
import math

WIDTH = 800
HEIGHT = 600

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True
dt = 0.016
COOLDOWN = 0.01

number_balls = random.randint(5, 14)
circles = []

def calculateNewVelocity(mass1, mass2, velocity1, velocity2):
    return ((mass1*(2*velocity1 - velocity2) + mass2*velocity2)/(mass1 + mass2))

def updateCooldown():
    for circle in circles:
        if circle['cooldown'] > 0:
            circle['cooldown'] -= dt;

def checkCircleCircleCollision(circle1, circle2):

    if(circle1['cooldown'] > 0 or circle2['cooldown'] > 0):
        return;

    radius_distance = circle1['r'] + circle2['r']
    x_distance = abs(circle2['x_pos'] - circle1['x_pos'])
    y_distance = abs(circle2['y_pos'] - circle1['y_pos'])
    center_distance = math.sqrt(x_distance**2 + y_distance**2)
    if radius_distance > center_distance:

        circle1['cooldown'] = COOLDOWN
        circle2['cooldown'] = COOLDOWN

        new_x_velocity1 = calculateNewVelocity(circle2['m'], circle1['m'], circle2['x_vel'], circle1['x_vel'])
        new_y_velocity1 = calculateNewVelocity(circle2['m'], circle1['m'], circle2['y_vel'], circle1['y_vel'])
        new_x_velocity2 = calculateNewVelocity(circle1['m'], circle2['m'], circle1['x_vel'], circle2['x_vel'])
        new_y_velocity2 = calculateNewVelocity(circle1['m'], circle2['m'], circle1['y_vel'], circle2['y_vel'])


        circle1['x_vel'] = new_x_velocity1
        circle1['y_vel'] = new_y_velocity1
        circle2['x_vel'] = new_x_velocity2
        circle2['y_vel'] = new_y_velocity2                                                                                                                                                                                                                                                                                                     
def checkCircleWallCollision(circle):                                                                                                                            
    if circle['x_pos'] + circle['r'] > WIDTH or circle['x_pos'] - circle['r'] < 0:
        circle['x_vel'] *= -1

    if circle['y_pos'] + circle['r'] > HEIGHT or circle['y_pos'] - circle['r'] < 0:
        circle['y_vel'] *= -1

def is_position_valid(new_x, new_y, new_radius, circles):
    for circle in circles:
        distance = math.sqrt((new_x - circle['x_pos'])**2 + (new_y - circle['y_pos'])**2)
        
        if distance < (new_radius + circle['r']):
            return False  
    
    return True 

def generate_balls(number_balls, circles):
    for i in range(number_balls):
        valid_position = False
        while not valid_position:
            x_position = random.randint(31, 769)
            y_position = random.randint(31, 569)
            radius = random.randint(20, 40)
            
            valid_position = is_position_valid(x_position, y_position, radius, circles)
            
        x_velocity = random.randint(-200, 200)
        y_velocity = random.randint(-200, 200)
        
        mass = random.randint(1, 10)

        circles.append({'id': i, 'x_pos': x_position, 'y_pos': y_position, 'm': mass, 'r': radius, 
                        'x_vel': x_velocity, 'y_vel': y_velocity, 'cooldown': 0})

generate_balls(number_balls, circles)

while running:
    for event in pygame.event.get():
        if  event.type == pygame.QUIT:
            running = False

    screen.fill("gray")
    
    updateCooldown()

    for circle in circles:
        circle['x_pos'] += circle['x_vel']*dt
        circle['y_pos'] += circle['y_vel']*dt
        pygame.draw.circle(screen, 'blue' , (circle['x_pos'], circle['y_pos']), circle['r'])

    for circle1 in circles:
        checkCircleWallCollision(circle1)
        for circle2 in circles:
            if circle1['id'] != circle2['id']:
                checkCircleCircleCollision(circle1, circle2)
                

    pygame.display.flip()
    clock.tick(60)


pygame.quit()
