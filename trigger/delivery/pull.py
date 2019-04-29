from concurrent.futures import ThreadPoolExecutor

def exec_pull():
    time.sleep(10)
    print(os.popen('cd / && ls').readlines())
