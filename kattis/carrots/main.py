#!/usr/bin/env python3
# from typing import *


# def solve(n: int, a: int) -> int:
def solve(n, a):
    return a


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    # failed to analyze input format
    # n = int(input())  # TODO: edit here
    n, a = list(map(int, input().split()))  # TODO: edit here
    a = solve(n, a)
    print(a)


if __name__ == '__main__':
    main()
