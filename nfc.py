import time

import nxppy

mifare = nxppy.Mifare()

while True:
    try:
        uid = mifare.select()
        print(uid)
        message = mifare.read()
        print(message)
    except nxppy.SelectError:
        pass
    except MemoryError:
        print('Could not read chip')
        pass
    time.sleep(1)
