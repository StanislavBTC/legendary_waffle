import time
from queue import Empty
from .queue import mp_queue_in, mp_queue_out

def sender_process():

    i = 0
    while True:
        mp_queue_in.put({"sender": f"event: {i}"})
        i += 1

        try:
            cmd = mp_queue_out.get_nowait()
            print("[Sender получил команду от TUI]", cmd)

            if cmd.get("cmd") == "pause":
                print("Sender: pause")
            elif cmd.get("cmd") == "reset":
                i = 0
        except Empty:
            pass

        time.sleep(1)