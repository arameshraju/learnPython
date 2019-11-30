#!/bin/python3
# Task
# Given a string, , of length  that is indexed from  to , print its even-indexed and odd-indexed characters as  space-separated strings on a single line (see the Sample below for more detail).
#
# Note:  is considered to be an even index.
#
# Input Format
#
# The first line contains an integer,  (the number of test cases).
# Each line  of the  subsequent lines contain a String, .
#

if __name__ == '__main__':
    n=int(input())
    S=['']*n
    for i in range(0,n) :
        sinput=input()
        e=""
        o=""
        for j in range(0,len(sinput)):
            if (j%2)==0 :
                e+=sinput[j]
            else:
                o+=sinput[j]

        S[i]= e +" " + o

    for ps in S:
        print(ps)
