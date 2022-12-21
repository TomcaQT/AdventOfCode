import datetime
import os
import day17, day21


def main():
    day = str(datetime.date.today().day)
    print('Testing values: ')
    day21.solve(f'inputs/test')
    print('My values: ')
    day21.solve(f'inputs/{day}')


if __name__ == '__main__':
    main()
