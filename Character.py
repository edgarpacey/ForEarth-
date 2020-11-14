import pygame

def draw_text(screen, text, size, color, x, y):
    font = pygame.font.SysFont(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    screen.blit(text_surface, text_rect)


class CutSceneOne:

    def __init__(self, player):

        # Variables
        self.name = 'test'
        self.step = 0
        self.timer = pygame.time.get_ticks()
        self.cut_scene_running = True

        # If we need to control the player while a cut scene running
        self.player = player

        # Dialogue
        self.text = {
            'one': "The Year is 2020...",
            'two': "Earth has reached to a point of ruins and is at verge of extinction...",
            'three': "Legend says if no one acts now, planet earth will not survive...",
            'four': "Will you be the savior and win the battle against pollution?",
            'five': "Will for do it...",
            'six': "For Earth!"
        }
        self.text_counter = 0

    def update(self):

        pressed = pygame.key.get_pressed()
        space = pressed[pygame.K_SPACE]

        # 1
        if self.step == 0:
            if int(self.text_counter) < len(self.text['one']):
                self.text_counter += 0.4
            else:
                if space:
                    self.text_counter = 0
                    self.step = 1

        # Two
        if self.step == 1:
            if int(self.text_counter) < len(self.text['two']):
                self.text_counter += 0.4
            else:
                if space:
                    self.text_counter = 0
                    self.step = 2

        # Three
        if self.step == 2:
            if int(self.text_counter) < len(self.text['three']):
                self.text_counter += 0.4
            else:
                if space:
                    self.text_counter = 0
                    self.step = 3

        # Three
        if self.step == 3:
            if int(self.text_counter) < len(self.text['four']):
                self.text_counter += 0.4
            else:
                if space:
                    self.text_counter = 0
                    self.step = 4

    # Three
        if self.step == 4:
            if int(self.text_counter) < len(self.text['five']):
                self.text_counter += 0.4
            else:
                if space:
                    self.text_counter = 0
                    self.step = 5

        if self.step == 5:
            if int(self.text_counter) < len(self.text['six']):
                self.text_counter += 0.4
            else:
                if space:
                    # Finish the cut scene
                    self.cut_scene_running = False

        return self.cut_scene_running

    def draw(self, screen):

        if self.step == 0:
            draw_text(
                screen,
                self.text['one'][0:int(self.text_counter)],
                25,
                (255, 255, 255),
                50,
                50
            )

        if self.step == 1:
            draw_text(
                screen,
                self.text['two'][0:int(self.text_counter)],
                25,
                (255, 255, 255),
                50,
                50
            )

        if self.step == 2:
            draw_text(
                screen,
                self.text['three'][0:int(self.text_counter)],
                25,
                (255, 255, 255),
                50,
                50
            )
        if self.step == 3:
            draw_text(
                screen,
                self.text['four'][0:int(self.text_counter)],
                25,
                (255, 255, 255),
                50,
                50
            )
        if self.step == 4:
            draw_text(
                screen,
                self.text['five'][0:int(self.text_counter)],
                25,
                (255, 255, 255),
                50,
                50
            )
        if self.step == 5:
            draw_text(
                screen,
                self.text['six'][0:int(self.text_counter)],
                25,
                (255, 255, 255),
                50,
                50
            )
class CutSceneTwo:

    def __init__(self, player):

        # Variables
        self.name = 'test'
        self.step = 0
        self.timer = pygame.time.get_ticks()
        self.cut_scene_running = True

        # If we need to control the player while a cut scene running
        self.player = player

        # Dialogue
        self.text = {
            'one': "Hello Newcomer...",
            'two': "[It appears that the floor is talking to you.]",
            'three': "It's me, mother-nature.",
            'four': "Mother-Nature: It's been a while I seen someone pick up this trash, you've revived me..",
            'five': "Mother-Nature: If you keep it, you can save me and the world.",
            'six': "Mother-Nature: Let's see your progress so far..."
        }
        self.text_counter = 0

    def update(self):

        pressed = pygame.key.get_pressed()
        space = pressed[pygame.K_SPACE]

        # 1
        if self.step == 0:
            if int(self.text_counter) < len(self.text['one']):
                self.text_counter += 0.4
            else:
                if space:
                    self.text_counter = 0
                    self.step = 1

        # Two
        if self.step == 1:
            if int(self.text_counter) < len(self.text['two']):
                self.text_counter += 0.4
            else:
                if space:
                    self.text_counter = 0
                    self.step = 2

        # Three
        if self.step == 2:
            if int(self.text_counter) < len(self.text['three']):
                self.text_counter += 0.4
            else:
                if space:
                    self.text_counter = 0
                    self.step = 3

        # Three
        if self.step == 3:
            if int(self.text_counter) < len(self.text['four']):
                self.text_counter += 0.4
            else:
                if space:
                    self.text_counter = 0
                    self.step = 4

    # Three
        if self.step == 4:
            if int(self.text_counter) < len(self.text['five']):
                self.text_counter += 0.4
            else:
                if space:
                    self.text_counter = 0
                    self.step = 5

        if self.step == 5:
            if int(self.text_counter) < len(self.text['six']):
                self.text_counter += 0.4
            else:
                if space:
                    # Finish the cut scene
                    self.cut_scene_running = False

        return self.cut_scene_running

    def draw(self, screen):

        if self.step == 0:
            draw_text(
                screen,
                self.text['one'][0:int(self.text_counter)],
                25,
                (255, 255, 255),
                50,
                50
            )

        if self.step == 1:
            draw_text(
                screen,
                self.text['two'][0:int(self.text_counter)],
                25,
                (255, 255, 255),
                50,
                50
            )

        if self.step == 2:
            draw_text(
                screen,
                self.text['three'][0:int(self.text_counter)],
                25,
                (255, 255, 255),
                50,
                50
            )
        if self.step == 3:
            draw_text(
                screen,
                self.text['four'][0:int(self.text_counter)],
                25,
                (255, 255, 255),
                50,
                50
            )
        if self.step == 4:
            draw_text(
                screen,
                self.text['five'][0:int(self.text_counter)],
                25,
                (255, 255, 255),
                50,
                50
            )
        if self.step == 5:
            draw_text(
                screen,
                self.text['six'][0:int(self.text_counter)],
                25,
                (255, 255, 255),
                50,
                50
            )

class CutSceneThree:

    def __init__(self, player):

        # Variables
        self.name = 'test'
        self.step = 0
        self.timer = pygame.time.get_ticks()
        self.cut_scene_running = True

        # If we need to control the player while a cut scene running
        self.player = player

        # Dialogue
        self.text = {
            'one': "Mother-Nature: Well, that's not much of a change...",
            'two': "Mother-Nature: Don't be discouraged, things don't change as quick as a snap.",
            'three': "Mother-Nature: Keep going, I'm sure something will change eventually.",
            'four': "Mother-Nature: Also, be careful of bees...",
            'five': "Mother-Nature: Since they lost their homes, they are aggravated.",
        }
        self.text_counter = 0

    def update(self):

        pressed = pygame.key.get_pressed()
        space = pressed[pygame.K_SPACE]

        # 1
        if self.step == 0:
            if int(self.text_counter) < len(self.text['one']):
                self.text_counter += 0.4
            else:
                if space:
                    self.text_counter = 0
                    self.step = 1

        # Two
        if self.step == 1:
            if int(self.text_counter) < len(self.text['two']):
                self.text_counter += 0.4
            else:
                if space:
                    self.text_counter = 0
                    self.step = 2

        # Three
        if self.step == 2:
            if int(self.text_counter) < len(self.text['three']):
                self.text_counter += 0.4
            else:
                if space:
                    self.text_counter = 0
                    self.step = 3

        # Three
        if self.step == 3:
            if int(self.text_counter) < len(self.text['four']):
                self.text_counter += 0.4
            else:
                if space:
                    self.text_counter = 0
                    self.step = 4

        if self.step == 4:
            if int(self.text_counter) < len(self.text['five']):
                self.text_counter += 0.4
            else:
                if space:
                    # Finish the cut scene
                    self.cut_scene_running = False

        return self.cut_scene_running

    def draw(self, screen):

        if self.step == 0:
            draw_text(
                screen,
                self.text['one'][0:int(self.text_counter)],
                25,
                (255, 255, 255),
                50,
                50
            )

        if self.step == 1:
            draw_text(
                screen,
                self.text['two'][0:int(self.text_counter)],
                25,
                (255, 255, 255),
                50,
                50
            )

        if self.step == 2:
            draw_text(
                screen,
                self.text['three'][0:int(self.text_counter)],
                25,
                (255, 255, 255),
                50,
                50
            )
        if self.step == 3:
            draw_text(
                screen,
                self.text['four'][0:int(self.text_counter)],
                25,
                (255, 255, 255),
                50,
                50
            )
        if self.step == 4:
            draw_text(
                screen,
                self.text['five'][0:int(self.text_counter)],
                25,
                (255, 255, 255),
                50,
                50
            )
        if self.step == 5:
            draw_text(
                screen,
                self.text['six'][0:int(self.text_counter)],
                25,
                (255, 255, 255),
                50,
                50
            )

class CutSceneFour:

    def __init__(self, player):

        # Variables
        self.name = 'test'
        self.step = 0
        self.timer = pygame.time.get_ticks()
        self.cut_scene_running = True

        # If we need to control the player while a cut scene running
        self.player = player

        # Dialogue
        self.text = {
            'one': "Hey, you've restored 25% of Earth!",
            'two': "I told you it will eventually happen!",
            'three': "Keep it up! You save the world in no time!",
        }
        self.text_counter = 0

    def update(self):

        pressed = pygame.key.get_pressed()
        space = pressed[pygame.K_SPACE]

        # 1
        if self.step == 0:
            if int(self.text_counter) < len(self.text['one']):
                self.text_counter += 0.4
            else:
                if space:
                    self.text_counter = 0
                    self.step = 1

        # Two
        if self.step == 1:
            if int(self.text_counter) < len(self.text['two']):
                self.text_counter += 0.4
            else:
                if space:
                    self.text_counter = 0
                    self.step = 2

        if self.step == 2:
            if int(self.text_counter) < len(self.text['three']):
                self.text_counter += 0.4
            else:
                if space:
                    # Finish the cut scene
                    self.cut_scene_running = False

        return self.cut_scene_running

    def draw(self, screen):

        if self.step == 0:
            draw_text(
                screen,
                self.text['one'][0:int(self.text_counter)],
                25,
                (255, 255, 255),
                50,
                50
            )

        if self.step == 1:
            draw_text(
                screen,
                self.text['two'][0:int(self.text_counter)],
                25,
                (255, 255, 255),
                50,
                50
            )
        if self.step == 2:
            draw_text(
                screen,
                self.text['three'][0:int(self.text_counter)],
                25,
                (255, 255, 255),
                50,
                50
            )

class CutSceneFive:

    def __init__(self, player):

        # Variables
        self.name = 'test'
        self.step = 0
        self.timer = pygame.time.get_ticks()
        self.cut_scene_running = True

        # If we need to control the player while a cut scene running
        self.player = player

        # Dialogue
        self.text = {
            'one': "Mother-Nature: Hey, you've restored 50% of Earth!",
            'two': "Mother-Nature: You could be...",
            'three': "Mother-Nature: Nevermind...",
            'four': "Mother-Nature: Those bees still going rampage!",
            'five': "Mother-Nature: Good Luck.",
        }
        self.text_counter = 0

    def update(self):

        pressed = pygame.key.get_pressed()
        space = pressed[pygame.K_SPACE]

        # 1
        if self.step == 0:
            if int(self.text_counter) < len(self.text['one']):
                self.text_counter += 0.4
            else:
                if space:
                    self.text_counter = 0
                    self.step = 1

        # Two
        if self.step == 1:
            if int(self.text_counter) < len(self.text['two']):
                self.text_counter += 0.4
            else:
                if space:
                    self.text_counter = 0
                    self.step = 2

        # Three
        if self.step == 2:
            if int(self.text_counter) < len(self.text['three']):
                self.text_counter += 0.4
            else:
                if space:
                    self.text_counter = 0
                    self.step = 3

        # Three
        if self.step == 3:
            if int(self.text_counter) < len(self.text['four']):
                self.text_counter += 0.4
            else:
                if space:
                    self.text_counter = 0
                    self.step = 4

        if self.step == 4:
            if int(self.text_counter) < len(self.text['five']):
                self.text_counter += 0.4
            else:
                if space:
                    # Finish the cut scene
                    self.cut_scene_running = False

        return self.cut_scene_running

    def draw(self, screen):

        if self.step == 0:
            draw_text(
                screen,
                self.text['one'][0:int(self.text_counter)],
                25,
                (255, 255, 255),
                50,
                50
            )

        if self.step == 1:
            draw_text(
                screen,
                self.text['two'][0:int(self.text_counter)],
                25,
                (255, 255, 255),
                50,
                50
            )

        if self.step == 2:
            draw_text(
                screen,
                self.text['three'][0:int(self.text_counter)],
                25,
                (255, 255, 255),
                50,
                50
            )
        if self.step == 3:
            draw_text(
                screen,
                self.text['four'][0:int(self.text_counter)],
                25,
                (255, 255, 255),
                50,
                50
            )
        if self.step == 4:
            draw_text(
                screen,
                self.text['five'][0:int(self.text_counter)],
                25,
                (255, 255, 255),
                50,
                50
            )
        if self.step == 5:
            draw_text(
                screen,
                self.text['six'][0:int(self.text_counter)],
                25,
                (255, 255, 255),
                50,
                50
            )

class CutSceneSix:

    def __init__(self, player):

        # Variables
        self.name = 'test'
        self.step = 0
        self.timer = pygame.time.get_ticks()
        self.cut_scene_running = True

        # If we need to control the player while a cut scene running
        self.player = player

        # Dialogue
        self.text = {
            'one': "Mother-Nature: Hey, you've restored 75% of Earth!",
            'two': "Mother-Nature: Almost There!",
            'three': "Mother-Nature: Just Need the finishing touches..",
            'four': "Mother-Nature: Also good news, the bees are not hostile anymore!",
            'five': "Mother-Nature: You recovered their homes, they thank you.",
        }
        self.text_counter = 0

    def update(self):

        pressed = pygame.key.get_pressed()
        space = pressed[pygame.K_SPACE]

        # 1
        if self.step == 0:
            if int(self.text_counter) < len(self.text['one']):
                self.text_counter += 0.4
            else:
                if space:
                    self.text_counter = 0
                    self.step = 1

        # Two
        if self.step == 1:
            if int(self.text_counter) < len(self.text['two']):
                self.text_counter += 0.4
            else:
                if space:
                    self.text_counter = 0
                    self.step = 2

        # Three
        if self.step == 2:
            if int(self.text_counter) < len(self.text['three']):
                self.text_counter += 0.4
            else:
                if space:
                    self.text_counter = 0
                    self.step = 3

        # Three
        if self.step == 3:
            if int(self.text_counter) < len(self.text['four']):
                self.text_counter += 0.4
            else:
                if space:
                    self.text_counter = 0
                    self.step = 4

        if self.step == 4:
            if int(self.text_counter) < len(self.text['five']):
                self.text_counter += 0.4
            else:
                if space:
                    # Finish the cut scene
                    self.cut_scene_running = False

        return self.cut_scene_running

    def draw(self, screen):

        if self.step == 0:
            draw_text(
                screen,
                self.text['one'][0:int(self.text_counter)],
                25,
                (255, 255, 255),
                50,
                50
            )

        if self.step == 1:
            draw_text(
                screen,
                self.text['two'][0:int(self.text_counter)],
                25,
                (255, 255, 255),
                50,
                50
            )

        if self.step == 2:
            draw_text(
                screen,
                self.text['three'][0:int(self.text_counter)],
                25,
                (255, 255, 255),
                50,
                50
            )
        if self.step == 3:
            draw_text(
                screen,
                self.text['four'][0:int(self.text_counter)],
                25,
                (255, 255, 255),
                50,
                50
            )
        if self.step == 4:
            draw_text(
                screen,
                self.text['five'][0:int(self.text_counter)],
                25,
                (255, 255, 255),
                50,
                50
            )
        if self.step == 5:
            draw_text(
                screen,
                self.text['six'][0:int(self.text_counter)],
                25,
                (255, 255, 255),
                50,
                50
            )

class CutSceneSeven:

    def __init__(self, player):

        # Variables
        self.name = 'test'
        self.step = 0
        self.timer = pygame.time.get_ticks()
        self.cut_scene_running = True

        # If we need to control the player while a cut scene running
        self.player = player

        # Dialogue
        self.text = {
            'one': "Mother-Nature: Hey, you've restored 100% of Earth!",
            'two': "Mother-Nature: You did it, you saved Planet Earth",
            'three': "Mother-Nature: Now, I think this place needs some final touches...",
        }
        self.text_counter = 0

    def update(self):

        pressed = pygame.key.get_pressed()
        space = pressed[pygame.K_SPACE]

        # 1
        if self.step == 0:
            if int(self.text_counter) < len(self.text['one']):
                self.text_counter += 0.4
            else:
                if space:
                    self.text_counter = 0
                    self.step = 1

        # Two
        if self.step == 1:
            if int(self.text_counter) < len(self.text['two']):
                self.text_counter += 0.4
            else:
                if space:
                    self.text_counter = 0
                    self.step = 2

        if self.step == 2:
            if int(self.text_counter) < len(self.text['three']):
                self.text_counter += 0.4
            else:
                if space:
                # Finish the cut scene
                    self.cut_scene_running = False

        return self.cut_scene_running

    def draw(self, screen):

        if self.step == 0:
            draw_text(
                screen,
                self.text['one'][0:int(self.text_counter)],
                25,
                (255, 255, 255),
                50,
                50
            )

        if self.step == 1:
            draw_text(
                screen,
                self.text['two'][0:int(self.text_counter)],
                25,
                (255, 255, 255),
                50,
                50
            )

        if self.step == 2:
            draw_text(
                screen,
                self.text['three'][0:int(self.text_counter)],
                25,
                (255, 255, 255),
                50,
                50
            )

class CutSceneEight:

    def __init__(self, player):

        # Variables
        self.name = 'test'
        self.step = 0
        self.timer = pygame.time.get_ticks()
        self.cut_scene_running = True

        # If we need to control the player while a cut scene running
        self.player = player

        # Dialogue
        self.text = {
            'one': "Mother-Nature: Nature is back into business!",
            'two': "Mother-Nature: All because of you Player!",
            'three': "Mother-Nature: Now, I need to give you a message player",
            'four': "I don't want your world to end up like mine did",
            'five': "Clean up after yourself, it's as simple as this game",
            'six': "Do it, For Earth!",
            'seven': "ROLL THE CREDITS"
        }
        self.text_counter = 0

    def update(self):

        pressed = pygame.key.get_pressed()
        space = pressed[pygame.K_SPACE]

        # 1
        if self.step == 0:
            if int(self.text_counter) < len(self.text['one']):
                self.text_counter += 0.4
            else:
                if space:
                    self.text_counter = 0
                    self.step = 1

        # Two
        if self.step == 1:
            if int(self.text_counter) < len(self.text['two']):
                self.text_counter += 0.4
            else:
                if space:
                    self.text_counter = 0
                    self.step = 2

        if self.step == 2:
            if int(self.text_counter) < len(self.text['three']):
                self.text_counter += 0.4
            else:
                if space:
                    self.text_counter = 0
                    self.step = 3

        if self.step == 3:
            if int(self.text_counter) < len(self.text['four']):
                self.text_counter += 0.4
            else:
                if space:
                    self.text_counter = 0
                    self.step = 4

        if self.step == 4:
            if int(self.text_counter) < len(self.text['five']):
                self.text_counter += 0.4
            else:
                if space:
                    self.text_counter = 0
                    self.step = 5

        if self.step == 5:
            if int(self.text_counter) < len(self.text['six']):
                self.text_counter += 0.4
            else:
                if space:
                    self.text_counter = 0
                    self.step = 6

        if self.step == 6:
            if int(self.text_counter) < len(self.text['seven']):
                self.text_counter += 0.4
            else:
                if space:
                # Finish the cut scene
                    self.cut_scene_running = False

        return self.cut_scene_running

    def draw(self, screen):

        if self.step == 0:
            draw_text(
                screen,
                self.text['one'][0:int(self.text_counter)],
                25,
                (255, 255, 255),
                50,
                50
            )

        if self.step == 1:
            draw_text(
                screen,
                self.text['two'][0:int(self.text_counter)],
                25,
                (255, 255, 255),
                50,
                50
            )

        if self.step == 2:
            draw_text(
                screen,
                self.text['three'][0:int(self.text_counter)],
                25,
                (255, 255, 255),
                50,
                50
            )

        if self.step == 3:
            draw_text(
                screen,
                self.text['four'][0:int(self.text_counter)],
                25,
                (255, 255, 255),
                50,
                50
            )
        if self.step == 4:
            draw_text(
                screen,
                self.text['five'][0:int(self.text_counter)],
                25,
                (255, 255, 255),
                50,
                50
            )
        if self.step == 5:
            draw_text(
                screen,
                self.text['six'][0:int(self.text_counter)],
                25,
                (255, 255, 255),
                50,
                50
            )
        if self.step == 6:
            draw_text(
                screen,
                self.text['seven'][0:int(self.text_counter)],
                25,
                (255, 255, 255),
                50,
                50
            )
class CutSceneManager:

    def __init__(self, screen):
        self.cut_scenes_complete = []
        self.cut_scene = None
        self.cut_scene_running = False

        # Drawing variables
        self.screen = screen
        self.window_size = 0

    def start_cut_scene(self, cut_scene):
        if cut_scene.name not in self.cut_scenes_complete:
            self.cut_scenes_complete.append(cut_scene.name)
            self.cut_scene = cut_scene
            self.cut_scene_running = True

    def end_cut_scene(self):
        self.cut_scene = None
        self.cut_scene_running = False

    def update(self):

        if self.cut_scene_running:
            if self.window_size < self.screen.get_height() * 0.3: self.window_size += 2
            self.cut_scene_running = self.cut_scene.update()
        else:
            self.end_cut_scene()

    def draw(self):
        if self.cut_scene_running:
            # Draw rect generic to all cut scenes
            pygame.draw.rect(self.screen, (0, 0, 0), (0, 0, self.screen.get_width(), self.window_size))
            # Draw specific cut scene details
            self.cut_scene.draw(self.screen)