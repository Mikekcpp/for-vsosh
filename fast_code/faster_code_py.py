from sys import setrecursionlimit
import threading

setrecursionlimit(10**9)
threading.stack_size(67108864)


def main():
    # write your code here
    pass


thread = threading.Thread(target=main)
thread.start()
