import datetime
import os
import day16


def main():
    day = str(datetime.date.today().day)
    print('Testing values: ')
    day16.solve(f'inputs/test')
    print('My values: ')
    day16.solve(f'inputs/{day}')


if __name__ == '__main__':
    main()

