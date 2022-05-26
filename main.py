import random
import pygame
import time
from pygame.locals import *

# initialize pygame
pygame.init()

# create screen (x, y) = (width, height).
screen = pygame.display.set_mode((1366, 768), pygame.FULLSCREEN)


# Title of game
pygame.display.set_caption("-->> NFS 0.001 <<--")

# Icone of a game
pygame.display.set_icon(pygame.image.load('vehicle.png'))

# Add the car_image.
carCollection = {0: pygame.image.load('car.png'), 1: pygame.image.load('car1.png'), 2: pygame.image.load('car2.png'), 3: pygame.image.load('car3.png'), 4: pygame.image.load('car4.png'), 5: pygame.image.load('car5.png'), 6: pygame.image.load('car6.png'), 7: pygame.image.load('car7.png'), 8: pygame.image.load('car8.png'), 9: pygame.image.load('car9.png'), 10: pygame.image.load('car10.png')}

# Variables
a1 = [39, 5, 15, 15, 9, 18, 10, 20, 14, 19]
b1 = [88, 58, 58, 67, 68, 72, 61, 72, 78, 70]
a2 = [2, 5, 30, 5, 2, 18, 10, 20, 8, 15]
b2 = [121, 140, 145, 135, 195, 170, 160, 225, 150, 125]
leftEngineLongTime = 0
acceleratedEngineAchived = False
carAccelerationDecreased = False
crashCounter = 0
levels = 1
# ----------------------------------------SOUNDS--------------------------------------------------

# startEnginSound = pygame.mixer.Sound('carEngineStart.mp3')
# carAcceleratingSound = pygame.mixer.Sound('carAcceleratedEngine.mp3')
# carEngineLoopExtrem = pygame.mixer.Sound('carEngineLoopExtrem.mp3')
# carEnginDecreaseAcceleration = pygame.mixer.Sound('carEnginDecreaseAcceleration.mp3')
# carEngineDecreaseStopEngine = pygame.mixer.Sound('carEngineDecreaseStopEngine.mp3')
# carStandEngineLoop = pygame.mixer.Sound('carStandEngineLoop.mp3')

#-------------------------------------------------------------------------------------------------
flag1_acceleration = 0
flag2_acceleration = 0
car_speed_increasing = False
car_speed_decreasing = False
car_acceleration = 0
car_accelerator_up = False
car_accelerator_down = False
hand_break = False
car_speedometer = 0
car_x_coordinate_list = [455, 585, 320, 200]
car_y_coordinate_list = [-300, -600, -900]
car_numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
car_x_coordinate = 125
car_y_coordinate = 630
car_properties = [800, 800, 800, 800, 800, 800, 800, 800, 800]
car_x_coordinate_update = 0
car_y_coordinate_update = 0
road_x_coordinate = 0
road_y_coordinate = 0
r_road_y_coordinate = 0
coordinate_update = 8
car_health_no = 100
car_health_no_colour = 255
gameOver = False
i = 0

def draw_car_on_screen(x, y, x1, x2, x3, y1, y2, y3, c1, c2, c3):
    global car_health_no
    global car_health_no_colour
    global car_x_coordinate
    global car_y_coordinate
    screen.blit(carCollection[0], (x, y))
    screen.blit(carCollection[c1], (x1, y1))
    screen.blit(carCollection[c2], (x2, y2))
    screen.blit(carCollection[c3], (x3, y3))
    if (x1 + a1[c1 - 1]) <= (x + 90) and (x1 + b1[c1 - 1]) >= (x + 35) and (y1 + b2[c1 - 1]) >= (y + 5) and (y1 + a2[c1 - 1]) <= (y + 125) or (x2 + a1[c2 - 1]) <= (x + 90) and (x2 + b1[c2 - 1]) >= (x + 35) and (y2 + b2[c2 - 1]) >= (y + 5) and (y2 + a2[c2 - 1]) <= (y + 125) or (x3 + a1[c3 - 1]) <= (x + 90) and (x3 + b1[c3 - 1]) >= (x + 35) and (y3 + b2[c3 - 1]) >= (y + 5) and (y3 + a2[c3 - 1]) <= (y + 125) or (x > 605 or  x < 106):
        car_health_no -= 2
        car_health_no_colour -= 5
        car_x_coordinate = 125
        car_y_coordinate = 630
        

def choose_cars():
    # X Co-Ordinate
    car_properties[0] = random.choice(car_x_coordinate_list)
    car_properties[1] = random.choice(car_x_coordinate_list)
    car_properties[2] = random.choice(car_x_coordinate_list)
    # Y Co-Ordinate
    car_properties[3] = random.choice(car_y_coordinate_list)
    car_properties[4] = random.choice(car_y_coordinate_list)
    car_properties[5] = random.choice(car_y_coordinate_list)
    # Car Numbers
    car_properties[6] = random.choice(car_numbers_list)
    car_properties[7] = random.choice(car_numbers_list)
    car_properties[8] = random.choice(car_numbers_list)
    # Exceptions
    if car_properties[0] == car_properties[1]:
        car_properties[0] = -300
    if car_properties[1] == car_properties[2]:
        car_properties[1] = -300
    if car_properties[0] == car_properties[2]:
        car_properties[2] = -300

