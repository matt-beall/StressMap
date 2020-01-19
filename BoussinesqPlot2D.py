# Boussinesq's Method of Estimate Stress
# analysis assumes an infitnite elastic half space or linear elastic material
# Point Load Case
# Calculating stresses less than a unit of depth will result in values that are not real
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 16:41:43 2019

@author: TQH
"""

import math
from math import pi, sqrt, pow
import numpy as np
import matplotlib
import matplotlib.cm as cm
import matplotlib.pyplot as plt

debugging = 0


def stressFunction(pVal, xVal, yVal, zVal):
    return (3*pVal*pow(zVal, 3)) / (2*pi*pow(math.sqrt(pow(xVal, 2) + pow(yVal, 2) + pow(zVal, 2)), 5))


def stressFunction2D(P, X, Y):
    retVal = (3*P*Y**3)/(2*pi*(np.sqrt((X)**2+(Y)**2))**5)
    return retVal


def plotStuff(P, X, Y, stressZPlot):

    bins = 10

    levels = [i*P/bins for i in range(1, bins)]

    CS = plt.contourf(X, Y, stressZPlot, levels=levels,
                      extend='both', cmap=cm.jet)
    plt.gca().invert_yaxis()
    CB = plt.colorbar(CS, shrink=0.8, extend='both')

    # print(X[0])
    # print(horizontalAxis)
    # print(verticalAxis)
    # print(stressZPlot)

    if(debugging):

        plt.figure()
        l0 = [levels[0] for i in range(len(stressZPlot[0]))]
        l1 = [levels[1] for i in range(len(stressZPlot[0]))]
        l2 = [levels[2] for i in range(len(stressZPlot[0]))]
        l3 = [levels[3] for i in range(len(stressZPlot[0]))]
        l4 = [levels[4] for i in range(len(stressZPlot[0]))]

        plt.plot(stressZPlot[0], 'b')
        plt.plot(stressZPlot[int(len(stressZPlot)/2)], 'r')
        plt.plot(stressZPlot[-1], 'g')
        plt.plot(l0, "k")
        plt.plot(l1, "k")
        plt.plot(l2, "k")
        plt.plot(l3, "k")
        plt.plot(l4, "k")

    plt.show()


def BoussinesqPlot2D(P):
    x = 0.0
    maxX = 0
    y = 0
    z = 0.1

    stressZ = stressFunction(P, x, y, z)

    while stressZ > 100:
        stressZ = stressFunction(P, x, y, z)
        z = z + 0.1

    maxZ = z

    print("Max Z: " + str(maxZ))

    stressZ = stressFunction(P, x, y, z)

    z = 1
    stepSize = 0.01
    minDepth = 0.1

    for z in np.arange(minDepth, maxZ, stepSize):
        x = 0.1
        while stressZ > 1:
            stressZ = stressFunction(P, x, y, z)
            x = x+stepSize

        if x > maxX:
            maxX = x

    horizontalAxis = np.arange(-maxX - 0.1, maxX + 0.1, stepSize)
    verticalAxis = np.arange(0, maxZ, stepSize)

    X, Y = np.meshgrid(horizontalAxis, verticalAxis)

    stressZPlot = stressFunction2D(P, X, Y)

    plotStuff(P, X, Y, stressZPlot)
    bins = 10

    levels = [i*P/bins for i in range(1, bins)]

    CS = plt.contourf(X, Y, stressZPlot, levels=levels,
                      extend='both', cmap=cm.jet)
    plt.gca().invert_yaxis()
    CB = plt.colorbar(CS, shrink=0.8, extend='both')

    # print(X[0])
    # print(horizontalAxis)
    # print(verticalAxis)
    # print(stressZPlot)

    plt.figure()

    l0 = [levels[0] for i in range(len(stressZPlot[0]))]
    l1 = [levels[1] for i in range(len(stressZPlot[0]))]
    l2 = [levels[2] for i in range(len(stressZPlot[0]))]
    l3 = [levels[3] for i in range(len(stressZPlot[0]))]
    l4 = [levels[4] for i in range(len(stressZPlot[0]))]

    plt.plot(stressZPlot[0], 'b')
    plt.plot(stressZPlot[int(len(stressZPlot)/2)], 'r')
    plt.plot(stressZPlot[-1], 'g')
    plt.plot(l0, "k")
    plt.plot(l1, "k")
    plt.plot(l2, "k")
    plt.plot(l3, "k")
    plt.plot(l4, "k")
    plt.show()


def main():
    BoussinesqPlot2D(500)


if __name__ == "__main__":
    main()
