from math import sqrt
from kivy.graphics import Color, Line
from kivy.uix.button import Button


def init_squares(self):
    with self.canvas:
        for i in range(self.board_len):
            self.board.append([])
            for j in range(self.board_len):
                self.board[i].append(Button(text="",
                                            color=(0, 0, 0),
                                            background_normal='',
                                            background_down='',
                                            background_color=self.square_color,
                                            on_press=self.on_press_square)
                                     )
                self.add_widget(self.board[i][j])


def init_lines(self):
    sq = int(sqrt(self.board_len))
    self.number_of_lines = self.board_len + 1

    self.h_lines = [None] * self.number_of_lines
    self.v_lines = [None] * self.number_of_lines

    with self.canvas:
        # inner lines
        Color(*self.line_color)
        for i in range(1, self.number_of_lines):
            if i % sq == 0:
                continue
            self.h_lines[i] = Line()
            self.v_lines[i] = Line()

        # frame
        Color(*self.frame_line_color)
        for i in range(0, self.number_of_lines, sq):
            self.h_lines[i] = Line()
            self.v_lines[i] = Line()


def update_squares(self, *args):
    smallest_size = self.get_smallest_dim()

    offset = -int(self.board_len / 2)
    size = smallest_size/(self.board_len+4)
    space = self.space_between_squares * self.width
    const_x = self.perspective_x - 0.5*(self.board_len % 2)*size

    for i in range(self.board_len):
        square_y = self.perspective_y - (i + 1)*size - (i * space)
        for j in range(self.board_len):
            square_x = const_x + (offset+j)*(size+space)
            self.board[i][j].pos = (square_x, square_y)
            self.board[i][j].size = (size, size)
            self.board[i][j].font_size = 0.6*size


def update_lines(self, *args):
    smallest_size = self.get_smallest_dim()

    size = smallest_size/(self.board_len+4)
    space = self.space_between_squares * self.width
    board_width = self.board_len*size + space*(self.board_len - 1)
    offset_x = self.perspective_x - board_width/2
    line_space = board_width/(self.number_of_lines-1)
    line_width = space

    for i in range(self.number_of_lines):
        # Vertical lines
        x1 = i*line_space + offset_x
        y1 = self.perspective_y - board_width
        x2 = x1
        y2 = self.perspective_y

        self.h_lines[i].points = (x1, y1, x2, y2)
        self.h_lines[i].width = line_width

        # Horizontal lines
        x1 = offset_x
        x2 = offset_x + board_width
        y1 = self.perspective_y - i*line_space
        y2 = y1

        self.v_lines[i].points = (x1, y1, x2, y2)
        self.v_lines[i].width = line_width


def get_smallest_dim(self):
    smallest_size = self.height if self.height < self.width else self.width
    return smallest_size