# Score Updater
score_value = 0
font = pygame.font.Font('font.ttf', 32)

def show_score():
    score = font.render("Score " + str(int(score_value)), True, (255, 255, 5))
    screen.blit(score, (880, 10))
# Speedometer
def speedo_meter():
    speedoMeter = font.render("Speed  " + str(car_speedometer) + "  K M / H", True, (166, 232, 138))
    screen.blit(speedoMeter, (880, 50))
# Car Health
def car_health():
    carHealt = font.render("Car Health  ", True, (255, 255, 255))
    carHealtC = font.render(str(car_health_no), True, (255, car_health_no_colour, 0))
    screen.blit(carHealt, (880, 100))
    screen.blit(carHealtC, (1100, 100))
# game menu loop
runTheGameMenu = True
while runTheGameMenu:
    screen.blit(pygame.image.load('menu.png'), (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                runTheGameMenu = False
    pygame.display.update()


# game loop
run_the_game = True
while run_the_game:
    # fill the BG color which should appear infinite time.
    #screen.fill((0, 0, 255))
    screen.blit(pygame.image.load('menu.png'), (0, 0))
    screen.blit(pygame.image.load('road.png'), (road_x_coordinate, road_y_coordinate - 600))
    screen.blit(pygame.image.load('road.png'), (road_x_coordinate, road_y_coordinate))

    # capture each event in 'event' variable which stores all the event happened like 'Close Window' here.
    for event in pygame.event.get():
        # If the 'event.type' exactly the same with the 'QUIT' event for 'Close Window'.
        if event.type == pygame.QUIT:
            run_the_game = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and car_acceleration > 1.5:
                car_x_coordinate_update = 10 + (car_acceleration / 10)
            elif event.key == pygame.K_LEFT and car_acceleration > 1.5:
                car_x_coordinate_update = -10 - (car_acceleration / 10)
            elif event.key == pygame.K_a:
                r_road_y_coordinate = 4
                car_accelerator_down = True
                car_accelerator_up = False
            elif event.key == pygame.K_SPACE:
                hand_break = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                car_x_coordinate_update = 0
                car_y_coordinate_update = 0
            elif event.key == pygame.K_UP:
                pass
            elif event.key == pygame.K_s:
                pass
            elif event.key == pygame.K_a:
                car_accelerator_up = True
                car_accelerator_down = False
            elif event.key == pygame.K_SPACE:
                hand_break = False

                
    # Car Acceleration
    car_speedometer = int(car_acceleration)
    if car_accelerator_down:
        car_acceleration += 0.2
    if car_accelerator_up:
        car_acceleration -= 0.2
    if car_acceleration <= 0:
        car_acceleration = 0
    if car_acceleration >= 80:
        car_acceleration -= 0.2
    if hand_break:
        car_acceleration -= 1
    
    road_y_coordinate += r_road_y_coordinate * (car_acceleration // 2)
    # Score Update Condition
    if car_speedometer >= 10:
        score_value += 0.1
    # Move the road
    if road_y_coordinate > 599:
        road_y_coordinate = 0
    # car X co ordinate update
    car_x_coordinate += car_x_coordinate_update
    # Call traffic
    if car_properties[3] >= 800 and car_properties[4] >= 800 and car_properties[5] >= 800:
        choose_cars()
    else:
        car_properties[3] += 12 + car_acceleration
        car_properties[4] += 12 + car_acceleration
        car_properties[5] += 12 + car_acceleration
    
    # Game Over Condition
    if crashCounter == 20:
        screen.fill((255, 255, 5))
        run_the_game = False
    
    # Score Update && Level Update && Speedometer Update && Car Frame Update
    show_score()
    speedo_meter()
    car_health()
    draw_car_on_screen(car_x_coordinate, car_y_coordinate, car_properties[0], car_properties[1], car_properties[2], car_properties[3], car_properties[4], car_properties[5], car_properties[6], car_properties[7], car_properties[8])
    pygame.display.update()
    if car_health_no <= 0:
        run_the_game = False

# Game Over
runTheGameMenu = True
while runTheGameMenu:
    screen.blit(pygame.image.load('menu.png'), (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                runTheGameMenu = False
    font1 = pygame.font.Font('font1.ttf', 80)
    game_over = font1.render("!! GAME OVER !!", True, (255, 14, 10))
    font2 = pygame.font.Font('font2.ttf', 60)
    game_score = font2.render("YOU SCORED :" + str(int(score_value)), True, (74, 129, 132))
    screen.blit(game_over, (183, 184))
    screen.blit(game_score, (383, 384))
    pygame.display.update()
