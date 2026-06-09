import os
import sys
args = sys.argv
if len(args) < 2:
    for file in os.listdir():
        if file[0] == '.':
            pass
        else:
            print(file)
elif args[1] == '-a':
    for f in os.listdir("."):
        print(f)
elif args[1] != '-a':
    os.chdir(args[1])
    for file in os.listdir():
        if file[0] == '.':
            pass
        else:
            print(file)
elif args[1] != '-a' and args[2] == "-a":
    os.chdir(args[1])
    for file in os.listdir():
        if file in os.listdir():
            print(file)