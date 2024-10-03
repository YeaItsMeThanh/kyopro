#!/usr/bin/env python3
# from typing import *


# def solve(a: str, b: str) -> int:
def solve(a, b):
    a, b = a.casefold(), b.casefold()
    return -1 if a < b else 0 if a == b else 1


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    a = input()
    b = input()
    a1 = solve(a, b)
    print(a1)


if __name__ == '__main__':
    main()
