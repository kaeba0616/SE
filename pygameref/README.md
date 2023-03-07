## game loop

1. Handles events

   - The main loop also has code that updates the game state based on which events have been created. This is usually called event handling.

   `pygame.event.get()`

2. Updates the game state
3. Draws the game state to the screen

## pygame.locals

- pygame has a constant variable for each of possible types in the pygame.locals modules
- since we used the "from pygame.locals import \*", we only have to type QUIT instead of pygame.locals.QUIT

` if event.type == pygame.locals.QUIT: => if event.type == QUIT:`

## pygame.quit()

- sort of the opposite of the pygame.init() function : it runs code that deactives the Pygame library.
- Your programs should always call pygame.quit() before they call sys.exit() to terminate the program.
  - Normally it doesn't really matter since Python closes it when the program exits anyway. But there is a bug in IDLE that
    causes IDLE to hang if a Pygame program terminates before pygame.quit() is called.
  - e.g. if you has pygame.QUIT event as soons as start the program, IDLE tell me key_get() error

## Pixel Coordinates

        X

0 1 2 3 4 5 6 7
1
2
Y 3
4
5
6

## display Surface

- the Surface object returned by pygame.display.set_mode() is called the display Surface
- anything that is drawn on the display surface object will be displayed on the window when the pygame.display.update() function is called
- it is a lot faster to draw on a Surface object than to draw a Surface object to the computer screen.

```
  DISPLAYSURF = pygame.display.set_mode((500,400),0,32)
  # (500, 400) = width, height / 0 = kind of flag e.g. pygame.RESIZABLE, pygame.FULLSCREEN / 32 = bits depth of color
```

## color

Color RGB Values
Aqua ( 0, 255, 255)
Black ( 0, 0, 0)
Blue ( 0, 0, 255)
Fuchsia (255, 0, 255)
Gray (128, 128, 128)
Green ( 0, 128, 0)
Lime ( 0, 255, 0)
Maroon (128, 0, 0)
Navy Blue ( 0, 0, 128)
Olive (128, 128, 0)
Purple (128, 0, 128)
Red (255, 0, 0)
Silver (192, 192, 192)
Teal ( 0, 128, 128)
White (255, 255, 255)
Yellow (255, 255, 0)

## Transparent Colors

- alpha value
  - it is a measure of how opaque( that is, not transparent) a color is.
  - with colors that have an alpha value, you can instead just colored tint to the color that is already there
  - an alpha value of 0 means the color is completely transparent and invisible
  - e.g. ( 0, 255, 0, 255)

` anotherSurface = DISPLAYSURF.convert_alpha()`

- pygame.color objects
  ```import pygame
      pygame.Color(255,0,0)
      myCOlor = pygame.Color(255,0,0,128)
      myCOlor == (255,0,0,128)
  ```

## RECT objects

1. The X coordinate of the top left corner.
2. The Y coordinate of the top right corner.
3. The width(in pixels) of the rectangle.
4. The height(in pixels) of the rectangle.

```import pygame
    spamRect = pygame.Rect(10,20,200,300)
    spamRect == (10,20,200,300)

    spamRect.right
    # print 210!! because start pixel is 10 and width is 200.

    spamRect.right = 350
    spam.left
    # print 150!! because right pixel is 350 and width is 200.
```

Attribute Name Description
myRect.left The int value of the X-coordinate of the left side of the rectangle.
myRect.right The int value of the X-coordinate of the right side of the rectangle.
myRect.top The int value of the Y-coordinate of the top side of the rectangle.
myRect.bottom The int value of the Y-coordinate of the bottom side.
myRect.centerx The int value of the X-coordinate of the center of the rectangle.
myRect.centery The int value of the Y-coordinate of the center of the rectangle.
myRect.width The int value of the width of the rectangle.
myRect.height The int value of the height of the rectangle.
myRect.size A tuple of two ints: (width, height)
myRect.topleft A tuple of two ints: (left, top)
myRect.topright A tuple of two ints: (right, top)
myRect.bottomleft A tuple of two ints: (left, bottom)
myRect.bottomright A tuple of two ints: (right, bottom)
myRect.midleft A tuple of two ints: (left, centery)
myRect.midright A tuple of two ints: (right, centery)
myRect.midtop A tuple of two ints: (centerx, top)
myRect.midbottom A tuple of two ints: (centerx, bottom)

## pygame module for drawing shapes

pygame.draw.rect 화면에 사각형을 그려줍니다  
 pygame.draw.ploygon 화면에 삼각형을 그려줍니다.
pygame.draw.circle 화면에 원을 그려줍니다.
pygame.draw.ellipse 화면에 타원을 그려줍니다.
pygame.draw.arc 화면에 원하는 만큼의 원을 그려줍니다.
원을 얼마나 그려줄지 정할 수 있습니다.  
 pygame.draw.line 화면에 선을 그려줍니다.
pygame.draw.lines 화면에 여러 개의 선을 이어서 그려줍니다.
pygame.draw.aaline 화면에 부드러운 선을 그려줍니다.
pygame.draw.aalines 화면에 부드러운 선을 여러개 이어서 그려줍니다.

## Primitive Drawing Functions [1.1]

```
import pygame, sys
from pygame.locals import *

pygame.init()


# set up the window
DISPLAYSURF = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption("Drawing")

# set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# draw on the surface object
DISPLAYSURF.fill(WHITE)

# ploygon - 삼각형
pygame.draw.polygon(
    DISPLAYSURF, GREEN, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106))
)
pygame.draw.line(DISPLAYSURF, BLUE, (60, 60), (120, 60), 4)
pygame.draw.line(DISPLAYSURF, BLUE, (120, 60), (60, 120))
pygame.draw.line(DISPLAYSURF, BLUE, (60, 120), (120, 120), 4)
pygame.draw.circle(DISPLAYSURF, BLUE, (300, 50), 20, 0)
pygame.draw.ellipse(DISPLAYSURF, RED, (300, 250, 40, 80), 1)
pygame.draw.rect(DISPLAYSURF, RED, (200, 150, 100, 50))

pixObj = pygame.PixelArray(DISPLAYSURF)
pixObj[480][380] = BLACK
pixObj[482][382] = BLACK
pixObj[484][384] = BLACK
pixObj[486][386] = BLACK
pixObj[488][388] = BLACK
del pixObj

# run the game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()


if __name__ == "__main__":
    main()
```
