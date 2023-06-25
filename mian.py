import sys
import math
import pygame
ROW = 6
COLUMN = 7

def create_Board():
    board = [[int(0) for _ in range(7)] for _ in range(6)]
    return board


def make_move(column, piece):
    for row in range(5, -1, -1):
        if board[row][column] == 0:
            board[row][column] = piece
            return True
    return False

def is_winner(piece):
    # check rows
    for row in range(6):
         for col in range(4):
            if board[row][col] == piece and board[row][col+1] == piece and \
                    board[row][col+2] == piece and board[row][col+3] == piece:
                 return True
        # check columns

    for col in range(7):
        for row in range(3):
            if board[row][col] == piece and board[row+1][col] == piece and \
                    board[row+2][col] == piece and board[row+3][col] == piece:
                return True
    return False

def draw_board(board):
    for c in range(COLUMN):
        for r in range(ROW):
            pygame.draw.rect(screen, (0, 100, 255), (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.lines(screen, (255, 255, 255), False, [[c*SQUARESIZE+SQUARESIZE, 0], [c*SQUARESIZE+SQUARESIZE, r*SQUARESIZE+2*SQUARESIZE]], 8)
            pygame.draw.lines(screen, (255, 255, 255), False, [[0, r*SQUARESIZE], [c*SQUARESIZE+2*SQUARESIZE, r*SQUARESIZE]], 5)
            if board[r][c] == 0:
                pygame.draw.circle(screen, (0, 0, 0), (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
            elif board[r][c] == 1:
                pygame.draw.circle(screen, (0, 255, 0), (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
            else:
                pygame.draw.circle(screen, (255, 0, 0), (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
    pygame.display.update()

board = create_Board()
pygame.init()
SQUARESIZE = 100
width = COLUMN * SQUARESIZE
high = (ROW+1) * SQUARESIZE
RADIUS = (SQUARESIZE/2 - 5)
screen = pygame.display.set_mode((width, high))
draw_board(board)
pygame.display.update()
players = [1, 2]
current_player = 0
game_over = False

while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            posx = event.pos[0]
            column = int(math.floor(posx/SQUARESIZE))
            if (column > -1) and (column < 8):
                if make_move(column, players[current_player]):
                    draw_board(board)

                if is_winner(players[current_player]):
                    print(f'Player {players[current_player]} wins!')
                    game_over = True
                    break
                else:
                    print('Column is full, try again.')
                current_player = (current_player + 1) % 2
            else:
                print('Column is not Found, try again.')