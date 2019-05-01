import os, re

def getMatchPosts(posts):
    match_posts = []
    for i in range(len(posts)):
        match = re.match(r'posts/(.*?).md', posts[i])
        match and match_posts.append(match.group(1))
    return match_posts

def compareCommits(commits):
    final_commits = {}
    for i in range(len(commits)):
        commit = commits[i]
        added, removed, modified = getMatchPosts(commit['added']), getMatchPosts(commit['removed']), getMatchPosts(commit['modified'])
        for j in range(len(added)):
            final_commits[added[j]] = 'ADDED'
        for k in range(len(removed)):
            del final_commits[removed[k]]
        for l in range(len(modified)):
            if final_commits.get(modified[l], None) != 'ADDED':
                final_commits[modified[l]] = 'MODIFIED'

    return final_commits

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
    final_commits = compareCommits(commits)
    print(final_commits)