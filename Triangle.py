#  File: Triangle.py

#  Description: --

#  Student Name: Ankita Sumeet

#  Student UT EID: as96977

#  Partner Name: Jingwen (Ivy) Lou

#  Partner UT EID: JL75477

#  Course Name: CS 313E

#  Unique Number: A9

#  Date Created: 10/6/2021

#  Date Last Modified: 10/8/2021 

import sys
from timeit import timeit

# returns the greatest path sum using exhaustive search
def brute_force (grid):
    return brute_force_helper(grid, 0 , 0, [], 0)

def brute_force_helper (grid, row, col, path_sums, current):
    # base case
    if row >= len(grid):
      current += grid[row][col]
      path_sums.append(current)
      return max(path_sums)
    else:
      current += grid[row][col]
      return max(brute_force_helper (grid, row + 1, col, path_sums, current), brute_force_helper (grid, row + 1, col+ 1, path_sums, current))  

# returns the greatest path sum using greedy approach
def greedy (grid):
    row = 1
    path = 0
    greatest_path_sum = grid[0][path]
    while(row < len(grid) and path < len(grid[row]) - 1):
        if grid[row][path] < grid[row][path + 1]:
            path += 1
        greatest_path_sum += grid[row][path]
        row += 1
    return greatest_path_sum

# returns the greatest path sum using divide and conquer (recursive) approach
def divide_conquer (grid):
    return divide_conquer_helper(grid, 0, 0)

def divide_conquer_helper(grid, row, col):
    # base case (no previous value)
    if row == len(grid) - 1: 
        if col == row: 
            # last element in 2D-list
            return grid[row][col]
            # max( adjacent value 1 , adjacent value 2 )
        return max(grid[row][col], grid[row][col + 1])
    else:
            # previous value + max( adjacent value 1 , adjacent value 2 )
        return grid[row][col] + max(divide_conquer_helper(grid, row + 1, col) , divide_conquer_helper(grid, row + 1, col + 1))
  

# returns the greatest path sum and the new grid using dynamic programming
def dynamic_prog (grid):
    triangle = [[0 for num in row] for row in grid]
    for i in range(len(triangle) - 1, -1, -1):
        for j in range(len(triangle[i])-1):
            if i == len(triangle) - 1:
                triangle[i][j] = grid[i][j]
                if j == len(triangle) - 2:
                    triangle[i][j + 1] = grid[i][j + 1]
            else:
                triangle[i][j] = grid[i][j] + max(triangle[i + 1][j], triangle[i + 1][j + 1])
    return triangle[0][0]

# reads the file and returnms a 2-D list that represents the triangle
def read_file ():
  # read number of lines
  line = sys.stdin.readline()
  line = line.strip() # eliminate whitespace 
  n = int (line)

  # create an empty grid with 0's
  grid = [[0 for i in range (n)] for j in range (n)]

  # read each line in the input file and add to the grid
  for i in range (n):
    line = sys.stdin.readline()
    line = line.strip() # eliminate whitespace 
    row = line.split() # separate by space 
    row = list (map (int, row))
    for j in range (len(row)):
      grid[i][j] = grid[i][j] + row[j]

  return grid 

def main ():
  # read triangular grid from file
  grid = read_file()
  
  '''
  # check that the grid was read in properly
  print (grid)
  '''

  # output greatest path from exhaustive search
  times = timeit ('brute_force({})'.format(grid), 'from __main__ import brute_force', number = 10)
  times = times / 10
  # print time taken using exhaustive search

  # output greatest path from greedy approach
  times = timeit ('greedy({})'.format(grid), 'from __main__ import greedy', number = 10)
  times = times / 10
  # print time taken using greedy approach

  # output greatest path from divide-and-conquer approach
  times = timeit ('divide_conquer({})'.format(grid), 'from __main__ import divide_conquer', number = 10)
  times = times / 10
  # print time taken using divide-and-conquer approach

  # output greatest path from dynamic programming 
  times = timeit ('dynamic_prog({})'.format(grid), 'from __main__ import dynamic_prog', number = 10)
  times = times / 10
  # print time taken using dynamic programming

if __name__ == "__main__":
  main()
