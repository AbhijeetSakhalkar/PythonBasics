# -*- coding: utf-8 -*-

import sys

def main():
    x, y, z = map(int, input().split())
    result = -1
    cont = True
    index=2
    a=[0]
    a.append(a[0]+x)
    a.append(a[1]-y)
    if a[0] == z:
        result = 0
        cont = False
    elif a[1] == z:
        result = 1
        cont = False
    elif a[0] > z and a[1] > z:
        cont =False

    while(cont):
        a.append(a[(2 * index) - 2] + x)
        a.append(a[(2 * index) - 1] - y)
        if a[(2 * index) - 1] == z:
            result = (2*index)-1
            cont = False
        elif a[(2 * index)] == z:
            result = a[(2 * index)]
            cont = False
        elif a[(2 * index) - 1] > z and a[(2 * index)] > z:
            cont=False
        else:
            index+=index


    print(result)


if __name__ == '__main__':
    main()