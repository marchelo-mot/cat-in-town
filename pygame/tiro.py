import pygame
import sys

# Inicialização do Pygame
pygame.init()

# Configurações da tela
screen_width = 1600
screen_height = 1200
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Disparo com Pygame")

# Cores
BLACK = (0, 0, 0)

# Carregar imagem do personagem
personagemImg = pygame.image.load('cubo.png')
personagemRect = personagemImg.get_rect()
personagemRect.center = (100, screen_height // 2)  # Posição inicial do personagem

# Classe para representar o tiro
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        # Criar uma superfície preta com tamanho 10x20
        self.image = pygame.Surface((10, 20))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 5

    def update(self):
        self.rect.x += self.speed
        # Remova o tiro quando ele sair da tela
        if self.rect.left > screen_width:
            self.kill()

# Grupo de sprites para os tiros
bullets = pygame.sprite.Group()

# Game Loop
running = True
while running:
    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Criar um novo tiro na posição do jogador
                new_bullet = Bullet(personagemRect.right, personagemRect.centery)
                bullets.add(new_bullet)

    # Atualização
    bullets.update()

    # Desenho
    screen.fill(BLACK)
    # Desenhar o personagem na tela
    screen.blit(personagemImg, personagemRect)

    # Desenhe os tiros
    bullets.draw(screen)

    # Atualize a tela
    pygame.display.flip()

    # Controle de velocidade
    pygame.time.Clock().tick(60)

# Encerramento do Pygame
pygame.quit()
sys.exit()