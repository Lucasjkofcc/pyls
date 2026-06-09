import os
import sys

args = sys.argv

if len(args) < 2:
    for file in os.listdir():
        if file[0] != '.':
            print(file)

elif len(args) > 2 and args[2] == "-a":
    os.chdir(args[1])
    for file in os.listdir():
        print(file)

elif args[1] == '-a':
    for file in os.listdir():
        print(file)

elif args[1] != '-a':
    os.chdir(args[1])
    for file in os.listdir():
        if file[0] != '.':
            print(file)