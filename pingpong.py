import pygame

pygame.init()
screen = pygame.display.set_mode((750, 500))
pygame.display.set_caption("Ping-pong")

paddle1points = 0
paddle2points = 0


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
        self.dx = 1
        self.dy = 1
        self.speed = 1


paddle1 = Paddle()
paddle2 = Paddle()
pong = Ball()
paddle1.rect.x = 25
paddle1.rect.y = 250
paddle2.rect.x = 715
paddle2.rect.y = 250
pong.rect.x = 375
pong.rect.y = 250

characters = pygame.sprite.Group()
characters.add(paddle1, paddle2, pong)


def redraw():
    global screen
    pygame.display.update()
    screen.fill((0, 0, 0))
    characters.draw(surface=screen)


class Run:
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

        pong.rect.x += pong.speed * pong.dx
        pong.rect.y += pong.speed * pong.dy

        # Wall and Paddle Bounces
        if pong.rect.y > 490:
            pong.dy = -1

        if pong.rect.y < 1:
            pong.dy = 1

        if pong.rect.x > 740:
            pong.rect.x, pong.rect.y = 375, 250
            pong.dx = -1
            paddle1.points += 1

        if pong.rect.x < 1:
            pong.rect.x, pong.rect.y = 375, 250
            pong.dx = 1
            paddle2.points += 1

        if paddle1.rect.colliderect(pong.rect):
             pong.dx = 1

        if paddle2.rect.colliderect(pong.rect):
            pong.dx = -1

        # Runs redraw function above
        redraw()
    pygame.quit()
    print("player1 = ", paddle1.points)
    print("player2 = ", paddle2.points)
