import datetime
import os
import day4


def main():
    day = str(datetime.date.today().day)
    day4.solve(f'inputs/{day}')


if __name__ == '__main__':
    main()

