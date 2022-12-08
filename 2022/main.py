import datetime
import os
import day9


def main():
    day = str(datetime.date.today().day)
    day9.solve(f'inputs/{day}')


if __name__ == '__main__':
    main()

