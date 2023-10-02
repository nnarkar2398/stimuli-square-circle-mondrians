#Narkar and Fenske (2023): A search for an affective index of inhibition in the narrowing of attention 
#reveals interactive effects of congruence and exposure on stimulus liking

#Code for generating the mondrian like patterns for squares for stimuli generation for Experiments 1-4.

#load required libraries, packages
from psychopy import visual, core, data, event, logging, sound, gui, misc, monitors
import numpy as np  # whole numpy lib is available, prepend 'np.'
import os  # handy system and path functions
from psychopy.constants import *  # things like STARTED, FINISHED
import random
import math

# initialize random number generator
random.seed()

# global variables
NUM_STIMULUS_POS = 8

COLORS = ['Red', 'Blue', 'Green', 'Purple', 'Pink', 'Orange', 'Yellow', 'Brown', 'Grey', 'Turquoise', 'Violet']

trialClock = core.Clock()
eventClock = core.Clock()
evalClock = core.Clock()
keyResp = event.BuilderKeyResponse()  # create an object of type KeyResponse

screenShNum = 11
mondrians_dir = "/Users/niyatee/Documents/PHD/Masters Thesis/Experiment 3/recognition phase stimuli/new/Square_mondrians"

#Create squares with random sizes and at random positions within the given the range
def inner_for(win):
    random.shuffle(COLORS)

    HorPoint1 = random.randint(1, 2) * (.2)
    HorPoint1 = HorPoint1 / (random.randint(1,5) - 0.5)
    HorPoint2 = 1
    HorPoint = HorPoint1 + HorPoint2

    ranXPos1 = random.randint(-2, 2)
    ranXPos2 = (random.random())
    ranXPos = ranXPos1 + ranXPos2

    ranYPos1 = random.randint(-2, 2)
    ranYPos2 = (random.random())
    ranYPos = ranYPos1 + ranYPos2

    square1 = visual.Rect(win, units='', lineWidth=1.5, lineColor='black', lineColorSpace='rgb', fillColor=COLORS[0],
                      fillColorSpace='rgb', width=(HorPoint), height=(HorPoint),
                      pos=(ranXPos, ranYPos), ori=0.0, opacity=1.0, contrast=1.0, depth=0, interpolate=True,
                      name=None, autoLog=None, autoDraw=False)
    square1.setAutoDraw(True)
    win.flip()

    win.flip(clearBuffer=False)
    win.flip()

    win.flip()

#repeat for as many as we need: 64 in total, 32 congruent: with a square mask, 32 incongruent: with a circle mask.
#create them on screen and save the screenshot as png
for trialrep in range(0,5):
    win = visual.Window([800, 600], fullscr=False, screen=0, allowGUI=False, allowStencil=False, monitor='testMonitor',
                        color='Pink', colorSpace='rgb', units='deg')
    for trial in range(0, 150):
        inner_for(win)
    win.getMovieFrame(buffer='front')
    screenShNum += 1
    win.saveMovieFrames(os.path.join(mondrians_dir, 'Squares' + str(screenShNum) + '.png'))
    win.close()
core.wait(0.5)
print("Done")
