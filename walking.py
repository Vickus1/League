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
    img_folder = os.path.join(game_folder, "assets")
    dirlist = os.listdir(img_folder)[5:8:1]
    print (dirlist)
##    img_folder2 = os.path.join(game_folder, "C:\\Users\Victor\Downloads\p1_fullwalk")
##    print (img_folder2)
##    img_folder3 = os.path.join(game_folder, "C:\\Users\Victor\Downloads\p3_walk")
##    global lists
##    lists = os.listdir('C:\\Users\Victor\Downloads\p1_fullwalk')

##    for i in range(len(lists)):
##        lists[i] = str(lists[i])
    #lists = list()
    #lists[0] =

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
    def __init__(self, rr, p1list):
        pygame.sprite.Sprite.__init__(self)
        # Create an image of the block and fill it with color
        # Could also be an image loaded
        self.list = p1list
        self.image = pygame.image.load(os.path.join(img_folder, self.list[0])).convert_alpha()
        self.image.set_colorkey(BLACK)
        #self.image = pygame.transform.scale(self.image, (20, 30))
        # Gets the rectangle object that has the dimensions of the image
        # Updates position by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()
        self.radius = rr
        pygame.draw.circle = (SCREEN, RED, self.rect.centerx, self.radius)
        self.rect.centerx = 480/2
        self.rect.bottom = 460 - 10
        self.speedx = 0
        self.count = 0
        self.jump = 10
        # True for right, False for left
        self.flag = True
        self.inverted = False
        self.final = False

    def update(self):
        #print (self.list[1])
        #print (self.rect.x)
        self.rect.bottom = 460 - 10
        self.speedx = 0
        #if self.flag == True:
        if self.inverted == False and self.final == False:
            self.image = pygame.image.load(os.path.join(img_folder, self.list[self.count%3])).convert()
            self.image.set_colorkey(BLACK)
        elif self.inverted == True and self.final == False:
            self.image = pygame.image.load(os.path.join(img_folder, self.list[self.count%3])).convert()
            self.image.set_colorkey(BLACK)
            self.image = pygame.transform.flip(self.image, True, False)
##        else:
##            self.image = pygame.image.load(os.path.join(img_folder, lists[self.count])).convert()
##            self.image = pygame.transform.flip(self.image, True, False)
##            self.image.set_colorkey(BLACK)
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_RIGHT]:
            self.flag = False
        if keystate[pygame.K_LEFT]:
            self.inverted = True
            self.flag = False

        if self.rect.x > WIDTH - 300 and self.inverted == False:
            self.flag = True
##        if keystate[pygame.K_LEFT] and self.count < 10:
##            self.speedx = -7
##            self.count += 1
##            self.flag = False
##            self.image.set_colorkey(BLACK)
        #if keystate[pygame.K_RIGHT]:
        if self.flag == False:
            pygame.time.delay(100)
            self.speedx = 9
            self.count += 1
            self.image.set_colorkey(BLACK)
            if self.inverted == True:
                self.speedx = -9
                if self.rect.x < 350:
                    self.speedx = 0
                    self.final = True


##        if keystate[pygame.K_DOWN]:
##            self.image = pygame.image.load(os.path.join(img_folder2, lists[-2])).convert()
##            self.image.set_colorkey(BLACK)
##            self.rect.bottom = 460 + 15
##        if keystate[pygame.K_SPACE]:
##            while self.jump > 0:
##                self.rect.y -= self.jump
##                self.jump -= 1
##                print (self.jump)
##        if self.count == 10:
##            self.count = 0
##        self.rect.x += self.speedx
##        if self.rect.right > 480:
##            self.rect.right = 480
##        elif self.rect.left < 0:
##            self.rect.left = 0
        #self.speedx = -0
        self.rect.bottom = 460 - 10
        self.rect.x += self.speedx
        if self.rect.x <= 0:
            self.rect.x = 480 - 480/4

class baby(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, 'p2.png')).convert_alpha()
        self.image.set_colorkey(BLACK)
        self.image = pygame.transform.scale(self.image, (50, 65))
        self.image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()
        self.rect.bottom = 460 - 10
        self.rect.x = 480 - 480/4 - 45
        self.speedx = -0.1
        self.final = False
        self.counter = 0

    def update(self):
        if self.final == True and self.counter == 0:
            self.image = pygame.transform.flip(self.image, True, False)
            self.counter += 1
        self.speedx = -0
        self.rect.bottom = 460 - 10
        #self.rect.x += self.speedx
        #if self.rect.x <= 0:
        #    self.rect.x = 480 - 480/4

class sami(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, 'p3.png')).convert_alpha()
        self.image.set_colorkey(BLACK)
        self.image = pygame.transform.scale(self.image, (50, 65))
        self.image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()
        self.rect.bottom = 460 - 10
        self.rect.x = WIDTH - 100
        self.speedx = -0.1

    def update(self):
        self.speedx = -0
        self.rect.bottom = 460 - 10
        self.rect.x += self.speedx
        if self.rect.x <= 0:
            self.rect.x = 480 - 480/4

