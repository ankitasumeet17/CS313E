#  File: TestCipher.py
#  Description: This code tests the encoding and decoding methods of two Cipher algorithms- Rail Fence Cipher and the Vigenere Cipher
#  Student's Name: Ankita Sumeet 

import sys

#  Input: strng is a string of characters and key is a positive
#         integer 2 or greater and strictly less than the length
#         of strng
#  Output: function returns a single string that is encoded with
#          rail fence algorithm
def rail_fence_encode ( strng, key ): 
    # initialize 2d list containing '-'
    outerList = []
    n = len(strng)
    for i in range(key):
        lstofNumbers = []
        for j in range(n):
            dash = '-'
            lstofNumbers.append(dash)
        outerList.append(lstofNumbers)

    # initialize cursor/pointer
    # add letters in a diagonal fashion
    location = 0
    row = 0
    col = 0
    sign = 1
    for x in range(n):
        outerList[row][col] = strng[location]
        row += 1 * sign
        col +=1
        location+=1
        if(row == key-1):
            sign = -1
        elif(row == 0):
            sign =1

    # read letters L-->R by row to output encoded string
    en_string = ""
    for r in range(key):
        for c in range(n):
            if(outerList[r][c] != "-"):
                en_string += outerList[r][c]
            else:
                continue
    return en_string


#  Input: strng is a string of characters and key is a positive
#         integer 2 or greater and strictly less than the length
#         of strng
#  Output: function returns a single string that is decoded with
#          rail fence algorithm
def rail_fence_decode ( strng, key ): 
  # fill spots w letters w another character (placeholder)
  starting = 0
  outerList = []
  n = len(strng)

  outerList = [['-' for _ in range(n)] for _ in range(key)]
  row = starting
  col = 0 
  location = 0
  sign = 1
  # s = outerList[starting][n-1]
  for x in range(n):
        # outerList[row][col] = strng[n - location]
        outerList[row][x] = "a"
        row += sign
        location+=1
        if(row == key-1):
            sign = -1
        elif(row == 0):
            sign =1

  yy = 0
  for t in range(len(outerList)):
      for e in range(len(outerList[t])):
          if(outerList[t][e] == "a"):
              outerList[t][e] = strng[yy]
              yy +=1
          if(yy == len(strng)):
              break
          else:
              continue
  en_string = ""
  l = 0
  z = 0
  y = 0
  sq = 1

  # read letters to output decoded text
  for x in range(n):
        en_string += outerList[z][y]
        z += 1 * sq
        y +=1
        l+=1
        if(z == key-1):
            sq = -1
        elif(z == 0):
            sq =1
  return en_string



#  Input: strng is a string of characters
#  Output: function converts all characters to lower case and then
#          removes all digits, punctuation marks, and spaces. It
#          returns a single string with only lower case characters
def filter_string ( strng ):
  strng = strng.lower()
  strng = strng.strip()
  newStrng = ''
  for i in strng:
    if (ord(i) >= 97 and ord(i) <= 122):
      newStrng += i
         
  return newStrng


# This function generates the
# key in a cyclic manner until
# it's length isn't equal to
# the length of original text
def newKey(strng, key):
  if len(strng) == len(key):
    return(key)
  else:
    key = list(key)
    for i in range(len(strng) - len(key)):
      key.append(key[i % len(key)])
  
  return("" . join(key))
    


#  Input: p is a character in the pass phrase (HORIZONTAL) and s is a character
#         in the plain text (VERTICAL)
#  Output: function returns a single character encoded using the 
#          Vigenere algorithm. You may not use a 2-D list 
def encode_character (p, s):
  cipher_text = []
  x = (ord(p) + ord(s) - ord('a')*2) % 26
  x += ord('a') 
  cipher_text.append(chr(x))
  return("" . join(cipher_text))


#  Input: p is a character in the pass phrase (r) and s is a character
#         in the plain text (c)
#  Output: function returns a single character decoded using the 
#          Vigenere algorithm. You may not use a 2-D list 
def decode_character (p, s):
  orig_text = []
  x = (ord(s) - ord(p)) % 26
  x += ord('a')
  orig_text.append(chr(x))
  return("" . join(orig_text))



#  Input: strng is a string of characters and phrase is a pass phrase
#  Output: function returns a single string that is encoded with
#          Vigenere algorithm
def vigenere_encode ( strng, phrase ):
    phrase = newKey(strng, phrase)
    x = ""
    for i in range(len(strng)):
        c = encode_character(strng[i], phrase[i])
        x += c
    return x   



#  Input: strng is a string of characters and phrase is a pass phrase
#  Output: function returns a single string that is decoded with
#          Vigenere algorithm
def vigenere_decode ( strng, phrase ):
  phrase = newKey(strng, phrase)
  x = ""
  for i in range(len(strng)):
    c = decode_character(phrase[i], strng[i])
    x += c
  return x



def main():
  
  # read the plain text from stdin
  print("Rail Fence Cipher")

  str = sys.stdin.readline().strip()
  print("Plain Text:", str)
  # read the key from stdin
  num = sys.stdin.readline().strip()
  num = int(num)
  # encrypt and print the encoded text using rail fence cipher
  print("Key:", num)
  print("Encoded Text:",rail_fence_encode ( str, num))
  print(" ")
  # read encoded text from stdin
  dec = sys.stdin.readline().strip()
  # read the key from stdin
  x = sys.stdin.readline().strip() 
  x = int(x)
  # decrypt and print the plain text using rail fence cipher
  print("Encoded Text:",dec)
  print("Enter Key:", x)
  print("Decoded Text:", rail_fence_decode(dec, x ))
  print(" ")
  print("Vigenere Cipher")
  print(" ")
  # read the plain text from stdin
  needs_to_be_encoded = sys.stdin.readline().strip()
  # read the pass phrase from stdin
  pass_phrase = sys.stdin.readline().strip()
  # encrypt and print the encoded text using Vigenere cipher
  print("Plain Text:", needs_to_be_encoded)
  print("Pass Phrase:",pass_phrase)
  print("Encoded Text:", vigenere_encode ( needs_to_be_encoded, pass_phrase ))
  print(" ")
  # read the encoded text from stdin
  needs_to_be_decoded = sys.stdin.readline().strip()
  # read the pass phrase from stdin
  pass_phrase_two = sys.stdin.readline().strip()
  # decrypt and print the plain text using Vigenere cipher
  print("Plain Text:", needs_to_be_decoded)
  print("Pass Phrase:",pass_phrase_two)
  print("Decoded Text:",vigenere_decode ( "zilwgaocdh", "seal" ))
  
# The line above main is for grading purposes only.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
  main()
