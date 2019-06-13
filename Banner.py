#!python3
"""
Created by Jared hall begun 6/13/2019
project will take a sting input and create a banner around the string
if run as main will request user input as sting
project iidea from http://usingpython.com/python-programming-challenges/
"""

# imports



# function to create top and bottom of banner

def dotted_line(letter_count):
    """
    takes int as input outputs string of * with input count +4
    """
    i = 1
    border = "****"
    while i <= letter_count :
        border += "*"
        # print(i) # for testing
        i += 1
    return border

def make_banner(name_input):
    """
    places text string inside * * with top and bottom borders of ****
    """
    length = len(name_input)
    # print(length) #for testing
    edge = dotted_line(length)
    banner = f"{edge}\n* {name_input} *\n{edge}"
    print(banner)
    


if __name__ == "__main__":
    
    user_input = input("please type your name: ")

    make_banner(user_input)

    

    input("push enter to close") # to keep window open