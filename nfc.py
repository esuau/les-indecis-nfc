import time

import nxppy


def main():
    mifare = nxppy.Mifare()

    while True:
        try:
            uid = mifare.select()
            print(uid)
            ndef_data = mifare.ndef_data()
            print(ndef_data)
        except nxppy.SelectError:
            pass
        except MemoryError:
            print('Could not read chip')
            pass
        time.sleep(1)


if __name__ == '__main__':
    main()
