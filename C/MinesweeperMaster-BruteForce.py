#!/usr/bin/env python
# William Wu, 2014 April 11
# w@qe-design.com 

# Commentary:
# - Squares are either bomb squares or safe squares. 
# - A safe square is either a zero square or nonzero square.
# 
# Proposed IFF conditions for a one-click win: 
# 1. Every safe square that is next to a bomb must have a zero square as a neighbor, UNLESS there is only one safe square in the whole grid.
# 2. The zero squares should be contiguous.  
#
# WARNING: Try not to injure yourself from laughing too hard at this.

import sys
import numpy as np
from itertools import combinations
from scipy.ndimage import label

# initialization
input_file = open(sys.argv[1])
line_count = 0
max_lines = 0
debug_flag = False
show_input_flag = False
shortcut_flag = True

# number of test cases
line = input_file.readline().strip()
T = int(line)

def get_neighbors(board,R,C,r,c):
    neighbors = []
    if r-1 >= 0 and c-1 >=0:
        neighbors.append(board[r-1,c-1])
    if r-1 >=0:
        neighbors.append(board[r-1,c])
    if r-1 >=0 and c+1 < C:
        neighbors.append(board[r-1,c+1])
    if c-1 >=0:
        neighbors.append(board[r,c-1])
    if c+1 < C:
        neighbors.append(board[r,c+1])
    if r+1 < R and c-1 >= 0:
        neighbors.append(board[r+1,c-1])
    if r+1 < R:
        neighbors.append(board[r+1,c])
    if r+1 < R and c+1 < C:
        neighbors.append(board[r+1,c+1])
    return neighbors


def display_board(board,counts,R,C,M):
    is_clicked = False
    for r in xrange(0,R):
        for c in xrange(0,C):
            if 1 == board[r][c]:
                sys.stdout.write('*')
            else:
                if (R*C - M) == 1:
                    sys.stdout.write('c')
                else:
                    if not is_clicked and "0"==counts[r][c]:
                        sys.stdout.write('c')
                        is_clicked = True
                    else:
                        sys.stdout.write('.')
        sys.stdout.write('\n')

def display_counts(counts,R,C):
    for r in xrange(0,R):
        for c in xrange(0,C):
            sys.stdout.write(counts[r][c])
        sys.stdout.write('\n')


# analysis
def analysis(R,C,M):

    # initialization
    A = R*C

    # shortcuts
    if shortcut_flag:
        if (A - M) in [2,3,5,7] and 1 not in [R,C]: 
            print "Impossible"
            return

    is_solved = False

    # create grids
    slots = range(0,A)

    for combo in combinations(slots, M): # iterate through all possible bomb placements

        # populate game board
        combo = set(combo)
        board = np.zeros((R,C))
        for r in xrange(0,R):
            for c in xrange(0,C):
                if (C*r + c) in combo:
                    board[r][c] = 1 # bomb 
                else:
                    board[r][c] = 0 # safe

        # compute count board
        counts = np.zeros((R,C),dtype=np.character)
        for r in xrange(0,R):
            for c in xrange(0,C):
                if board[r][c] == 1:
                    counts[r][c] = 'X'
                else:
                    counts[r][c] = str(sum(get_neighbors(board,R,C,r,c)))

        # initialization
        is_satisfactory = True

        # check first condition, if there is more than one safe square
        if A - M > 1: 
            for r in xrange(0,R):
                for c in xrange(0,C):
                    if board[r][c] == 0: # non-bomb square
                        neighbor_counts = get_neighbors(counts,R,C,r,c)
                        if "X" in neighbor_counts: # this non-bomb square is next to a bomb
                            if "0" not in neighbor_counts: # but it has no zero squares as neighbors
                                is_satisfactory = False
                                break
                if not is_satisfactory:
                    break

        if A-M > 1:
            # check that safe squares are connected 
            # create binary matrix where bomb squares are 0s and safe squares are 1s
            # this condition may be unnecessary
            board2 = np.zeros((R,C))
            for r in xrange(0,R):
                for c in xrange(0,C):
                    if board[r][c] == 1:
                        board2[r][c] = 0 # bomb
                    else:
                        board2[r][c] = 1 # safe
            labels, n = label(np.array(board2), np.ones((3,3))) 
            if n != 1:
                is_satisfactory = False

        if A - M > 1:
            # check that ZEROS are connected 
            # create binary matrix where zero squares are 1, and all other squares are 0 
            board3 = np.zeros((R,C))
            for r in xrange(0,R):
                for c in xrange(0,C):
                    if counts[r][c] == "0":
                        board3[r][c] = 1 
                    else:
                        board3[r][c] = 0 
            labels, n = label(np.array(board3), np.ones((3,3)))  
            if n != 1:
                is_satisfactory = False

        # if satisfactory, we are done, do not try other combinations anymore
        if is_satisfactory:
            if debug_flag:
                print combo
                print board
                print counts
            display_board(board,counts,R,C,M) 
            is_solved = True
            break

    if not is_solved:
        print "Impossible"


# main method
def main():

    # process each case
    for t in xrange(0,T):

        # read case
        R, C, M = map(int, input_file.readline().strip().split())

        if show_input_flag:
            print "Case #{0}: R={1},C={2},M={3},B={4}".format(t+1,R,C,M,(R*C-M))
        else:
            print "Case #%d:" % (t+1)
        analysis(R,C,M) 

if __name__ == '__main__':
    main()
