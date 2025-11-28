#второй файл в CORE

import os
import asyncio
import time

read_fd, write_fd = os.pipe()

async def sender():
    os.close(read_fd)  # Закрываем дескриптор чтения
    while True:
        # Пример данных для отправки
        msg = "1, 2\n" # Например, загрузка и выгрузка
        os.write(write_fd, msg.encode())
        print("Отправлено:", msg.strip())
        await asyncio.sleep(1)  

def on_data_available():
    raw = os.read(read_fd, 1024)
    if raw:
        for line in raw.split(b"\n"):
            if line:
                print("Получено:", line.decode().strip())

async def receiver():
    os.close(write_fd)
    loop = asyncio.get_running_loop()
    loop.add_reader(read_fd, on_data_available)
    while True:
        await asyncio.sleep(1)

async def main():
    await asyncio.gather(sender(), receiver())

if __name__ == "__main__":
    asyncio.run(main())