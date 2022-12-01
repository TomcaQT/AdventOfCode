import datetime
import os
import day2


def main():
    day = str(datetime.date.today().day)
    day2.solve(f'inputs/{day}')


if __name__ == '__main__':
    main()

