#!/usr/bin/env python
# William Wu, 2013 April 11
# w@qe-design.com 

import sys
import numpy as np

# initialization
input_file = open(sys.argv[1])
line_count = 0
max_lines = 0
debug_flag = True

# number of test cases
line = input_file.readline().strip()
T = int(line)

# determine outcome 
def result(nums1,nums2):
    intersection = list(set(nums1) & set(nums2))
    n = len(intersection)
    if 0 == n:
        return "Volunteer cheated!"
    elif 1 == n:
        return str(int(intersection[0]))
    else:
        return "Bad magician!"

# main method
def main():
    # preallocation
    board1 = np.zeros((4,4))
    board2 = np.zeros((4,4))

    # process each case
    for t in xrange(0,T):

        a1 = int(input_file.readline().strip())
        for u in xrange(0,4):
            board1[u,:] = map(int,input_file.readline().strip().split())

        a2 = int(input_file.readline().strip())
        for u in xrange(0,4):
            board2[u,:] = map(int,input_file.readline().strip().split())

        nums1 = board1[a1-1,:] 
        nums2 = board2[a2-1,:]

        # print report
        print "Case #%d: %s" % (t+1,result(nums1,nums2))
        

if __name__ == '__main__':
    main()
