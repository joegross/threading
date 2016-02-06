#!/usr/bin/env python

import threading
import os
import os.path
import time


# reader thread subclasses threading.Thread
class ShuttleLog(threading.Thread):

    def __init__(self, logfile, fh, lock):
        threading.Thread.__init__(self)
        self.logfile = logfile
        self.fh = fh
        self.lock = lock

    def run(self):
        with open(self.logfile, 'r') as input_file:
            while True:
                line = input_file.readline()
                while line:
                    with lock:
                        fh.write(line)
                    line = input_file.readline()
                time.sleep(1)

# main function to instantiate each thread and run it
out = 'combined.log'
if os.path.exists(out):
    os.unlink(out)
fh = open(out, 'a', 1)
lock = threading.Lock()
for logfile in os.listdir(os.getcwd()):
    if logfile.startswith("log."):
        # create a read thread for each file
        t = ShuttleLog(logfile, fh, lock)
        # daemonize thread:
        t.daemon = True
        # start the thread
        t.start()

print "done initializing"

while True:
    time.sleep(1)
