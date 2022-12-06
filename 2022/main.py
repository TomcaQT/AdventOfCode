import datetime
import os
import day7


def main():
    day = str(datetime.date.today().day)
    day7.solve(f'inputs/{day}')


if __name__ == '__main__':
    main()

