#-*- coding:utf-8 -*-

import sys
import random

class ComputeService(object):
    
    ''' 
    @NAME 午餐业务服务类
    @COMMENT 
    @RETURN_CODE 20010-20020
    '''

    def __init__(self):
        pass

    def compute(self,fee,amount):
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
        