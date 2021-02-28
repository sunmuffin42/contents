# contents

Use this to generate text files, contents.out and catalog.out, of all the titles in a directory. Using `make contents`, it will search recursively, and sort the entire list alphabetically, ignoring subdirectory structure. Using `make catalog`, it will search recursively and output a file that maintains the structure of all subdirectories.

`$ make contents`

contents.out
```
01. An Introduction to Language 7th edition.pdf
01 Intro.pdf
02 Descriptive Stats.pdf
...
```

`$ make catalog`

catalog.out
```
Intro Books/
    01. An Introduction to Language 7th edition.pdf
    01 Intro.pdf
02 Descriptive Stats.pdf
...
```

You'll need to pull out copies of `contents_acq.py`, `catalog_traversal.py`, and `makefile` into the directory you want to catalog.