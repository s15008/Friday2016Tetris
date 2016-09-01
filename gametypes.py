import random

import pyglet

class TetrominoType(object):
    def __init__(self, block_image, blockGhostImage, local_block_coords_by_orientation):
        self.blockImage = block_image
        self.blockGhostImage = blockGhostImage
        self.localBlockCoordsByOrientation = local_block_coords_by_orientation

    @staticmethod
    def class_init(block_image, blockGhostImage, block_size):
        # 通常ミノ画像イメージ
        cyan = block_image.get_region(x=0, y=0, width=block_size,
                                      height=block_size)
        yellow = block_image.get_region(x=block_size, y=0, width=block_size,
                                        height=block_size)
        green = block_image.get_region(x=block_size * 2, y=0, width=block_size,
                                       height=block_size)
        red = block_image.get_region(x=block_size * 3, y=0, width=block_size,
                                     height=block_size)
        blue = block_image.get_region(x=block_size * 4, y=0, width=block_size,
                                      height=block_size)
        orange = block_image.get_region(x=block_size * 5, y=0,
                                        width=block_size, height=block_size)
        purple = block_image.get_region(x=block_size * 6, y=0,
                                        width=block_size, height=block_size)
        # ゴーストミノ画像イメージ
        cyan_g = blockGhostImage.get_region(x=0, y=0, width=block_size,
                                      height=block_size)
        yellow_g = blockGhostImage.get_region(x=block_size, y=0, width=block_size,
                                        height=block_size)
        green_g = blockGhostImage.get_region(x=block_size * 2, y=0, width=block_size,
                                       height=block_size)
        red_g = blockGhostImage.get_region(x=block_size * 3, y=0, width=block_size,
                                     height=block_size)
        blue_g = blockGhostImage.get_region(x=block_size * 4, y=0, width=block_size,
                                      height=block_size)
        orange_g = blockGhostImage.get_region(x=block_size * 5, y=0,
                                        width=block_size, height=block_size)
        purple_g = blockGhostImage.get_region(x=block_size * 6, y=0,
                                        width=block_size, height=block_size)

        TetrominoType.TYPES = [
            # type I
            TetrominoType(cyan, cyan_g,
                          {
                              Tetromino.RIGHT: [(0, 1), (1, 1), (2, 1), (3, 1)],
                              Tetromino.DOWN: [(1, 0), (1, 1), (1, 2), (1, 3)],
                              Tetromino.LEFT: [(0, 2), (1, 2), (2, 2), (3, 2)],
                              Tetromino.UP: [(2, 0), (2, 1), (2, 2), (2, 3)],
                          }
                          ),
            # type O
            TetrominoType(yellow, yellow_g,
                          {
                              Tetromino.RIGHT: [(0, 0), (0, 1), (1, 0), (1, 1)],
                              Tetromino.DOWN: [(0, 0), (0, 1), (1, 0), (1, 1)],
                              Tetromino.LEFT: [(0, 0), (0, 1), (1, 0), (1, 1)],
                              Tetromino.UP: [(0, 0), (0, 1), (1, 0), (1, 1)],
                          }
                          ),
            # type S
            TetrominoType(green, green_g,
                          {
                              Tetromino.RIGHT: [(2, 0), (1, 0), (1, 1), (0, 1)],
                              Tetromino.DOWN: [(1, 0), (1, 1), (2, 1), (2, 2)],
                              Tetromino.LEFT: [(2, 0), (1, 0), (1, 1), (0, 1)],
                              Tetromino.UP: [(1, 0), (1, 1), (2, 1), (2, 2)],
                          }
                          ),
            # type Z
            TetrominoType(red, red_g,
                          {
                              Tetromino.RIGHT: [(2, 2), (1, 2), (1, 1), (0, 1)],
                              Tetromino.DOWN: [(2, 0), (2, 1), (1, 1), (1, 2)],
                              Tetromino.LEFT: [(2, 2), (1, 2), (1, 1), (0, 1)],
                              Tetromino.UP: [(2, 0), (2, 1), (1, 1), (1, 2)],
                          }
                          ),
            # type J
            TetrominoType(blue, blue_g,
                          {
                              Tetromino.RIGHT: [(2, 1), (1, 1), (0, 1), (0, 2)],
                              Tetromino.DOWN: [(1, 0), (1, 1), (1, 2), (2, 2)],
                              Tetromino.LEFT: [(2, 0), (2, 1), (1, 1), (0, 1)],
                              Tetromino.UP: [(0, 0), (1, 0), (1, 1), (1, 2)],
                          }
                          ),
            # type L
            TetrominoType(orange, orange_g,
                          {
                              Tetromino.RIGHT: [(2, 2), (2, 1), (1, 1), (0, 1)],
                              Tetromino.DOWN: [(2, 0), (1, 0), (1, 1), (1, 2)],
                              Tetromino.LEFT: [(0, 0), (0, 1), (1, 1), (2, 1)],
                              Tetromino.UP: [(1, 0), (1, 1), (1, 2), (0, 2)],
                          }
                          ),
            # type T
            TetrominoType(purple, purple_g,
                          {
                              Tetromino.RIGHT: [(2, 1), (1, 1), (0, 1), (1, 2)],
                              Tetromino.DOWN: [(1, 0), (1, 1), (1, 2), (2, 1)],
                              Tetromino.LEFT: [(2, 1), (1, 1), (0, 1), (1, 0)],
                              Tetromino.UP: [(1, 0), (1, 1), (1, 2), (0, 1)],
                          }
                          ),
        ]

    @staticmethod
    def random_type():
        return random.choice(TetrominoType.TYPES)

