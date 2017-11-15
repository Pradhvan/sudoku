
import argparse

from Tkinter imprt TK, canvas, Frame, Button, BOTH, TOP, BOTTOM

BOARDS = ['debug', 'noob', 'l33t', 'error']

MARGIN = 20

SIDE = 50

WIDTH = HEIGHT = MARGIN * 2 + SIDE * 9


class SudokuError(Exception):
    """ An application specific error """
    pass


class SudokuBoard(object):
    """Sudoku board representation"""
    def__init__(self, board_file):
        self.board = board_file 

