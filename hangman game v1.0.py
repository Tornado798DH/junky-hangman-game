#JUST SAYING HI :)
#Tornado DH

import pygame
import math
import random

#display settings
pygame.init()

width = 1200
height = 500

win = pygame.display.set_mode((width,height))
pygame.display.set_caption("hangman game by the greatest Tornado DH")

#varibles
WHITE=(255,255,255)
BLACK = (0,0,0)

Letter_Font = pygame.font.SysFont("comicsans",40)
Word_Font = pygame.font.SysFont('comicsans', 60)
Title_Font = pygame.font.SysFont('comicsans', 70)

Hangman_image_counter=0
words = ["IDE", "REPLIT", "PYTHON", "PYGAME","TALL","TEST","HAPPY","INTERNATIONAL","MECHATRONICS"]
word = random.choice(words)
guessed = []

#resources load
images = []

for i in range(7):
    image = pygame.image.load("resources/hangman"+str(i)+".png")
    images.append(image)

#buttons settings
radius = 20
gap = 15
start_x = round((width - (radius*2 + gap)*13) / 2)
start_y = 400
A = 65
letters = []

for i in range(26):
    x= start_x + gap*2 + ((radius*2 + gap)*(i % 13))
    y= start_y +((radius*2 + gap)*(i // 13))
    letters.append([x,y,chr(A+i),True])

#drawing and that stuff
def buttons_draw():
    for ltr in letters:
        x,y,letter,visible = ltr
        if visible:
            pygame.draw.circle(win, BLACK, (x, y), radius, 3)
            text = Letter_Font.render(letter, 1, BLACK)
            win.blit(text, (x - text.get_width() / 2, y - text.get_height() / 2))

def title_draw():
    text = Title_Font.render("HANGMAN", 1, BLACK)
    win.blit(text, (width / 2 - text.get_width() / 2, 20))

def word_draw():
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = Word_Font.render(display_word, 1, BLACK)
    win.blit(text, (400, 200))

def draw():
    win.fill(WHITE)

    title_draw()
    word_draw()
    buttons_draw()

    win.blit(images[Hangman_image_counter], (150, 100))
    pygame.display.update()

def mouse_click():
    global Hangman_image_counter
    global run

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        position_Of_Mouse = pygame.MOUSEBUTTONDOWN
        if event.type == position_Of_Mouse:
            m_x, m_y = pygame.mouse.get_pos()
            for ltr in letters:
                x, y, letter, visible = ltr
                if visible:
                    dis = math.sqrt((x - m_x) ** 2 + (y - m_y) ** 2)
                    if radius > dis:
                        ltr[3] = False
                        guessed.append(letter)
                        if letter not in word:
                            Hangman_image_counter += 1

def display_message(message):
    pygame.time.delay(1000)
    win.fill(WHITE)
    text = Word_Font.render(message, 1, BLACK)
    win.blit(text, (width/2 - text.get_width()/2, height/2 - text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(3000)

#game loop settings
clock = pygame.time.Clock()
run = True

while run:
    clock.tick(60)

    mouse_click()
    draw()

    won = True
    for letter in word:
        if letter not in guessed:
            won = False
            break

    if won:
        display_message("You WON!")
        break
    if Hangman_image_counter == 6:
        display_message("You LOST!")
        break