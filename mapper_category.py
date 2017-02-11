#!/usr/bin/python3

import sys
from common import splitter


def main():
    for line in sys.stdin:
        splitter(line, 6, 3, 4)

if __name__ == "__main__":
    main()
