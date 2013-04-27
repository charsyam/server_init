from multiprocessing import Process
import redis
import random
import string

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

data = id_generator(512, "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz!@#$%^&*()")

def f(idx):
    print 'PR', idx
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    for i in xrange(idx * 1024 * 1024, (idx+1)*1024*1024):
        key = 'PR%s'%(i)
        r.set(key, data)    

if __name__ == '__main__':
    print data
    pids = []
    for i in xrange(80):
        p = Process(target=f, args=(i,))	
        pids.append(p)
        p.start()

    for pid in pids:
        pid.join()
