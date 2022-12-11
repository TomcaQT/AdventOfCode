import datetime
import os
import day12


def main():
    day = str(datetime.date.today().day)
    day12.solve(f'inputs/{day}')


if __name__ == '__main__':
    main()

