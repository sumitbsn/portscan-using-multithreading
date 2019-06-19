#!/usr/bin/env python
import socket
import subprocess
import sys
from datetime import datetime
import threading
import Queue as queue

print_lock = threading.Lock()

if len(sys.argv) !=2 :
    print ("Usage: portscan.py <host>")
    sys.exit(1)

host = sys.argv[1]

def scan(port):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        con = s.connect((host, port))
        with print_lock:
            print('Port: ' + str(port) + ' is open')
        con.close()
    
    except:
        pass


def threader():
    while True:
        worker = q.get()
        scan(worker)
        q.task_done()



if __name__ == "__main__":

    #subprocess.call('clear', shell=True)

    threadcount = 100

    q = queue.Queue()
    startTime = datetime.now()

    for x in range(threadcount):
        t = threading.Thread(target=threader)
        t.daemon = True
        t.start()

    for worker in range(1, 1000):
        q.put(worker)

    q.join()

    print('Time taken:', datetime.now() - startTime)


