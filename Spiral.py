#  File: Spiral.py

#  Description: created a number spiral and added certain values around a given number

#  Student Name: Madeline Reichel - test

#  Student UT EID: mr57723

#  Partner Name: Jennifer Kim

#  Partner UT EID: ck27924

#  Course Name: CS 313E

#  Unique Number: 52520

#  Date Created: 08/29/2022

#  Date Last Modified: 09/02/2022

# Input: n is an odd integer between 1 and 100
# Output: returns a 2-D list representing a spiral
#         if n is even add one to n

import sys

def create_spiral(n):
    newList = [[0] * n for c in range(n)] #create empty list
    newList[n//2][n//2] = 1
    r = n//2
    c = n//2
    num = 1
    for a in range(1,n):
       for y in range(a): 
           num += 1
           if a % 2 == 1:
               c += 1
           else:
               c -= 1
           newList[r][c] = num
       for x in range(a): 
           num += 1 
           if a % 2 == 1:
               r += 1
           else:
               r -= 1 
           newList[r][c] = num
    c = 0
    for a in range(n-1):
        num += 1
        c += 1
        newList[r][c] = num
    return newList

# Input: spiral is a 2-D list and n is an integer
# Output: returns an integer that is the sum of the
#         numbers adjacent to n in the spiral
#         if n is outside the range return 0

def sum_adjacent_numbers(spiral, newInput):
    r = 0
    c = 0
    for i in range(len(spiral)):
        for j in range(len(spiral[i])):
            if newInput == spiral[i][j]: 
                r = i
                c = j
    sumOutput = 0
    for a in range(r-1, r+2):
        for b in range(c-1, c+2):
            if a == -1 or b == -1:
                continue
            try:
                sumOutput += spiral[a][b]
            except: 
                    sumOutput += 0
    return int(sumOutput) - int(newInput)
    

def main():

    file = sys.stdin.read()
    fileList = file.split("\n")
    fileList.remove('')
    
    spiral = create_spiral(int(fileList[0]))
    for num in range(1, len(fileList)):
        print(sum_adjacent_numbers(spiral, int(fileList[num])))
if __name__ == "__main__":
    main()