class Tetromino(object):
    RIGHT, DOWN, LEFT, UP = range(4)
    CLOCKWISE_ROTATIONS = {RIGHT: DOWN, DOWN: LEFT, LEFT: UP, UP: RIGHT}

    def __init__(self):
        self.x = 0
        self.y = 0
        self.tetrominoType = TetrominoType.random_type()
        self.orientation = Tetromino.RIGHT
        self.blockBoardCoords = self.calc_block_board_coords()

    def get_deepcopy(self):
        copy = Tetromino()
        copy.x = self.x
        copy.y = self.y
        copy.tetrominoType = self.tetrominoType
        copy.orientation = self.orientation
        copy.blockBoardCoords = self.blockBoardCoords

        return copy

    def calc_block_board_coords(self):
        local_block_coords = self.tetrominoType.localBlockCoordsByOrientation[
            self.orientation]
        grid_coords = []
        for coord in local_block_coords:
            grid_coord = (coord[0] + self.x, coord[1] + self.y)
            grid_coords.append(grid_coord)
        return grid_coords

    def set_position(self, x, y):
        self.x = x
        self.y = y
        self.blockBoardCoords = self.calc_block_board_coords()

    def move_down(self):
        self.y -= 1
        self.blockBoardCoords = self.calc_block_board_coords()

    def move_up(self):
        self.y += 1
        self.blockBoardCoords = self.calc_block_board_coords()

    def move_left(self):
        self.x -= 1
        self.blockBoardCoords = self.calc_block_board_coords()

    def move_right(self):
        self.x += 1
        self.blockBoardCoords = self.calc_block_board_coords()

    def rotate_clockwise(self):
        self.orientation = Tetromino.CLOCKWISE_ROTATIONS[self.orientation]
        self.blockBoardCoords = self.calc_block_board_coords()

    def rotate_counterclockwise(self):
        self.orientation = Tetromino.CLOCKWISE_ROTATIONS[self.orientation]
        self.orientation = Tetromino.CLOCKWISE_ROTATIONS[self.orientation]
        self.orientation = Tetromino.CLOCKWISE_ROTATIONS[self.orientation]
        self.blockBoardCoords = self.calc_block_board_coords()

    def command(self, command):
        if command == Input.MOVE_DOWN:
            self.move_down()
        elif command == Input.MOVE_RIGHT:
            self.move_right()
        elif command == Input.MOVE_LEFT:
            self.move_left()
        elif command == Input.ROTATE_CLOCKWISE:
            self.rotate_clockwise()

    def undo_command(self, command):
        if command == Input.MOVE_DOWN:
            self.move_up()
        elif command == Input.MOVE_RIGHT:
            self.move_left()
        elif command == Input.MOVE_LEFT:
            self.move_right()
        elif command == Input.ROTATE_CLOCKWISE:
            self.rotate_counterclockwise()

    def clear_row_and_adjust_down(self, board_grid_row):
        new_block_board_coords = []
        for coord in self.blockBoardCoords:
            if coord[1] > board_grid_row:
                adjusted_coord = (coord[0], coord[1] - 1)
                new_block_board_coords.append(adjusted_coord)
            if coord[1] < board_grid_row:
                new_block_board_coords.append(coord)
        self.blockBoardCoords = new_block_board_coords
        return len(self.blockBoardCoords) > 0

    def draw(self, screen_coords, isGhost=False):
        if isGhost:
            image = self.tetrominoType.blockGhostImage
        else:
            image = self.tetrominoType.blockImage

        for coords in screen_coords:
            image.blit(coords[0], coords[1])

