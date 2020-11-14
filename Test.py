import pygame, sys, os
pygame.init()
from pygame.locals import *
from Character  import CutSceneManager, CutSceneOne
pygame.display.set_caption('For Earth!')
screen = pygame.display.set_mode((1000, 600), 0, 32)
mainClock = pygame.time.Clock()
font = pygame.font.SysFont(None, 20)

###### CUT SCENE ##############
# class Player(pygame.sprite.Sprite):
#
#     def __init__(self):
#         super().__init__()
#         self.image = pygame.Surface((50, 50))
#         self.image.fill((0, 0, 0))
#         self.rect = self.image.get_rect(center=(400, 300))
#
#     def update(self, cut_scene_manager):
#
#         if self.rect.centerx > 399:
#             cut_scene_manager.start_cut_scene(CutSceneOne(self))
#
#         if cut_scene_manager.cut_scene is None:
#             pressed = pygame.key.get_pressed()
#             if pressed[pygame.K_LEFT]:
#                 self.rect.x -= 5
#             if pressed[pygame.K_RIGHT]:
#                 self.rect.x += 5
#
#     def draw(self, screen):
#         screen.blit(self.image, self.rect.center)



##### FADING SCREEEEN #########
def fade():
    fade = pygame.Surface((1000, 600))
    fade.fill((0, 0, 0))
    for alpha in range(0, 200):
        fade.set_alpha(alpha)
        screen.blit(fade, (0, 0))
        pygame.display.update()
        pygame.time.delay(5)

# Images
Earth = pygame.image.load('Earth.png')
hub1 = pygame.image.load('Level 1.png')
Logo = pygame.image.load('Title Screen2.png')
trash = pygame.image.load('Trash.png')
level_two = pygame.image.load('Level 2.png')
level_three = pygame.image.load('Level 3.png')
level_four = pygame.image.load('Level 4.png')
bee = pygame.image.load('Bee.png')
# Sprite
stationary = pygame.image.load(os.path.join("Character", "WalkDown1.png"))
rect_p = stationary.get_rect()
# rect_stationary = stationary.get_rect()
left = [None]*10
for picIndex in range(1, 4):
    left[picIndex-1] = pygame.image.load(os.path.join("Character", "WalkLeft" + str(picIndex) + ".png"))
    picIndex += 1

right = [None]*10
for picIndex in range(1, 4):
    right[picIndex-1] = pygame.image.load(os.path.join("Character", "WalkRight" + str(picIndex) + ".png"))
    picIndex += 1
up = [None]*10
for picIndex in range(1, 4):
    up[picIndex-1] = pygame.image.load(os.path.join("Character", "WalkUp" + str(picIndex) + ".png"))
    picIndex += 1
down = [None]*10
for picIndex in range(1, 4):
    down[picIndex-1] = pygame.image.load(os.path.join("Character", "WalkDown" + str(picIndex) + ".png"))
    picIndex += 1
##### BEEEEEEEEEEEEEEES ######
#----------BEE1-----------#
rect_b = bee.get_rect()
rect_b.x = 500
rect_b.y = 400
rect_bchangex = -5
rect_bchangey = 5
def enemy(rect_b):
    screen.blit(bee, (rect_b.x, rect_b.y))
#---------- BEE2-----------#
rect_b2 = bee.get_rect()
rect_b2.x = 500
rect_b2.y = 400
rect_b2changex = 5
rect_b2changey = -5
def enemy2(rect_b2):
    screen.blit(bee, (rect_b2.x, rect_b2.y))
# BEEE 3 ####
rect_b3 = bee.get_rect()
rect_b3.x = 500
rect_b3.y = 400
rect_b3changex = -5
rect_b3changey = -5
def enemy3(rect_b3):
    screen.blit(bee, (rect_b3.x, rect_b3.y))
# BEEE 4 #####
rect_b4 = bee.get_rect()
rect_b4.x = 500
rect_b4.y = 300
rect_b4changex = -5
rect_b4changey = 0
def enemy4(rect_b4):
    screen.blit(bee, (rect_b4.x, rect_b4.y))
# BEEE 5
rect_bu = bee.get_rect()
rect_bu.x = 250
rect_bu.y = 400
rect_buchangex = 0
rect_buchangey = -5
def enemyu(rect_bu):
    screen.blit(bee, (rect_bu.x, rect_bu.y))
# BEEE 6
rect_bu2 = bee.get_rect()
rect_bu2.x = 750
rect_bu2.y = 400
rect_bu2changex = 0
rect_bu2changey = 5
def enemyu2(rect_bu2):
    screen.blit(bee, (rect_bu2.x, rect_bu2.y))

