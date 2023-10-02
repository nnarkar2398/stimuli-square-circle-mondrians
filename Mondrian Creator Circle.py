#Narkar and Fenske (2023): A search for an affective index of inhibition in the narrowing of attention 
#reveals interactive effects of congruence and exposure on stimulus liking

#Code for generating the mondrian like patterns for circles for stimuli generation

#load required libraries, packages
from psychopy import visual, core, data, event, logging, gui, misc, monitors
import numpy as np  # whole numpy lib is available, prepend 'np.'
import os  # handy system and path functions
from psychopy.constants import *  # things like STARTED, FINISHED
import random
import math

#initialize random number generator
random.seed()

#global variables
NUM_STIMULUS_POS = 8

COLORS = ['Red','Blue','Green','Purple','Pink','Orange','Yellow','Brown','Grey','Turquoise','Violet']

# Setup the Psycho variables (screen, stimuli, sounds, etc)
win = visual.Window([800,600], fullscr=False, screen=0, allowGUI=False, allowStencil=False, monitor='testMonitor', color='White', colorSpace='rgb', units='deg')
trialClock = core.Clock()
eventClock = core.Clock()
evalClock = core.Clock()
keyResp = event.BuilderKeyResponse()  # create an object of type KeyResponse

screenShNum = 103
mondrians_dir = "/Users/niyatee/Documents/PHD/Undergrads/Kaya/New Stimuli/New"

#Create circles with random sizes and at random positions within the given the range
def inner_for(win):
    random.shuffle(COLORS)
    
    HorPoint1 = random.randint(0,1)*(.2)
    HorPoint1=HorPoint1 / (random.randint(1,5) - 0.5)
    HorPoint2 = 0.5
    HorPoint = HorPoint1 + HorPoint2
    
    ranXPos1 = random.randint(-2,2)
    ranXPos2 = (random.random())
    ranXPos = ranXPos1 + ranXPos2
    
    ranYPos1 = random.randint(-2,2)
    ranYPos2 = (random.random())
    ranYPos = ranYPos1 + ranYPos2
    
    circle1 = visual.Circle(win, units='', lineWidth=1.5, lineColor='black', lineColorSpace='rgb', fillColor = COLORS[0], 
                      fillColorSpace='rgb', radius=(HorPoint),
                      pos=(ranXPos, ranYPos), ori=0.0, opacity=1.0, contrast=1.0, depth=0, interpolate=True,
                      name=None, autoLog=None, autoDraw=False)
    circle1.setAutoDraw(True)
    win.flip()
    
    win.flip(clearBuffer=False)
    win.flip()
    
    win.flip()

#repeat for as many as we need: 64 in total, 32 congruent: with a circle mask, 32 incongruent: with a square mask.
#create them on screen and save the screenshot as png
for trialrep in range(0,41):
    win = visual.Window([800, 600], fullscr=False, screen=0, allowGUI=False, allowStencil=False, monitor='testMonitor',
                        color='Pink', colorSpace='rgb', units='deg')
    for trial in range(0,150):
        inner_for(win)
    win.getMovieFrame(buffer='front')
    screenShNum += 1
    win.saveMovieFrames(os.path.join(mondrians_dir,'Circles' + str(screenShNum) + '.png'))
    win.close()
core.wait(0.5)
print("Done")