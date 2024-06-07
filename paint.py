from pygame import *
import random

init()
size = width, height = 800, 600
screen = display.set_mode(size)
button = 0
# colors
RED = (255, 0, 0)
ORANGE = (255, 122, 56)
YELLOW = (255, 225, 56)
CYAN = (56, 255, 189)
BLUE = (56, 222, 255)
PURPLE = (155, 56, 255)
PINK = (255, 94, 199)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
GRAY = (145, 145, 145)
# random color
red = random.randint(1, 256)
green = random.randint(1, 256)
blue = random.randint(1, 256)
# texts and font
font = font.SysFont("Times New Roman", 20)
text = font.render("Random Color", True, WHITE)
text1 = font.render("Eraser", True, WHITE)
text2 = font.render("+", True, WHITE)
text3 = font.render("_", True, WHITE)
text4 = font.render("Star Brush", True, WHITE)
text5 = font.render("Clear", True, WHITE)
text6 = font.render("Add Bear", True, WHITE)
text7 = font.render("Save", True, WHITE)
# default settings
STARBRUSH = False
color = GREEN
drawcolor = True
SAVEFILE = False
brushsize = 8
starbrushsize = 25
ADDBEAR = False
screen.fill(BLACK)
# pics
starPic = image.load("star.png")
starPic = transform.scale(starPic, (starbrushsize, starbrushsize))
bearPic = image.load("bear.png")
bearPic = transform.scale(bearPic, (150, 150))


def getVal(tup):
  """ getVal returns the (position+1) of the first 1 within a tuple.
        This is used because MOUSEBUTTONDOWN and MOUSEMOTION deal with
        mouse events differently
    """
  for i in range(3):
    if tup[i] == 1:
      return i + 1
  return 0


def drawColourbox(screen, color):

  draw.rect(screen, RED, (0, 0, 75, 75))
  draw.rect(screen, ORANGE, (0, 75, 75, 75))
  draw.rect(screen, YELLOW, (0, 150, 75, 75))
  draw.rect(screen, GREEN, (0, 225, 75, 75))
  draw.rect(screen, CYAN, (0, 300, 75, 75))
  draw.rect(screen, BLUE, (0, 375, 75, 75))
  draw.rect(screen, PURPLE, (0, 450, 75, 75))
  draw.rect(screen, PINK, (0, 525, 75, 75))
  # eraser (black)
  draw.rect(screen, GRAY, (100, 20, 55, 25))
  screen.blit(text1, Rect(100, 20, 50, 25))
  # current color box
  draw.rect(screen, color, (170, 20, 30, 25))
  # save image
  draw.rect(screen, GRAY, (220, 20, 50, 25))
  screen.blit(text7, Rect(225, 20, 50, 25))
  # random color
  draw.rect(screen, GRAY, (300, 20, 120, 25))
  screen.blit(text, Rect(300, 20, 100, 50))
  # change brush size (+)
  draw.rect(screen, GRAY, (440, 20, 25, 25))
  screen.blit(text2, Rect(445, 20, 25, 25))
  # change brush size (-)
  draw.rect(screen, GRAY, (470, 20, 25, 25))
  screen.blit(text3, Rect(477, 13, 25, 25))
  # star brush
  draw.rect(screen, GRAY, (505, 20, 100, 25))
  screen.blit(text4, Rect(510, 20, 100, 25))
  # clear
  draw.rect(screen, GRAY, (610, 20, 60, 25))
  screen.blit(text5, Rect(615, 20, 60, 25))
  # add bear pic
  draw.rect(screen, GRAY, (680, 20, 85, 25))
  screen.blit(text6, Rect(685, 20, 85, 25))


