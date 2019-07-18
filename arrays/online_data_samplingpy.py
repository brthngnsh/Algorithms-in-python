# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 18:45:23 2019

@author: PlagueDoctor
"""

#Random sampling - online data

#Design a program that takes as input a size k, and reads packets, 
#continuously maintaining auniform random subset of size k of the read packets.
#Hint: Suppose you have a procedure which selects k packets from the first n > k packets as specified. 
#How would you deal with the (n + 1)th packet?

def online_data_sampling(packets,k):
    #packets is a list
    import itertools
    import random
    sampling_result = list(itertools.islice(packets,k))
    num_seen_so_far = k
    #read k elements
    for x in packets:
        num_seen_so_far += 1
        idx_to_replace = random.randrange(num_seen_so_far)
        # Generate a randon number in [0, nufl-seen-so-far -  1], and if thjs
        # nunber is jn [0, k - 1], we replace that e.lement fron the sanpTe with
        # x.
        if idx_to_replace < k :
            sampling_result[idx_to_replace] = x
    return sampling_result