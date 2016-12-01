import pygame, sys, time, random
from pygame.locals import *
import os

pygame.init()
HEIGHT = 460
WIDTH = 480
FPS = 30

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption('Test3')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# set up the assets (music and file for games)
# 1. gives the folder name of where this script is located
game_folder = os.path.dirname(__file__)
print (game_folder)
img_folder = os.path.join(game_folder, "img")
print (img_folder)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # Create an image of the block and fill it with color
        # Could also be an image loaded
        self.image = pygame.image.load(os.path.join(img_folder, 'playerShip1_blue.png')).convert()
        self.image.set_colorkey(BLACK)
        self.image = pygame.transform.scale(self.image, (20, 30))
        # Gets the rectangle object that has the dimensions of the image
        # Updates position by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -7
        if keystate[pygame.K_RIGHT]:
            self.speedx = 7
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        elif self.rect.left < 0:
            self.rect.left = 0

# class baby(pygame.sprite.Sprite):
#     def __init__(self):
#         pygame.sprite.Sprite.__init__(self)
#         self.image = pygame.image.load(os.path.join(img_folder, 'p3_walk01.png')).convert()
#         self.image.set_colorkey(BLACK)
#         self.image = pygame.transform.scale(self.image, (20, 30))
#         self.rect = self.image.get_rect()
#         self.rect.centerx = WIDTH/4
#         self.rect.bottom = HEIGHT - 10



class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, 'meteorGrey_big2.png')).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.top = 5
        #self.rect.centerx = WIDTH/2
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(-10, 0)
        self.speedx = random.randrange(-3,3)
        self.speedy = random.randrange(2,7)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy/10
        if self.rect.bottom > HEIGHT:
            self.rect.top = 0
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, player_x, player_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, 'laserBlue16.png')).convert()
        self.image = pygame.transform.scale(self.image, (5, 15))
        self.rect = self.image.get_rect()
        self.rect.centerx = player_x
        self.rect.bottom = player_y
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()

all_sprites = pygame.sprite.Group()
player1 = Player()
#Babycy = baby()
mobs = pygame.sprite.Group()
all_sprites.add(player1)
bullets = pygame.sprite.Group()

for i in range(3):
    m = Mob()
    mobs.add(m)
    all_sprites.add(m)
font_name = pygame.font.match_font('arial')

def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, False, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

background = pygame.image.load(os.path.join(img_folder, 'blue.png')).convert()
background_rect = background.get_rect()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

clock = pygame.time.Clock()
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
            pygame.quit()
            running = False
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                bullet1 = Bullet(player1.rect.centerx-12, player1.rect.y)
                bullet2 = Bullet(player1.rect.centerx+12, player1.rect.y)
                all_sprites.add(bullet1, bullet2)
                bullets.add(bullet1, bullet2)

            #updating
    all_sprites.update()

        # pygame.sprite.spritecollide(player1, mobs, False)
    bullet_hit = pygame.sprite.groupcollide(bullets, mobs, True, True)
    if bullet_hit:
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)

        # SCREEN.fill(BLACK)
    SCREEN.blit(background, background_rect)
    all_sprites.draw(SCREEN)
    draw_text(SCREEN, 'HELLO', 18, WIDTH / 2, 10)
    draw_text(SCREEN, 'bbrbrbrb', 26, WIDTH/2, 50)
    pygame.display.flip()