######### OBJECTIVE ################
trash = pygame.image.load('Trash.png')
trashes = [
    pygame.Rect(100, 200, 73, 49),
    pygame.Rect(200, 250, 73, 49),
    pygame.Rect(500, 200, 73, 49),
    pygame.Rect(600, 400, 73, 49),
    pygame.Rect(800, 300, 73, 49)
]
trashe = [
    pygame.Rect(100, 400, 73, 49),
    pygame.Rect(200, 350, 73, 49),
    pygame.Rect(600, 200, 73, 49),
    pygame.Rect(600, 400, 73, 49),
    pygame.Rect(800, 200, 73, 49)
]
trashs = [
    pygame.Rect(850, 450, 73, 49),
    pygame.Rect(200, 450, 73, 49),
    pygame.Rect(500, 200, 73, 49),
    pygame.Rect(600, 400, 73, 49),
    pygame.Rect(800, 300, 73, 49),
    pygame.Rect(600, 400, 73, 49),
    pygame.Rect(200, 350, 73, 49),
]
trashse = [
    pygame.Rect(500, 200, 73, 49),
    pygame.Rect(200, 450, 73, 49),
    pygame.Rect(800, 200, 73, 49)
]
# SCORE #
score_value = 0

# PLAYER RECT AND MOVEMENT #
sx = 500
sy = 100
rect_p.x = 478
rect_p.y = 400
vel = 3
move_left = False
move_right = False
move_up = False
move_down = False
stepIndex = 0
# ENEMY MOVEMENT #

def player_move():
    global stepIndex

    if stepIndex >= 4:
        stepIndex = 1
    if move_left:
        screen.blit(left[stepIndex//3], (rect_p.x, rect_p.y))
        stepIndex += 1
    elif move_right:
        screen.blit(right[stepIndex//3], (rect_p.x, rect_p.y))
        stepIndex += 1
    elif move_up:
        screen.blit(up[stepIndex//3], (rect_p.x, rect_p.y))
        stepIndex += 1
    elif move_down:
        screen.blit(down[stepIndex//3], (rect_p.x, rect_p.y))
        stepIndex += 1
    else:
        screen.blit(stationary, (rect_p.x, rect_p.y))


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


pygame.MOUSEBUTTONDOWN = False


def main_menu():
    while True:

        screen.fill((0, 0, 0))
        # draw_text('For Earth - Main Menu', font, (255, 255, 255), screen, 20, 20)
        screen.blit(Earth, (400, 10))
        # screen.blit(Logo, (-150, -20))
        screen.blit(Logo, (-100, 50))
        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(50, 300, 300, 75)
        button_2 = pygame.Rect(50, 450, 300, 75)
        if button_1.collidepoint((mx, my)):
            if pygame.MOUSEBUTTONDOWN:
                fade()
                cutscene()
        if button_2.collidepoint((mx, my)):
            if pygame.MOUSEBUTTONDOWN:
                game()
        pygame.draw.rect(screen, (255, 0, 0), button_1)
        pygame.draw.rect(screen, (255, 0, 0), button_2)

        pygame.MOUSEBUTTONDOWN = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    pygame.MOUSEBUTTONDOWN = True


        pygame.display.update()
        mainClock.tick(60)
def cutscene():
    class Player(pygame.sprite.Sprite):

        def __init__(self):
            super().__init__()
            self.image = pygame.Surface((50, 50))
            self.image.fill((0, 0, 0))
            self.rect = self.image.get_rect(center=(400, 300))

        def update(self, cut_scene_manager):

            if self.rect.centerx > 399:
                cut_scene_manager.start_cut_scene(CutSceneOne(self))

            if cut_scene_manager.cut_scene is None:
                pressed = pygame.key.get_pressed()
                if pressed[pygame.K_LEFT]:
                    self.rect.x -= 5
                if pressed[pygame.K_RIGHT]:
                    self.rect.x += 5

        def draw(self, screen):
            screen.blit(self.image, self.rect.center)


    player = Player()
    cut_scene_manager = CutSceneManager(screen)
    while True:

        mainClock.tick(60)

        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_c:
                    game()
        # Update objects
        player.update(cut_scene_manager)
        cut_scene_manager.update()

        # Draw objects
        screen.fill((0, 0, 0))
        player.draw(screen)
        cut_scene_manager.draw()

        pygame.display.flip()

def game():
    running = True
    while running:

        screen.fill((0,0,0))
        screen.blit(hub1, (50, 90))
        for t in trashes:
            screen.blit(trash, (t[0], t[1]))

        global move_left, move_up, move_down, move_right, stepIndex, rect_p, score_value
        # draw_text('Score: ' + str(score_value), font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        userInput = pygame.key.get_pressed()
        if userInput[pygame.K_LEFT]:
            rect_p.x -= vel
            move_left = True
            move_right = False
            move_down = False
            move_up = False
        elif userInput[pygame.K_RIGHT]:
            rect_p.x += vel
            move_left = False
            move_right = True
            move_down = False
            move_up = False
        elif userInput[pygame.K_UP]:
            rect_p.y -= vel
            move_left = False
            move_right = False
            move_down = False
            move_up = True
        elif userInput[pygame.K_DOWN]:
            rect_p.y += vel
            move_left = False
            move_right = False
            move_down = True
            move_up = False
        else:
            move_left = False
            move_right = False
            move_down = False
            move_up = False
            stepIndex = 0

        for t in trashes:
            if t.colliderect(rect_p):
                trashes.remove(t)
                score_value += 10
                if score_value == 50:
                    fade()
                    main_menu()

        player_move()
        draw_text('Score: ' + str(score_value), font, (255, 255, 255), screen, 20, 20)
        pygame.display.update()
        mainClock.tick(60)

main_menu()
