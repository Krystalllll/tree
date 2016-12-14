#!/usr/bin/env python3

import os
import string
import subprocess
import sys
import re


indent = '│   '
space = '    '
branch = '├── '
child_branch = '└── '


def sort_key(s):
    return re.sub('[^A-Za-z0-9]+', '', s).lower()


#reference: http://stackoverflow.com/questions/15312953/choose-a-file-starting-with-a-given-string
def print_tree(cpath, padding):
    files = [file for file in os.listdir(cpath) if not file.startswith('.')]
    files = sorted(files, key=sort_key)
    num_dir = 0
    num_file = 0
    for index in range(len(files)):
        file = files[index]
        if index < len(files) - 1:
            next_padding = indent
            print(padding + branch + file)
        else:
            print(padding + child_branch + file)
            next_padding = space
        if os.path.isfile(os.path.join(cpath, file)):
            num_file += 1
        else:
            num_dir += 1
            t_num_dir, t_num_file = print_tree(os.path.join(cpath, file), padding + next_padding)
            num_dir += t_num_dir
            num_file += t_num_file
    return num_dir, num_file


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print(".")
        pathway = os.getcwd() + '/'
    # elif len(sys.argv) == 2:
    else:
        temway = sys.argv[1]
        if temway[0] != '/':
            pathway = os.getcwd() + '/' + temway + '/'
        else:
            pathway = temway + '/'
        print(temway)
    num_dir, num_file = print_tree(pathway, "")
    print('\n' + str(num_dir) + " directories, " + str(num_file) + " files")
