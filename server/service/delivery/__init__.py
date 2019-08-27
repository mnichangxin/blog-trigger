from concurrent.futures import ThreadPoolExecutor

from .pull import exec_pull
from .compare import compareCommits
from .convert import convertMd

def getDeliveryData(data):
    final_commits = compareCommits(data['commits'])
    delivery_data = {
        'ADDED': [],
        'REMOVED': [],
        'MODIFIED': []
    }
    for commit in final_commits:
        commit_status = final_commits[commit]
        if commit_status == 'ADDED' or commit_status == 'MODIFIED':
            delivery_data[commit_status].append({
                'id': commit,
                'content': convertMd(commit)
            })
        else:
            delivery_data[commit_status].append({
                'id': commit
            })
    print(delivery_data)
    return delivery_data

def delivery(data):
    # executor = ThreadPoolExecutor(1)
    # executor.submit(exec_sh)
    # print(compareCommits(data['commits']))
    delivery_data = getDeliveryData(data)