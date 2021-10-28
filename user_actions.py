# (c) 2021 Itai Shek
def on_press_square(self, btn):
    if self.current_square:
        self.current_square.background_color = self.square_color
    self.current_square = btn
    self.current_square.background_color = self.square_color_when_pressed


def on_press_number(self, btn):
    if self.current_square:
        self.current_square.text = btn.text


def clear_board(self, *args):
    if self.current_square:
        self.current_square.background_color = self.square_color
        self.current_square = None
    for i in range(self.board_len):
        for j in range(self.board_len):
            self.board[i][j].text = ""


def on_keyboard_down(self, keyboard, keycode, text, modifiers):
    if keycode[1] in self.all_keys:
        if self.current_square:
            self.current_square.text = keycode[1]
    elif keycode[1] in ['backspace', 'delete', 'numpaddecimal']:
        self.on_press_del()
    return True


def keyboard_closed(self):
    self._keyboard.unbind(on_key_down=self.on_keyboard_down)
    self._keyboard = None


def on_press_del(self, *args):
    if self.current_square:
        self.current_square.text = ""


def on_press_solve(self, btn):
    # Disable solve button until it finishes
    btn.disabled = True

    empty = True

    # check if the initial board is valid
    for i, row in enumerate(self.board):
        for j, cell in enumerate(row):
            if cell.text and not self.is_board_valid(self.board, cell.text, (i, j)):
                self.unsolvable_popup(btn)
                return

            # check if the board is empty
            empty = empty and not cell.text

    if empty:
        btn.disabled = False
        return

    # solve the board
    if self.solve(self.board):
        self.current_square.background_color = self.square_color
        self.current_square = None
    else:
        self.unsolvable_popup(btn)

    btn.disabled = False
