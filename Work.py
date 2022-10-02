import sys
import time


# Input: v an integer representing the minimum lines of code and
#        k an integer representing the productivity factor
# Output: computes the sum of the series (v + v // k + v // k**2 + ...)
#         returns the sum of the series
def sum_series (v, k):
  sum = v
  p = 1
  while (v // (k**p)) > 0:
    sum += (v // (k**p))
    p += 1
  return sum 

# Input: n an integer representing the total number of lines of code
#        k an integer representing the productivity factor
# Output: returns v the minimum lines of code to write using linear search
def linear_search (n, k):
  for i in range(1, n+1):
    if sum_series(i, k) >= n:
      return i

# Input: n an integer representing the total number of lines of code
#        k an integer representing the productivity factor
# Output: returns v the minimum lines of code to write using binary search
def binary_search (n, k):
   top = n
   bot = 0
   mid = (top + bot) // 2
   while(bot != mid and top != mid):
    if (sum_series(mid, k) == n):
      return mid
    elif (sum_series(mid, k) < n):
      bot = mid 
      mid = (top + bot) // 2
    elif (sum_series(mid, k) > n):
      top = mid 
      mid = (top + bot) // 2
   return mid + 1


def main():
  # read number of cases
  line = sys.stdin.readline()
  line = line.strip()
  num_cases = int(line)

  for i in range (num_cases):
    line = sys.stdin.readline()
    line = line.strip()
    inp =  line.split()
    n = int(inp[0])
    k = int(inp[1])

    start = time.time()
    print("Binary Search: " + str(binary_search(n, k)))
    finish = time.time()
    print("Time: " + str(finish - start))

    print()

    start = time.time()
    print("Linear Search: " + str(linear_search(n, k)))
    finish = time.time()
    print("Time: " + str(finish - start))

    print()
    print()

if __name__ == "__main__":
  main()
