import datetime
import os
import day10


def main():
    day = str(datetime.date.today().day)
    day10.solve(f'inputs/{day}')


if __name__ == '__main__':
    main()

