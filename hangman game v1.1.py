import pygame
import math
import random

pygame.init()

# Constants
WIDTH = 1200
HEIGHT = 500

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

TITLE_FONT = pygame.font.SysFont('comicsans', 70)
WORD_FONT = pygame.font.SysFont('comicsans', 60)
LETTER_FONT = pygame.font.SysFont('comicsans', 40)

A = 65
radius = 20
gap = 15
start_x = round((WIDTH - (radius * 2 + gap) * 13) / 2)
start_y = 400

words = ["IDE", "REPLIT", "PYTHON", "PYGAME", "TALL", "TEST", "HAPPY", "INTERNATIONAL", "MECHATRONICS"]


#resources load
images = []
for i in range(7):
    image = pygame.image.load("resources/hangman"+str(i)+".png")
    images.append(image)


#main class
class HangmanGame:
    def __init__(self):
        self.win = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Hangman Game by the greatest Tornado DH")
        self.word = random.choice(words)
        self.guessed = set()
        self.Hangman_image_counter = 0


# buttons settings
        self.letters = []
        for i in range(26):
            x = start_x + gap * 2 + ((radius * 2 + gap) * (i % 13))
            y = start_y + ((radius * 2 + gap) * (i // 13))
            self.letters.append([x, y, chr(A + i), True])


# drawing and that stuff
    def draw(self):
        self.win.fill(WHITE)
        self.draw_title()
        self.draw_word()
        self.draw_buttons()
        self.win.blit(images[self.Hangman_image_counter], (150, 100))
        pygame.display.update()

    def draw_title(self):
        text = TITLE_FONT.render("HANGMAN", 1, BLACK)
        self.win.blit(text, (WIDTH / 2 - text.get_width() / 2, 20))

    def draw_word(self):
        display_word = ''.join(letter + ' ' if letter in self.guessed else '_ ' for letter in self.word)
        text = WORD_FONT.render(display_word, 1, BLACK)
        self.win.blit(text, (400, 200))

    def draw_buttons(self):
        for letter in self.letters:
            x, y, char, visible = letter
            if visible:
                pygame.draw.circle(self.win, BLACK, (x, y), radius, 3)
                text = LETTER_FONT.render(char, 1, BLACK)
                self.win.blit(text, (x - text.get_width() / 2, y - text.get_height() / 2))

    def display_message(self, message):
        pygame.time.delay(1000)
        self.win.fill(WHITE)
        text = WORD_FONT.render(message, 1, BLACK)
        self.win.blit(text, (WIDTH / 2 - text.get_width() / 2, HEIGHT / 2 - text.get_height() / 2))
        pygame.display.update()
        pygame.time.delay(3000)


#MOUSE CLICK
    def mouse_click(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()
                for letter in self.letters:
                    x, y, char, visible = letter
                    if visible:
                        if math.sqrt((x - m_x) ** 2 + (y - m_y) ** 2) < radius:
                            letter[3] = False
                            self.guessed.add(char)
                            if char not in self.word:
                                self.Hangman_image_counter += 1
        return False


#RUN
    def run(self):
        clock = pygame.time.Clock()
        run = True


#main loop
        while run:
            clock.tick(60)

            if self.mouse_click():
                break

            self.draw()

            if all(letter in self.guessed for letter in self.word):
                self.display_message("You WON!")
                break

            if self.Hangman_image_counter == 6:
                self.display_message("You LOST!")
                break

        pygame.quit()


#running the game
game = HangmanGame()
game.run()
