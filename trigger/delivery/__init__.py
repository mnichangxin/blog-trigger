from concurrent.futures import ThreadPoolExecutor

from .pull import exec_pull
from .compare import compareCommits

def delivery(data):
    # executor = ThreadPoolExecutor(1)
    # executor.submit(exec_sh)
    compareCommits(data.commits)