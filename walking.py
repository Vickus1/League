import pygame, sys, time, random
from pygame.locals import *
import os
import textforbaby

pygame.init()
HEIGHT = 460
WIDTH = 780
FPS = 30

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption("Baby's Christmas Gift")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# set up the assets (music and file for games)
# 1. gives the folder name of where this script is located
if True:
    game_folder = os.path.dirname(__file__)
    print (game_folder)
    img_folder = os.path.join(game_folder, "img")
    print (img_folder)
    img_folder2 = os.path.join(game_folder, "C:\\Users\Victor\Downloads\p1_fullwalk")
    print (img_folder2)
    img_folder3 = os.path.join(game_folder, "C:\\Users\Victor\Downloads\p3_walk")
    global lists
    lists = os.listdir('C:\\Users\Victor\Downloads\p1_fullwalk')

    for i in range(len(lists)):
        lists[i] = str(lists[i])

class FpsClock:
    def __init__(self):
        self.frame_duration = 0.000
        self.this_frame_time = 0
        self.last_frame_time = 0
        return

    def tick(self):
        "Call this every frame"
        self.this_frame_time = self.get_current_time()
        self.frame_duration = (self.this_frame_time - self.last_frame_time) / 1000.000
        self.last_frame_time = self.this_frame_time
        return

    def get_frame_duration(self):
        "Returns the length of the previous frame, in seconds"
        return self.frame_duration

    def get_current_time(self):
        "Used internally. Returns current time in ms."
        return pygame.time.get_ticks()

    def begin(self):
        "Starts/restarts the timer. Call just before your main loop."
        self.last_frame_time = self.get_current_time()
        return

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # Create an image of the block and fill it with color
        # Could also be an image loaded
        self.image = pygame.image.load(os.path.join(img_folder2, 'p1_walk01.png')).convert()
        self.image.set_colorkey(BLACK)
        #self.image = pygame.transform.scale(self.image, (20, 30))
        # Gets the rectangle object that has the dimensions of the image
        # Updates position by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()
        self.radius = 25
        pygame.draw.circle = (SCREEN, RED, self.rect.centerx, self.radius)
        self.rect.centerx = 480/2
        self.rect.bottom = 460 - 10
        self.speedx = 0
        self.count = 0
        self.jump = 10
        # True for right, False for left
        self.flag = True

    def update(self):
        global lists
        self.rect.bottom = 460 - 10
        self.speedx = 0
        if self.flag == True:
            self.image = pygame.image.load(os.path.join(img_folder2, lists[self.count])).convert()
            self.image.set_colorkey(BLACK)
        else:
            self.image = pygame.image.load(os.path.join(img_folder2, lists[self.count])).convert()
            self.image = pygame.transform.flip(self.image, True, False)
            self.image.set_colorkey(BLACK)
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT] and self.count < 10:
            self.speedx = -7
            self.count += 1
            self.flag = False
            self.image.set_colorkey(BLACK)
        if keystate[pygame.K_RIGHT] and self.count < 10:
            self.speedx = 7
            self.count += 1
            self.flag = True
            self.image.set_colorkey(BLACK)
        if keystate[pygame.K_DOWN]:
            self.image = pygame.image.load(os.path.join(img_folder2, lists[-2])).convert()
            self.image.set_colorkey(BLACK)
            self.rect.bottom = 460 + 15
        if keystate[pygame.K_SPACE]:
            while self.jump > 0:
                self.rect.y -= self.jump
                self.jump -= 1
                print (self.jump)
        if self.count == 10:
            self.count = 0
        self.rect.x += self.speedx
        if self.rect.right > 480:
            self.rect.right = 480
        elif self.rect.left < 0:
            self.rect.left = 0

class baby(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder3, 'p3_walk02.png')).convert()
        self.image.set_colorkey(BLACK)
        self.image = pygame.transform.scale(self.image, (50, 65))
        self.image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()
        self.rect.bottom = 460 - 10
        self.rect.x = 480 - 480/4 - 45
        self.speedx = -0.1

    def update(self):
        self.speedx = -0
        self.rect.bottom = 460 - 10
        self.rect.x += self.speedx
        if self.rect.x <= 0:
            self.rect.x = 480 - 480/4


font_name = pygame.font.match_font('arial')
def draw_text1(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    if type(text) == str:
        text_surface = font.render(text, False, RED)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (x, y)
        return text_rect
    else:
        text_surface = font.render(text[0], False, RED)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (x, 2*y)
        return text_rect

def draw_text2(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    if type(text)==str:
        text_surface = font.render(text, False, RED)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (x, y)
        surf.blit(text_surface, text_rect)
    else:
        text_surface1 = font.render(text[0], False, RED)
        text_rect1 = text_surface1.get_rect()
        text_rect1.topleft = (x+60, y-60)
        text_surface2 = font.render(text[1], False, RED)
        text_rect2 = text_surface2.get_rect()
        text_rect2.topleft = (x+60, y-30)
        surf.blit(text_surface1, text_rect1)
        surf.blit(text_surface2, text_rect2)

def draw_bubble(surf, x, y, sizex, sizey, boolx):
    bubble = pygame.image.load(os.path.join(img_folder3, 'comic-2.png')).convert_alpha()

    if sizey ==65:
        bubble_recty = y
        bubble_rectx = x
    else:
        bubble_recty = y-60
        bubble_rectx = x+60
    bubble = pygame.transform.scale(bubble, (sizex+20, sizey))
    bubble = pygame.transform.flip(bubble, boolx, False)
    surf.blit(bubble, (bubble_rectx, bubble_recty))

if True:
    all_sprites = pygame.sprite.Group()
    player1 = Player()
    babycy = baby()
    mobs = pygame.sprite.Group()
    all_sprites.add(player1, babycy)

    background = pygame.image.load(os.path.join(img_folder, 'blue.png')).convert()
    background_rect = background.get_rect()
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))

    timer = FpsClock()
    clockuuu = pygame.time.Clock()
    running = True
    timer.begin()
    tick_time = 0
i = 0
talk = ""
while running:
    clockuuu.tick(FPS)
    for event in pygame.event.get():
        if event.type == QUIT :
            sys.exit()
            pygame.quit()
            running = False
        if event.type == KEYDOWN:
             if event.key == K_a:
                i = i+1
                talk = textforbaby.chooseText(i)
            #updating

    # tick_interval = 0.500
    #
    # tick_time += timer.get_frame_duration()
    # #print (tick_time)
    # if tick_time > tick_interval:
    #     babycy.speedx = 0
    #
    # timer.tick()
    all_sprites.update()
    SCREEN.blit(background, background_rect)
    all_sprites.draw(SCREEN)

    if i%2 == 1:
        me = draw_text1(SCREEN, talk, 20, 60, 290)
        #print (me[2])
        if type(talk)==str:
            draw_bubble(SCREEN, 480/2 - 190, 460/2 + 50, me[2], 65, False)
            draw_text2(SCREEN, talk, 20, 60, 290)
        else:
            draw_bubble(SCREEN, 480/2 - 190, 460/2 + 50, me[2]+20, 65*2, False)
            draw_text2(SCREEN, talk, 20, 60, 290)

    elif i == 0:
        pass
    elif i%2 == 0:
        #baby's bubble
        me2 = draw_text1(SCREEN, talk, 20, 480 - 160, 460 - 130)
        print (me2[2])
        draw_bubble(SCREEN, 480 - 480/4 - 50, 460 - 140, me2[2], 65, True)
        draw_text2(SCREEN, talk, 20, 480 - 160, 460 - 130)

    pygame.display.flip()
