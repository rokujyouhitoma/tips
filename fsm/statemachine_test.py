from statemachine import StateMachine
import math

STATE_ONES         = 'STATE_ONES'
STATE_TENS         = 'STATE_TENS'
STATE_TWENTIES     = 'TWENTIES'
STATE_OUT_OF_RANGE = 'STATE_OUT_OF_RANGE'

def ones_counter(val):
    while True:
        if val <= 0 or val >= 30:
            newState = STATE_OUT_OF_RANGE
            break
        elif 20 <= val < 30:
            newState = STATE_TWENTIES
            break
        elif 10 <= val < 20:
            newState = STATE_TENS
            break
        else:
            val = math_func(val)
    return (newState, val)

def tens_counter(val):
    while True:
        if val <= 0 or val >= 30:
            newState = STATE_OUT_OF_RANGE
            break
        elif 1 <= val < 10:
            newState = STATE_ONES
            break
        elif 20 <= val < 30:
            newState = STATE_TWENTIES
            break
        else:
            val = math_func(val)
    return (newState, val)

def twenties_counter(val):
    while True:
        if val <= 0 or val >= 30:
            newState = STATE_OUT_OF_RANGE
            break
        elif 1 <= val < 10:
            newState = STATE_ONES
            break
        elif 10 <= val < 20:
            newState = STATE_TENS
            break
        else:
            val = math_func(val)
    return (newState, val)

def math_func(n):
    return abs(math.sin(n))*31

if __name__== '__main__':
    m = StateMachine()
    m.add_state(STATE_ONES, ones_counter, end_state=False)
    m.add_state(STATE_TENS, tens_counter, end_state=False)
    m.add_state(STATE_TWENTIES, twenties_counter, end_state=False)
    m.add_state(STATE_OUT_OF_RANGE, None, end_state=True)
    m.set_start(STATE_ONES)
    m.run(1)
