from math import sqrt


# returns the row and column of the first empty cell
def find_empty_cell(self, b):
    for i in range(self.board_len):
        for j in range(self.board_len):
            if b[i][j].text == '':
                return i, j

    return None


# True - valid
def is_board_valid(self, b, num, pos):
    row, col = pos

    # check row
    for i in range(self.board_len):
        if b[row][i].text == num and i != col:
            return False

    # check column
    for i in range(self.board_len):
        if b[i][col].text == num and i != row:
            return False

    # check box
    sq = int(sqrt(self.board_len))
    box_row = sq*(row//sq)
    box_col = sq*(col//sq)

    for i in range(box_row, box_row + sq):
        for j in range(box_col, box_col + sq):
            if b[i][j].text == num and pos != (i, j):
                return False

    return True


# solve with backtracking
def solve(self, b):
    pos = self.find_empty_cell(b)
    if not pos:
        return True     # Done

    row, col = pos

    for num in self.all_keys:
        if self.is_board_valid(b, num, pos):
            b[row][col].text = num

            if self.solve(b):
                return True

            b[row][col].text = ''

    return False
