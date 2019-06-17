#!python3
"""
Created by Jared hall 6/17/2019
project will solve sudoku puzzles
"""

# create puzzle get inputs

# create lists
bfill = "_"

puzzle = [[bfill]*9,[bfill]*9,[bfill]*9,[bfill]*9,[bfill]*9,[bfill]*9,[bfill]*9,[bfill]*9,[bfill]*9]





#solve puzzle


# print it readable

def display_array(array):
    for row in array:
        for item in row:
            print(item, end=' ')
        print()


# TODO put lines between the groups of 3

# test puzzle here
test_puzzle = [[5,3,bfill,bfill,7,bfill,bfill,bfill,bfill],[6,bfill,bfill,1,9,5,bfill,bfill,bfill],[bfill,9,8,bfill,bfill,bfill,bfill,6,bfill],[8,bfill,bfill,bfill,6,bfill,bfill,bfill,3],[4,bfill,bfill,8,bfill,3,bfill,bfill,1],[7,bfill,bfill,bfill,2,bfill,bfill,bfill,6],[bfill,6,bfill,bfill,bfill,bfill,2,8,bfill],[bfill,bfill,bfill,4,1,9,bfill,bfill,5],[bfill,bfill,bfill,bfill,8,bfill,bfill,7,9]]



if __name__ == "__main__":

    display_array(test_puzzle)

    # print(puzzle)
    input("push enter to close") # to keep window open