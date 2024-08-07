#!/bin/python3

__author__ = "Manoj Kumar Arram"

"""
https://www.hackerrank.com/challenges/migratory-birds
"""


# !/bin/python3


#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

# from collections import Counter

def migratoryBirds(arr):
    # Write your code here
    d = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    for i in arr:
        d[i] = d[i] + 1
    final = {}
    for k, v in d.items():
        if v in final:
            final[v].append(k)
        else:
            final[v] = [k]
    print(min(final[max(final.keys())]))
    # if to use inbuilt functions.
    # print(Counter(map(int, arr)).most_common(1)[0][0])

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    # fptr.write(str(result) + '\n')

    # fptr.close()
