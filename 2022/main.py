import datetime
import os
import day3


def main():
    day = str(datetime.date.today().day)
    day3.solve(f'inputs/{day}')


if __name__ == '__main__':
    main()

