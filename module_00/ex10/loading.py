import time
import sys

def ft_progress(lst):
    start = time.time()
    max_val = max(lst)
    length = len(lst)
    eta = 0
    barsize = 50
    for value in lst:
        progress = int(value / max_val * 100)
        bar = int(value / max_val * barsize)
        duration = time.time() - start
        if not progress == 0:
            eta = duration / progress * 100 - duration
        print(f"ETA: {'{:.2f}'.format(eta)}s [{'{:3d}'.format(progress)}%] [{'{}>{}'.format('='*bar, ' '*(barsize-bar))}] {value+1}/{length} | elapsed time {'{:.2f}'.format(duration)}", end='\r', file=sys.stdout, flush=True)
        yield value
        
if __name__ == "__main__":       
    listy = range(1000)
    ret = 0
    for elem in ft_progress(listy):
        ret += (elem + 3) % 5
        time.sleep(0.005)
    print()
    print(ret)