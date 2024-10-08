#!/usr/bin/env python3
# from typing import *


# def solve(n: int, a: List[str]) -> List[str]:
def solve(n, a):
    return [a1[0] + str(len(a1) - 2) + a1[-1] if len(a1) > 10 else a1 for a1 in a]


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    n = int(input())
    a = [None for _ in range(n)]
    for i in range(n):
        a[i] = input()
    ans = solve(n, a)
    for i in range(n):
        print(ans[i])


if __name__ == '__main__':
    main()
