import time
from .queue import mp_queue

def sender_process():
    i = 0 
    while True:
        mp_queue.put({"Отправлено": f"send event {i}"})
        i += 1
        time.sleep(1)
