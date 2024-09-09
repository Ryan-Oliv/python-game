# 1. Import ---------------------------------------------------------------------------
# pip install pygame
import pygame

import random

from ghost import Ghost
from bat import Bat
from shoot import Shoot

# 2. Inicialização --------------------------------------------------------------------
# Iniciar o pygame
pygame.init()

# Iniciando a janela com a config de resolução de 840x480
# Cria uma canvas, uma tela em branco para pintar
WIDTH_SCREEN = 840  # Largura
HEIGHT_SCREEN = 480  # Altura

display = pygame.display.set_mode([WIDTH_SCREEN, HEIGHT_SCREEN])

# Preenche o fundo da janela com a cor RGB
display.fill([0, 0, 0])

# Muda o titulo da janela
pygame.display.set_caption("Game Ryan - Python")

# Carregar a imagem para criar o icone. Converter a imagem para o formato icone
icone = pygame.image.load("data/icone.png")
pygame.display.set_icon(icone)

# 3. Elementos de Tela ----------------------------------------------------------------

# 3.1 Personagens

# Criando um grupo de imagens para carregar todas as imagens necessárias de uma unica vez
objectGroup = pygame.sprite.Group()
batGroup = pygame.sprite.Group()
shootGroup = pygame.sprite.Group()

# Criar um fundo (BackGround) para o fantasma
bg = pygame.sprite.Sprite(objectGroup)
bg.image = pygame.image.load("data/background.jpg")
bg.image = pygame.transform.scale(bg.image, [840, 480])
bg.rect = bg.image.get_rect()

# Criar o objeto Ghost - Fantasma
ghost = Ghost(objectGroup)

# 3.2 Fonte ----------------------------------------------------------------------------
score_font = pygame.font.Font("font/Pixeltype.ttf", 50)
gameOver_font = pygame.font.Font("font/Pixeltype.ttf", 200)

# 3.3 Música ---------------------------------------------------------------------------
pygame.mixer.music.load("data/alienblues.wav")
pygame.mixer.music.play(-1)


# 3.4 Som -------------------------------------------------------------------------------
attack = pygame.mixer.Sound("data/magic1.wav")
# Criando o objeto sprite para criar a imagem
# ghost = pygame.sprite.Sprite(drawGroup)
# # Carregar a imagem dentro do elemento sprite
# ghost.image = pygame.image.load("data/ghost-x4.gif")
# # Redimensionar a imagem para ocupar 100% do retângulo
# ghost.image = pygame.transform.scale(ghost.image, [100, 100])
# # Colocar a imagem em um retangulo
# ghost.rect = pygame.Rect(50, 50, 100, 100)

# 4. Variáveis Globais ----------------------------------------------------------------

# Variável para controlar o loop

gameLoop = True
gameOver = False

timer = 20
pontos = 0

# Criar um clock para ajustar os frames por segundo (FPS)
clock = pygame.time.Clock()

# 5. Função Principal -----------------------------------------------------------------


def main():
    global gameLoop
    global gameOver
    global timer
    global pontos

    while gameLoop:
        # Clock para 60fps
        clock.tick(140)

        # Loop para verificar os possiveis eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameLoop = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    attack.play()
                    print("Tiro")
                    newShoot = Shoot(objectGroup, shootGroup)
                    newShoot.rect.center = ghost.rect.center

        objectGroup.update()

        if not gameOver:

            # Criação de vários morcegos
            timer += 1
            if timer > 30:
                timer = 0
                if random.random() < 0.3:
                    newBat = Bat(objectGroup, batGroup)

            # Colisão de morcegos com o fantasma
            colisao = pygame.sprite.spritecollide(
                ghost, batGroup, False, pygame.sprite.collide_mask)

            if colisao:
                print("Game")
                gameOver = True

            # Colisão de tiros com o morcego
            tiros = pygame.sprite.groupcollide(
                shootGroup, batGroup, True, True, pygame.sprite.collide_mask)

            # Contagem de morcegos mortos
            if tiros:
                pontos += 1
                print(" Matou ", pontos)
            # A cor de fundo da janela

            display.fill([0, 0, 0])

            # Desenho os elementos do grupo na janela
            objectGroup.draw(display)

            # Inserir a pontuação na tela
            score_render = score_font.render(
                f'SCORE: {pontos}', False, 'White')
            display.blit(score_render, (650, 50))
            pygame.display.update()

            if gameOver:
                gameOver_Msg = gameOver_font.render(
                    f'GAMEOVER', False, 'White')
                display.blit(gameOver_Msg, (125, 150))

            pygame.display.update()


if __name__ == '__main__':
    main()