class Board(object):
    STARTING_ZONE_HEIGHT = 4
    HOLD_X = -7
    HOLD_Y = 15
    NEXT_X = 14
    NEXT_Y = 15
    NEXT_X2 = NEXT_X
    NEXT_Y2 = NEXT_Y - 5
    NEXT_X3 = NEXT_X2
    NEXT_Y3 = NEXT_Y2 - 5

    NEXT_BLOCK_MAX = 3

    def __init__(self, x, y, grid_width, grid_height, block_size):
        self.x = x
        self.y = y
        self.gridWidth = grid_width
        self.gridHeight = grid_height
        self.blockSize = block_size
        self.spawnX = int(grid_width * 1 / 3)
        self.spawnY = grid_height

        # 次のテトリミノのリスト
        self.nextTetrominos = []
        for _ in range(self.NEXT_BLOCK_MAX):
            self.nextTetrominos.append(Tetromino())
        self.set_next_tetrominos_position()

        # ホールド中のテトリミノ
        self.holdedTetromino = None
        self.isHolded = False

        # 落下中のテトリミノズ
        self.fallingTetromino = None
        self.spawn_tetrominos()
        self.tetrominos = []

        # ゴーストミノ
        self.ghostTetromino = Tetromino()
        self.update_ghost_tetrimino()

    """
    set_next_tetrominos_position
    ネクストテトリミノズにキューする
    """
    def set_next_tetrominos_position(self):
        self.nextTetrominos[0].set_position(Board.NEXT_X, Board.NEXT_Y)
        self.nextTetrominos[1].set_position(Board.NEXT_X2, Board.NEXT_Y2)
        self.nextTetrominos[2].set_position(Board.NEXT_X3, Board.NEXT_Y3)

    """
    spawn_tetrominos
    ネクストテトロミノリストから落下テトロミノにセットする
    """
    def spawn_tetrominos(self):
        self.fallingTetromino = self.nextTetrominos.pop(0)
        self.fallingTetromino.set_position(self.spawnX, self.spawnY)
        self.nextTetrominos.append(Tetromino())
        self.set_next_tetrominos_position()

    """
    command_falling_tetromino
    入力を見て移動可能であればテトロミノを入力方向に移動する
    """
    def command_falling_tetromino(self, command):
        self.fallingTetromino.command(command)
        if command == Input.ROTATE_CLOCKWISE:
            self.super_rotation()
        else:
            if not self.is_valid_position():
                print("other")
                self.fallingTetromino.undo_command(command)

    """
    super_rotation
    スーパーテーション
    """
    #TODO: スーパーローテーション
    def super_rotation(self):
        for coord in self.fallingTetromino.blockBoardCoords:
            # 左壁面に入り込んでいた場合
            if coord[0] < 0:
                self.fallingTetromino.command(Input.MOVE_RIGHT)
                if not self.is_valid_position():
                    print("not")
                    self.fallingTetromino.undo_command(Input.MOVE_RIGHT)
                    self.fallingTetromino.undo_command(Input.ROTATE_CLOCKWISE)
                print("side Left")
            # 左壁面に入り込んでいた場合
            elif coord[0] >= self.gridWidth:
                self.fallingTetromino.command(Input.MOVE_LEFT)
                self.fallingTetromino.command(Input.ROTATE_CLOCKWISE)
                if not self.is_valid_position():
                    self.fallingTetromino.undo_command(Input.MOVE_LEFT)
                print("side Right")
            else:
                if not self.is_valid_position():
                    print("noside")
        if not self.is_valid_position():
            self.fallingTetromino.undo_command(Input.ROTATE_CLOCKWISE)

    """
    hard_drop
    押した時点の落下予定位置にテトロミノを固定する
    ゴーストテトロミノ依存

    """
    def hard_drop(self):
        self.fallingTetromino.x = self.ghostTetromino.x
        self.fallingTetromino.y = self.ghostTetromino.y

    """
    hold_tetromino
    落下テトロミノとホールドテトロミノをスワッププレイする
    一度ホールドしたら新しいテトロミノになるまでホールド出来ない
    """
    def hold_tetromino(self):
        if self.isHolded:
            return
        self.isHolded = True

        # ホールドが空だった場合
        if self.holdedTetromino is None:
            self.holdedTetromino = self.fallingTetromino
            self.holdedTetromino.set_position(Board.HOLD_X , Board.HOLD_Y)
            self.spawn_tetrominos()
            self.isHolded = False
        else:
            tmp =  self.fallingTetromino
            self.fallingTetromino = self.holdedTetromino
            self.holdedTetromino = tmp
            self.fallingTetromino.set_position(self.spawnX, self.spawnY)
            self.holdedTetromino.set_position(Board.HOLD_X , Board.HOLD_Y)

    """
    update_ghost_tetrimino
    ゴーストテトリミノの位置を更新する
    """
    def update_ghost_tetrimino(self):
        self.ghostTetromino = self.fallingTetromino.get_deepcopy()
        while True:
            if not self.is_valid_position(self.ghostTetromino):
                self.ghostTetromino.undo_command(Input.MOVE_DOWN)
                break
            self.ghostTetromino.command(Input.MOVE_DOWN)

    """
    is_valid_position
    テトリミノが落下可能かどうかを判断する
    落下可能ならTrueを返す
    """
    def is_valid_position(self, targetTetromino=None):
        if targetTetromino is None: targetTetromino = self.fallingTetromino
        non_falling_block_coords = []
        for tetromino in self.tetrominos:
            non_falling_block_coords.extend(tetromino.blockBoardCoords)
        for coord in targetTetromino.blockBoardCoords:
            out_of_bounds = coord[0] < 0 or coord[0] >= self.gridWidth or coord[1] < 0
            overlapping = coord in non_falling_block_coords
            if out_of_bounds or overlapping:
                return False
        return True

    """
    find_full_rows
    横一列が揃っている列を探す
    """
    def find_full_rows(self):
        non_falling_block_coords = []
        for tetromino in self.tetrominos:
            non_falling_block_coords.extend(tetromino.blockBoardCoords)

        row_counts = {}
        for i in range(self.gridHeight + Board.STARTING_ZONE_HEIGHT):
            row_counts[i] = 0
        for coord in non_falling_block_coords:
            row_counts[coord[1]] += 1

        full_rows = []
        for row in row_counts:
            if row_counts[row] == self.gridWidth:
                full_rows.append(row)
        return full_rows

    def clear_row(self, grid_row):
        tetrominos = []
        for tetromino in self.tetrominos:
            if tetromino.clear_row_and_adjust_down(grid_row):
                tetrominos.append(tetromino)
        self.tetrominos = tetrominos

    def clear_rows(self, grid_rows):
        grid_rows.sort(reverse=True)
        for row in grid_rows:
            self.clear_row(row)

    """
    update_tick
    テトリミノ落下時の処理
    """
    def update_tick(self, isInfinity):
        num_cleared_rows = 0
        game_lost = False
        self.fallingTetromino.command(Input.MOVE_DOWN)
        if not self.is_valid_position():
            self.fallingTetromino.undo_command(Input.MOVE_DOWN)
            if not isInfinity:
                self.tetrominos.append(self.fallingTetromino)
                full_rows = self.find_full_rows()
                self.clear_rows(full_rows)
                game_lost = self.is_in_start_zone(self.fallingTetromino)
                if not game_lost:
                    self.spawn_tetrominos()
                num_cleared_rows = len(full_rows)
                # テトロミノが落下したらホールド禁止を解除する
                self.isHolded = False

        return num_cleared_rows, game_lost

    def is_in_start_zone(self, tetromino):
        for coords in tetromino.blockBoardCoords:
            if coords[1] >= self.gridHeight:
                return True
        return False

    def grid_coords_to_screen_coords(self, coords):
        screen_coords = []
        for coord in coords:
            coord = (self.x + coord[0] * self.blockSize,
                     self.y + coord[1] * self.blockSize)
            screen_coords.append(coord)
        return screen_coords

    def draw(self):
        # 積まれてるミノの描画
        for tetromino in self.tetrominos:
            screen_coords = self.grid_coords_to_screen_coords(
                tetromino.blockBoardCoords)
            tetromino.draw(screen_coords)

        # ゴーストテトロミノの描画
        if self.ghostTetromino is not None:
            screen_coords = self.grid_coords_to_screen_coords(self.ghostTetromino.blockBoardCoords)
            self.ghostTetromino.draw(screen_coords, isGhost=True)

        # 落下ミノの描画
        screen_coords = self.grid_coords_to_screen_coords(self.fallingTetromino.blockBoardCoords)
        self.fallingTetromino.draw(screen_coords)

        # ネクストテトリミノの描画
        for mino in self.nextTetrominos:
            screen_coords = self.grid_coords_to_screen_coords(mino.blockBoardCoords)
            mino.draw(screen_coords)

        # ホールドテトロミノの描画
        if self.holdedTetromino is not None:
            screen_coords = self.grid_coords_to_screen_coords(self.holdedTetromino.blockBoardCoords)
            self.holdedTetromino.draw(screen_coords)

