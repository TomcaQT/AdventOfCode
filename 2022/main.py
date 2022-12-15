import datetime
import os
import day15


def main():
    day = str(datetime.date.today().day)
    print('Testing values: ')
    day15.solve(f'inputs/test', 10, 20)
    print('My values: ')
    day15.solve(f'inputs/{day}', 2000000, 4000000)


if __name__ == '__main__':
    main()

