#!/usr/bin/env python
import os
import shutil
from glob import glob

files = glob("../../../../NASA-3D-Resources/**/*.lwo", recursive=True)
for file in files:
    #print(file)
    src = "/".join(file.split("/")[:7])
    dst = src.split("/")[-1]
    #print(src, dst)
    if not os.path.isdir(dst):
        shutil.copytree(src, dst)


files = glob("**/*.lwo", recursive=True)
lines = []
lines.append(f"from lwo_helper import load_lwo")
for i, file in enumerate(files):
    #print(i, file)
    lines.append(f"")
    lines.append(f"def test_load_nasa{i}():")
    lines.append(f"    infile = \"tests/lwo_nasa/src/{file}\"")
    lines.append(f"    load_lwo(infile, cancel_search=True)")

f = open("../test_load_lwo_nasa.py", 'w')
f.writelines("\n".join(lines))
f.close()
