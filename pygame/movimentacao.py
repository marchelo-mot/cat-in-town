import pygame, sys
import math

pygame.init()

largura_janela = 1000  
altura_janela = 800
pygame.display.set_caption('Game do Mario')
clock = pygame.time.Clock()
fgExit = False
personagemImg = pygame.image.load('cubo.png')
cenario = pygame.image.load('cenario.png')
# Set the size for the image
DEFAULT_IMAGE_SIZE = (200, 200)
escala = (1000, 800)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

  
# Scale the image to your needed size
personagemImg = pygame.transform.scale(personagemImg, DEFAULT_IMAGE_SIZE)
personagemRect = personagemImg.get_rect()
cenario = pygame.transform.scale(cenario, escala)
tela = pygame.display.set_mode((largura_janela, altura_janela))
x = (largura_janela * 0.1)
y = (altura_janela * 0.1)
x1 = 0
x2 = 0
y1 = 0
y2 = 0
personagem_speed = 0
estado_personagem = 1
xmario = x+45
ymario = y+50


x_1 = x
y_1 = y
print ('vamos la')

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((10, 5))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 5

    def update(self):
        self.rect.x += self.speed
        # Remova o tiro quando ele sair da tela
        if self.rect.left > altura_janela:
            self.kill()

bullets = pygame.sprite.Group()
        

while not fgExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fgExit = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                x1 = 0
            if event.key == pygame.K_RIGHT:
                x2 = 0
            if event.key == pygame.K_UP:
                y1 = 0
            if event.key == pygame.K_DOWN:
                y2 = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1 = -5
            if event.key == pygame.K_RIGHT:
                x2 = 5
            if event.key == pygame.K_UP:
                y1 = -5
            if event.key == pygame.K_DOWN:
                y2 = 5
            if event.key == pygame.K_SPACE:
                # Criar um novo tiro na posição do jogador
                new_bullet = Bullet(personagemRect.rect.right, personagemRect.rect.centery)
                bullets.add(new_bullet)    
                
    x += x1 + x2
    y += y1 + y2
    xmario = x+45
    ymario = y+65

      # Atualização
    bullets.update()

    # Desenhe os tiros
    bullets.draw(tela)

    # Atualize a tela
    pygame.display.flip()

    # Controle de velocidade
    pygame.time.Clock().tick(60)
    
        
    x_1 = x
    y_1 = y
    tela.blit(cenario,(0,0))
    tela.blit(personagemImg, (x, y))
    pygame.display.update()
    clock.tick(60)

pygame.quit()