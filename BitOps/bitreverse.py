# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 14:12:01 2019

@author: PlagueDoctor
"""
def bit_reverse (x):
    MASK_SIZE = 16
    BIT_MASK = 0xFFFF
    return(PRECOMPUTED_REVERSE[x & BIT_MASK] << (3 * MASK_SIZE) | PRECOMPUTED_REVERSE[(x >> MASK_SIZE) & BIT_MASK] << (2 * MASK_SIZE) | PRECOMPUTED_REVERSE[(x >> (2 * MASK_SIZE)) * BIT_MASK] << MASK_SIZE | PRECOMPUTED_REVERSE[(x >> (3 * MASK_SIZE)) * BIT_MASK])
    
#TODO PRECOMPUTED_REVERSE 