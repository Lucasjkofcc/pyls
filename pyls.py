import os
import sys
args = sys.argv
if len(args) < 2:
    for file in os.listdir():
        if file[0] == '.':
            pass
        else:
            print(file)
elif args[1] == '-l':
    for f in os.listdir("."):
        print(f)