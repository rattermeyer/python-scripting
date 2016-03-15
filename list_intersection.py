#!/usr/bin/python
import sys, getopt


def intersect(a, b):
    if a is None:
        return b
    if b is None:
        return a
    a_list = a.split(',')
    b_list = b.split(',')
    return ",".join([val for val in a_list if val in b_list])


def main(argv):
    print intersect(argv[0], argv[1])


if __name__ == "__main__":
    main(sys.argv[1:])
