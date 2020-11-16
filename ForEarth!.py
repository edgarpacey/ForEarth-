import pygame, sys, os
pygame.init()
from pygame.locals import *
from Character import CutSceneManager, CutSceneOne, CutSceneTwo, CutSceneThree, CutSceneFour
from Character import CutSceneFive, CutSceneSix, CutSceneSeven, CutSceneEight
pygame.display.set_caption('For Earth!')
screen = pygame.display.set_mode((1000, 600), 0, 32)
mainClock = pygame.time.Clock()
font = pygame.font.SysFont(None, 35)

pygame.mixer.music.load('1 AM (Normal).mp3')
pygame.mixer.music.play(-1)

##### FADING SCREEEEN #########
def fade():
    fade = pygame.Surface((1000, 600))
    fade.fill((0, 0, 0))
    for alpha in range(0, 200):
        fade.set_alpha(alpha)
        screen.blit(fade, (0, 0))
        pygame.display.update()
        pygame.time.delay(5)

def fade2():
    fade2 = pygame.Surface((1000, 600))
    fade2.fill((255, 255, 255))
    for alpha in range(0, 200):
        fade2.set_alpha(alpha)
        screen.blit(fade2, (0, 0))
        pygame.display.update()
        pygame.time.delay(5)
# Images
Earth = pygame.image.load('Earth.png')
Start = pygame.image.load("Start.png")
Credits = pygame.image.load('Credits.png')
Tutorial = pygame.image.load('Tutorial.png')
hub1 = pygame.image.load('Level 1.png')
Logo = pygame.image.load('Title Screen2.png')
trash = pygame.image.load('Trash.png')
level_two = pygame.image.load('Level 2.png')
level_three = pygame.image.load('Level 3.png')
level_four = pygame.image.load('Level 4.png')
level_five = pygame.image.load('Level 5.png')
final_screen = pygame.image.load('Final Screen.png')
bee = pygame.image.load('Bee.png')
frog = pygame.image.load('Frog.png')
Earth_Stage0 = pygame.image.load('Earth Stage 0.png')
Earth_Stage1 = pygame.image.load('Earth Stage 1.png')
Earth_Stage2 = pygame.image.load('Earth Stage 2.png')
Earth_Stage3 = pygame.image.load('Earth Stage 3.png')
Earth_Stage4 = pygame.image.load('Earth Final Stage.png')
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
trashss = [
    pygame.Rect(200, 250, 73, 49),
    pygame.Rect(500, 200, 73, 49),
    pygame.Rect(600, 400, 73, 49)
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

    if int(stepIndex) >= 4:
        stepIndex = 1
    if move_left:
        screen.blit(left[int(stepIndex)//3], (rect_p.x, rect_p.y))
        stepIndex += 0.25
    elif move_right:
        screen.blit(right[int(stepIndex)//3], (rect_p.x, rect_p.y))
        stepIndex += 0.25
    elif move_up:
        screen.blit(up[int(stepIndex)//3], (rect_p.x, rect_p.y))
        stepIndex += 0.25
    elif move_down:
        screen.blit(down[int(stepIndex)//3], (rect_p.x, rect_p.y))
        stepIndex += 0.25
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

        button_1 = pygame.Rect(50, 250, 300, 75)
        button_2 = pygame.Rect(50, 450, 300, 75)
        button_3 = pygame.Rect(50, 350, 300, 75)
        if button_1.collidepoint((mx, my)):
            if pygame.MOUSEBUTTONDOWN:
                fade()
                cutscene()
        if button_2.collidepoint((mx, my)):
            if pygame.MOUSEBUTTONDOWN:
                credits()
        if button_3.collidepoint((mx, my)):
            if pygame.MOUSEBUTTONDOWN:
                tutorial()
        pygame.draw.rect(screen, (255, 0, 0), button_1)
        pygame.draw.rect(screen, (255, 0, 0), button_2)
        pygame.draw.rect(screen, (255, 0, 0), button_3)
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
        screen.blit(Start, (56, 260))
        screen.blit(Credits, (56, 465))
        screen.blit(Tutorial, (56, 365))
        pygame.display.update()
        mainClock.tick(60)

def cutscene():
    global Earth_Stage0
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
        screen.blit(Earth_Stage0, (300, 100))

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

        #PLAYER BOUNDERIES
        if rect_p.x <= 50:
            rect_p.x = 50
        elif rect_p.x >= 915:
            rect_p.x = 910

        if rect_p.y <= 200:
            rect_p.y = 200
        elif rect_p.y >= 450:
            rect_p.y = 450

        for t in trashes:
            if t.colliderect(rect_p):
                trashes.remove(t)
                score_value += 10
                if score_value == 50:
                    fade()
                    cutscenetwo()

        player_move()
        draw_text('Score: ' + str(score_value), font, (255, 255, 255), screen, 20, 20)
        pygame.display.update()
        mainClock.tick(60)

def cutscenetwo():
    global hub1
    class Player(pygame.sprite.Sprite):

        def __init__(self):
            super().__init__()
            self.image = pygame.Surface((50, 50))
            self.image.fill((0, 0, 0))
            self.rect = self.image.get_rect(center=(400, 300))

        def update(self, cut_scene_manager):

            if self.rect.centerx > 399:
                cut_scene_manager.start_cut_scene(CutSceneTwo(self))

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
                    progresscheck1()
        # Update objects
        player.update(cut_scene_manager)
        cut_scene_manager.update()

        # Draw objects
        screen.fill((0, 0, 0))
        player.draw(screen)
        cut_scene_manager.draw()
        screen.blit(hub1, (50, 90))

        pygame.display.flip()

def progresscheck1():
    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(Earth_Stage0, (300, 100))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_c:
                    fade2()
                    cutscene3()
        pygame.display.update()
def cutscene3():
    global Earth_Stage1
    class Player(pygame.sprite.Sprite):

        def __init__(self):
            super().__init__()
            self.image = pygame.Surface((50, 50))
            self.image.fill((0, 0, 0))
            self.rect = self.image.get_rect(center=(400, 300))

        def update(self, cut_scene_manager):

            if self.rect.centerx > 399:
                cut_scene_manager.start_cut_scene(CutSceneThree(self))

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
                    level_2()
        # Update objects
        player.update(cut_scene_manager)
        cut_scene_manager.update()

        # Draw objects
        screen.fill((0, 0, 0))
        player.draw(screen)
        cut_scene_manager.draw()
        screen.blit(Earth_Stage1, (300, 100))

        pygame.display.flip()

def level_2():
    running = True
    while running:
        global move_left, move_up, move_down, move_right, vel, rect_bchangey, rect_b2changex
        global stepIndex, score_value, rect_b, rect_bchangex, rect_b2changey


        screen.fill((0, 0, 0))
        screen.blit(level_two, (50, 90))

        for r in trashs:
            screen.blit(trash, (r[0], r[1]))
        player_move()
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
        for t in trashs:
            if t.colliderect(rect_p):
                trashs.remove(t)
                score_value += 10
                if score_value == 100:
                    level_2()
        ##### BEE 1 MOVEMENT #####
        rect_b.x += rect_bchangex
        if rect_b.x <= 35:
            rect_bchangex = 5
        elif rect_b.x >= 920:
            rect_bchangex = -5

        rect_b.y += rect_bchangey
        if rect_b.y <= 75:
            rect_bchangey = 5
        elif rect_b.y >= 480:
            rect_bchangey = -5
        ##### BEE 2 MOVEMENT #####
        rect_b2.x += rect_b2changex
        if rect_b2.x <= 35:
            rect_b2changex = 5
        elif rect_b2.x >= 920:
            rect_b2changex = -5

        rect_b2.y += rect_b2changey
        if rect_b2.y <= 75:
            rect_b2changey = 5
        elif rect_b2.y >= 480:
            rect_b2changey = -5

        #PLAYER BOUNDERIES
        if rect_p.x <= 50:
            rect_p.x = 50
        elif rect_p.x >= 915:
            rect_p.x = 910

        if rect_p.y <= 200:
            rect_p.y = 200
        elif rect_p.y >= 450:
            rect_p.y = 450

        if rect_b.colliderect(rect_p):
            cutscene3()
        if rect_b2.colliderect(rect_p):
            cutscene3()
        if score_value == 120:
            fade()
            progresscheck2()

        enemy(rect_b)
        enemy(rect_b2)
        draw_text('Score: ' + str(score_value), font, (255, 255, 255), screen, 20, 20)
        pygame.display.update()
        mainClock.tick(60)

def progresscheck2():
    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(Earth_Stage1, (300, 100))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_c:
                    fade2()
                    cutscene4()
        pygame.display.update()
def cutscene4():
    global Earth_Stage2
    class Player(pygame.sprite.Sprite):

        def __init__(self):
            super().__init__()
            self.image = pygame.Surface((50, 50))
            self.image.fill((0, 0, 0))
            self.rect = self.image.get_rect(center=(400, 300))

        def update(self, cut_scene_manager):

            if self.rect.centerx > 399:
                cut_scene_manager.start_cut_scene(CutSceneFour(self))

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
                    level3()
        # Update objects
        player.update(cut_scene_manager)
        cut_scene_manager.update()

        # Draw objects
        screen.fill((0, 0, 0))
        player.draw(screen)
        cut_scene_manager.draw()
        screen.blit(Earth_Stage2, (300, 100))
        draw_text('Press [c] to see changes', font, (255, 255, 255), screen, 20, 20)
        pygame.display.flip()

def level3():
    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(level_three, (50, 90))
        global move_left, move_up, move_down, move_right, vel, rect_bchangey, rect_b2changex
        global stepIndex, score_value, trashes, rect_b, rect_bchangex, rect_b2changey
        global rect_bu2changey, rect_buchangey
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        for t in trashe:
            screen.blit(trash, (t[0], t[1]))
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
        for t in trashe:
            if t.colliderect(rect_p):
                trashe.remove(t)
                score_value += 10
                if score_value == 100:
                    level_2()
        ##### BEE 1 MOVEMENT #####
        rect_b.x += rect_bchangex
        if rect_b.x <= 35:
            rect_bchangex = 5
        elif rect_b.x >= 920:
            rect_bchangex = -5

        rect_b.y += rect_bchangey
        if rect_b.y <= 75:
            rect_bchangey = 5
        elif rect_b.y >= 480:
            rect_bchangey = -5
        ##### BEE 2 MOVEMENT #####
        rect_b2.x += rect_b2changex
        if rect_b2.x <= 35:
            rect_b2changex = 5
        elif rect_b2.x >= 920:
            rect_b2changex = -5

        rect_b2.y += rect_b2changey
        if rect_b2.y <= 75:
            rect_b2changey = 5
        elif rect_b2.y >= 480:
            rect_b2changey = -5

        rect_bu2.y += rect_bu2changey
        if rect_bu2.y <= 75:
            rect_bu2changey = 5
        elif rect_bu2.y >= 480:
            rect_bu2changey = -5

        rect_bu.y += rect_buchangey
        if rect_bu.y <= 75:
            rect_buchangey = 5
        elif rect_bu.y >= 480:
            rect_buchangey = -5

        #PLAYER BOUNDERIES
        if rect_p.x <= 50:
            rect_p.x = 50
        elif rect_p.x >= 915:
            rect_p.x = 910

        if rect_p.y <= 200:
            rect_p.y = 200
        elif rect_p.y >= 450:
            rect_p.y = 450

        for t in trashe:
            if t.colliderect(rect_p):
                trashe.remove(t)
                score_value += 10

        if rect_b.colliderect(rect_p):
            cutscene4()
        if rect_b2.colliderect(rect_p):
            cutscene4()
        if rect_bu.colliderect(rect_p):
            cutscene4()
        if rect_bu2.colliderect(rect_p):
            cutscene4()
        if score_value == 170:
            fade()
            progresscheck3()

        player_move()
        enemy(rect_b)
        enemy(rect_b2)
        enemyu(rect_bu)
        enemyu2(rect_bu2)
        draw_text('Score: ' + str(score_value), font, (255, 255, 255), screen, 20, 20)
        pygame.display.update()
        mainClock.tick(60)

def progresscheck3():
    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(Earth_Stage2, (300, 100))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_c:
                    fade2()
                    cutscene5()
        draw_text('Press [c] to see changes', font, (255, 255, 255), screen, 20, 20)
        pygame.display.update()
def cutscene5():
    global Earth_Stage3
    class Player(pygame.sprite.Sprite):

        def __init__(self):
            super().__init__()
            self.image = pygame.Surface((50, 50))
            self.image.fill((0, 0, 0))
            self.rect = self.image.get_rect(center=(400, 300))

        def update(self, cut_scene_manager):

            if self.rect.centerx > 399:
                cut_scene_manager.start_cut_scene(CutSceneFive(self))

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
                    level4()
        # Update objects
        player.update(cut_scene_manager)
        cut_scene_manager.update()

        # Draw objects
        screen.fill((0, 0, 0))
        player.draw(screen)
        cut_scene_manager.draw()
        screen.blit(Earth_Stage3, (300, 100))
        draw_text('Press [c] to see changes', font, (255, 255, 255), screen, 20, 20)
        pygame.display.flip()

def level4():
    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(level_four, (50, 90))
        global move_left, move_up, move_down, move_right, vel, rect_bchangey, rect_b2changex
        global stepIndex, score_value, trashes, rect_b, rect_bchangex, rect_b2changey
        global rect_bu2changey, rect_buchangey, rect_b3changex, rect_b3changey, rect_b4changex
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        for t in trashse:
            screen.blit(trash, (t[0], t[1]))
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
        for t in trashe:
            if t.colliderect(rect_p):
                trashe.remove(t)
                score_value += 10
                if score_value == 100:
                    level_2()
        ##### BEE 1 MOVEMENT #####
        rect_b.x += rect_bchangex
        if rect_b.x <= 35:
            rect_bchangex = 5
        elif rect_b.x >= 920:
            rect_bchangex = -5

        rect_b.y += rect_bchangey
        if rect_b.y <= 75:
            rect_bchangey = 5
        elif rect_b.y >= 480:
            rect_bchangey = -5
        ##### BEE 2 MOVEMENT #####
        rect_b2.x += rect_b2changex
        if rect_b2.x <= 35:
            rect_b2changex = 5
        elif rect_b2.x >= 920:
            rect_b2changex = -5

        rect_b2.y += rect_b2changey
        if rect_b2.y <= 75:
            rect_b2changey = 5
        elif rect_b2.y >= 480:
            rect_b2changey = -5
        # BEE 3
        rect_bu2.y += rect_bu2changey
        if rect_bu2.y <= 75:
            rect_bu2changey = 5
        elif rect_bu2.y >= 480:
            rect_bu2changey = -5
        #BEE4
        rect_bu.y += rect_buchangey
        if rect_bu.y <= 75:
            rect_buchangey = 5
        elif rect_bu.y >= 480:
            rect_buchangey = -5
        # BEE 5
        rect_b3.x += rect_b3changex
        if rect_b3.x <= 35:
            rect_b3changex = 5
        elif rect_b3.x >= 920:
            rect_b3changex = -5

        rect_b3.y += rect_b3changey
        if rect_b3.y <= 75:
            rect_b3changey = 5
        elif rect_b3.y >= 480:
            rect_b3changey = -5
        # BEE 6
        rect_b4.x += rect_b4changex
        if rect_b4.x <= 35:
            rect_b4changex = 5
        elif rect_b4.x >= 920:
            rect_b4changex = -5
        for t in trashse:
            if t.colliderect(rect_p):
                trashse.remove(t)
                score_value += 10

        if rect_b.colliderect(rect_p):
            cutscene5()
        if rect_b2.colliderect(rect_p):
            cutscene5()
        if rect_bu.colliderect(rect_p):
            cutscene5()
        if rect_bu2.colliderect(rect_p):
            cutscene5()
        if rect_b4.colliderect(rect_p):
            cutscene5()
        if rect_b3.colliderect(rect_p):
            cutscene5()

        #PLAYER BOUNDERIES
        if rect_p.x <= 50:
            rect_p.x = 50
        elif rect_p.x >= 915:
            rect_p.x = 910

        if rect_p.y <= 200:
            rect_p.y = 200
        elif rect_p.y >= 450:
            rect_p.y = 450

        if score_value == 200:
            fade()
            progresscheck4()

        player_move()
        enemy(rect_b)
        enemy(rect_b2)
        enemy3(rect_b3)
        enemy4(rect_b4)
        enemyu(rect_bu)
        enemyu2(rect_bu2)
        draw_text('Score: ' + str(score_value), font, (255, 255, 255), screen, 20, 20)
        pygame.display.update()
        mainClock.tick(60)

def progresscheck4():
    running = True
    while running:
        screen.fill((0, 0, 0))
        screen.blit(Earth_Stage3, (300, 100))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_c:
                    fade2()
                    cutscene6()
        draw_text('Press [c] to see changes', font, (255, 255, 255), screen, 20, 20)
        pygame.display.update()
def cutscene6():
    global Earth_Stage4
    class Player(pygame.sprite.Sprite):

        def __init__(self):
            super().__init__()
            self.image = pygame.Surface((50, 50))
            self.image.fill((0, 0, 0))
            self.rect = self.image.get_rect(center=(400, 300))

        def update(self, cut_scene_manager):

            if self.rect.centerx > 399:
                cut_scene_manager.start_cut_scene(CutSceneSix(self))

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
                    level_final()
        # Update objects
        player.update(cut_scene_manager)
        cut_scene_manager.update()

        # Draw objects
        screen.fill((0, 0, 0))
        draw_text('Press [c] to see changes', font, (255, 255, 255), screen, 20, 20)
        player.draw(screen)
        cut_scene_manager.draw()
        screen.blit(Earth_Stage4, (300, 100))

        pygame.display.flip()

def level_final():
    running = True
    while running:
        global move_left, move_up, move_down, move_right, vel, rect_bchangey, rect_b2changex
        global stepIndex, score_value, rect_b, rect_bchangex, rect_b2changey


        screen.fill((0, 0, 0))
        screen.blit(level_five, (50, 90))

        for t in trashss:
            screen.blit(trash, (t[0], t[1]))
        player_move()
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
        for t in trashss:
            if t.colliderect(rect_p):
                trashss.remove(t)
                score_value += 10
                if score_value == 100:
                    main_menu()
        ##### BEE 1 MOVEMENT #####
        rect_b.x += rect_bchangex
        if rect_b.x <= 35:
            rect_bchangex = 5
        elif rect_b.x >= 920:
            rect_bchangex = -5

        rect_b.y += rect_bchangey
        if rect_b.y <= 75:
            rect_bchangey = 5
        elif rect_b.y >= 480:
            rect_bchangey = -5
        ##### BEE 2 MOVEMENT #####
        rect_b2.x += rect_b2changex
        if rect_b2.x <= 35:
            rect_b2changex = 5
        elif rect_b2.x >= 920:
            rect_b2changex = -5

        rect_b2.y += rect_b2changey
        if rect_b2.y <= 75:
            rect_b2changey = 5
        elif rect_b2.y >= 480:
            rect_b2changey = -5

        #PLAYER BOUNDERIES
        if rect_p.x <= 50:
            rect_p.x = 50
        elif rect_p.x >= 915:
            rect_p.x = 910

        if rect_p.y <= 200:
            rect_p.y = 200
        elif rect_p.y >= 450:
            rect_p.y = 450

        if score_value == 230:
            fade()
            cutscene7()

        enemy(rect_b)
        enemy(rect_b2)
        draw_text('Score: ' + str(score_value), font, (255, 255, 255), screen, 20, 20)
        pygame.display.update()
        mainClock.tick(60)

def cutscene7():
    global level_five
    class Player(pygame.sprite.Sprite):

        def __init__(self):
            super().__init__()
            self.image = pygame.Surface((50, 50))
            self.image.fill((0, 0, 0))
            self.rect = self.image.get_rect(center=(400, 300))

        def update(self, cut_scene_manager):

            if self.rect.centerx > 399:
                cut_scene_manager.start_cut_scene(CutSceneSeven(self))

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
                    fade()
                    cutscene8()
        # Update objects
        player.update(cut_scene_manager)
        cut_scene_manager.update()

        # Draw objects
        screen.fill((0, 0, 0))
        draw_text('Press [c] to see changes', font, (255, 255, 255), screen, 20, 20)
        player.draw(screen)
        cut_scene_manager.draw()
        screen.blit(level_five, (50, 90))

        pygame.display.flip()

def cutscene8():
    global final_screen
    class Player(pygame.sprite.Sprite):

        def __init__(self):
            super().__init__()
            self.image = pygame.Surface((50, 50))
            self.image.fill((0, 0, 0))
            self.rect = self.image.get_rect(center=(400, 300))

        def update(self, cut_scene_manager):

            if self.rect.centerx > 399:
                cut_scene_manager.start_cut_scene(CutSceneEight(self))

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
                    credits()
        # Update objects
        player.update(cut_scene_manager)
        cut_scene_manager.update()

        # Draw objects
        screen.fill((0, 0, 0))
        draw_text('Press [c] to proceed to Credits', font, (255, 255, 255), screen, 20, 20)
        player.draw(screen)
        cut_scene_manager.draw()
        screen.blit(final_screen, (50, 90))

        pygame.display.flip()

def credits():
    running = True
    while running:
        screen.fill((0, 0, 0))

        draw_text('Credits (Press [Esc] to Return)', font, (255, 255, 255), screen, 20, 20)
        draw_text('Lead Developer: Edgar T.', font, (255, 255, 255), screen, 20, 200)
        draw_text('Lead Designer: Samantha L.', font, (255, 255, 255), screen, 20, 300)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False


        pygame.display.update()
        mainClock.tick(60)

def tutorial():
    running = True
    while running:
        screen.fill((0, 0, 0))
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

        draw_text('Tutorial (Press [Esc] to Return)', font, (255, 255, 255), screen, 20, 20)
        draw_text('Move Around Using the Arrow Keys', font, (255, 255, 255), screen, 20, 100)
        draw_text('Collect Trash to clean the Level.', font, (255, 255, 255), screen, 20, 135)
        draw_text('Once, Level is clean, you move on to the next.', font, (255, 255, 255), screen, 20, 170)
        draw_text('Avoid the Bees', font, (255, 255, 255), screen, 20, 205)
        player_move()
        pygame.display.update()
        mainClock.tick(60)
main_menu()