class InfoDisplay(object):
    ROWS_CLEARED_X = 180
    ROWS_CLEARED_Y = 155
    SCORE_POINTS_X = 180
    SCORE_POINTS_Y = 305


    def __init__(self, window):
        self.rowsClearedLabel = pyglet.text.Label('0',
                                                  font_size=14,
                                                  x=InfoDisplay.ROWS_CLEARED_X,
                                                  y=InfoDisplay.ROWS_CLEARED_Y
                                                  )
        self.scorePointsLabel = pyglet.text.Label('0',
                                                  font_size=14,
                                                  x=InfoDisplay.SCORE_POINTS_X,
                                                  y=InfoDisplay.SCORE_POINTS_Y
                                                  )

        self.pausedLabel = pyglet.text.Label('PAUSED',
                                             font_size=32,
                                             x=window.width // 2,
                                             y=window.height // 2,
                                             anchor_x='center',
                                             anchor_y='center'
                                             )
        self.gameoverLabel = pyglet.text.Label('GAME OVER',
                                               font_size=32,
                                               x=window.width // 2,
                                               y=window.height // 2,
                                               anchor_x='center',
                                               anchor_y='center'
                                               )
        self.showPausedLabel = False
        self.showGameoverLabel = False

    """
    set_rows_cleared
    削除したラインの数の描画を更新する　
    """
    def set_rows_cleared(self, num_rows_cleared):
        self.rowsClearedLabel.text = str(num_rows_cleared)

    """
    set_score_points
    スコアポイントの描画を更新する　
    """
    def set_score_points(self, score_points):
        self.scorePointsLabel.text = str(score_points)

    def draw(self):
        self.rowsClearedLabel.draw()
        self.scorePointsLabel.draw()
        if self.showPausedLabel:
            self.pausedLabel.draw()
        if self.showGameoverLabel:
            self.gameoverLabel.draw()

