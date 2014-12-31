from __future__ import generators
import sys

from math import sin

def math_gen(n):
    while True:
        yield n
        n = abs(sin(n))*31

def jump_to(val):
    if  0 <= val < 10:
        return 'ONES'
    elif 10 <= val < 20:
        return 'TENS'
    elif 20 <= val < 30:
        return 'TWENTIES'
    else:
        return 'OUT_OF_RANGE'

def get_ones(iter):
    global cargo
    while True:
        print('ONES State:')
        while jump_to(cargo)=='ONES':
            print('  %s' % cargo)
            cargo = iter.next()
        yield (jump_to(cargo), cargo)

def get_tens(iter):
    global cargo
    while True:
        print('TENS State:')
        while jump_to(cargo)=='TENS':
            print('  %s' % cargo)
            cargo = iter.next()
        yield (jump_to(cargo), cargo)

def get_twenties(iter):
    global cargo
    while True:
        print('TWENTIES State:')
        while jump_to(cargo)=='TWENTIES':
            print('  %s' % cargo)
            cargo = iter.next()
        yield (jump_to(cargo), cargo)

def exit(iter):
    jump = 'twenties'.upper()
    yield (jump, iter.next())
    sys.exit()

def scheduler(gendct, start):
    global cargo
    coroutine = start
    while True:
        (coroutine, cargo) = gendct[coroutine].next()

if __name__ == '__main__':
    num_stream = math_gen(1)
    cargo = num_stream.next()
    gendct = {
        'ONES'        : get_ones(num_stream),
        'TENS'        : get_tens(num_stream),
        'TWENTIES'    : get_twenties(num_stream),
        'OUT_OF_RANGE': exit(num_stream)}
    scheduler(gendct, jump_to(cargo))
