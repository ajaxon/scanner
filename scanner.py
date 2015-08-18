import socket
import threading
from Queue import Queue

host = '127.0.0.1'
lock = threading.Lock()


def port_scan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, port))
        lock.acquire()
        print "Port " + str(port) + " is open"
        lock.release()
        s.close()
    except:
        return False


# thread

q = Queue()


# Work that thread will do
def worker():
    while True:
        port = q.get()
        port_scan(port)
        q.task_done()

# Add port numbers to queue to check
for i in range(10000):
    q.put(i)
# Threads
for i in range(100):
    t = threading.Thread(target=worker)
    # t.daemon = True
    t.start()



