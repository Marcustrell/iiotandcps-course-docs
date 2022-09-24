import glob
import os
import shutil
import sys
import distutils.dir_util
import mmgcli

def copy(src, dest):
    files = []
    for r, d, f in os.walk(src):
        for file in f:
            if '.md' in file and not 'base.md' in file:
                files.append(os.path.join(r, file))

    if os.path.exists(dest):
        distutils.dir_util.remove_tree(dest)

    def filter(src, names):
        return [name for name in names if 'base.md' in name]

    shutil.copytree(src, dest, ignore=filter)

    print(files)

    for file in files:
        os.remove(file)
    
if __name__ == '__main__':
    copy(os.path.join('.', 'src', 'docs'), os.path.join('.', 'build', 'docs'))
