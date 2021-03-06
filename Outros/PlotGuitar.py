import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches


def getPlot():
    plt.ion()
    fig, ax = plt.subplots(figsize=(20,6))
    return ax

def plot(Notes,ax,night=True):
    # scale = get_notes(key, intervals)
    # Plot Strings
    background = ['white', 'black']
    for i in range(1,7):
        ax.plot([i for a in range(22)])
    # Plotting Frets
    for i in range(1,21):
        if i == 12:
            ax.axvline(x=i, color='gray', linewidth=3.5)
            continue
        ax.axvline(x=i, color=background[night-1], linewidth=0.5)
    
    #ax.grid(linestyle='-', linewidth='0.5', color='black')
    ax.set_axisbelow(True)
    
    # setting height and width of displayed guitar
    ax.set_xlim([0.5, 21])
    ax.set_ylim([0.4, 6.5])
    ax.set_facecolor(background[night])
    # to_plot = find_notes(scale)
    
    # ACHTUNG!!!
    # for y_val, key in zip([1,2,3,4,5,6], 'EADGBE'):
    #     for i in notes[key]:
    #         font = 12
    #         x = i+0.5  # /figheight
    #         p = mpatches.Circle((x, y_val), 0.2)
    #         ax.add_patch(p)
    #         note = strings[key][i]
    #         # if note is root make it a bit bigger
    #         if note == scale[0]:
    #             font=14.5
    #         ax.annotate(note, (i+0.5, y_val), color='w', weight='bold', 
    #                         fontsize=font, ha='center', va='center')
    ax.add_patch(mpatches.Circle((Notes,5),1))
    plt.yticks(np.arange(1,7), ['E', 'A', 'D', 'G', 'B', 'E'])
    # plt.xticks(np.arange(21)+0.5, np.arange(0,22))
    # plt.show()
    plt.plot()
    plt.draw()
    plt.pause(4.000000000000001)
    plt.clf()
count = 0
while count < 10:
    plot(count)
    count = count + 1
