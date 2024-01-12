# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 13:24:57 2023

@author: bdpac
"""

import numpy as np
import matplotlib.pyplot as plt

from lover_class import *
from Ben_bea_trajectory import *

#Takes a model and shows the change in the bluffing coefficient (delta) on top and the trajectory of
#the two variables beneath.
def bluffing_effect_plotter(model, args=(), range_1=(-10,10), range_2=None, timeRange = 25 ,p0=(-.5,-.8)):
    t=np.linspace(0, timeRange, timeRange*10)
    trajectory = integrate.odeint(model, p0, t, args=args)
       
    fig, axs = plt.subplots(2, constrained_layout=True)
    fig.suptitle('Effect of Bluffing')
    l1,l2, = axs[0].plot(t, list(map(delta, t)))
    l1.set_label('B2')
    l2.set_label('B1')
    axs[0].legend()
    line1, = axs[1].plot(t, trajectory[:, 0], label='Interest of Benedick')
    line2, = axs[1].plot(t, trajectory[:, 1], label='Interest of Beatrice')
    
    axs[1].annotate(" P0 ", (0,1))
    axs[1].axvline(x=0, linestyle='dashed')
    
    axs[1].annotate(" P1 ", (4,2))
    axs[1].axvline(x=4, linestyle='dashed')
    
    axs[1].annotate(" P2 ", (6,1))
    axs[1].axvline(x=6, linestyle='dashed')
    
    axs[1].annotate(" P3 ", (7,2))
    axs[1].axvline(x=7, linestyle='dashed')
    
    axs[1].annotate(" P4 ", (12,1))
    axs[1].axvline(x=12, linestyle='dashed')
    
    axs[1].annotate(" P5 ", (17,2))
    axs[1].axvline(x=17, linestyle='dashed')
    axs[1].legend()
    
if __name__ == "__main__":
    bluffing_effect_plotter(delta_model,args=(benedick, beatrice), range_1 = (-10,10))