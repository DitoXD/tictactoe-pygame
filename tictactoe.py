import pygame
import sys
import numpy as np

WIDTH = 600 # This is the width of the window for the game
HEIGHT = 600 # This is the height of the window for the game
BOARD_COLS = 3 # This is the number of columns on the board
BOARD_ROWS = 3 # This is the number of rows on the board
BG_COLOUR = (110, 199, 228) # This is the background colour for the window in rgb format (Red,Green,Blue)
LINE_COLOUR = (93, 117, 191) # This is the board line colour for the window in rgb format (Red,Green,Blue)
CIRCLE_COLOUR = (255, 255, 255) # This is the circle colour for the game in rgb format (Red,Green,Blue)
CROSS_COLOUR = (111, 101, 100 ) # This is the cross colour for the game in rgb format (Red,Green,Blue)

game_board = np.zeros((BOARD_ROWS,BOARD_COLS))  # This is to create our calculative game board which will 
                                                # let us assign the values and keep track of plays in the 
                                                # game

screen = pygame.display.set_mode((WIDTH, HEIGHT)) # This creates the window for the game
pygame.display.set_caption("TIC-TAC-TOE") # This sets the name of the window to the String specified
screen.fill(BG_COLOUR) # This sets the background color to the constant we specified from before


# This is a function to draw our game board which wil be the interface for the game
def draw_game_board():
    # These are lines used to make the borders for each space in the game
    pygame.draw.line(screen, LINE_COLOUR, (200,10), (200,590), width=5)
    pygame.draw.line(screen, LINE_COLOUR, (400,10), (400,590), width=5)
    pygame.draw.line(screen, LINE_COLOUR, (10,200), (590,200), width=5)
    pygame.draw.line(screen, LINE_COLOUR, (10,400), (590,400), width=5)

# This is a function to assign a player to a spot on the board
def mark_square(row, col, player): 
    game_board[row][col] = player

# This is a function to check is a spot is empty
def available_square(row, col):
    return game_board[row][col] == 0

# This is a function to check if the board is full
def is_board_full():
    count = 0
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if game_board[row][col] == 0:
                return False
    return True

# This is a function to draw the appropriate symbol per each players move
def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if game_board[row][col] == 1:
                pygame.draw.line(screen, CROSS_COLOUR, (int(col * 200 + 50),int(row * 200 + 150)), (int(col * 200 + 150),int(row * 200 + 50)), width=20)
                pygame.draw.line(screen, CROSS_COLOUR, (int(col * 200 + 50),int(row * 200 + 50)), (int(col * 200 + 150),int(row * 200 + 150)), width=20)
            elif game_board[row][col] == 2:
                pygame.draw.circle(screen, CIRCLE_COLOUR, (int(col * 200 + 100),int(row * 200 + 100)), 60, width=15)

#checks if the player has won the game
def check_win(player):
    # vertical win 
    for col in range(BOARD_COLS):
        if game_board[0][col] == player and game_board[1][col] == player and game_board[2][col] == player:
            draw_vertical_winning_line(col, player)
            return True
    
    # horizontal win
    for row in range(BOARD_ROWS):
        if game_board[row][0] == player and game_board[row][1] == player and game_board[row][2] == player:
            draw_horizontal_winning_line(row, player)
            return True

    # ascending diagonal win
    if game_board[2][0] == player and game_board[1][1] == player and game_board[0][2] == player:
        draw_asc_diagonal_winning_line(player)
        return True

    # descending diagonal win
    if game_board[0][0] == player and game_board[1][1] == player and game_board[2][2] == player:
        draw_dsc_diagonal_winning_line(player)
        return True

    # no win
    return False

# This function draws the line in a column if the player won in that column
def draw_vertical_winning_line(col, player):
    posX = col * 200 + 100

    if player == 1:
        win_line_colour = CROSS_COLOUR
    elif player == 2:
        win_line_colour = CIRCLE_COLOUR

    pygame.draw.line(screen, win_line_colour, (posX, 15), (posX, HEIGHT - 15), width=10)

# This function draws the line in a row if the player won in that row
def draw_horizontal_winning_line(row, player):
    posY = row * 200 + 100

    if player == 1:
        win_line_colour = CROSS_COLOUR
    elif player == 2:
        win_line_colour = CIRCLE_COLOUR

    pygame.draw.line(screen, win_line_colour, (15, posY), (WIDTH - 15, posY), width=10)

# This function draws the line in the ascending diagonal if the player won in the ascending diagonal
def draw_asc_diagonal_winning_line(player):
    if player == 1:
        win_line_colour = CROSS_COLOUR
    elif player == 2:
        win_line_colour = CIRCLE_COLOUR

    pygame.draw.line(screen, win_line_colour, (15, HEIGHT - 15), (WIDTH - 15, 15), width=15)

# This function draws the line in the descending diagonal if the player won in the descending diagonal
def draw_dsc_diagonal_winning_line(player):
    if player == 1:
        win_line_colour = CROSS_COLOUR
    elif player == 2:
        win_line_colour = CIRCLE_COLOUR

    pygame.draw.line(screen, win_line_colour, (15, 15), (WIDTH - 15, HEIGHT - 15), width=15)

# This function allows the players to restart the game
def restart():
    screen.fill( BG_COLOUR)
    draw_game_board()
    player = 1
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            game_board[row][col] = 0


def main():
    pygame.init() # makes the 'game'
    draw_game_board() # Creates the window and plots the board accordingly
    player = 1 # The game will always start with Player 1
    game_over = False # keeps track of the game state of end 

    # mainloop which maintains the game state alive
    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # if the user presses the X on the window, the game will end
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and not game_over: # gets the click on the board

                mouse_x = event.pos[0] # the x position of the click
                mouse_y = event.pos[1] # the y position of the click

                clicked_row = int(mouse_y // 200)   # converts the y position into easy to use values of 
                                                    # [0,1,2] depending on the section of the board 
                                                    # selected
                clicked_col = int(mouse_x // 200)   # converts the x position into easy to use values of 
                                                    # [0,1,2] depending on the section of the board 
                                                    # selected

                if available_square(clicked_row, clicked_col): # checks if the spot is available
                    if player == 1:
                        mark_square(clicked_row,clicked_col,1) # assigns the play to player one
                        game_over = check_win(player) # if the player wins, the game over is set to True
                        player = 2 # passes the turn to player 2

                    elif player == 2:
                        mark_square(clicked_row,clicked_col,2) # assigns the play to player two
                        game_over = check_win(player) # if the player wins, the game over is set to True
                        player = 1 # passes the turn to player 1
                    
                    draw_figures() # draws the appropriate figures per play

            if event.type == pygame.KEYDOWN:    # at any point in the game, the letter R can be 
                                                # pressed to restart the game
                if event.key == pygame.K_r:
                    restart()
                    game_over = False


        pygame.display.update() # shows the updates to the game



if __name__ == "__main__": # makes sure the file being ran is this file 
    main()
