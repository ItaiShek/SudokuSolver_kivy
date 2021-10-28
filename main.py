from kivy.config import Config

Config.set('graphics', 'width', '500')
Config.set('graphics', 'height', '600')


from kivy.properties import NumericProperty
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy import require, platform

require("2.0.0")


class MainWidget(Widget):
    from version import __version__
    from board import init_lines, init_squares, update_lines, update_squares, get_smallest_dim
    from keypad import init_keypad, update_keypad
    from user_actions import on_keyboard_down, keyboard_closed, clear_board
    from user_actions import on_press_number, on_press_square, on_press_del, on_press_solve
    from solver import solve, is_board_valid, find_empty_cell
    from popups import unsolvable_popup, about_popup

    perspective_x = NumericProperty(0)
    perspective_y = NumericProperty(0)

    space_between_squares = 0.0035

    board = []
    board_len = 9       # must be a perfect square, 4x4, 9x9, 16x16, etc...
    cpy_board = []

    square_color = (1, 1, 1)
    square_color_when_pressed = (198.0/232.0, 193.0/232.0, 147.0/232.0)

    h_lines = []    # Horizontal lines
    v_lines = []    # Vertical lines
    number_of_lines = 0
    line_color = (117.0/232.0, 117.0/232.0, 117.0/232.0)
    frame_line_color = (0, 0, 0)

    current_square = None
    keypad = None

    all_keys = []

    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)
        self.init_squares()
        self.init_lines()
        self.init_keypad()

        if self.is_desktop():
            self._keyboard = Window.request_keyboard(self.keyboard_closed, self)
            self._keyboard.bind(on_key_down=self.on_keyboard_down)

        self.bind(size=self.update_lines)
        self.bind(size=self.update_squares)
        self.bind(size=self.update_keypad)

    def is_desktop(self):
        if platform in ['linux', 'win', 'macosx']:
            return True
        return False


class SudokuSolver(App):
    def build(self):
        return MainWidget()


if __name__ == '__main__':
    SudokuSolver().run()
