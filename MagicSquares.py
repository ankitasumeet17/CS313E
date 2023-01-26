import math
#  File: MagicSquare.py

#  Description: This program creates a magic square and sums numbers asdjacent to n. 

#  Student's Name: Ankita Sumeet 

#  Student's UT EID: as96977
 
#  Partner's Name: Sakshee Jain

#  Partner's UT EID: smj2855

#  Course Name: CS 313E 

#  Unique Number: A2

#  Date Created: 9/6/21

#  Date Last Modified: 9/9/21

import sys

# Populate a 2-D list with numbers from 1 to n2
# This function must take as input an integer. You may assume that
# n >= 1 and n is odd. This function must return a 2-D list (a list of
# lists of integers) representing the square.
# Example 1: make_square(1) should return [[1]]
# Example 2: make_square(3) should return [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
def make_square ( n ):
    
    outerList = []
    for i in range(n):
        lstofNumbers = []
        for j in range(n):
            number = 0
            # intialize a square of 0s given dimensions (n)
            lstofNumbers.append(number)
        outerList.append(lstofNumbers)
    print_square(outerList)
    return outerList


# Print the magic square in a neat format where the numbers
# are right justified. This is a helper function.
# This function must take as input a 2-D list of integers
# This function does not return any value
# Example: Calling print_square (make_square(3)) should print the output
# 4 9 2
# 3 5 7
# 8 1 6
def print_square ( magic_square ):
    n = len(magic_square)
    currentNum = 1
    #setting the magic square to 1
    magic_square[int(n-1)][int((n) /2)] = currentNum
    #row is 4
    row =int(n-1)
    #column 2
    col = int((n) /2)
    #honestly idk locaiton does
    location =0
    for x in range((n**2)-1):
        # we want to print two
        currentNum +=1
        # print((row+1)%n,(col+1)%n )
        #[0][3]
        #[1][4]
        #[2][0]
        #[3][1]
        #[4][2]
        location = magic_square[(row+1)%n][(col+1)%n]
        if location == 0: # an empty spot 
            #print("This is the first one", currentNum)
            #updating cursor with new value
            magic_square[(row+1)%n][(col+1)%n] = currentNum
            #this is just the cursor of what the number is
            #location = magic_square[(row+1)%n][(col+1)%n]
            #print("location one", location)
            # were updating row and num
            row = (row+1) %n
            col = (col+1)%n
        else: 
            # accounts for out of bounds
            #print("hi")
            """if(row+1 >= n or col+1 >= n):
                # to print out two
                #print("hello")
                if (row+1 >= n and col+1 >= n):
                    location = magic_square[row-n][col-n]
                elif (row+1 >= n):
                    location = magic_square[row-n][col]
                elif (col+1 >= n):
                    location = magic_square[row][col-n]
            # accounts for currently filled spot """
            #put outside the if statement and remove line 100
            if(location!=0):
                #print(currentNum)
                #print("location two", location)
                if(row == 0):
                    magic_square[n-1][col] = currentNum
                    location = magic_square[n-1][col]
                    row = n-1
                    col = col
                else:
                    magic_square[row-1][col] = currentNum
                    location = magic_square[row-1][col]
                    row = row-1
                    col = col
                #print("location three", location)
        #print(row, col)
    #for row in magic_square:
    #    print(row)
    return magic_square


# Check that the 2-D list generated is indeed a magic square
# This function must take as input a 2-D list, and return a boolean
# This is a helper function.
# Example 1: check_square([[1, 2], [3, 4]]) should return False
# Example 2: check_square([[4, 9, 2], [3, 5, 7], [8, 1, 6]]) should return True
def check_square ( magic_square ):
    rSUm = 0
    cSum = 0
    dSum = 0 
    
    n = len(magic_square)

    for row in len(range(magic_square)):
        if(row >= len(magic_square) or row <0):
            continue
        else:
            rSUm += magic_square[row][0]

    for col in len(range(magic_square)):
        if(col >= len(magic_square) or col <0):
            continue
        else:
            cSum += magic_square[0][col]

    for row in len(range(magic_square)):
        for col in len(range(magic_square)):
            if(row >= len(magic_square) or col >= len(magic_square) or row <0 or col < 0):
                continue
            else:
                dSum += magic_square[row+1][col+1]

    if ((rSUm == cSum) and (rSUm == dSum)):
        return True      
    else:
        return False

    #  For a magic square of size n, the sum is n * (n2 + 1) / 2
    # SUM BOTH DIAGONALS 
    

# Input: square is a 2-D list and n is an integer
# Output: returns an integer that is the sum of the
#         numbers adjacent to n in the magic square
#         if n is outside the range return 0
def sum_adjacent_numbers (square, n):
    #find n in square
    #find adjacent to n
    #add adjacent
    s = 0
    l = len(square)
    #n =23
    for row in range(len(square)):
        for col in range(len(square)):
            if square[row][col] == n:
                for r in range(row-1,row+2):
                    for c in range(col-1, col+2):
                        if(r >= len(square) or c >= len(square) or r <0 or c < 0):
                            continue
                        else:
                            s += square[r][c]
                            #print(r, c)
    if(abs(n) <= l**2 and n > 0):
        s-=n   
    else:
        s = 0  
    return s
            
def main():
  # read the input file from stdin
    num = sys.stdin.readline().strip()
    num = int(num)
  # create the magic square
    ol = make_square(num)
    #print_square(ol)
    #sum_adjacent_numbers(ol,23)
    #count = len(sys.stdin.readline())
    #print(count)
    line = sys.stdin.readline().strip()
    #print(line)
    while line != "":
        xx = int(line)
        #print(xx)
        print(sum_adjacent_numbers(ol,xx))
        line = sys.stdin.readline().strip()

        
    #cnt += 1"""
  # print the sum of the adjacent numbers 

# This line above main is for grading purposes. It will not affect how
# your code will run while you develop and test it.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
  main()