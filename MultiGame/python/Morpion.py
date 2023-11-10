import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Définir la taille de la fenêtre
largeur, hauteur = 300, 300
taille_fenetre = (largeur, hauteur)

# Tour handle
player1 = True

# Couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)

# Créer la fenêtre
fenetre = pygame.display.set_mode(taille_fenetre)
pygame.display.set_caption("Morpion")

def CreateBoard():
    return [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

def ShowBoard(array):
    # Remplir la fenêtre avec la couleur blanche
    fenetre.fill(NOIR) 

    # Dessiner les lignes de séparation horizontales
    for i in range(1, 3):
        pygame.draw.line(fenetre, BLANC, (0, i * 100), (300, i * 100), 2)

    # Dessiner les lignes de séparation verticales
    for j in range(1, 3):
        pygame.draw.line(fenetre, BLANC, (j * 100, 0), (j * 100, 300), 2)

    for i in range(3):
        for j in range(3):
            font = pygame.font.Font(None, 74)
            text = font.render(array[j][i], True, BLANC)
            fenetre.blit(text, (j * 100 + 30, i * 100 + 30))

def GetCellPos(mouse_pos):
    x, y = mouse_pos
    col = x // 100
    row = y // 100
    return col, row

def CheckWin(array):
    # Vérifier les lignes
    for row in array:
        if row[0] == row[1] == row[2] != " ":
            return row[0]

    # Vérifier les colonnes
    for col in range(3):
        if array[0][col] == array[1][col] == array[2][col] != " ":
            return array[0][col]

    # Vérifier les diagonales
    if array[0][0] == array[1][1] == array[2][2] != " ":
        return array[0][0]
    if array[0][2] == array[1][1] == array[2][0] != " ":
        return array[0][2]

    return None  # Aucun gagnant

def CheckTie(array):
    isTie = True
    for i in range(3):
        for j in range(3):
            if array[j][i] == " ":
                isTie = False
    return isTie



# Créer le tableau
array = CreateBoard()

# Boucle Principale
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            col, row = GetCellPos(mouse_pos)
            if (player1):
                if(array[col][row] == " "):
                    array[col][row] = "X"
                    player1 = not player1
            else:
                if(array[col][row] == " "):
                    array[col][row] = "O"
                    player1 = not player1
            winner = CheckWin(array)
            tie = CheckTie(array)
            if winner:
                print(f"Le joueur {winner} a gagné !")
                pygame.quit()
                sys.exit()
            if tie:
                print("Congratulations, You have a tie !")

    # Afficher le tableau
    ShowBoard(array)

    # Mettre à jour l'affichage
    pygame.display.flip()