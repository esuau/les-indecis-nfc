# coding=utf-8
import json
import time

import nxppy


def main():
    mifare = nxppy.Mifare()

    while True:
        try:
            uid = mifare.select()
            print(uid)
            ndef_data = mifare.ndef_data()
            data = json.loads(ndef_data[5:])
            print(data)
        except nxppy.SelectError:
            pass
        except MemoryError:
            print('Could not read chip')
            pass
        except ValueError:
            print('Could not parse data from JSON')
            pass
        time.sleep(1)


if __name__ == '__main__':
    main()
