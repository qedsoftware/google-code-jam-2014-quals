#!/usr/bin/env python
# William Wu, 2013 April 12
# w@qe-design.com 

import sys
import copy

# initialization
input_file = open(sys.argv[1])
line_count = 0
max_lines = 0
debug_flag = True
war_strategy = "naive"
deceitful_war_strategy = "naive"

# number of test cases
line = input_file.readline().strip()
T = int(line)


# find lowest upper bound: smallest element of data that is larger than x
# returns None if doesn't exist
def find_lub(data,x):
    for d in data:
        if d > x:
            return d
    return None
    
# war score
def war(n_arr,k_arr):
    score = 0
    if war_strategy == "naive":
        for n in n_arr:

            # if debug_flag:
            #     print n_arr
            #     print k_arr

            if n > k_arr[-1]: # if ken cannot beat it, he plays his smallest card, and naomi earns a point
                k = k_arr[0]
                k_arr.remove(k_arr[0])
                result = 1
            else: # if ken can beat it, he plays the smallest card larger than it, and naomi gets nothing
                lub = find_lub(k_arr,n)
                k_arr.remove(lub)
                k = lub
                result = 0
            score += result 

            # if debug_flag:
            #     print n,k,result
            #     print ""
    return score    


# deceitful war score
def deceitful_war(n_arr,k_arr):
    b = len(n_arr)
    if deceitful_war_strategy == "naive":
        score = 0
        for i in xrange(0,b):
            n = n_arr[i]

            k_largest = k_arr[-1]
            k_smallest = k_arr[0]

            if n < k_smallest:
                # lie -- make ken think n is slightly less than ken's largest 
                # so ken uses his largest
                k_arr.remove(k_largest)
            else:  # n > k_smallest
                # lie -- make ken think n is bigger than his largest
                # so ken uses his smallest
                k_arr.remove(k_smallest)
                score += 1 

        return score

# main method
def main():

    # data = [0.1,0.3,0.8,1.0]
    # target = -1 
    # print data, target
    # print find_lub(data,target)

    # process each case
    for t in xrange(0,T):

        # read num of blocks
        b = int(input_file.readline().strip())

        # naomi blocks
        n_arr = map(float,input_file.readline().strip().split())
        n_arr.sort()

        # ken blocks
        k_arr = map(float,input_file.readline().strip().split())
        k_arr.sort()


        print n_arr
        print k_arr

        # compute scores
        w_score = war(copy.copy(n_arr),copy.copy(k_arr))
        dw_score = deceitful_war(copy.copy(n_arr),copy.copy(k_arr))

        # print report
        print "Case #%d: %d %d" % (t+1,dw_score,w_score)
        

if __name__ == '__main__':
    main()
