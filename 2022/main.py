import datetime
import os
import day8


def main():
    day = str(datetime.date.today().day)
    day8.solve(f'inputs/{day}')


if __name__ == '__main__':
    main()

