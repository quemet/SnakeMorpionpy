import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Constante
LARGEUR, HAUTEUR = 500, 500
TAILLE_FENETRE = (LARGEUR, HAUTEUR)
CELL_SIZE = 20
NB_CELS = LARGEUR // CELL_SIZE
FPS = 10

# Couleurs
ROUGE = (255, 0, 0)
GREEN = (0, 255, 0)
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)

# Créer la fenêtre
fenetre = pygame.display.set_mode(TAILLE_FENETRE)
pygame.display.set_caption("Snake")

# Création de la police
font = pygame.font.Font(None, 74)

def CreateBoard():
    return [[" " for _ in range(NB_CELS)] for _ in range(NB_CELS)]

def ShowBoard(array):
    # Remplire la fenêtre avec la couleur noire
    fenetre.fill(NOIR)

    # Dessiner les lignes de séparation horizontales
    for i in range(1, NB_CELS):
        pygame.draw.line(fenetre, BLANC, (0, i * CELL_SIZE), (LARGEUR, i * CELL_SIZE), 2)

    # Dessiner les lignes de séparations verticales
    for j in range(1, NB_CELS):
        pygame.draw.line(fenetre, BLANC, (j * CELL_SIZE, 0), (j * CELL_SIZE, HAUTEUR), 2)

    for i in range(NB_CELS):
        for j in range(NB_CELS):
            text = font.render(array[j][i], True, BLANC)
            fenetre.blit(text, (j * CELL_SIZE + 30, i * CELL_SIZE + 30))

array = CreateBoard()

clock = pygame.time.Clock()

# Boucle Principale
while True :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Dessiner le tableau de jeu
    ShowBoard(array)

    # Mettre à jour l'affichage
    pygame.display.flip()

    # Contrôler la vitesse du jeu
    clock.tick(FPS)