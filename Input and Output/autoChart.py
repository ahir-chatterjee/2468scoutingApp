# a stacked bar plot with errorbars
import numpy as np
import matplotlib.pyplot as plt

def createBarChart(aR,sW,sC,teams,matchNum):

    N = 6
    autoRun = np.array(aR)
    switch = np.array(sW)
    scale = np.array(sC)
    ind = np.arange(N)    # the x locations for the groups
    width = 0.35       # the width of the bars: can also be len(x) sequence

    p1 = plt.bar(ind, autoRun, width, color='b')
    p2 = plt.bar(ind, switch, width, bottom=autoRun, color='r')
    p3 = plt.bar(ind, scale, width, bottom=autoRun+switch, color='g')

    plt.title("qm" + (str)(matchNum))
    plt.tick_params(labelright=True)
    plt.xticks(ind, teams)
    plt.yticks(np.arange(0, 5, .5))
    plt.legend((p1[0], p2[0], p3[0]), ('Auto Run', 'Switch', 'Scale'))

    plt.savefig("qm" + (str)(matchNum) + "auto.png")

if __name__ == '__main__':
    createBarChart()
