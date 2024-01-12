# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 09:27:09 2023

@author: bdpac

BandBTrajectory
"""

import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import integrate

from lover_class import Lover

#Benedick Parameters

benedick = Lover(0.5, 3, -0.5, -0.2)


#Beatrice Parameters

beatrice = Lover(0.4,3, -0.5, -0.2)


#false affection values
Xstar_1= 2
Xstar_2= 2

#points of interest in the play
P=[0,3,6,7,12,16]

def reaction(x,R_PLUS,R_MINUS):
    numerator = math.exp(x)-math.exp(-x)
    denominator = math.exp(x)/R_PLUS - math.exp(-x)/R_MINUS
    return numerator/denominator

def delta_1(t):
    if t>=P[2] and t<P[5]:
        return 2
    else :
        return 0

def delta_2(t):
    if t>=P[3] and t<P[5]:
        return 2
    else :
        return 0

def delta(t):

    return np.array([delta_1(t), delta_2(t)])

def delta_model(X, t, lover_1, lover_2):
    X_1, X_2 = X
    delta_2, delta_1 = delta(t)
    dX_1 = -lover_1.alpha*X_1 + reaction(X_2+delta_2, lover_1.positive_limit, lover_1.negative_limit) + lover_1.gamma*lover_2.appeal
    dX_2 = -lover_2.alpha*X_2 + reaction(X_1+delta_1, lover_2.positive_limit, lover_2.negative_limit) + lover_2.gamma*lover_1.appeal
    return np.array([dX_1, dX_2])

def annotate_point(point, title):
    plt.text(point[0],point[1], title, horizontalalignment='right')
    plt.plot(point[0], point[1], marker='o', markeredgecolor = "blue", markerfacecolor='blue')

def trajectory_plotter(model, args = (), range_1=(-10,10), range_2=None, timeRange = 18 ,p0=(-.5,-.8),
                       point_array = [], show=False):
    t=np.linspace(0, timeRange, timeRange*10)
    trajectory = integrate.odeint(model, p0, t, args=args)
    
    for i in range(len(point_array)):
        annotate_point(trajectory[P[i]*10], " P"+ str(i) +" ")
    
    plt.plot(trajectory[:,0], trajectory[:,1], color="blue")
    plt.xlabel("Love of Benedick")
    plt.ylabel("love of Beatrice")
    plt.xlim([-2,6])
    plt.ylim([-2,7])
    plt.figure(dpi=1200)
    if show:
        plt.show()

if __name__ == "__main__":
    trajectory_plotter(delta_model, args=(benedick, beatrice), range_1 = (-10,10), point_array=P, show = True)