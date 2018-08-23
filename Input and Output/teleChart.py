# a stacked bar plot with errorbars
import numpy as np
import matplotlib.pyplot as plt

def createBarChart(v,sW,oSW,sC,h,a,teams,matchNum):

    N = 6
    vault = np.array(v)
    switch = np.array(sW)
    oppSwitch = np.array(oSW)
    scale = np.array(sC)
    hang = np.array(h)
    assistance = np.array(a)
    
    ind = np.arange(N)    # the x locations for the groups
    width = 0.35       # the width of the bars: can also be len(x) sequence

    p1 = plt.bar(ind, scale, width, color='b') #blue
    p2 = plt.bar(ind, vault, width, bottom=scale, color='g') #green
    p3 = plt.bar(ind, switch, width, bottom=scale+vault, color='r') #red
    p4 = plt.bar(ind, oppSwitch, width, bottom=scale+vault+switch, color='#FFA500') #orange
    p5 = plt.bar(ind, hang, width, bottom=scale+vault+switch+oppSwitch, color='#9400D3') #purple
    p6 = plt.bar(ind, assistance, width, bottom=scale+vault+switch+oppSwitch+hang, color='#FF00FF') #pink

    plt.title("qm" + (str)(matchNum))
    plt.tick_params(labelright=True)
    plt.xticks(ind, teams)
    plt.yticks(np.arange(0, 20, 1))
    plt.legend((p1[0], p2[0], p3[0], p4[0], p5[0], p6[0]), ('Scale', 'Vault', 'Switch', "oppSwitch", "Hang", "Assistance"))

    plt.savefig("qm" + (str)(matchNum) + "tele.png")
    
if __name__ == '__main__':
    createBarChart()
