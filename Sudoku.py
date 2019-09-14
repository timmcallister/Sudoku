#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 09:38:15 2019

@author: tim
"""

class Board:
    def __init__(self):
        pass
        self.rows, self.cols = (9, 9)
        self.board = [[None for i in range(self.cols)] for j in range(self.rows)]
    
    def set_square(self, row, column, value):
        self.board[row][column] = value

    def unset_square(self, row, column):
        self.board[row][column] = None
        
    def temp_square(self, row, column, value, brd):
        brd[row][column] = value
        return brd

    def untemp_square(self, row, column, brd):
        brd[row][column] = None
        return brd
        
    def draw_board(self):
        for i in range(self.rows):
            print('| ', end='')
            for j in range(self.cols):
                block = self.board[i][j]
                if(block):
                    print(' ' + str(block), end=' ')
                else:
                    print(' - ', end='')
                if  ((j+1)%3 == 0):
                    print('|', end='')
                    
            print('\n')
            if ((i+1)%3 == 0):
                for i in range(self.cols - 3):
                    print(' === ', end='')
            print('\n')
                    
    def in_row(self, row, value, brd):
        return value in brd[row]
    
    def in_col(self, col, value, brd):
        search_col = []
        
        for i in range(len(brd)):
            search_col.append(brd[i][col])
            
        return value in search_col
    
    def in_block(self, row, col, value, brd):
        x_val = int(col/3)
        y_val = int(row/3)
        
        search_block = []
        
        for i in range(int(len(brd)/3)):
            for j in range(int(len(brd[0])/3)):
                search_block.append(brd[j+y_val*3][i+x_val*3])
                
        return value in search_block
    
    def is_valid(self, row, col, val, brd):
        return not (in_row(row, val, brd) or in_col(col, val, brd) or in_block(row, col, val, brd))
    
    def solve(self, brd):
        empty_spaces = []
        
        for row_index, row in enumerate(brd):
            for col_index, col in enumerate(row):
                if col == None:
                    empty_spaces.append((row_index, col_index))
                    
        if not empty_spaces:
            return brd
        
        for space in empty_spaces:
            possible = False
            for i in range(9):
                if is_valid(space[0], space[1], i, brd):
                    
                
                
        
        return False 
                    
                    