class Bullet(pygame.sprite.Sprite):
    def __init__(self, player_x, player_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, 'laserGreen10.png')).convert()
        self.image = pygame.transform.scale(self.image, (5, 15))
        self.image = pygame.transform.rotate(self.image, 90)
        self.rect = self.image.get_rect()
        self.rect.centerx = player_x
        self.rect.bottom = player_y
        self.speedy = 20

    def update(self):
        self.rect.x += self.speedy
        if self.rect.bottom < 0:
            self.kill()

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

def drawheart(surf):
    heartrect = pygame.image.load(os.path.join(img_folder, 'heart.png')).convert_alpha()
    #samirect = pygame.transform.flip(samirect, True, False)
    heart_rectx = WIDTH - 450
    heart_recty = varheight - 20
    surf.blit(heartrect, (heart_rectx, heart_recty))

def draw_bubble(surf, x, y, sizex, sizey, boolx):
    bubble = pygame.image.load(os.path.join(img_folder, 'comic-2.png')).convert_alpha()

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
    player1 = Player(25, dirlist)
    babycy = baby()
    samicy = sami()
    mobs = pygame.sprite.Group()
    mobs.add(samicy)
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
counter = 0
varheight = HEIGHT-100
while running:
    clockuuu.tick(FPS)
    for event in pygame.event.get():
        if event.type == QUIT :
            sys.exit()
            pygame.quit()
            running = False
        if event.type == KEYDOWN:
            if event.key == K_a:
                if i<19:
                    i = i+1
                if i < 11:
                    talk = textforbaby.chooseText(i)
                else:
                    talk = textforbaby.withSami(i)
            elif event.key == K_ESCAPE:
                sys.exit()
                pygame.quit()
                running = False

            elif event.key == K_SPACE:
                i += 1
                bullet1 = Bullet(player1.rect.centerx, player1.rect.y+36)
                bullet2 = Bullet(player1.rect.centerx, player1.rect.y+24)
                all_sprites.add(bullet1, bullet2)
                #bullets.add(bullet1, bullet2)

    #print (i)
    all_sprites.update()
    SCREEN.blit(background, background_rect)
    all_sprites.draw(SCREEN)
    bullet_hit = pygame.sprite.groupcollide(all_sprites, mobs, True, True)
    #print (bullet_hit)
    if player1.final == True:
        draw_text2(SCREEN, "KISS", 30, WIDTH-400, HEIGHT-130)
        drawheart(SCREEN)
        babycy.final = True

    if i%2 == 1 and i<11:
        me = draw_text1(SCREEN, talk, 20, 60, 290)
        #print (me[2])
        if type(talk)==str:
            draw_bubble(SCREEN, 480/2 - 190, 460/2 + 50, me[2], 65, False)
            draw_text2(SCREEN, talk, 20, 60, 290)

        else:
            draw_bubble(SCREEN, 480/2 - 190, 460/2 + 50, me[2]+20, 65*2, False)
            draw_text2(SCREEN, talk, 25, 60, 290)
    elif i==0 or i>18:
        if i>18:
            varheight = varheight - 10
            draw_text2(SCREEN, "Ahhhhh", 30, WIDTH-100, varheight)
        else:
            pass

    #sami
    elif (i%2 == 1) and (i >= 11):
        me = draw_text1(SCREEN, talk, 25, 60, 290)
        #print (me[2])
        if type(talk)==str:
            draw_bubble(SCREEN, 480+50, 460/2 + 50, me[2], 65, False)
            draw_text2(SCREEN, talk, 25, 540, 290)
            #drawsami(SCREEN)
            mobs.update()
            mobs.draw(SCREEN)
            #draw_text2(SCREEN, "Press Enter to shoot", 30, WIDTH-500, 30)
    # me vs sami
    elif i%2 == 0 and i>=11:
        me = draw_text1(SCREEN, talk, 25, 60, 290)
        #print (me[2])
        if type(talk)==str:
            draw_bubble(SCREEN, 480/2 - 150, 460/2 + 50, me[2], 65, False)
            draw_text2(SCREEN, talk, 25, 100, 290)
            #drawsami(SCREEN)
            mobs.update()
            mobs.draw(SCREEN)
            if i == 18:
                counter += 1
                if counter%10==0 or counter%10==1 or counter%10==2 or counter%10==3 or counter%10==4 or counter%10==5:
                    draw_text2(SCREEN, "Press Space to shoot", 30, WIDTH-500, 30)
                if bullet_hit:
                    draw_text2(SCREEN, "Ahhhhh", 30, WIDTH-100, HEIGHT-100)



    elif i%2 == 0 and i<11:
        #baby's bubble
        me2 = draw_text1(SCREEN, talk, 20, 480 - 160, 460 - 130)
        #print (me2[2])
        draw_bubble(SCREEN, 480 - 480/4 - 50, 460 - 140, me2[2], 65, True)
        draw_text2(SCREEN, talk, 20, 480 - 160, 460 - 130)

    pygame.display.flip()
