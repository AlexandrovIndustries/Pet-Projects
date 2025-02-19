import pygame
import random
import time
import sys
import pandas as pd
from tkinter import Tk, Label, Button


pygame.init()


SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
GRID_SIZE = 30
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE
SIDE_PANEL_WIDTH = 150


COLORS = [
    (0, 0, 0),
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
    (255, 255, 0),
    (255, 0, 255),
    (0, 255, 255),
    (255, 165, 0)
]


SHAPES = [
    [[1, 1, 1, 1]],
    [[1, 1], [1, 1]],
    [[0, 1, 0], [1, 1, 1]],
    [[1, 1, 0], [0, 1, 1]],
    [[0, 1, 1], [1, 1, 0]],
    [[1, 1, 1], [0, 1, 0]],
    [[1, 1, 1], [1, 0, 0]]
]

class Tetris:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH + SIDE_PANEL_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Тетрис')
        self.clock = pygame.time.Clock()
        self.grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
        self.current_shape = self.get_new_shape()
        self.next_shape = self.get_new_shape()
        self.shape_x = GRID_WIDTH // 2 - len(self.current_shape[0]) // 2
        self.shape_y = 0
        self.score = 0
        self.start_time = time.time()
        self.game_over = False
        self.scores = self.load_scores()

    def get_new_shape(self):
        return random.choice(SHAPES)

    def draw_grid(self):
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                color = COLORS[self.grid[y][x]]
                pygame.draw.rect(self.screen, color, (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE), 0)
                pygame.draw.rect(self.screen, (255, 255, 255), (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE), 1)

    def draw_shape(self, shape, offset_x, offset_y):
        for y, row in enumerate(shape):
            for x, cell in enumerate(row):
                if cell:
                    color = COLORS[cell]
                    pygame.draw.rect(self.screen, color, ((offset_x + x) * GRID_SIZE, (offset_y + y) * GRID_SIZE, GRID_SIZE, GRID_SIZE), 0)
                    pygame.draw.rect(self.screen, (255, 255, 255), ((offset_x + x) * GRID_SIZE, (offset_y + y) * GRID_SIZE, GRID_SIZE, GRID_SIZE), 1)

    def rotate_shape(self, shape):
        return [[shape[y][x] for y in range(len(shape))] for x in range(len(shape[0]) - 1, -1, -1)]

    def valid_move(self, shape, offset_x, offset_y):
        for y, row in enumerate(shape):
            for x, cell in enumerate(row):
                if cell:
                    new_x = offset_x + x
                    new_y = offset_y + y
                    if new_x < 0 or new_x >= GRID_WIDTH or new_y >= GRID_HEIGHT or self.grid[new_y][new_x]:
                        return False
        return True

    def merge_shape(self, shape, offset_x, offset_y):
        for y, row in enumerate(shape):
            for x, cell in enumerate(row):
                if cell:
                    self.grid[offset_y + y][offset_x + x] = cell

    def clear_lines(self):
        lines_cleared = 0
        for y in range(GRID_HEIGHT):
            if all(self.grid[y]):
                del self.grid[y]
                self.grid.insert(0, [0 for _ in range(GRID_WIDTH)])
                lines_cleared += 1
        self.score += lines_cleared ** 2

    def draw_score_and_time(self):
        font = pygame.font.SysFont('Arial', 18)
        score_text = font.render(f'Score: {self.score}', True, (255, 255, 255))
        self.screen.blit(score_text, (SCREEN_WIDTH + 10, 200))
        elapsed_time = int(time.time() - self.start_time)
        time_text = font.render(f'Time: {elapsed_time}s', True, (255, 255, 255))
        self.screen.blit(time_text, (SCREEN_WIDTH + 10, 220))

    def draw_scores(self):
        font = pygame.font.SysFont('Arial', 18)
        scores_text = font.render('Scores:', True, (255, 255, 255))
        self.screen.blit(scores_text, (SCREEN_WIDTH + 10, 250))
        for i, score in enumerate(self.scores):
            score_text = font.render(f'{i + 1}. {score}', True, (255, 255, 255))
            self.screen.blit(score_text, (SCREEN_WIDTH + 10, 270 + i * 20))

    def load_scores(self):
        try:
            scores_df = pd.read_csv('scores.csv')
            return scores_df['Score'].tolist()
        except FileNotFoundError:
            return []

    def save_scores(self):
        scores_df = pd.DataFrame(self.scores, columns=["Score"])
        scores_df.to_csv('scores.csv', index=False)

    def show_game_over_window(self):
        root = Tk()
        root.title("Game Over")
        root.geometry("200x100") 

        def restart_game():
            root.destroy()
            self.__init__()
            self.run()

        def quit_game():
            root.destroy()
            pygame.quit()
            sys.exit()

        Label(root, text=f"Game Over! Your score: {self.score}").pack(pady=10)
        Button(root, text="Restart", command=restart_game).pack(pady=5)
        Button(root, text="Quit", command=quit_game).pack(pady=5)

        self.scores.append(self.score)
        self.save_scores()
        scores_df = pd.DataFrame(self.scores, columns=["Score"])
        Label(root, text="Scores:").pack(pady=10)
        Label(root, text=scores_df.to_string(index=False)).pack(pady=10)

        root.mainloop()

    def run(self):
        while not self.game_over:
            self.screen.fill((0, 0, 0))
            self.draw_grid()
            self.draw_shape(self.current_shape, self.shape_x, self.shape_y)
            self.draw_shape(self.next_shape, GRID_WIDTH + 1, 2)
            self.draw_score_and_time()
            self.draw_scores()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT and self.valid_move(self.current_shape, self.shape_x - 1, self.shape_y):
                        self.shape_x -= 1
                    elif event.key == pygame.K_RIGHT and self.valid_move(self.current_shape, self.shape_x + 1, self.shape_y):
                        self.shape_x += 1
                    elif event.key == pygame.K_DOWN and self.valid_move(self.current_shape, self.shape_x, self.shape_y + 1):
                        self.shape_y += 1
                    elif event.key == pygame.K_UP:
                        rotated_shape = self.rotate_shape(self.current_shape)
                        if self.valid_move(rotated_shape, self.shape_x, self.shape_y):
                            self.current_shape = rotated_shape

            if not self.valid_move(self.current_shape, self.shape_x, self.shape_y + 1):
                self.merge_shape(self.current_shape, self.shape_x, self.shape_y)
                self.score += sum(sum(row) for row in self.current_shape)  
                self.clear_lines()
                self.current_shape = self.next_shape
                self.next_shape = self.get_new_shape()
                self.shape_x = GRID_WIDTH // 2 - len(self.current_shape[0]) // 2
                self.shape_y = 0
                if not self.valid_move(self.current_shape, self.shape_x, self.shape_y):
                    self.game_over = True
            else:
                self.shape_y += 1

            pygame.display.flip()
            self.clock.tick(10)  

        self.show_game_over_window()

if __name__ == '__main__':
    game = Tetris()
    game.run()