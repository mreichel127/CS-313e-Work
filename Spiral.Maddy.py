#  File: Spiral.py

#  Description:

#  Student Name:

#  Student UT EID:

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 

#  Date Created:

#  Date Last Modified:

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
    for i in range(len(spiral)):
        for j in range(len(spiral[i])):
            if newInput == j: 
                numIndex = [i][j]
                print(numIndex)
    sumOutput = 0
    for i in range(8):
        try:
            sumOutput += spiral[0][0]
        except IndexError():
            pass
    return sumOutput
    

def main():

    file = sys.stdin.read()
    fileList = file.split("\n")
    fileList.remove('')
    #print(fileList)
    
    spiral = create_spiral(int(fileList[0]))
    
    output = sum_adjacent_numbers(spiral, fileList[1])
    
    for r in spiral:
        print(r)
if __name__ == "__main__":
    main()