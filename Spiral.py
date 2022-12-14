#  File: Spiral.py

#  Description: created a number spiral and added certain values around a given number

#  Student Name: Madeline Reichel 

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
    newList = [[0] * n for c in range(n)] #create empty 2D list
    newList[n//2][n//2] = 1
    r = n//2
    c = n//2
    num = 1
    for a in range(1,n): #add numbers into the spiral 
       for y in range(a): #change column index on sprial and adds numbers to spiral 
           num += 1
           if a % 2 == 1:
               c += 1
           else:
               c -= 1
           newList[r][c] = num
       for x in range(a): #changes row index and adds numbers to spiral based on new index
           num += 1 
           if a % 2 == 1:
               r += 1
           else:
               r -= 1 
           newList[r][c] = num
    c = 0
    for a in range(n-1): #adds numbers on the top row of the spiral 
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
            if newInput == spiral[i][j]: #finds the location of the input number in the spiral
                r = i 
                c = j 
    sumOutput = 0
    for a in range(r-1, r+2):
        for b in range(c-1, c+2):
            if a == -1 or b == -1: #uses exception handling to skip out-of-range errors
                continue
            try:
                sumOutput += spiral[a][b] #sums up the numbers that are adjacent to the input number
            except: #ignore index that do not exist
                    sumOutput += 0 
    return int(sumOutput) - int(newInput) 
    
def main(): 
    file = sys.stdin.read() #reads the input file and adds it to a single list seperated by commas
    fileList = file.split("\n")
    fileList.remove('')
    
    spiral = create_spiral(int(fileList[0])) #creates the spiral using the first integer in the input file which determines the dimensions of the spiral
    for num in range(1, len(fileList)): #loops through the rest of the integers in the input file to print sum of adjacent numbers
        print(sum_adjacent_numbers(spiral, int(fileList[num])))
        
if __name__ == "__main__":
    main()
