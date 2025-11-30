import asyncio
import threading
from queue import Empty
from CORE.modules.obmen_dannimi.queue import mp_queue_in, mp_queue_out

asyncio_in = asyncio.Queue()     
asyncio_out = asyncio.Queue()   

loop = None


def _reader_thread():

    global loop

    while loop is None:
        pass

    while True:
        
        msg = mp_queue_in.get()  
        asyncio.run_coroutine_threadsafe(
            asyncio_in.put(msg),
            loop
        )


def _writer_thread():

    while True:
        try:
            cmd = asyncio_out.get_nowait()
            mp_queue_out.put(cmd)
        except Empty:
            pass


def start_bridge(event_loop):

    global loop
    loop = event_loop

    threading.Thread(target=_reader_thread, daemon=True).start()
    threading.Thread(target=_writer_thread, daemon=True).start()

    return asyncio_in, asyncio_out