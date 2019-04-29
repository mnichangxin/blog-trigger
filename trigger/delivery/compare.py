import os, filecmp, re

def compareFile(f1, f2):
    return filecmp.cmp(f1, f2)

def matchPosts(posts):
    matchPosts = []
    for i in range(len(posts)):
        match = re.match(r'posts/(.*?).md', posts[i])
        match and matchPosts.append(match.group(1))
    return matchPosts

def compareCommits(commits):
    finalCommits = {}
    for i in range(len(commits)):
        commit = commits[i]
        added, removed, modified = matchPosts(commit['added']), matchPosts(commit['removed']), matchPosts(commit['modified'])
        for j in range(len(added)):
            finalCommits[added[j]] = 'ADDED'
        for k in range(len(removed)):
            del finalCommits[removed[k]]
        for l in range(len(modified)):
            if finalCommits.get(modified[l], None) != 'ADDED':
                finalCommits[modified[l]] = 'MODIFIED'

    return finalCommits

if __name__ == '__main__':
    commits = [{
        "added": [],
        "removed": [],
        "modified": [
            "posts/test.md",
            "trigger/api/hooks/__init__.py",
            "trigger/delivery/__init__.py",
            "trigger/delivery/compare.py",
            "trigger/delivery/pull.py"
        ]
    }]
    finalCommits = compareCommits(commits)
    print(finalCommits)