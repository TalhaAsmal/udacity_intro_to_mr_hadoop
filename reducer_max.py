#!/usr/bin/python3

import sys


def main():
    old_key = None
    max_val = 0

    for line in sys.stdin:
        data = line.strip().split("\t")
        if len(data) != 2:
            continue

        new_key, curr_val = data

        if old_key and old_key != new_key:
            print("{}\t{}".format(old_key, max_val))
            max_val = 0

            old_key = new_key
        max_val = max(max_val, curr_val)

    print("{}\t{}".format(old_key, max_val))

if __name__ == "__main__":
    main()
