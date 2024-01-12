# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 10:00:48 2024

@author: bdpac

Lover Class 
"""

"""
Use this to define one individual in a love story. note that we use the simplified 
version of appeal and reaction to appeal(gamma) in our models, usually these would be an array
of appeal values and an array of reaction functions, which would be summed together to 
get our total appeal.
"""
class Lover:
    
    def __init__(self, alpha, positive_limit, negative_limit, appeal, gamma = 1):
        self.alpha = alpha
        self.positive_limit = positive_limit
        self.negative_limit = negative_limit
        self. appeal = appeal    
        self.gamma = gamma
    