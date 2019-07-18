# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 17:36:07 2019

@author: PlagueDoctor
"""

def buy_and_sell_twice(prices):
    min_so_far,max_profit=float('inf'),0
    #first profit :-
    first_profit=[]
    for i,prices in enumerate(prices):
        min_so_far=min(min_so_far,prices)
        max_profit=max(max_profit,prices-min_so_far)
        first_profit[i]=max_profit
    #second buy|sell :-
    max_price_so_far = float('-inf')
    for i,prices in reversed(list(enumerate(prices[1:],1))):
        max_profit=(max_profit,prices)
        max_profit=max(max_profit,max_price_so_far-prices + first_profit[i-1])
    return max_profit
        