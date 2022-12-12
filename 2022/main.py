import datetime
import os
import day13


def main():
    day = str(datetime.date.today().day)
    print('Testing values: ')
    day13.solve(f'inputs/test')
    print('My values: ')
    day13.solve(f'inputs/{day}')


if __name__ == '__main__':
    main()

