#!/usr/bin/python3

import sys

def main():
    oldKey = None
    val = 0

    for line in sys.stdin:
        data = line.strip().split("\t")
        if len(data) != 2:
            continue

        newKey, curVal = data

        if oldKey and oldKey != newKey:
            print("{}\t{}".format(oldKey, val))
            val = 0

        oldKey = newKey
        val += float(curVal)

    print("{}\t{}".format(oldKey, val))

if __name__ == "__main__":
    main()