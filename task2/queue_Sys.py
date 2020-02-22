from tweets2image import getTweets
from image2video import convert
import queue
import time 
import threading
import multiprocessing

keyNames = ['BU_ece','realDonaldTrump','CNN','ArianaGrande','PrimeVideo','PDChina','nytimes','justinbieber','BillGates']
threads = 12

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
    print(" ----- done ------- ")

q = queue.Queue()
threads = []

for i in range(threads):
  t = threading.Thread(target=worker)
  t.start()
  threads.append(t)

for key in keyNames:
  q.put(key)

q.join()

for i in range(threads):
  q.put(None)

for t in threads:
  t.join()

