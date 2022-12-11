import datetime
import os
import day11


def main():
    day = str(datetime.date.today().day)
    day11.solve(f'inputs/{day}')


if __name__ == '__main__':
    main()

