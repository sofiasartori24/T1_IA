import pygame, sys # type: ignore
from first_screen import First_Screen
from tic_tac_toe import Tic_Tac_Toe
from tic_tac_toe_models import Tic_Tac_Toe_Models
import time

# constants 
WIDTH = 600
HEIGHT = 700
SQUARE_SIZE = 200
BG_COLOR = (253, 216, 230)

pygame.init()

player = 1
game_over = False
is_playing = False
start_game = False
computer_turn = False
is_playing_with_computer = False
is_playing_with_player = False
text = "Make a Move"
models = Tic_Tac_Toe_Models()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill((BG_COLOR))

first_screen = First_Screen(screen=screen)
tic_tac_toe = Tic_Tac_Toe(screen=screen)

pygame.display.set_caption('TIC TAC TOE')

def makeText(result_models):
    result = result_models[0]
    text = " "
    print(result)
    if result == "Draw":
        text = "It's a Draw, Play Again!"
    if result == "xwins": 
        text = "X wins, Play Again!"
    if result == "owins": 
        text = "O wins, Play Again!"
    if result == "inGame": 
        text = "Game is still goins! Make a Move"
    print(result)
    rect = pygame.Rect(0, 600, 600, 100)  # Coordenadas x, y e dimensões do retângulo
    pygame.draw.rect(screen, BG_COLOR, rect)
    font = pygame.font.Font(None, 25)
    text_surface = font.render(text, True, (0, 0, 0))  # render the text onto a surface
    text_rect = text_surface.get_rect(center=(WIDTH // 2, 650))  # get the rectangle that encloses the text
    screen.blit(text_surface, text_rect)
    return text
    

while True:
    for event in pygame.event.get():
        if not is_playing:
            if game_over:
                print("game over: " + text)
                screen.fill((BG_COLOR))
                first_screen.setup_game_over(text)
            else:
                screen.fill((BG_COLOR))
                first_screen.setup()
        elif start_game:
            tic_tac_toe.restart()
            screen.fill((BG_COLOR)) 
            tic_tac_toe.draw_lines()
            start_game = False
            game_over = False
        if event.type == pygame.QUIT:
            sys.exit()

        if computer_turn:
            computer_turn = False 
            if not tic_tac_toe.is_game_over():
                computer_move = tic_tac_toe.find_best_move()
                tic_tac_toe.mark_square(computer_move[0], computer_move[1], 2)
                tic_tac_toe.draw_figures()
                prediction = models.predict_tree_with_draw_experts(tic_tac_toe.get_position())
                text = makeText(prediction)
                print(text)
                if prediction[0] != "inGame":
                    game_over = True
                    is_playing = False
                    is_playing_with_computer = False
                    player = 1  

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseX = event.pos[0] # x
            mouseY = event.pos[1] # y
            clicked_row = int(mouseY // SQUARE_SIZE)
            clicked_col = int(mouseX // SQUARE_SIZE)

            if is_playing_with_player:
                if tic_tac_toe.available_square( clicked_row, clicked_col ):
                    tic_tac_toe.mark_square( clicked_row, clicked_col, player )
                    tic_tac_toe.draw_figures()   
                    player = 1 if player == 2 else 2 
                tic_tac_toe.check_win(player)
                prediction = models.predict_tree_with_draw_experts(tic_tac_toe.get_position())
                text = makeText(prediction)
                print(text)
                if prediction[0] != "inGame":
                    game_over = True
                    is_playing = False
                    is_playing_with_player = False
                    player = 1

            elif is_playing_with_computer and not computer_turn and not game_over:
                if tic_tac_toe.available_square( clicked_row, clicked_col ):
                    tic_tac_toe.mark_square( clicked_row, clicked_col, player )
                    tic_tac_toe.draw_figures()   
                    computer_turn = True

                prediction = models.predict_tree_with_draw_experts(tic_tac_toe.get_position())
                text = makeText(prediction)
                print(text)
                if prediction[0] != "inGame":
                    game_over = True
                    is_playing = False
                    is_playing_with_computer = False
                    computer_turn = False 
                    player = 1
            else:
                if game_over:
                    if first_screen.check_PxP_button_game_over(event=event):
                        is_playing = True
                        is_playing_with_player = True
                        start_game = True
                    if first_screen.check_PxC_button_game_over(event=event):
                        start_game = True
                        is_playing = True
                        is_playing_with_computer = True
                else:    
                    if first_screen.check_PxP_button(event=event):
                        is_playing = True
                        start_game = True
                        is_playing_with_player = True
                    if first_screen.check_PxC_button(event=event):
                        start_game = True
                        is_playing = True
                        is_playing_with_computer = True
            
    pygame.display.update()


    