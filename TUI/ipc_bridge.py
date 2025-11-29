import threading
import asyncio
from CORE.modules.obmen_dannimi.queue import mp_queue

asyncio_queue = asyncio.Queue()
_event_loop = None


def _mp_reader_thread():
    global _event_loop
    while True:
        msg = mp_queue.get()
        if _event_loop is not None:
            asyncio.run_coroutine_threadsafe(
                asyncio_queue.put(msg),
                _event_loop
            )


def start_bridge(loop):
    global _event_loop
    _event_loop = loop

    t = threading.Thread(target=_mp_reader_thread, daemon=True)
    t.start()

    return asyncio_queue