#-*- coding:utf-8 -*-

import sys
import random

class ComputeService(object):
    
    ''' 
    @NAME 拆分计算
    @COMMENT 
    @RETURN_CODE 
    '''

    def __init__(self):
        pass

    def compute(self,fee,amount):

        if amount > 10000:
            amount = 10000

        pools = []
        balance = fee
        for n in range(0,amount-1):
            avg = int(balance / (amount - n))
            print(avg)
            item = random.randint(int(avg * 0.5) ,avg)
            balance = balance - item
            pools.append(item)
        pools.append(balance)
        random.shuffle(pools)
        return pools
        