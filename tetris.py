import pyglet

import gametypes

WIDTH = 800
HEIGHT = 600
BOARD_X = 275
BOARD_Y = 50
GRID_WIDTH = 10
GRID_HEIGHT = 20
BLOCK_SIZE = 25

window = pyglet.window.Window(WIDTH, HEIGHT)
window.set_vsync(False)

###### load resources ######
backgroundImage = pyglet.resource.image('background.png')
blocksImage = pyglet.resource.image('blocks.png')
blocksGhostImage = pyglet.resource.image('blocks_ghost.png')
gametypes.TetrominoType.class_init(blocksImage, blocksGhostImage, BLOCK_SIZE)

###### init game state ######
board = gametypes.Board(BOARD_X, BOARD_Y, GRID_WIDTH, GRID_HEIGHT, BLOCK_SIZE)
infoDisplay = gametypes.InfoDisplay(window)
input = gametypes.Input()
game = gametypes.Game(board, infoDisplay, input, backgroundImage)

@window.event
def on_key_press(symbol, modifiers):
    input.process_keypress(symbol, modifiers)

@window.event
def on_text_motion(motion):
    input.process_text_motion(motion)

@window.event
def on_draw():
    game.draw()

def update(dt):
    game.update()

pyglet.clock.schedule_interval(update, 1 / 60.0)
pyglet.app.run()