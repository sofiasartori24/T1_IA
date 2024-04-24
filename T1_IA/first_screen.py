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

class First_Screen():

    def __init__(self, screen):
        self = self
        self.screen = screen
        
    def check_PxC_button(self, event):
        return self.button_PxC_rect.collidepoint(event.pos[0], event.pos[1])
    
    def check_PxP_button(self, event):
        return self.button_PxP_rect.collidepoint(event.pos[0], event.pos[1])
        
    def check_PxP_button_game_over(self, event):
        return self.button_PxP_rect_game_over.collidepoint(event.pos[0], event.pos[1])
    
    def check_PxC_button_game_over(self, event):
        return self.button_PxC_rect_game_over.collidepoint(event.pos[0], event.pos[1])

    def setup(self): 
        # set up the font
        font = pygame.font.Font(None, 36) 
        title_font = pygame.font.Font(None, 120) 

        # clear the screen
        self.screen.fill((BG_COLOR))  

        # render title
        self.text_surface = title_font.render('Tic Tac Toe!', True, (CIRCLE_COLOR))  # render the text onto a surface
        self.text_rect = self.text_surface.get_rect(center=(WIDTH // 2, 220))  # get the rectangle that encloses the text
        # blit the text onto the screen
        self.screen.blit(self.text_surface, self.text_rect)

        # render player x player button
        self.button_PxP_text = font.render('Player X Player', True, BLACK)
        self.button_PxP_rect = pygame.Rect(175, 400, 275, 40) #button_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
        pygame.draw.rect(self.screen, BLACK, self.button_PxP_rect, 2, border_radius=10)  # draw button outline
        self.screen.blit(self.button_PxP_text, pygame.Rect(210, 410, 250, 40))  # draw button text

        # render player x computer button
        self.button_PxC_text = font.render('Player X Computer', True, BLACK)
        self.button_PxC_rect = pygame.Rect(175, 450, 275, 40) 
        pygame.draw.rect(self.screen, BLACK, self.button_PxC_rect, 2, border_radius=10)  # draw button outline
        self.screen.blit(self.button_PxC_text, pygame.Rect(210, 460, 300, 40)) 

        pygame.display.flip()

    def setup_game_over(self, text): 
        # set up the font
        font = pygame.font.Font(None, 36) 
        game_over_font = pygame.font.Font(None, 100)

        # clear the screen
        self.screen.fill((BG_COLOR))  

        # render Game Over
        self.game_over_text = game_over_font.render("GAME OVER!", True, CIRCLE_COLOR)
        self.game_over_rect = self.game_over_text.get_rect(center=(WIDTH // 2, 150))
        self.screen.blit(self.game_over_text, self.game_over_rect)

        # render title
        self.text_surface = font.render(text, True, (0, 0, 0)) 
        self.text_rect = self.text_surface.get_rect(center=(WIDTH // 2, 250)) 
        self.screen.blit(self.text_surface, self.text_rect)

        # render player x player button
        self.button_PxP_text_game_over = font.render('Player X Player', True, BLACK)
        self.button_PxP_rect_game_over = pygame.Rect(175, 400, 275, 40) 
        pygame.draw.rect(self.screen, BLACK, self.button_PxP_rect_game_over, 2, border_radius=10)  # draw button outline
        self.screen.blit(self.button_PxP_text_game_over, pygame.Rect(210, 410, 250, 40))  # draw button text

        # render player x computer button
        self.button_PxC_text_game_over = font.render('Player X Computer', True, BLACK)
        self.button_PxC_rect_game_over = pygame.Rect(175, 450, 275, 40) 
        pygame.draw.rect(self.screen, BLACK, self.button_PxC_rect_game_over, 2, border_radius=10)  # draw button outline
        self.screen.blit(self.button_PxC_text_game_over, pygame.Rect(210, 460, 300, 40)) 

        pygame.display.flip()
    