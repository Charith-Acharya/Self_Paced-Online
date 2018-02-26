#!/usr/bin/env python3

# file: testing.py

import time


def writefile(name, text):
    ts = time.strftime('%Y%m%d-%H%M%S')
    # fname = '{}_{}'.format(name, ts)
    fname = '{}.{}.txt'.format(name, ts)
    f = open(fname, 'w')
    f.write(text)
    f.close
    

def one():
    print('executed one')
    return 'executed one'

def two():
    print('executed two')
    return 'executed two'

def efunc():
    print('exiting.\n')
    return 'exiting'

prompt = 'Options: a or b. Type "q" to exit. > '

dispdict = {
    'a' : one,
    'b' : two,
    'q' : efunc,
    }

def menusel(p, d):
    '''
    Display menu to user. 
    This function uses a "dispatcher dictionary".

    ARGS:
    p:  prompt which is shown to the user
    d:  the dispatcher dictionary which holds the menu options
    '''
    while True:
        response = input(p)
        if dd[response]() == 'exiting':
            break


if __name__ == '__main__':
    menusel(prompt, dispdict)

