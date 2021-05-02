# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 09:41:44 2021

@author: max
"""

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Total population, N. Will be set at Uk Pop but needs discussing
N = 66650
# Initial number of infected and recovered individuals, I0 and R0. Values can be set at previous end results e.g I1 & R1.
I0, R0 = 1, 0 
# Everyone else, S0, is susceptible to infection initially.
S0 = (N - I0 - R0)/10000
# Contact rate, beta, and mean recovery rate, gamma, (in 1/days). Contact rate, gamma will be a function of the bit values. needs to be discussed. 
beta, gamma = 0.6, 1./10 
# A grid of time points (in days) Will be set at 56 (2 months)
t = np.linspace(0, 56, 56)

# The SIR model differential equations. Can be altered with our equations or we can use theirs.
def deriv(y, t, N, beta, gamma):
    S, I, R = y
    dSdt = -beta * S * I / N
    dIdt = beta * S * I / N - gamma * I
    dRdt = gamma * I
    return dSdt, dIdt, dRdt

# Initial conditions vector. for attempts 2 onwards initial conditions will be end conditions of previous run.
y0 = S0, I0, R0
# Integrate the SIR equations over the time grid, t.
ret = odeint(deriv, y0, t, args=(N, beta, gamma))
S, I, R = ret.T

# Plot the data on three separate curves for S(t), I(t) and R(t) We can get rid of R(t) if we decide not to use it.
#currently it is in multiples of 1000 is we decide to change it it will have to be done here aswell otherwise plot won't work.
fig = plt.figure(facecolor='w')
ax = fig.add_subplot(111, facecolor='#dddddd', axisbelow=True)
ax.plot(t, S/66650, 'b', alpha=0.5, lw=2, label='Susceptible')
ax.plot(t, I/66650, 'r', alpha=0.5, lw=2, label='Infected')
ax.plot(t, R/66650, 'g', alpha=0.5, lw=2, label='Recovered with immunity')
ax.set_xlabel('Time /days') #axis labels
ax.set_ylabel('Number (1.0x10^7)')
ax.set_ylim(0,7.0)
ax.yaxis.set_tick_params(length=0)
ax.xaxis.set_tick_params(length=0)
ax.grid(b=True, which='major', c='w', lw=2, ls='-')
legend = ax.legend()
legend.get_frame().set_alpha(0.5)
for spine in ('top', 'right', 'bottom', 'left'):
    ax.spines[spine].set_visible(False)
plt.show() #plot can also be savesd as a .svg file using, plt.savefig('plot1.svg') or we can add it to one document but i'm not sure how to do that yet.