class Input(object):
    TOGGLE_PAUSE, MOVE_DOWN, MOVE_LEFT, MOVE_RIGHT, ROTATE_CLOCKWISE, TOGGLE_HOLD, Z = range(7)

    def __init__(self):
        self.action = None

    def process_keypress(self, symbol, modifiers):
        if symbol == pyglet.window.key.SPACE:
            self.action = Input.TOGGLE_PAUSE
        if symbol == pyglet.window.key.LSHIFT:
            self.action = Input.TOGGLE_HOLD
        if symbol == pyglet.window.key.Z:
            self.action = Input.Z

    def process_text_motion(self, motion):
        if motion == pyglet.window.key.MOTION_LEFT:
            self.action = Input.MOVE_LEFT
        elif motion == pyglet.window.key.MOTION_RIGHT:
            self.action = Input.MOVE_RIGHT
        elif motion == pyglet.window.key.MOTION_UP:
            self.action = Input.ROTATE_CLOCKWISE
        elif motion == pyglet.window.key.MOTION_DOWN:
            self.action = Input.MOVE_DOWN

    def consume(self):
        action = self.action
        self.action = None
        return action

class GameTick(object):
    def __init__(self, tick_on_first_call=False):
        self.tick = tick_on_first_call
        self.started = tick_on_first_call

    def is_tick(self, next_tick_time):
        def set_tick(dt):
            self.tick = True

        if not self.started:
            self.started = True
            pyglet.clock.schedule_once(set_tick, next_tick_time)
            return False
        elif self.tick:
            self.tick = False
            pyglet.clock.schedule_once(set_tick, next_tick_time)
            return True
        else:
            return False

