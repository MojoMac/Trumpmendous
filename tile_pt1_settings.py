import pygame as pg
import tile_pt1_sprites as gs
pg.mixer.init()
#defining colors for objects in scene using RGB parameters
WHITE = (255, 255, 255)
BLACK = (0,0,0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0,255,0)
ORANGE = (255, 89, 0)
YELLOW = (255,204,0)
PURPLE = (67, 0, 148)

#set the screen size [width, height]
WIDTH = 1280
HEIGHT = 736

#frame rate
FPS = 240

#player settings
PLAYERGRAV = .6


PLAYERSPEED = 6

#standard size
TILESIZE = 32
TILEIMG = pg.image.load("gray brick tile.png")
TRAPIMG = pg.image.load('lava trap.jpg')
BOTTOMLAYERIMG = pg.image.load('lavalayer.jpg')
ENDGOALIMG = pg.image.load('goldblock.png')

hitsound = pg.mixer.Sound('Wilhelm Scream sound effect - Copy.wav')
hitsound.set_volume(1000)
#game title
TITLE = 'Get Jiggy with it'

TILEMAP1 = ['111111111111111111111111111111111111111111111111111111gggg1',
            '1.........................................................1',
            '1.........................................................1',
            '1.........................................................1',
            '1.........................................................1',
            '1.....................................................1...1',
            '1.........................................................1',
            '1.........................................................1',
            '1.........................................................1',
            '1........................................................11',
            '1.......................................................111',
            '1....1........1.....1......1....................1......1111',
            '1....1....................................................1',
            '1...11.......................... ..1.....1................1',
            '1.........................................................1',
            '1.........................................................1',
            '1.........................................................1',
            '11........................................................1',
            '1.........................................................1',
            '1.........................................................1',
            '1.....11.....1............................................1',
            '1............1111........11...............................1',
            '1.........................................................1',
            '1.........................................................1',
            '1..............................1..........................1',
            '1.........................................................1',
            '1.........................................................1',
            '1.........................................................1',
            '1...............1.......1111..............................1',
            '1.........................................................1',
            '1.........................................................1',
            '1.........................................................1',
            '1.............1...........................................1',
            '1.........................................................1',
            '1.........................................................1',
            '1..................................................1......1',
            '1...............11..........................1.............1',
            '1.................................111.....................1',
            '1......................1...1..............................1',
            '1.....................................................1...1',
            '1.........................................................1',
            '1.........................................................1',
            '1.........................................................1',
            '1........................................................11',
            '1.........................................................1',
            '1.........................................................1',
            '1.........................................................1',
            '1....................................................111111',
            '1...................................................1111111',
            '1..................................................11111111',
            '1.................................................111111111',
            '1.........................................................1',
            '1.........................................................1',
            '1.........................................11..............1',
            '1.........................................................1',
            '1..................1......1...............................1',
            '1........111.......................11.....................1',
            '1.........................................................1',
            '1.........................................................1',
            '111.......................................................1',
            '1111......................................................1',
            '1.........................................................1',
            '1.........................................................1',
            '1.........11......11......1111111.........................1',
            '1.......................................111......1........1',
            '1.........................................................1',
            '1........................................................11',
            '1.........................................................1',
            '1.........................................................1',
            '1.........................................................1',
            '1......................................................1..1',
            '1.........................................................1',
            '1.........................................................1',
            '1.........................................................1',
            '1........................................................11',
            '1.........................................................1',
            '1.........................................................1',
            '1.........................................................1',
            '1.................................................1111....1',
            '1.........................................................1',
            '1..........................111.......11....1..............1',
            '1.........................................................1',
            '1..................111....................................1',
            '1.........................................................1',
            '1..........111............................................1',
            '1.....1...................................................1',
            '1....11...................................................1',
            '1.p.111...................................................1',
            '1111111...................................................1',
            '1111111...................................................1',
            '11111111111111111111111111111111111111111111111111111111111'
            ]


#tiles info
TILEWIDTH = TILESIZE
TILEHEIGHT = TILESIZE
MAPWIDTH = len(TILEMAP1[0]) * TILEWIDTH
MAPHEIGHT = len(TILEMAP1) * TILEHEIGHT

MAPIMG = 'trump game wallpaper 2.jpg'

print(MAPWIDTH)