import time
from queue import Empty
from .queue import mp_queue_in

def receiver_process():

    i = 0 
    while True:
        mp_queue_in.put({"Получено": f"tick {i}"})
        i += 1

        try:

            cmd = mp_queue_in.get_nowait()
            print("[Receivir получил CMD]:", cmd)

            if cmd.get("cmd") == "cmd":
                print("Receiver pause")
            elif cmd.get("cmd") == "reset":
                pass

        except Empty:
            pass 

        time.sleep(1)