def drawScene(screen, button, brushsize):
  global color
  # Draw circle if the left mouse button is down.
  mx, my = mouse.get_pos()

  if mx - brushsize > 75 and my - brushsize > 70:
    # color and eraser
    if button == 1 and drawcolor == True:
      draw.circle(screen, color, (mx, my), brushsize)
    # star brush
    if button == 1 and STARBRUSH == True:
      screen.blit(starPic, Rect(mx, my, starbrushsize, starbrushsize))
    if button == 1 and ADDBEAR == True:
      screen.blit(bearPic, Rect(mx, my, 150, 150))
    # clear
  display.flip()


def clearScene():
  draw.rect(screen, BLACK, (75, 70, 725, 530))
  display.flip()


def saveimage():
  drawing = Rect(75, 70, 725, 530)
  sub = screen.subsurface(drawing)
  image.save(sub, "imageSaved.png")
  display.update()


running = True
myClock = time.Clock()

# Game Loop
while running:
  for e in event.get():  # checks all events that happen
    if e.type == QUIT:
      running = False
    if e.type == MOUSEBUTTONDOWN:
      mx, my = e.pos
      button = e.button
      # choosing colors
      if mx < 75:
        if 0 < my < 75:
          drawcolor = True
          color = RED
          STARBRUSH = False
          ADDBEAR = False
        if 75 < my < 150:
          drawcolor = True
          color = ORANGE
          STARBRUSH = False
          ADDBEAR = False
        if 150 < my < 225:
          drawcolor = True
          color = YELLOW
          STARBRUSH = False
          ADDBEAR = False
        if 225 < my < 300:
          drawcolor = True
          color = GREEN
          STARBRUSH = False
          ADDBEAR = False
        if 300 < my < 375:
          drawcolor = True
          color = CYAN
          STARBRUSH = False
          ADDBEAR = False
        if 375 < my < 450:
          drawcolor = True
          color = BLUE
          STARBRUSH = False
          ADDBEAR = False
        if 450 < my < 525:
          drawcolor = True
          color = PURPLE
          STARBRUSH = False
          ADDBEAR = False
        if 525 < my < 600:
          drawcolor = True
          color = PINK
          STARBRUSH = False
          ADDBEAR = False
      # Eraser
      if 100 < mx < 150 and 20 < my < 45:
        drawcolor = True
        color = BLACK
        STARBRUSH = False
        ADDBEAR = False
      # generating random colors
      if 300 < mx < 425 and 20 < my < 45:
        color = (red, green, blue)
        red = random.randint(1, 255)
        green = random.randint(1, 255)
        blue = random.randint(1, 255)
        drawcolor = True
        STARBRUSH = False
        ADDBEAR = False
      # changing brush size (+)
      if 440 < mx < 465 and 20 < my < 45:
        if drawcolor == True:
          brushsize += 2
          if brushsize == 0:
            brushsize = 2
        if STARBRUSH == True:
          starbrushsize += 5
          starPic = transform.scale(starPic, (starbrushsize, starbrushsize))
      # changing brush size (-)
      if 470 < mx < 495 and 20 < my < 45:
        if drawcolor == True and brushsize >= 2:
          brushsize -= 2
        if STARBRUSH == True and starbrushsize > 15:
          starbrushsize -= 5
          starPic = transform.scale(starPic, (starbrushsize, starbrushsize))
      # star brush
      if 505 < mx < 605 and 20 < my < 45:
        STARBRUSH = True
        drawcolor = False
        ADDBEAR = False
      if 610 < mx < 670 and 20 < my < 45:
        clearScene()
      # add bear pic
      if 685 < mx < 770 and 20 < my < 45:
        ADDBEAR = True
        drawcolor = False
        STARBRUSH = False
      # save image
      if 220 < mx < 270 and 20 < my < 45:
        saveimage()

    if e.type == MOUSEMOTION:
      mx, my = e.pos
      button = getVal(e.buttons)
      if ADDBEAR == True:
        button = getVal(e.buttons) - 1

  drawScene(screen, button, brushsize)
  drawColourbox(screen, color)
  myClock.tick(450)

quit()
