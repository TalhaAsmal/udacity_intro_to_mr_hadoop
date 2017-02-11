#!/usr/bin/python3

import sys

def splitter(line, req_length, key_key, val_key):
    data = line.strip().split('\t')
    if len(data) != req_length:
        return

    print("{}\t{}".format(data[key_key], data[val_key]))
    return