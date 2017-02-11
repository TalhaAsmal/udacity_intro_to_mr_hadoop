#!/usr/bin/python3

import sys

def main():
    for line in sys.stdin:
        data = line.strip().split('\t')
        if len(data) != 6:
            continue

        print("{}\t{}".format(data[3], data[4]))

if __name__ == "__main__":
    main()