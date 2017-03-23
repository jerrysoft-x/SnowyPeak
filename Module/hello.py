#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

''' a test module '''

__author__ = 'Jerry Li'


def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello, world!')
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__ == '__main__':
    print(__author__)
    print(__name__)
    print(sys.argv)
    test()
