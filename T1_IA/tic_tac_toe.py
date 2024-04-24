import pygame, sys # type: ignore
import numpy as np
import pandas as pd

# constants 
WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 15
WIN_LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = 200
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = 55

# rgb: red green blue
RED = (255, 0, 0)
BG_COLOR = (253, 216, 230)
LINE_COLOR = (238, 136, 175)
CIRCLE_COLOR = (214, 41, 118)
CROSS_COLOR = (66, 66, 66)

class Tic_Tac_Toe:
	def __init__(self, screen):
		# console board
		self = self
		pygame.init()
		self.screen = screen
		self.board = np.zeros((BOARD_ROWS, BOARD_COLS))

	def draw_lines(self):
	# 1 horizontal
		pygame.draw.line( self.screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH )
		# 2 horizontal
		pygame.draw.line( self.screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH )

		# 1 vertical
		pygame.draw.line( self.screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH )
		# 2 vertical
		pygame.draw.line( self.screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH )

	def draw_figures(self):
		for row in range(BOARD_ROWS):
			for col in range(BOARD_COLS):
				if self.board[row][col] == 1:
					pygame.draw.circle( self.screen, CIRCLE_COLOR, (int( col * SQUARE_SIZE + SQUARE_SIZE//2 ), int( row * SQUARE_SIZE + SQUARE_SIZE//2 )), CIRCLE_RADIUS, CIRCLE_WIDTH )
				elif self.board[row][col] == 2:
					pygame.draw.line( self.screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH )	
					pygame.draw.line( self.screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_WIDTH )

	def mark_square(self,row, col, player):
		self.board[row][col] = player

	def available_square(self, row, col):
		return self.board[row][col] == 0

	def is_board_full(self):
		for row in range(BOARD_ROWS):
			for col in range(BOARD_COLS):
				if self.board[row][col] == 0:
					return False

		return True
	def check_win(self, player):
	# vertical win check
		for col in range(BOARD_COLS):
			if self.board[0][col] == player and self.board[1][col] == player and self.board[2][col] == player:
				self.draw_vertical_winning_line(col, player)
				return True

		# horizontal win check
		for row in range(BOARD_ROWS):
			if self.board[row][0] == player and self.board[row][1] == player and self.board[row][2] == player:
				self.draw_horizontal_winning_line(row, player)
				return True

		# asc diagonal win check
		if self.board[2][0] == player and self.board[1][1] == player and self.board[0][2] == player:
			self.draw_asc_diagonal(player)
			return True

		# desc diagonal win chek
		if self.board[0][0] == player and self.board[1][1] == player and self.board[2][2] == player:
			self.draw_desc_diagonal(player)
			return True

		return False

	def draw_vertical_winning_line(self, col, player):
		posX = col * SQUARE_SIZE + SQUARE_SIZE//2

		if player == 1:
			color = CIRCLE_COLOR
		elif player == 2:
			color = CROSS_COLOR

		pygame.draw.line( self.screen, color, (posX, 15), (posX, HEIGHT - 15), LINE_WIDTH )

	def draw_horizontal_winning_line(self, row, player):
		posY = row * SQUARE_SIZE + SQUARE_SIZE//2

		if player == 1:
			color = CIRCLE_COLOR
		elif player == 2:
			color = CROSS_COLOR

		pygame.draw.line( self.screen, color, (15, posY), (WIDTH - 15, posY), WIN_LINE_WIDTH )

	def draw_asc_diagonal(self, player):
		if player == 1:
			color = CIRCLE_COLOR
		elif player == 2:
			color = CROSS_COLOR

		pygame.draw.line( self.screen, color, (15, HEIGHT - 15), (WIDTH - 15, 15), WIN_LINE_WIDTH )

	def draw_desc_diagonal(self, player):
		if player == 1:
			color = CIRCLE_COLOR
		elif player == 2:
			color = CROSS_COLOR

		pygame.draw.line( self.screen, color, (15, 15), (WIDTH - 15, HEIGHT - 15), WIN_LINE_WIDTH )

	def restart(self):
		self.screen.fill( BG_COLOR )
		self.draw_lines()
		for row in range(BOARD_ROWS):
			for col in range(BOARD_COLS):
				self.board[row][col] = 0

	def get_position(self):
		names = ['1','2','3','4','5','6','7','8','9']
		raw_position = []
		for row in range(BOARD_ROWS):
			for col in range(BOARD_COLS):
				if self.board[row][col] == 0:
					raw_position.append('b')
				if self.board[row][col] == 1:
					raw_position.append('o')
				if self.board[row][col] == 2:
					raw_position.append('x')
		data = pd.DataFrame([raw_position], columns=names)
		print(data)
		return data
	# functions for ia playing 
	def is_game_over(self):
		return self.check_win_for_min_max(1) or self.check_win_for_min_max(2) or np.all(self.board != 0)

	def evaluate_board(self):
		if self.check_win_for_min_max(1):
			return -10
		elif self.check_win_for_min_max(2):
			return 10
		elif np.all(self.board != 0):
			return 0
		
	def check_win_for_min_max(self ,player):
		# vertical win check
		for col in range(BOARD_COLS):
			if self.board[0][col] == player and self.board[1][col] == player and self.board[2][col] == player:
				return True

		# horizontal win check
		for row in range(BOARD_ROWS):
			if self.board[row][0] == player and self.board[row][1] == player and self.board[row][2] == player:
				return True

		# asc diagonal win check
		if self.board[2][0] == player and self.board[1][1] == player and self.board[0][2] == player:
			return True

		# desc diagonal win chek
		if self.board[0][0] == player and self.board[1][1] == player and self.board[2][2] == player:
			return True

		return False
		
	def minimax(self, depth, maximizing_player):
		if depth == 0 or self.is_game_over():
			return self.evaluate_board()

		if maximizing_player:
			max_eval = -np.inf
			for i in range(3):
				for j in range(3):
					if self.board[i, j] == 0:
						self.board[i, j] = 2
						eval = self.minimax(depth - 1, False)
						self.board[i, j] = 0
						if eval is not None:  
							max_eval = max(max_eval, eval)
			return max_eval if max_eval != -np.inf else 0
		else:
			min_eval = np.inf
			for i in range(3):
				for j in range(3):
					if self.board[i, j] == 0:
						self.board[i, j] = 1
						eval = self.minimax(depth - 1, True)
						self.board[i, j] = 0
						if eval is not None:  
							min_eval = min(min_eval, eval)
			return min_eval if min_eval != np.inf else 0


	def find_best_move(self):
		best_move = None
		best_score = -np.inf
		for i in range(3):
			for j in range(3):
				if self.board[i, j] == 0:
					self.board[i, j] = 2
					score = self.minimax(9, False)  # maximum depth
					self.board[i, j] = 0
					if score > best_score:
						best_score = score
						best_move = (i, j)
		return best_move