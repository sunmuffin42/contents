import os, json

path = os.getcwd() + "/.." # if you put the entire "contents" folder into the top level directory you want to search
# path = "./" # if you just put the makefile and python files directly into the top level directory you want to search

for dirpath, dirnames, filenames in os.walk(path):
    directory_level = dirpath.replace(path, "")
    directory_level = directory_level.count(os.sep)
    indent = " " * 4
    print("{}{}/".format(indent*directory_level, os.path.basename(dirpath)))
    # for f in [filename for filename in filenames if filename[-3:].lower() in ["pdf", "txt", "jvu"]]:
    for f in [filename for filename in filenames if filename[-3:].lower()]:
        print("{}{}".format(indent*(directory_level+1), f))