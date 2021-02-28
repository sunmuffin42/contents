import re, sys
old_string = "".join([i for i in sys.stdin])
metadata = re.compile(r"\n([rwx\-]{10}.+(20|:)\d{2} |d.*)")
dirinfo = re.compile(r"\n.+\ntotal \d+")
lines = re.compile(r"\n{2,}")
renew = old_string
for regex, replace in zip([metadata,dirinfo,lines], [r"\n", "", r"\n"]):
    renew = re.sub(regex, replace, renew)

listed = sorted(renew.split("\n"))
relisted = "\n".join(listed)
sys.stdout.write(relisted)