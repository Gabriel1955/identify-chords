import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

def getValueNote(note):
    notes = ['A','A#','B','C','C#','D','D#','E','F','F#','G','G#']
    value = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    return value[notes.index(note)]

def addNote(note, stringGuitar,ax):
    if stringGuitar < 1 or stringGuitar > 6:
        return -1
    stringsGuitarNotes = ['E', 'B', 'G', 'D', 'A', 'E']
    stringGuitarNote = stringsGuitarNotes[stringGuitar-1]
    
    interval = getValueNote(note)-getValueNote(stringGuitarNote)
    deslocamentoPlot = 0.5
   # if stringGuitarNote != note:
    #    deslocamentoPlot = interval/(2*interval)
    interval = ((interval + 12) % 12) + deslocamentoPlot
    string = 6 - (stringGuitar -1)
    ax.add_patch(mpatches.Circle((interval,string),0.2))
    ax.annotate(note, (interval, string), color='w', weight='bold', 
                            fontsize=14.5, ha='center', va='center')


def getNewPlot(night=True):
    fig, ax = plt.subplots(figsize=(20,6))
    return ax

def updatePlot(ax,night=True):
    ax.clear()
    plt.ion()
    background = ['white', 'black']
    for i in range(1,7):
        ax.plot([i for a in range(22)])
    # Plotting Frets
    for i in range(1,21):
        if i == 13 or i == 1:
            ax.axvline(x=i, color='gray', linewidth=3.5)
            continue
        ax.axvline(x=i, color=background[night-1], linewidth=0.5)
    
    ax.set_axisbelow(True)
    ax.set_xlim([0.5, 21])
    ax.set_ylim([0.4, 6.5])
    ax.set_facecolor(background[night])
    plt.yticks(np.arange(1,7), ['E', 'A', 'D', 'G', 'B', 'E'])
        
def show():
    plt.draw()
    plt.pause(0.000000000000001)

# ax = getNewPlot()
# updatePlot(ax)
# addNote('C#',1,ax)
# show()

