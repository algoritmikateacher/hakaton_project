#создай игру "Лабиринт"!
from pygame import *

window = display.set_mode((700, 500))
display.set_caption('лабиринт')

background = transform.scale(image.load('background.jpg'), (700, 500))
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()
game = True
clock = time.Clock()

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        elif keys[K_s] and self.rect.y < 420:
            self.rect.y += self.speed
        elif keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        elif keys[K_d] and self.rect.x < 620:
            self.rect.x += self.speed

class Enemy(GameSprite):
    direction = 'left'
    def update(self):
        if self.rect.x == 600:
            self.direction = 'left'
        if self.rect.x == 400:
            self.direction = 'right'
            
        if self.direction == 'left':
            self.rect.x -= self.speed
        if self.direction == 'right':
            self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self, color1, color2, color3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((self.color1, self.color2, self.color3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


player = Player('58485538b772315a9e4dd5d9.png', 100, 100, 5)
enemy = Enemy('cyborg.png', 500, 300, 5)
money = GameSprite('treasure.png', 600, 400, 5)
wall1 = Wall(107, 164, 255, 350, 150, 10, 350)

font.init()
font = font.Font(None, 70)
win = font.render('YOU WIN!', True, (255, 251, 0))
lose = font.render('YOU LOSER!', True, (255, 51, 0))

finish = False
money_sound = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')
while game:
    
    for e in event.get():
        if e.type == QUIT:
            game = False 
    if finish != True:
        window.blit(background, (0, 0))
        if sprite.collide_rect(player, money):
            window.blit(win, (200, 200))
            finish = True
            money_sound.play()
        if sprite.collide_rect(player, enemy) or sprite.collide_rect(player, wall1):
            window.blit(lose, (200, 200))
            finish = True
            kick.play()
        
        wall1.draw_wall()
        player.update()
        player.reset()
        enemy.update()
        enemy.reset()
        money.reset()
    clock.tick(60)
    display.update()
