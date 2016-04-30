#!usr/bin/env python
from __future__ import print_function
from __future__ import division
from collections import *
from heapq import *
from bisect import *
from math import *
from itertools import *
from random import *

def main():
    cases=int(raw_input())
    for j in xrange(cases):
        word=raw_input()
        _list=list()
        _list=word[0]
        prev=word[0]
        for i in xrange(1,len(word)):
        	if ord(word[i])>=ord(prev):
        		_list=insert_str(_list,word[i],i+1)
        		prev=word[i]
        	else:
        		_list=insert_str(_list,word[i],0)
        _list=''.join(_list)
        print("Case #",j+1,":"," ",_list[::-1],sep="")
        
def insert_str (source_str, insert_str, pos):
    return source_str[:pos]+insert_str+source_str[pos:]

if __name__=='__main__':
	main()
