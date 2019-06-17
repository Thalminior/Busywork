#!python3
"""
Created by Jared hall 6/17/2019
project will take two lists returns a list that contains only the elements that are common between the lists (without duplicates)
project idea from http://www.practicepython.org/exercise/2014/04/10/10-list-overlap-comprehensions.html
"""



#test lists
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

if __name__ == "__main__":
    
    c = set(a).intersection(b)
    print(c)
    #  this was far easyer than i expected, but i learned of set function so bonus on to next project

    input("push enter to close") # to keep window open