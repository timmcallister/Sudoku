#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 09:38:15 2019
@author: tim
"""


class Board():
    def __init__(self):
        self.rows, self.cols = (9, 9)
        self.board = [[None for i in range(self.cols)]
                      for j in range(self.rows)]

    def set_square(self, row, column, value):
        self.board[row][column] = value

    def unset_square(self, row, column):
        self.board[row][column] = None

    def draw_board(self):
        for i in range(self.rows):
            print('| ', end='')
            for j in range(self.cols):
                block = self.board[i][j]
                if (block):
                    print(' ' + str(block), end=' ')
                else:
                    print(' - ', end='')
                if ((j + 1) % 3 == 0):
                    print('|', end='')

            print('\n')
            if ((i + 1) % 3 == 0):
                for i in range(self.cols - 3):
                    print(' === ', end='')
            print('\n')

    def in_row(self, row, value):
        return value in self.board[row]

    def in_col(self, col, value):
        search_col = []

        for i in range(len(self.board)):
            search_col.append(self.board[i][col])

        return value in search_col

    def in_block(self, row, col, value):
        x_val = int(col / 3)
        y_val = int(row / 3)

        search_block = []

        for i in range(int(len(self.board) / 3)):
            for j in range(int(len(self.board[0]) / 3)):
                search_block.append(self.board[j + y_val * 3][i + x_val * 3])

        return value in search_block

    def is_valid(self, row, col, val):

        return not (self.in_row(row, val) or self.in_col(col, val)
                    or self.in_block(row, col, val))
        
    def get_board(self):
        return self.board

    def set_board(self, brd):
      if len(brd) != 9:
        print("Cannot set board!")
        return False
      
      for i in brd:
        if len(i) != 9:
          print("Cannot set board!")
          return False

      self.board = brd




def solve(brd):

    empty_spaces = []
    
    for row_index, row in enumerate(brd.get_board()):
        for col_index, col in enumerate(row):
            if col == None:
                empty_spaces.append((row_index, col_index))
                
    if not empty_spaces:
        return brd
    
    target = empty_spaces[0]

    for i in range(9):
        if brd.is_valid(target[0], target[1], i+1):
            brd.set_square(target[0], target[1], i+1)
            solution = solve(brd)
            if not solution:
                brd.unset_square(target[0], target[1])
            else: 
                return solution
                
    return False

input_board = []

print("Please enter the board using 0's for empty spaces: ")

for i in range(9):
  input_board.append([None if int(x) == 0 else int(x) for x in input()])

brd = Board()

brd.set_board(input_board)

solution = solve(brd)

print('\n\n')

solution.draw_board()


            
