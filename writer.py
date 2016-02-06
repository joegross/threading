#!/usr/bin/env python

import threading
import time
import string
import random


class WriteLog(threading.Thread):

    def __init__(self, logfile):
        threading.Thread.__init__(self)
        self.logfile = logfile

    def run(self):
        with open(self.logfile, 'w', 0) as out:
            while True:
                out.write("%s thread:%s %s\n" % (time.asctime(time.localtime(time.time())), self.ident, random.choice(list(string.ascii_letters))*10000))
                time.sleep(1)

out = 'log'
# threads = []
for i in range(0, 100):
    t = WriteLog('%s.%s' % (out, i))
    t.daemon = True
    t.start()
    # threads.append(t)
while True:
    time.sleep(1)