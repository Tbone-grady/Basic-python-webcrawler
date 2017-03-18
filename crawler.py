import sys
import thread
import Queue
import urllib
import urlparse
import time
import os
import sys

dupcheck = set()
q = Queue.Queue(100)
q.put(sys.argv[1])
def queueRLs(html, orgLink):
  for url in re.findall('''<a[^>]+href=["'](.[^"']+)["']''', html, re.I):
    link = url.split("#", 1)[0] if url.startwith("http") else
'{uri.scheme}://{uri.netloc}'.format(uri=urlparse.urlparse(origLink))
