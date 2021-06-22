import sys
"""This module counts the number of lines in standard input
Input: any string from system stanrds input"""

count = 0
for line in sys.stdin:
    count += 1

print(count, 'lines in standard input')

