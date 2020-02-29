import os
import subprocess
from tweets2image import getTweets
from image2video import convert
import queue
import time 
import threading
import multiprocessing

keyWords = ['ArianaGrande','PrimeVideo','PDChina','nytimes','justinbieber','BillGates']
threads_num = 12

q = queue.Queue()
threads = []

def worker():
  count = 0
  while True:
    item = q.get()
    if item is None:
      break
    getTweets(item)
    convert(item)
    count += 1
    q.task_done()
    print(" ------ Current Done ------ ")

for i in range(threads_num):
  t = threading.Thread(target = worker)
  t.start()
  threads.append(t)

for key in keyWords:
  q.put(key)

q.join()

for i in range(threads_num):
  q.put(None)

for t in threads:
  t.join()

