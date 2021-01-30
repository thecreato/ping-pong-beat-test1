import pygame

pygame.init()
screen = pygame.display.set_mode((750, 500))
pygame.display.set_caption("Ping-pong")


class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10, 75])
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.points = 0
        self.speed = 1


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10, 10])
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.dirx = 1
        self.diry = 1
        self.speed = 1


paddle1 = Paddle()
paddle2 = Paddle()
ball = Ball()
paddle1.rect.x = 25
paddle1.rect.y = 250
paddle2.rect.x = 715
paddle2.rect.y = 250
ball.rect.x = 375
ball.rect.y = 250

characters = pygame.sprite.Group()
characters.add(paddle1, paddle2, ball)


def redraw():
    global screen
    pygame.display.update()
    screen.fill((0, 0, 0))
    characters.draw(surface=screen)


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        paddle1.rect.y -= paddle1.speed
    if key[pygame.K_s]:
        paddle1.rect.y += paddle1.speed
    if key[pygame.K_UP]:
        paddle2.rect.y -= paddle2.speed
    if key[pygame.K_DOWN]:
        paddle2.rect.y += paddle2.speed
    redraw()

    ball.speed * ball.dirx
    ball.speed * ball.diry

    if ball.rect.x < 10:
        ball.dirx = 1
    if ball.rect.x > 740:
        ball.dirx = -1
    if ball.rect.y < 10:
        ball.diry = 1
    if ball.rect.y > 490:
        ball.diry = -1
