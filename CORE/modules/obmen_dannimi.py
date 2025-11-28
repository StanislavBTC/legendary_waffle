#второй файл в CORE

import subprocess
from typing import TextIO, cast

proc = subprocess.Popen(
    ["python3", "child_script.py"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    text=True
)

stdin = cast(TextIO, proc.stdin)
stdout = cast(TextIO,proc.stdout )

stdin.write("analyze traffic\n")
stdout.flush()

response = stdout.readline()
print(response)