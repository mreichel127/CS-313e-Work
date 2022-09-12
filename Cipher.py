#  File: Cipher.py

#  Description: created a number spiral and added certain values around a given number

#  Student Name: Madeline Reichel

#  Student UT EID: mr57723

#  Partner Name: Jennifer Kim

#  Partner UT EID: ck27924

#  Course Name: CS 313E

#  Unique Number: 52520

#  Date Created: 09/06/2022

#  Date Last Modified: 09/12/2022

import math
import sys
# Input: strng is a string of 100 or less of upper case, lower case, 
#        and digits
# Output: function returns an encrypted string 
def encrypt ( strng ):
  while (math.sqrt(len(strng))) // 1 != math.sqrt(len(strng)):
    strng += "*"
  
  k = int (math.sqrt(len(strng)))
  index=0
  table= [[0 for i in range(k)] for j in range(k)] #create an empty table
  for i in range(len(table)-1, -1, -1):
    for j in range (len(table)): #keeps columns constant while increasing the index of rows until it hits length of table
      table[j][i]= strng[index]
      index +=1
  
  newList=[] 
  for i in range(len(table)): #traverses through the table and adds the encrypted string in to a list
    for j in range(len(table)):
      if table[i][j] != "*":
        newList.append(table[i][j])
        encryptStr= "".join(newList) #creates a new string of the encrypted sentence from the list after removing "*"
  return (encryptStr)

# Input: strng is a string of 100 or less of upper case, lower case, 
#        and digits
# Output: function returns an encrypted string 
def decrypt ( strng ):
  k = 1
  while k * k < len(strng):
    k += 1
  q = k*k
  numStar = q-len(strng)
  count = 0
  table= [[0 for i in range(k)] for j in range(k)] #create an empty table
  if numStar != 0:  
    for c in range(len(table)):
      for r in range (len(table)-1, -1, -1): #keeps columns constant while increasing the index of rows until it hits length of table
        table[r][c] = '*'
        count +=1
        if (count == numStar):
          break
      if (count == numStar):
        break

  index = 0
  for i in range(len(table)): #traverses through the table and adds the encrypted string in to a list
    for j in range(len(table)):
      if table[i][j] != "*":
        table[i][j] = strng[index]
        index += 1

  newList = [] #put decrypted grid into string
  for c in range(k-1, -1, -1):
    for r in range(k):
      newList.append(table[r][c])
  out = "".join(newList)
  return (out.replace('*', ''))

def main():
  input=sys.stdin.read() #reads an input of integers on separate lines
  split_input=input.split("\n") #adds the input into a single line list
  strP= split_input[0]
  strQ= split_input[1]

  print (encrypt(strP))   # encrypts and prints the string P
  print (decrypt(strQ)) # decrypts and prints the string P
  # read the strings P and Q from standard input

if __name__ == "__main__":
  main()
