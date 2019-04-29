import os, filecmp

def compareFile(f1, f2):
    return filecmp.cmp(f1, f2)

def compareCommits(commits):
    REMOVED = -1
    ADDED = 1
    MODIFIED = 2
    n = len(commits)

if __name__ == '__main__':
    print(compareFile(os.path.abspath('./posts/test.md'), os.path.abspath('./posts/test2.md')))