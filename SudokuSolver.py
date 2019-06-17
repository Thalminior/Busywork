#!python3
"""
Created by Jared hall 6/17/2019
project will solve sudoku puzzles
"""




# imports
import numpy as np


# create puzzle get inputs

# create lists
bfill = 0

# test puzzle here test taken from https://en.wikipedia.org/wiki/Sudoku
test_puzzle = np.array([[5,3,bfill,bfill,7,bfill,bfill,bfill,bfill],[6,bfill,bfill,1,9,5,bfill,bfill,bfill],[bfill,9,8,bfill,bfill,bfill,bfill,6,bfill],[8,bfill,bfill,bfill,6,bfill,bfill,bfill,3],[4,bfill,bfill,8,bfill,3,bfill,bfill,1],[7,bfill,bfill,bfill,2,bfill,bfill,bfill,6],[bfill,6,bfill,bfill,bfill,bfill,2,8,bfill],[bfill,bfill,bfill,4,1,9,bfill,bfill,5],[bfill,bfill,bfill,bfill,8,bfill,bfill,7,9]])


puzzle = np.array([[bfill]*9,[bfill]*9,[bfill]*9,[bfill]*9,[bfill]*9,[bfill]*9,[bfill]*9,[bfill]*9,[bfill]*9])

zero_locations = np.transpose(np.nonzero(test_puzzle < 1))
# x = puzzle.put






#solve puzzle

# test across


# print it readable

def display_array(array_in):
    for row in array_in:
        for item in row:
            if item == 0:
                item = "_"
            print(item, end=' ')
        print()


# TODO put lines between the groups of 3

# finish = 



if __name__ == "__main__":

    # print(y)


    display_array(test_puzzle)
    # display_array(y)
    # print(y)
    # display_array(finish)


    input("push enter to close") # to keep window open