#  File: MagicSquare.py

#  Description: Generate a given magic square through permutation.

#  Student Name: Ankita Sumeet 

#  Student UT EID: as96977

#  Partner Name: Jingwen (Ivy) Lou

#  Partner UT EID: jl75477

#  Course Name: CS 313E

#  Unique Number: A14

#  Date Created: 10/27/21

#  Date Last Modified: 10/27/21

import sys
import math
import timeit

# checks if a 1-D list if converted to a 2-D list is magic
# a is 1-D list of integers
# returns True if a is magic and False otherwise
def is_magic ( a ):
  a = convert(a)
  rowSum = sum(a[0])
  # check rows
  for row in a:
    if rowSum - sum(row[:-1]) != row[-1]:
      return False
  # check columns
  for col in zip(*a):
    if rowSum - sum(col[:-1]) != col[-1]:
      return False
  # down left diagonal 
  n = len(a)
  diag = []
  for i in range(n):
    diag.append(a[i][i])
  if rowSum - sum(diag[:-1]) != diag[-1]:
    return False
  # upper right diagonal 
  diag = []
  for i in range(n):
    diag.append(a[i][n - 1 -i])
  if rowSum - sum(diag[:-1]) != diag[-1]:
    return False

  return True

# convert a, a 1-D list of integers, to a 2-D magic square
def convert( lst ):
  n = math.sqrt(len(lst))
  a2D = []
  temp = []

  for num in lst:
    temp.append(num)
    if len(temp) == 3:
      a2D.append(temp)
      temp = []

  return a2D

# this function recursively permutes all magic squares
# a is 1-D list of integers and idx is an index in a
# function stores all 1-D lists that are magic in the list all_magic
def permute(a, idx, all_magic):
    n = math.sqrt(len(all_magic))
    if len(all_magic) == 3:
        track = 15
    elif len(all_magic) == 4:
        track = 34

    return permuteHelper ( a, idx, all_magic, n, track)

# helper function 
def permuteHelper ( a, idx, all_magic, n, track):
  if idx == len(a):
    print(a)
  else:
    for i in range(idx,len(a)):
      a[idx], a[i] = a[i], a[idx]

      # check rows 
      if (idx+2) % n == 0:
          rowTrack = track - sum(a[idx - (n-2):idx+1])
          if rowTrack not in a[idx+1:]:
             a[idx], a[i] = a[i], a[idx]
             continue  
      elif (idx + 1) % n == 0:
          if sum(a[(idx - (n-1)):idx + 1]) != track:
              a[idx], a[i] = a[i], a[idx]
              continue 

      # check columns 
      if (idx >= len(a) - n):
          if sum(a[idx % n:idx + 1:n]) != track:
              a[idx], a[i] = a[i], a[idx]
              continue
      elif (idx > n - 1):
          if sum(a[idx % n:idx + 1:n]) >= track:
              a[idx], a[i] = a[i], a[idx]
              continue

      # check diagonals 
      if (idx == len(a) - n):
          if sum(a[n - 1:idx + 1:n - 1]) != track:
              a[idx], a[i] = a[i], a[idx]
              continue
      elif (idx == len(a) - 1):
          if sum(a[0:idx + 1:n + 1]) != track:
              a[idx], a[i] = a[i], a[idx]
              continue 


def main():
  # read the dimension of the magic square
  line = sys.stdin.readline()
  line = line.strip()
  n = int (line)

  # create an empty list for all magic squares
  all_magic = []

  # create the 1-D list that has the numbers 1 through n^2
  a = [ i for i in range(1, n**2 + 1)]

  # generate all magic squares using permutation 
  permute(a, 0, all_magic)

  # print all magic squares
  [print(square) for square in all_magic]

if __name__ == "__main__":
  main()
  # print(timeit.timeit("main()", number=1, globals=globals()))