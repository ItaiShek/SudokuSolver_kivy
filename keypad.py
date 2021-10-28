# (c) 2021 Itai Shek
from math import sqrt

from kivy.graphics import Color, Rectangle
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout


def init_keypad(self):

    self.keypad = BoxLayout()

    self.keypad.cols = 2
    self.keypad.orientation = "horizontal"

    numbers = GridLayout(cols=int(sqrt(self.board_len)))
    # Create the digit buttons
    for i in range(self.board_len):
        if i == 9:
            break
        text = str(i + 1)
        self.all_keys.append(text)
        numbers.add_widget(Button(text=text, on_press=self.on_press_number))

    # Add 'ABC' buttons for boards that are larger than 9X9
    while i < self.board_len-1:
        text = chr(56 + i)
        numbers.add_widget(Button(text=text, on_press=self.on_press_number))
        self.all_keys.append(chr(i+88))
        i += 1

    box = BoxLayout(orientation="vertical")
    box.add_widget(numbers)
    box.add_widget(Button(text="X", size_hint=(1, 0.3), on_press=self.on_press_del))
    self.keypad.add_widget(box)

    options = BoxLayout(orientation="vertical")
    options.add_widget(Button(text="Solve", on_press=self.on_press_solve))
    options.add_widget(Button(text="Clear", on_press=self.clear_board))
    options.add_widget(Button(text="About", on_press=self.about_popup))
    self.keypad.add_widget(options)
    self.add_widget(self.keypad)

    with self.canvas.before:
        Color(0, 0, 0, 1)
        self.keypad_bg = Rectangle(size=self.keypad.size, pos=self.keypad.pos)


def update_keypad(self, *args):
    smallest_size = self.get_smallest_dim()

    size = smallest_size/(self.board_len+4)
    space = self.space_between_squares * self.width
    board_width = self.board_len*size + space*(self.board_len - 1)

    y = 20

    keypad_width = dp(self.width/2)
    keypad_height = self.perspective_y - board_width - dp(2*y)

    keypad_pos_x = keypad_width*0.5
    keypad_pos_y = dp(y)

    self.keypad.size = (keypad_width, keypad_height)
    self.keypad.pos = (keypad_pos_x, keypad_pos_y)

    self.keypad_bg.pos = self.keypad.pos
    self.keypad_bg.size = self.keypad.size
