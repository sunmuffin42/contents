import os, json

path = "./"
# os.walk(pathcd)

# for i in os.walk(path):
#     i # will return tuple(absolute/path/to/pwd, [dirs], [files])
#         # then the next item will be the dirs[0] as the pwd
#         # depth first

for dirpath, dirnames, filenames in os.walk(path):
    directory_level = dirpath.replace(path, "")
    directory_level = directory_level.count(os.sep)
    indent = " " * 4
    print("{}{}/".format(indent*directory_level, os.path.basename(dirpath)))
    for f in [filename for filename in filenames if filename[-3:].lower() in ["pdf", "txt", "jvu"]]:
        print("{}{}".format(indent*(directory_level+1), f))