class Game(object):
    TICK_SPEED_0 = 0.6
    TICK_SPEED_1 = 0.4
    TICK_SPEED_2 = 0.2
    TICK_SPEED_3 = 0.1
    TICK_SPEED_4 = 0.05
    SCORE_LINE_0 = 0
    SCORE_LINE_1 = 5
    SCORE_LINE_2 = 10
    SCORE_LINE_3 = 15
    SCORE_LINE_4 = 20

    def __init__(self, board, info_display, key_input, background_image):
        self.board = board
        self.infoDisplay = info_display
        self.input = key_input
        self.backgroundImage = background_image
        self.paused = False
        self.lost = False
        self.numRowsCleared = 0 #削除したラインの数
        self.scorePoints = 0 #スコア
        self.tickSpeed = self.TICK_SPEED_0 #落下スピード間隔
        self.ticker = GameTick()

        # インフィニティ
        self.isInfinity = False

    """
    add_rows_cleared
    削除した列を加算する
    """
    def add_rows_cleared(self, rows_cleared):
        self.numRowsCleared += rows_cleared
        self.infoDisplay.set_rows_cleared(self.numRowsCleared)

    """
    add_score_points
    削除した列に応じてスコアポイントを加算する
    """
    def add_score_points(self, rows_cleared):
        if rows_cleared <= 0:
            return
        elif rows_cleared == 1:
            self.scorePoints += 1
        elif rows_cleared == 2:
            self.scorePoints += 2
        elif rows_cleared == 3:
            self.scorePoints += 5
        elif rows_cleared <= 4:
            self.scorePoints += 8

        self.infoDisplay.set_score_points(self.scorePoints)

    """
    change_tick_speed
    スコアポイントに応じたテトロミノの落下スピード変更
    """
    def change_tick_speed(self, scorePoints):
        if scorePoints >= self.SCORE_LINE_4:
            self.tickSpeed = self.TICK_SPEED_4
        elif scorePoints >= self.SCORE_LINE_3:
            self.tickSpeed = self.TICK_SPEED_3
        elif scorePoints >= self.SCORE_LINE_2:
            self.tickSpeed = self.TICK_SPEED_2
        elif scorePoints >= self.SCORE_LINE_1:
            self.tickSpeed = self.TICK_SPEED_1
        else:
            self.tickSpeed = self.TICK_SPEED_0

    def toggle_pause(self):
        self.paused = not self.paused
        self.infoDisplay.showPausedLabel = self.paused

    def update(self):
        if self.lost:
            self.infoDisplay.showGameoverLabel = True
        else:
            command = self.input.consume()
            if command == Input.TOGGLE_PAUSE:
                self.toggle_pause()
            if not self.paused:
                if command and command != Input.TOGGLE_PAUSE:
                    self.isInfinity = True
                    self.board.command_falling_tetromino(command)
                    if command == Input.TOGGLE_HOLD:
                        self.board.hold_tetromino()
                    if command == Input.Z:
                        self.board.hard_drop()
                        self.isInfinity = False
                if self.ticker.is_tick(self.tickSpeed) or command == Input.Z:
                    rows_cleared, self.lost = self.board.update_tick(self.isInfinity)
                    self.add_rows_cleared(rows_cleared)
                    self.add_score_points(rows_cleared)
                    self.change_tick_speed(self.scorePoints)
                    self.isInfinity = False
                self.board.update_ghost_tetrimino()

    def draw(self):
        self.backgroundImage.blit(0, 0)
        self.board.draw()
        self.infoDisplay.draw()
