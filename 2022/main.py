import datetime
import os
import day5


def main():
    day = str(datetime.date.today().day)
    day5.solve(f'inputs/{day}')


if __name__ == '__main__':
    main()

