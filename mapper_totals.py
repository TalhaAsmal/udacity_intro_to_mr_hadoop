#!/usr/bin/python3

import sys


def main():
    for line in sys.stdin:
        data = line.strip().split('\t')
        if len(data) != 6:
            continue

        print("{}\t{}".format("Sales Value", data[4]))
        print("{}\t{}".format("Sales Count", 1))

if __name__ == "__main__":
    main()
