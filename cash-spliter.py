# -*- coding:utf8 -*-

import sys
import random

def split_integer(total,num):
    pools = []
    balance = total
    for n in range(0,num-1):
        avg = int(balance / (num - n))
        print(avg)
        item = random.randint(int(avg * 0.5) ,avg)
        balance = balance - item
        pools.append(item)
    pools.append(balance)
    random.shuffle(pools)
    return pools

def main():
    if len(sys.argv) == 1:
        total = int(input("total cash: "))
        num = int(input("number: "))
    else:
        total = int(sys.argv[1])
        num = int(sys.argv[2])
    print(split_integer(total,num))

if __name__ == '__main__':
    main()