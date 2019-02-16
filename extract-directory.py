#!/usr/bin/env python

import os
import sys

DIRECTORY_FILE_PATH = os.path.join('raw_directory')
CSV_OUTPUT_DIR = os.path.join('refined_directory.csv')

def writer(work):
    f = open(CSV_OUTPUT_DIR, 'a')
    f.write(work + '\n')
    f.close()
    

def extract(directory):
    print(len(directory))
    for i in range(0, len(directory), 4):
        _work = directory[i] + "," + directory[i+1] + "," + directory[i+2] + "," + directory[i+3]
        writer(_work)

def main():
    with open(DIRECTORY_FILE_PATH, 'r') as f:
        _directory = f.read().splitlines()
        _directory = list(filter(None, _directory))

        extract(_directory)
        print('Done! Check refined_directory.csv file!')

if __name__ == '__main__':
    main()