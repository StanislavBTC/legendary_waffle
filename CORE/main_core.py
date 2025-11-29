from multiprocessing import Process
from modules.obmen_dannimi.sender import sender_process
from modules.obmen_dannimi.receiver import receiver_process

def start_core_process():
    p1 = Process(target = sender_process, daemon=True)
    p2 = Process(target = receiver_process, daemon=True)

    p1.start()
    p2.start()
    