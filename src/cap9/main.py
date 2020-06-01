import time
import rename_dates as re_dates
from rename_dates.create_example_files import create_example_files


def main():
    try:
        create_example_files()
    except:
        print('Files already exist')
    else:
        print('Files created')
        time.sleep(3)

    re_dates.rename_dates()


if __name__ == '__main__':
    main()
