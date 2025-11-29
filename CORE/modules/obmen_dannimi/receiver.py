import time
from .queue import mp_queue

def receiver_process():
    i = 0 
    while True:
        mp_queue.put({"Получено": f"recv event {i}"})
        i += 1
        time.sleep(1)
