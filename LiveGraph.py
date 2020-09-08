import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

fig = plt.figure()
fig.patch.set_facecolor('black')
fig.canvas.set_window_title('Alltime GSP Z3T0Games')
ax1 = fig.add_subplot(1,1,1)
ax1.set_facecolor("black")
ax1.spines["bottom"].set_color("white")
ax1.spines["left"].set_color("white")
ax1.spines["bottom"].set_linewidth(5)
ax1.spines["left"].set_linewidth(5)
ax1.spines['right'].set_visible(False)
ax1.spines['top'].set_visible(False)
ax1.tick_params(axis='x', colors='white', length=7, width=5)
ax1.tick_params(axis='y', colors='white',length=7, width=5)

def animate(i):
    pullData = open("GSP.txt","r").read()
    dataArray = pullData.split('\n')
    xar = []
    yar = []
    for eachLine in dataArray:
        if len(eachLine)>1:
            x,y = eachLine.split(',')
            xar.append(int(x))
            yar.append(int(y))
    ax1.clear()
    ax1.plot(xar,yar,linewidth=8)
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()