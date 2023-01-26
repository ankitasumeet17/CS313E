#  File: WordSearch.py

#  Description: A program that reads in a word grid of a certain dimension and finds the position of the first letter of each given in a word from a list of words. 

#  Student Name: Ankita Sumeet

#  Student UT EID: as96977

#  Partner Name: Sakshee Jain

#  Partner UT EID: smj2855

#  Course Name: CS 313E 

#  Unique Number: A1

#  Date Created: 8/30/21

#  Date Last Modified: 9/3/21

import sys

# Input: None
# Output: function returns a 2-D list that is the grid of letters and
#         1-D list of words to search
def read_input(): 

    global let
    
    '''word grid/list ?????'''

    dimension = sys.stdin.readline().strip()
    dimension = int(dimension)

    '''skip blank line'''
    sys.stdin.readline()
    letter = ''
    
    outterList = []
    #word_grid = {letter:tup} # dict

    rows, cols = (dimension, dimension)
    
    for i in range(rows):
        lstofLetters = []
        line = sys.stdin.readline().strip()
        for j in range(cols):
            #print(cols)
            #print(line)
            letter = line[j*2]
            #tup = (i,j)
            lstofLetters.append(letter)
        outterList.append(lstofLetters)

    
    '''skip blank line'''
    sys.stdin.readline()

    num = sys.stdin.readline()
    num = num.strip()
    num = int(num)

    lstWord = []  # word , tuple of position 
    for word in range(num):
        word = sys.stdin.readline().strip()
        #find_word(outterList, word)
        lstWord.append(word)

    #let = [char for char in word]
    return outterList, lstWord

def find_word(grid, word):
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            if dx == 0 and dy == 0:
                continue

            for y in range(len(grid)):
                for x in range(len(grid)):
                    found = True
                    for i in range(len(word)):
                        xf = i * dx + x
                        yf = i * dy + y

                        if xf >= len(grid):
                            found = False
                            break
                        if yf >= len(grid):
                            found = False
                            break

                        if grid[yf][xf] != word[i]:
                            found = False
                            break

                    if found:
                        return (y+1, x+1)
    return (0, 0)

def main():
  # read the input file from stdin
  word_grid, word_list = read_input()

  # find each word and print its location
  for word in word_list:
    location = find_word (word_grid, word)
    print(word + ": " + str(location))

if __name__ == "__main__":
  main()

