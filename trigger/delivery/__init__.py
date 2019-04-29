from concurrent.futures import ThreadPoolExecutor

from .pull import exec_pull
from .compare import compareCommits
from .convert import convertMd

def getDeliveryData(data):
    finalCommits = compareCommits(data['commits'])
    deliveryData = {
        'ADDED': [],
        'REMOVED': [],
        'MODIFIED': []
    }
    for commit in finalCommits:
        commitStatus = finalCommits[commit]
        if commitStatus == 'ADDED' or commitStatus == 'MODIFIED':
            deliveryData[commitStatus].append({
                'id': commit,
                'content': convertMd(commit)
            })
        else:
            deliveryData[commitStatus].append({
                'id': commit
            })
    print(deliveryData)
    return deliveryData

def delivery(data):
    # executor = ThreadPoolExecutor(1)
    # executor.submit(exec_sh)
    # print(compareCommits(data['commits']))
    deliveryData = getDeliveryData(data)