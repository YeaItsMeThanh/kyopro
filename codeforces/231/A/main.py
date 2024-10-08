#!/usr/bin/env python3
# from typing import *


# def solve(a: int, b: List[int], c: List[int], d: List[int]) -> int:
def solve(a, b, c, d):
    return sum(1 for a2 in (b[a1] + c[a1] + d[a1] for a1 in range(a)) if a2 >= 2)


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    a = int(input())
    b = [None for _ in range(a)]
    c = [None for _ in range(a)]
    d = [None for _ in range(a)]
    for i in range(a):
        b[i], c[i], d[i] = map(int, input().split())
    a1 = solve(a, b, c, d)
    print(a1)


if __name__ == '__main__':
    main()
