# from platform import python_branch
# from kiwisolver import strength
# from numpy import block
from shutil import move
from keyboard import play
import  pygame 
from pygame.locals import *


pygame.init()

screen_width = 1000
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption('  Breakout  Game  create by HMB')

#define  colures

bg = (255, 255, 255)

#block colours
block_red = (255, 153, 153)
block_yellow = (255,255,153)
block_green = (153, 255, 179)
block_blue = (153, 204, 255)


# block_red = (242, 85, 96)
# block_green = (86, 174, 87)
# block_blue = (69, 177, 232)

# Paddle color
paddle_col = (142,135,123)
paddle_outline = (100,100,100)

#define game variables

cols = 6
rows = 8
clock = pygame.time.Clock()
fps = 100


#brick wall class
class wall():
    def __init__(self):
        self.width = screen_width // cols
        self.height = 40

    def create_wall(self):
        self.blocks = []
        # define an empty list for an individual block
        block_individual = []
        for row in range(rows):
            #reset the block row list 
            block_row = []
            # iterate through each column in that row 
            for col in range(cols):
                block_x = col * self.width
                block_y = row * self.height
                rect = pygame.Rect(block_x, block_y, self.width, self.height)
                #assign block strenght based on row
                if row < 2:
                    strength = 4
                elif row < 4:
                    strength = 3
                elif row < 6:
                    strength = 2
                elif row < 8:
                    strength = 1
                # crete a list at this point to store the rect and colour data
                block_individual = [rect, strength]
                #append that individual block to the block row 
                block_row.append(block_individual)
            #append the row to the full list of blocks
            self.blocks.append(block_row)


    def draw_wall(self):
        for row in self.blocks:
            for block in row:
                #assign a color basded on strength
                if block[1] == 4:
                    block_col = block_blue
                elif block[1] == 3:
                    block_col = block_green
                elif block[1] == 2:
                    block_col = block_yellow
                elif block[1] == 1:
                    block_col = block_red
                
                pygame.draw.rect(screen, block_col, block[0])
                pygame.draw.rect(screen, bg, (block[0]), 1)



#paddle 

class paddle():
    def __init__(self):
        #define paddle variables
        self.height = 20
        self.width = int(screen_width / cols)
        self.x  = int((screen_width / 2) - (self.width / 2 ))
        self.y = screen_height - (self.height * 2)
        self.speed = 10
        self.rect = Rect(self.x, self.y, self.width, self.height)
        self.direction = 0


    def move(self):
        #reset movement direction 
        self.direction = 0
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
            self.direction = -1
        if key[pygame.K_RIGHT] and self.rect.right < screen_width:
            self.rect.x += self.speed
            self.direction = 1
    def draw(self):
        pygame.draw.rect(screen, paddle_col, self.rect)
        pygame.draw.rect(screen, paddle_outline, self.rect, 3)



    
# create a wall
wall = wall()
wall.create_wall()


# create paddle
player_paddle = paddle()

run = True
while run:
    clock.tick(fps)
    screen.fill(bg)
    #draw wall

    wall.draw_wall()

    #draw paddle
    player_paddle.draw()
    player_paddle.move()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

pygame.quit()
