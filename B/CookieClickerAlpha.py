#!/usr/bin/env python
# William Wu, 2014 April 11
# w@qe-design.com 

import os, sys
import numpy as np
import math

# initialization
input_file = open(sys.argv[1])
line_count = 0
max_lines = 0
debug_flag = False

# number of test cases
line = input_file.readline().strip()
T = int(line)

# main method
def main():
    # process each case
    for t in xrange(0,T):

        # read case
        C, F, X = map(float, input_file.readline().strip().split())
        r = 2

        if debug_flag:
            print "C: ", C
            print "F: ", F
            print "X: ", X

        ub = 100000
        lb = 0
        finish_times = [0] * (ub - lb + 1) 
        farm_times = [0] * (ub - lb + 1) 
        finish_times[0] = X/r 
        farm_times[0] = 0

        N_min = 0
        time_min = finish_times[0]

        for N in xrange(1,ub+1):
            farm_times[N] = farm_times[N-1] + C/(r+(N-1)*F)
            finish_times[N] = X/(r + N*F) + farm_times[N]
            if finish_times[N] < time_min: # update minimum 
                time_min = finish_times[N]
                N_min = N
            # speed hack: if the sequence ever starts increasing, just stop, because finish_times is bimodal
            if finish_times[N] > finish_times[N-1]:
                break

        if debug_flag:
            print time_min
            print N_min
            print finish_times

        # print report
        print "Case #%d: %s" % (t+1,time_min)


if __name__ == '__main__':
    main()
