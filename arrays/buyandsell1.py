# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 16:34:32 2019

@author: PlagueDoctor
"""

#Buy and sell stocks once
def buy_and_sell_1(pricelist):
    max_profit , min_so_far = 0.0 , float("inf")
    for price in pricelist:
        max_profit_today = price-min_so_far
        max_profit = max(max_profit,max_profit_today)
        min_so_far = min(min_so_far,price)
    return max_profit
