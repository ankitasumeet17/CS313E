#  File: Reducible.py

#  Description: use has table to find the longest reducible word in a given file

#  Student Name: Ivy Lou

#  Student UT EID: JL75477

#  Partner Name: Ankita Sumeet

#  Partner UT EID: as96977

#  Course Name: CS 313E

#  Unique Number: 

#  Date Created:

#  Date Last Modified:
import sys

# Input: takes as input a positive integer n
# Output: returns True if n is prime and False otherwise
def is_prime ( n ):
  if (n == 1):
    return False
  limit = int (n ** 0.5) + 1
  div = 2
  while (div < limit):
    if (n % div == 0):
      return False
    div += 1
  return True

# Input: takes as input a string in lower case and the size
#        of the hash table 
# Output: returns the index the string will hash into
def hash_word (s, size):
  hash_idx = 0
  for j in range (len(s)):
    letter = ord (s[j]) - 96
#arrayindex = hugenumber %  arraysize
    hash_idx = (hash_idx * 26 + letter) % size
  return hash_idx

# Input: takes as input a string in lower case and the constant
#        for double hashing 
# Output: returns the step size for that string 
def step_size (s, const):
  hash_idx = hash_word(s,const)
  return const - hash_idx

# Input: takes as input a string and a hash table 
# Output: no output; the function enters the string in the hash table, 
#         it resolves collisions by double hashing
def insert_word (s, hash_table):
  p = hash_word(s, len(hash_table)) #startng position
  if (hash_table[p] != ""): #if already has a word, increment
    newPos = step_size(s, 3)
    i = 1
    while (hash_table[(p + newPos * i) % len(hash_table)] != ""): #not empty
      i += 1 #increment
    hash_table[(p + newPos * i) % len(hash_table)] = s
  else:
    hash_table[p] = s #place word

# Input: takes as input a string and a hash table 
# Output: returns True if the string is in the hash table 
#         and False otherwise
def find_word (s, hash_table):
  p = hash_word(s, len(hash_table))
  if (hash_table[p] == s):
    return True #if found the word, True
  if (hash_table[p] != ""): #not empty
    newPos = step_size(s, 3) #go to the next spot
    i = 1
    while (hash_table[(p + newPos * i) % len(hash_table)] != ""):
      if (hash_table[(p + newPos * i) % len(hash_table)] == s):
        return True
      i += 1
  return False #otherwise False
  
# Input: string s, a hash table, and a hash_memo 
#        recursively finds if the string is reducible
# Output: if the string is reducible it enters it into the hash memo 
#         and returns True and False otherwise
def is_reducible (s, hash_table, hash_memo):
  if len(s) == 1:
    return s == "a" or s == "i" or s == "o" #end letters
  if not find_word(s, hash_table):
    return False
# check if word is inside the memo
  if find_word(s, hash_memo):
    return True
  helper_output = helper(s, hash_table) #call helper to check if its reducible
  for sub_word in helper_output:
    if is_reducible(sub_word, hash_table, hash_memo):
      insert_word(s, hash_memo)
      return True
  return False

def helper(s, hash_table):
  reducible = []
  for i in range(len(s)):
    sub_word = s[:i] + s[i+1:] #reduce letter 
    if find_word(sub_word, hash_table) or sub_word in ('a', 'i', 'o'):
      reducible.append(sub_word)
  return reducible

# Input: string_list a list of words
# Output: returns a list of words that have the maximum length
def get_longest_words (string_list):
  longestWords = []
  longestLength = len(string_list[0])
  for i in range(len(string_list)):
    if len(string_list[i]) == longestLength:
      longestWords.append(string_list[i])
    else:
      return longestWords

def main():
  # create an empty word_list
  word_list = []
  # read words from words.txt and append to word_list
  for line in sys.stdin:
      line = line.strip()
      word_list.append(line)

  # find length of word_list
  n = len(word_list)

  # determine prime number N that is greater than twice
  # the length of the word_list
  primeNum = n * 2
  while (is_prime(primeNum) == False):
    primeNum += 1
  # create and empty hash_list
  hash_list = []

  # populate the hash_list with N blank strings
  for i in range(primeNum):
    hash_list.append("")

  # hash each word in word_list into hash_list
  # for collisions use double hashing
  for word in word_list:
    insert_word(word, hash_list)

# create an empty hash_memo of size M
  # we do not know a priori how many words will be reducible
  # let us assume it is 10 percent (fairly safe) of the words
  # then M is a prime number that is slightly greater than 
  # 0.2 * size of word_list
  hash_memo = []
  primeM = int(n * 0.2)
  while (is_prime(primeM) == False):
    primeM += 1

  # populate the hash_memo with M blank strings
  for i in range(primeM):
    hash_memo.append("")

  # create and empty list reducible_words
  reducible_words = []
#   print(is_reducible("sprite", hash_list, hash_memo))
#   exit()
  # for each word in the word_list recursively determine
  # if it is reducible, if it is, add it to reducible_words
  # as you recursively remove one letter at a time check
  # first if the sub-word exists in the hash_memo. if it does
  # then the word is reducible and you do not have to test
  # any further. add the word to the hash_memo.
  for word in word_list:
    reducible = is_reducible(word, hash_list, hash_memo)
    if reducible:
      reducible_words.append(word)

  #creating an empty list that will be used to sort our reducible_words list by length
  lengthList = []
  for word in reducible_words:
    lengthList.append((len(word), word))
  lengthList.sort(reverse = True)

  #replace the reducible_words list with the lengthList
  for i in range(len(lengthList)):
    reducible_words[i] = lengthList[i][1]

  # find words of the maximum length in reducible_words
  longestWords = get_longest_words(reducible_words)

  # print the reducible words in alphabetical order
  # one word per line
  longestWords.sort()
  for word in longestWords:
    print(word)

# This line above main is for grading purposes. It will not 
# affect how your code will run while you develop and test it.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
  main()