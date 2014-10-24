#-*- coding: utf-8 -*-
import math

def make_suffix_array(s):
    l = len(s)
    sa = list(range(l))
    sa.sort(cmp=lambda a,b: -1 if s[a] < s[b] else 1)
    return sa

def binarySearch(s, sa, key):
    low  = 0
    high = len(sa) - 1;
    while low <= high:
        mid = int(math.floor((low + high) / 2))
        val = s[sa[mid]:sa[mid] + len(key)]
        #print("(mid, key, val): %s, %s, %s" % (mid, key, val))
        if val == key:
            return mid
        elif val < key:
            low = mid + 1
        else:
            high = mid - 1
    return None

if __name__ == '__main__':
    s    = 'abracadabra'
    word = 'racadabra'
    s    = u'ぁっぉトイプー'
    word = u'ぉ'
    sa = make_suffix_array(s)
    r = binarySearch(s, sa, word)
    if r: print(s[sa[r]:sa[r]+len(word)])
