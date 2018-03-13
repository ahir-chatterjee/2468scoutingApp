# Plots a radar chart.
#https://stackoverflow.com/questions/42227409/tutorial-for-python-radar-chart-plot

from math import pi
import matplotlib.pyplot as plt
import os

def createMultiRadarPlot(team1,team2,team3):
    # Set data
    bot = ['Switch', 'Scale', 'Hang', 'Vault']
    #values = [agility, switch, scale, hang, vault]
    values1 = [team1[1],team1[2],team1[3],team1[4]]
    values2 = [team2[1],team2[2],team2[3],team2[4]]
    values3 = [team3[1],team3[2],team3[3],team3[4]]
    for i in range(0,len(values1)):
        if(values1[i] == 0):
            values1[i] = 0.15
    for i in range(0,len(values2)):
        if(values2[i] == 0):
            values2[i] == 0.15
    for i in range(0,len(values3)):
        if(values3[i] == 0):
            values3[i] == 0.15
    
    N = len(bot)
    
    x_as = [n / float(N) * 2 * pi for n in range(N)] #radians around
    
    # Because our chart will be circular we need to append a copy of the first 
    # value of each list at the end of each list with data
    values1 += values1[:1]
    values2 += values2[:1]
    values3 += values3[:1]
    x_as += x_as[:1]
    
    
    # Set color of axes
    plt.rc('axes', linewidth=0.5, edgecolor="#888888")
    
    
    # Create polar plot
    ax = plt.subplot(111, polar=True)
    
    
    # Set clockwise rotation. That is:
    ax.set_theta_offset(pi / 2)
    ax.set_theta_direction(-1)
    
    
    # Set position of y-labels
    ax.set_rlabel_position(0)
    
    
    # Set color and linestyle of grid
    ax.xaxis.grid(True, color="#888888", linestyle='solid', linewidth=0.5)
    ax.yaxis.grid(True, color="#888888", linestyle='solid', linewidth=0.5)
    
    
    # Set number of radial axes and remove labels
    plt.xticks(x_as[:-1], [])
    
    # Set yticks
    plt.yticks([5], ["5"])
    
    
    # Plot data
    ax.plot(x_as, values1, color="#539EFF", linewidth=3, linestyle='solid', zorder=3)
    ax.plot(x_as, values2, color="#d62822", linewidth=3, linestyle='solid', zorder=3)
    ax.plot(x_as, values3, color="#25d167", linewidth=3, linestyle='solid', zorder=3)
    
    # Fill area
    #ax.fill(x_as, values, 'b', alpha=0.3)
    
    # Set axes limits
    plt.ylim(0, 5)
    
    
    # Draw ytick labels to make sure they fit properly
    for i in range(N):
    	angle_rad = i / float(N) * 2 * pi
    
    	if angle_rad == 0:
    		ha, distance_ax = "center", 1
    	elif 0 < angle_rad < pi:
    		ha, distance_ax = "left", 1
    	elif angle_rad == pi:
    		ha, distance_ax = "center", 1
    	else:
    		ha, distance_ax = "right", 1
    
    	ax.text(angle_rad, 5 + distance_ax, bot[i], size=20, horizontalalignment=ha, verticalalignment="center")
    
    
    # Show polar plot
    plt.savefig(team1[0] + "+" + team2[0] + "+" + team3[0] + ".png")
    ax.clear()

if __name__ == '__main__':
    createMultiRadarPlot()
