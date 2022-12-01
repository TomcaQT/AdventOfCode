import datetime
import os
import day1



def read_input(day: str):
    lines = []
    with open(f'inputs/{day}') as file:
        lines = file.readlines()
    return lines


def main():
    data = read_input(str(datetime.date.today().day) )
    day1.solve(data)


if __name__ == '__main__':
    main()

