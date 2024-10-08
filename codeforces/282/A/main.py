#!/usr/bin/env python3
# from typing import *


# def solve(n: int, a: List[str]) -> int:
def solve(n, a):
    return sum(1 if a1[1] == '+' else -1 for a1 in a)


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    n = int(input())
    a = [None for _ in range(n)]
    for i in range(n):
        a[i] = input()
    a1 = solve(n, a)
    print(a1)


if __name__ == '__main__':
    main()
