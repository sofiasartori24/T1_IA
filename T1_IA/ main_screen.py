import pygame, sys # type: ignore

pygame.init()

# constants 
WIDTH = 600
HEIGHT = 600

# rgb: red green blue
RED = (255, 0, 0)
BG_COLOR = (253, 216, 230)
LINE_COLOR = (238, 136, 175)
CIRCLE_COLOR = (214, 41, 118)
CROSS_COLOR = (66, 66, 66)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('TIC TAC TOE')

# set up the font
font = pygame.font.Font(None, 36)  

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # clear the screen
    screen.fill((BG_COLOR))  

    # render title
    text_surface = font.render('Hello, Lets Play Tic Tac Toe!', True, (0, 0, 0))  # render the text onto a surface
    text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT - 500))  # get the rectangle that encloses the text

    # render player x player button
    button_text = font.render('Player X Player', True, BLACK)
    button_rect = pygame.Rect(200, 300, 200, 40) #button_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))


    pygame.draw.rect(screen, BLACK, button_rect, 2, border_radius=10)  # draw button outline
    screen.blit(button_text, pygame.Rect(210, 310, 200, 40))  # draw button text

    # blit the text onto the screen
    screen.blit(text_surface, text_rect)

    pygame.display.flip()


    