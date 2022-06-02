import psutil
import os
import time


if __name__ == '__main__':
    pid = os.getpid()
    p = psutil.Process()
    print('Process info:')
    print(f'name   : {p.name()}')
    print(f'exe    : {p.exe()}')

    data = []
    while True:
        data += range(10000)
        info = p.memory_full_info()

        # convert to mb
        memory = info.uss / 1024 / 1024
        print('Memory used: {:.2f} MB'.format(memory))

        time.sleep(1)
