#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.10),
    on December 22, 2020, at 18:56
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.2.10'
expName = 'GuessTheSound'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\wangs\\OneDrive - The University of Western Ontario\\Desktop\\Project BL\\Guess The Sound\\GuessTheSound_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Welcome"
WelcomeClock = core.Clock()
InstructionTxt = visual.TextStim(win=win, name='InstructionTxt',
    text="Welcome to 'Guess the Sound!'\n\n\nIn this task, you will be presented with different environmental sounds one by one. Listen to each sound and try to give it a label so that another person, seeing only your labels, can form an idea of what the sound was like.\n\n\n",
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
WelcomeContinueKey = keyboard.Keyboard()
count = 0
WelcomContinue = visual.TextStim(win=win, name='WelcomContinue',
    text='Press SPACE to continue',
    font='Arial',
    pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "Welcome2"
Welcome2Clock = core.Clock()
InstructionTxt2 = visual.TextStim(win=win, name='InstructionTxt2',
    text='Each sound will only last a few seconds and will be only played once so please listen carefully.\n\nYou can leave your answer blank, but please try to label as many items as possible.\n\n\n',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
WelcomeContinue2 = visual.TextStim(win=win, name='WelcomeContinue2',
    text='Press SPACE to continue',
    font='Arial',
    pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
WelcomeContinueKey2 = keyboard.Keyboard()

# Initialize components for Routine "StartAdjustment"
StartAdjustmentClock = core.Clock()
VolumeBeginTxt = visual.TextStim(win=win, name='VolumeBeginTxt',
    text='We will first play some music to make sure your volume is at a comfortable level.\n\n',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
VolumeContinue = visual.TextStim(win=win, name='VolumeContinue',
    text='Press SPACE when you are ready for the sound check',
    font='Arial',
    pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
VolumeContinueKey = keyboard.Keyboard()

# Initialize components for Routine "VolumeAdjustment"
VolumeAdjustmentClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Please adjust your volume to a comfortable level.\n',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
Music = sound.Sound('volumeadjust.wav', secs=-1, stereo=True, hamming=True,
    name='Music')
Music.setVolume(0.3)
EndAdjustment = keyboard.Keyboard()
AdjustContinue = visual.TextStim(win=win, name='AdjustContinue',
    text='Press SPACE when you are ready to begin the task',
    font='Arial',
    pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "Start"
StartClock = core.Clock()
StartTxt = visual.TextStim(win=win, name='StartTxt',
    text='We will now begin the task',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Count3"
Count3Clock = core.Clock()
no3 = visual.TextStim(win=win, name='no3',
    text='3',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Count2"
Count2Clock = core.Clock()
no2 = visual.TextStim(win=win, name='no2',
    text='2',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Count1"
Count1Clock = core.Clock()
no1 = visual.TextStim(win=win, name='no1',
    text='1',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Study"
StudyClock = core.Clock()
Question = visual.TextStim(win=win, name='Question',
    text='What is this sound?\n',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
ResponseBox = visual.TextBox2(
     win, text='default text', font='Arial',
     pos=(0, -0.2),     letterHeight=0.03,
     size=None, borderWidth=2.0,
     color='black', colorSpace='rgb',
     opacity=1,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=None,
     anchor='center',
     fillColor='white', borderColor='black',
     flipHoriz=False, flipVert=False,
     editable=True,
     name='ResponseBox',
     autoLog=True,
)
SubmitClick = event.Mouse(win=win)
x, y = [None, None]
SubmitClick.mouseClock = core.Clock()
ClickTheButton = visual.TextStim(win=win, name='ClickTheButton',
    text="Click 'Submit' to continue.",
    font='Arial',
    pos=(0, -0.03), height=0.025, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
SoundItem = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='SoundItem')
SoundItem.setVolume(1.1)
ItemNo = visual.TextStim(win=win, name='ItemNo',
    text='default text',
    font='Arial',
    pos=(0, 0.45), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
Submit = visual.TextBox2(
     win, text='Submit', font='Arial',
     pos=(0, -0.4),     letterHeight=0.03,
     size=(0.15, 0.1), borderWidth=2.0,
     color='black', colorSpace='rgb',
     opacity=1,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=None,
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False,
     editable=False,
     name='Submit',
     autoLog=True,
)

# Initialize components for Routine "End"
EndClock = core.Clock()
ThankyouMssg = visual.TextStim(win=win, name='ThankyouMssg',
    text='This is the end of the experiment.\n\n\n\nThank you for your participation!',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Welcome"-------
continueRoutine = True
# update component parameters for each repeat
WelcomeContinueKey.keys = []
WelcomeContinueKey.rt = []
_WelcomeContinueKey_allKeys = []
# keep track of which components have finished
WelcomeComponents = [InstructionTxt, WelcomeContinueKey, WelcomContinue]
for thisComponent in WelcomeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
WelcomeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Welcome"-------
while continueRoutine:
    # get current time
    t = WelcomeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=WelcomeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *InstructionTxt* updates
    if InstructionTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        InstructionTxt.frameNStart = frameN  # exact frame index
        InstructionTxt.tStart = t  # local t and not account for scr refresh
        InstructionTxt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(InstructionTxt, 'tStartRefresh')  # time at next scr refresh
        InstructionTxt.setAutoDraw(True)
    
    # *WelcomeContinueKey* updates
    waitOnFlip = False
    if WelcomeContinueKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        WelcomeContinueKey.frameNStart = frameN  # exact frame index
        WelcomeContinueKey.tStart = t  # local t and not account for scr refresh
        WelcomeContinueKey.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(WelcomeContinueKey, 'tStartRefresh')  # time at next scr refresh
        WelcomeContinueKey.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(WelcomeContinueKey.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(WelcomeContinueKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if WelcomeContinueKey.status == STARTED and not waitOnFlip:
        theseKeys = WelcomeContinueKey.getKeys(keyList=['space'], waitRelease=False)
        _WelcomeContinueKey_allKeys.extend(theseKeys)
        if len(_WelcomeContinueKey_allKeys):
            WelcomeContinueKey.keys = _WelcomeContinueKey_allKeys[-1].name  # just the last key pressed
            WelcomeContinueKey.rt = _WelcomeContinueKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *WelcomContinue* updates
    if WelcomContinue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        WelcomContinue.frameNStart = frameN  # exact frame index
        WelcomContinue.tStart = t  # local t and not account for scr refresh
        WelcomContinue.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(WelcomContinue, 'tStartRefresh')  # time at next scr refresh
        WelcomContinue.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WelcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Welcome"-------
for thisComponent in WelcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('InstructionTxt.started', InstructionTxt.tStartRefresh)
thisExp.addData('InstructionTxt.stopped', InstructionTxt.tStopRefresh)
thisExp.addData('WelcomContinue.started', WelcomContinue.tStartRefresh)
thisExp.addData('WelcomContinue.stopped', WelcomContinue.tStopRefresh)
# the Routine "Welcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Welcome2"-------
continueRoutine = True
# update component parameters for each repeat
WelcomeContinueKey2.keys = []
WelcomeContinueKey2.rt = []
_WelcomeContinueKey2_allKeys = []
# keep track of which components have finished
Welcome2Components = [InstructionTxt2, WelcomeContinue2, WelcomeContinueKey2]
for thisComponent in Welcome2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Welcome2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Welcome2"-------
while continueRoutine:
    # get current time
    t = Welcome2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Welcome2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *InstructionTxt2* updates
    if InstructionTxt2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        InstructionTxt2.frameNStart = frameN  # exact frame index
        InstructionTxt2.tStart = t  # local t and not account for scr refresh
        InstructionTxt2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(InstructionTxt2, 'tStartRefresh')  # time at next scr refresh
        InstructionTxt2.setAutoDraw(True)
    
    # *WelcomeContinue2* updates
    if WelcomeContinue2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        WelcomeContinue2.frameNStart = frameN  # exact frame index
        WelcomeContinue2.tStart = t  # local t and not account for scr refresh
        WelcomeContinue2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(WelcomeContinue2, 'tStartRefresh')  # time at next scr refresh
        WelcomeContinue2.setAutoDraw(True)
    
    # *WelcomeContinueKey2* updates
    waitOnFlip = False
    if WelcomeContinueKey2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        WelcomeContinueKey2.frameNStart = frameN  # exact frame index
        WelcomeContinueKey2.tStart = t  # local t and not account for scr refresh
        WelcomeContinueKey2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(WelcomeContinueKey2, 'tStartRefresh')  # time at next scr refresh
        WelcomeContinueKey2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(WelcomeContinueKey2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(WelcomeContinueKey2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if WelcomeContinueKey2.status == STARTED and not waitOnFlip:
        theseKeys = WelcomeContinueKey2.getKeys(keyList=['space'], waitRelease=False)
        _WelcomeContinueKey2_allKeys.extend(theseKeys)
        if len(_WelcomeContinueKey2_allKeys):
            WelcomeContinueKey2.keys = _WelcomeContinueKey2_allKeys[-1].name  # just the last key pressed
            WelcomeContinueKey2.rt = _WelcomeContinueKey2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Welcome2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Welcome2"-------
for thisComponent in Welcome2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('InstructionTxt2.started', InstructionTxt2.tStartRefresh)
thisExp.addData('InstructionTxt2.stopped', InstructionTxt2.tStopRefresh)
thisExp.addData('WelcomeContinue2.started', WelcomeContinue2.tStartRefresh)
thisExp.addData('WelcomeContinue2.stopped', WelcomeContinue2.tStopRefresh)
# check responses
if WelcomeContinueKey2.keys in ['', [], None]:  # No response was made
    WelcomeContinueKey2.keys = None
thisExp.addData('WelcomeContinueKey2.keys',WelcomeContinueKey2.keys)
if WelcomeContinueKey2.keys != None:  # we had a response
    thisExp.addData('WelcomeContinueKey2.rt', WelcomeContinueKey2.rt)
thisExp.addData('WelcomeContinueKey2.started', WelcomeContinueKey2.tStartRefresh)
thisExp.addData('WelcomeContinueKey2.stopped', WelcomeContinueKey2.tStopRefresh)
thisExp.nextEntry()
# the Routine "Welcome2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "StartAdjustment"-------
continueRoutine = True
# update component parameters for each repeat
VolumeContinueKey.keys = []
VolumeContinueKey.rt = []
_VolumeContinueKey_allKeys = []
# keep track of which components have finished
StartAdjustmentComponents = [VolumeBeginTxt, VolumeContinue, VolumeContinueKey]
for thisComponent in StartAdjustmentComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
StartAdjustmentClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "StartAdjustment"-------
while continueRoutine:
    # get current time
    t = StartAdjustmentClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=StartAdjustmentClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *VolumeBeginTxt* updates
    if VolumeBeginTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        VolumeBeginTxt.frameNStart = frameN  # exact frame index
        VolumeBeginTxt.tStart = t  # local t and not account for scr refresh
        VolumeBeginTxt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(VolumeBeginTxt, 'tStartRefresh')  # time at next scr refresh
        VolumeBeginTxt.setAutoDraw(True)
    
    # *VolumeContinue* updates
    if VolumeContinue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        VolumeContinue.frameNStart = frameN  # exact frame index
        VolumeContinue.tStart = t  # local t and not account for scr refresh
        VolumeContinue.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(VolumeContinue, 'tStartRefresh')  # time at next scr refresh
        VolumeContinue.setAutoDraw(True)
    
    # *VolumeContinueKey* updates
    waitOnFlip = False
    if VolumeContinueKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        VolumeContinueKey.frameNStart = frameN  # exact frame index
        VolumeContinueKey.tStart = t  # local t and not account for scr refresh
        VolumeContinueKey.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(VolumeContinueKey, 'tStartRefresh')  # time at next scr refresh
        VolumeContinueKey.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(VolumeContinueKey.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(VolumeContinueKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if VolumeContinueKey.status == STARTED and not waitOnFlip:
        theseKeys = VolumeContinueKey.getKeys(keyList=['space'], waitRelease=False)
        _VolumeContinueKey_allKeys.extend(theseKeys)
        if len(_VolumeContinueKey_allKeys):
            VolumeContinueKey.keys = _VolumeContinueKey_allKeys[-1].name  # just the last key pressed
            VolumeContinueKey.rt = _VolumeContinueKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in StartAdjustmentComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "StartAdjustment"-------
for thisComponent in StartAdjustmentComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('VolumeBeginTxt.started', VolumeBeginTxt.tStartRefresh)
thisExp.addData('VolumeBeginTxt.stopped', VolumeBeginTxt.tStopRefresh)
thisExp.addData('VolumeContinue.started', VolumeContinue.tStartRefresh)
thisExp.addData('VolumeContinue.stopped', VolumeContinue.tStopRefresh)
# check responses
if VolumeContinueKey.keys in ['', [], None]:  # No response was made
    VolumeContinueKey.keys = None
thisExp.addData('VolumeContinueKey.keys',VolumeContinueKey.keys)
if VolumeContinueKey.keys != None:  # we had a response
    thisExp.addData('VolumeContinueKey.rt', VolumeContinueKey.rt)
thisExp.addData('VolumeContinueKey.started', VolumeContinueKey.tStartRefresh)
thisExp.addData('VolumeContinueKey.stopped', VolumeContinueKey.tStopRefresh)
thisExp.nextEntry()
# the Routine "StartAdjustment" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "VolumeAdjustment"-------
continueRoutine = True
# update component parameters for each repeat
Music.setSound('volumeadjust.wav', hamming=True)
Music.setVolume(0.3, log=False)
EndAdjustment.keys = []
EndAdjustment.rt = []
_EndAdjustment_allKeys = []
# keep track of which components have finished
VolumeAdjustmentComponents = [text, Music, EndAdjustment, AdjustContinue]
for thisComponent in VolumeAdjustmentComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
VolumeAdjustmentClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "VolumeAdjustment"-------
while continueRoutine:
    # get current time
    t = VolumeAdjustmentClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=VolumeAdjustmentClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    # start/stop Music
    if Music.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Music.frameNStart = frameN  # exact frame index
        Music.tStart = t  # local t and not account for scr refresh
        Music.tStartRefresh = tThisFlipGlobal  # on global time
        Music.play(when=win)  # sync with win flip
    
    # *EndAdjustment* updates
    waitOnFlip = False
    if EndAdjustment.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        EndAdjustment.frameNStart = frameN  # exact frame index
        EndAdjustment.tStart = t  # local t and not account for scr refresh
        EndAdjustment.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(EndAdjustment, 'tStartRefresh')  # time at next scr refresh
        EndAdjustment.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(EndAdjustment.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(EndAdjustment.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if EndAdjustment.status == STARTED and not waitOnFlip:
        theseKeys = EndAdjustment.getKeys(keyList=['space'], waitRelease=False)
        _EndAdjustment_allKeys.extend(theseKeys)
        if len(_EndAdjustment_allKeys):
            EndAdjustment.keys = _EndAdjustment_allKeys[-1].name  # just the last key pressed
            EndAdjustment.rt = _EndAdjustment_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *AdjustContinue* updates
    if AdjustContinue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        AdjustContinue.frameNStart = frameN  # exact frame index
        AdjustContinue.tStart = t  # local t and not account for scr refresh
        AdjustContinue.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(AdjustContinue, 'tStartRefresh')  # time at next scr refresh
        AdjustContinue.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in VolumeAdjustmentComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "VolumeAdjustment"-------
for thisComponent in VolumeAdjustmentComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
Music.stop()  # ensure sound has stopped at end of routine
thisExp.addData('Music.started', Music.tStartRefresh)
thisExp.addData('Music.stopped', Music.tStopRefresh)
thisExp.addData('AdjustContinue.started', AdjustContinue.tStartRefresh)
thisExp.addData('AdjustContinue.stopped', AdjustContinue.tStopRefresh)
# the Routine "VolumeAdjustment" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Start"-------
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
StartComponents = [StartTxt]
for thisComponent in StartComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
StartClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Start"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = StartClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=StartClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *StartTxt* updates
    if StartTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        StartTxt.frameNStart = frameN  # exact frame index
        StartTxt.tStart = t  # local t and not account for scr refresh
        StartTxt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(StartTxt, 'tStartRefresh')  # time at next scr refresh
        StartTxt.setAutoDraw(True)
    if StartTxt.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > StartTxt.tStartRefresh + 2.0-frameTolerance:
            # keep track of stop time/frame for later
            StartTxt.tStop = t  # not accounting for scr refresh
            StartTxt.frameNStop = frameN  # exact frame index
            win.timeOnFlip(StartTxt, 'tStopRefresh')  # time at next scr refresh
            StartTxt.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in StartComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Start"-------
for thisComponent in StartComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('StartTxt.started', StartTxt.tStartRefresh)
thisExp.addData('StartTxt.stopped', StartTxt.tStopRefresh)

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('GuessSounds_conditions.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Count3"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    Count3Components = [no3]
    for thisComponent in Count3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Count3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Count3"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Count3Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Count3Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *no3* updates
        if no3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            no3.frameNStart = frameN  # exact frame index
            no3.tStart = t  # local t and not account for scr refresh
            no3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(no3, 'tStartRefresh')  # time at next scr refresh
            no3.setAutoDraw(True)
        if no3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > no3.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                no3.tStop = t  # not accounting for scr refresh
                no3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(no3, 'tStopRefresh')  # time at next scr refresh
                no3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Count3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Count3"-------
    for thisComponent in Count3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('no3.started', no3.tStartRefresh)
    trials.addData('no3.stopped', no3.tStopRefresh)
    
    # ------Prepare to start Routine "Count2"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    Count2Components = [no2]
    for thisComponent in Count2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Count2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Count2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Count2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Count2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *no2* updates
        if no2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            no2.frameNStart = frameN  # exact frame index
            no2.tStart = t  # local t and not account for scr refresh
            no2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(no2, 'tStartRefresh')  # time at next scr refresh
            no2.setAutoDraw(True)
        if no2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > no2.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                no2.tStop = t  # not accounting for scr refresh
                no2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(no2, 'tStopRefresh')  # time at next scr refresh
                no2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Count2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Count2"-------
    for thisComponent in Count2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('no2.started', no2.tStartRefresh)
    trials.addData('no2.stopped', no2.tStopRefresh)
    
    # ------Prepare to start Routine "Count1"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    count += 1
    number = str(count) + "/60"
    
    
    # keep track of which components have finished
    Count1Components = [no1]
    for thisComponent in Count1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Count1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Count1"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Count1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Count1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *no1* updates
        if no1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            no1.frameNStart = frameN  # exact frame index
            no1.tStart = t  # local t and not account for scr refresh
            no1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(no1, 'tStartRefresh')  # time at next scr refresh
            no1.setAutoDraw(True)
        if no1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > no1.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                no1.tStop = t  # not accounting for scr refresh
                no1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(no1, 'tStopRefresh')  # time at next scr refresh
                no1.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Count1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Count1"-------
    for thisComponent in Count1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('no1.started', no1.tStartRefresh)
    trials.addData('no1.stopped', no1.tStopRefresh)
    
    # ------Prepare to start Routine "Study"-------
    continueRoutine = True
    # update component parameters for each repeat
    ResponseBox.setText('\n\n')
    # setup some python lists for storing info about the SubmitClick
    SubmitClick.clicked_name = []
    gotValidClick = False  # until a click is received
    SoundItem.setSound(SoundFiles, hamming=True)
    SoundItem.setVolume(1.1, log=False)
    ItemNo.setText(number)
    # keep track of which components have finished
    StudyComponents = [Question, ResponseBox, SubmitClick, ClickTheButton, SoundItem, ItemNo, Submit]
    for thisComponent in StudyComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    StudyClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Study"-------
    while continueRoutine:
        # get current time
        t = StudyClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=StudyClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Question* updates
        if Question.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Question.frameNStart = frameN  # exact frame index
            Question.tStart = t  # local t and not account for scr refresh
            Question.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Question, 'tStartRefresh')  # time at next scr refresh
            Question.setAutoDraw(True)
        
        # *ResponseBox* updates
        if ResponseBox.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ResponseBox.frameNStart = frameN  # exact frame index
            ResponseBox.tStart = t  # local t and not account for scr refresh
            ResponseBox.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ResponseBox, 'tStartRefresh')  # time at next scr refresh
            ResponseBox.setAutoDraw(True)
        # *SubmitClick* updates
        if SubmitClick.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            SubmitClick.frameNStart = frameN  # exact frame index
            SubmitClick.tStart = t  # local t and not account for scr refresh
            SubmitClick.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(SubmitClick, 'tStartRefresh')  # time at next scr refresh
            SubmitClick.status = STARTED
            SubmitClick.mouseClock.reset()
            prevButtonState = [0, 0, 0]  # if now button is down we will treat as 'new' click
        if SubmitClick.status == STARTED:  # only update if started and not finished!
            buttons = SubmitClick.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    for obj in [Submit]:
                        if obj.contains(SubmitClick):
                            gotValidClick = True
                            SubmitClick.clicked_name.append(obj.name)
                    if gotValidClick:  # abort routine on response
                        continueRoutine = False
        
        # *ClickTheButton* updates
        if ClickTheButton.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ClickTheButton.frameNStart = frameN  # exact frame index
            ClickTheButton.tStart = t  # local t and not account for scr refresh
            ClickTheButton.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ClickTheButton, 'tStartRefresh')  # time at next scr refresh
            ClickTheButton.setAutoDraw(True)
        # start/stop SoundItem
        if SoundItem.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            SoundItem.frameNStart = frameN  # exact frame index
            SoundItem.tStart = t  # local t and not account for scr refresh
            SoundItem.tStartRefresh = tThisFlipGlobal  # on global time
            SoundItem.play(when=win)  # sync with win flip
        
        # *ItemNo* updates
        if ItemNo.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ItemNo.frameNStart = frameN  # exact frame index
            ItemNo.tStart = t  # local t and not account for scr refresh
            ItemNo.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ItemNo, 'tStartRefresh')  # time at next scr refresh
            ItemNo.setAutoDraw(True)
        
        # *Submit* updates
        if Submit.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Submit.frameNStart = frameN  # exact frame index
            Submit.tStart = t  # local t and not account for scr refresh
            Submit.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Submit, 'tStartRefresh')  # time at next scr refresh
            Submit.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in StudyComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Study"-------
    for thisComponent in StudyComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('Question.started', Question.tStartRefresh)
    trials.addData('Question.stopped', Question.tStopRefresh)
    trials.addData('ResponseBox.text',ResponseBox.text)
    ResponseBox.reset()
    trials.addData('ResponseBox.started', ResponseBox.tStartRefresh)
    trials.addData('ResponseBox.stopped', ResponseBox.tStopRefresh)
    # store data for trials (TrialHandler)
    trials.addData('SubmitClick.started', SubmitClick.tStart)
    trials.addData('SubmitClick.stopped', SubmitClick.tStop)
    trials.addData('ClickTheButton.started', ClickTheButton.tStartRefresh)
    trials.addData('ClickTheButton.stopped', ClickTheButton.tStopRefresh)
    SoundItem.stop()  # ensure sound has stopped at end of routine
    trials.addData('SoundItem.started', SoundItem.tStartRefresh)
    trials.addData('SoundItem.stopped', SoundItem.tStopRefresh)
    trials.addData('ItemNo.started', ItemNo.tStartRefresh)
    trials.addData('ItemNo.stopped', ItemNo.tStopRefresh)
    #if trials.thisN == 2: # i.e. trials 0, 1, 2 have been completed
     #   trials.finished = True # end the loop early
     
    
    if count == 60:
        trials.finished = true
        #trials.status = PsychoJS.Status.FINISHED
    trials.addData('Submit.started', Submit.tStartRefresh)
    trials.addData('Submit.stopped', Submit.tStopRefresh)
    # the Routine "Study" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


# ------Prepare to start Routine "End"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
EndComponents = [ThankyouMssg]
for thisComponent in EndComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
EndClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "End"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = EndClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=EndClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ThankyouMssg* updates
    if ThankyouMssg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ThankyouMssg.frameNStart = frameN  # exact frame index
        ThankyouMssg.tStart = t  # local t and not account for scr refresh
        ThankyouMssg.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ThankyouMssg, 'tStartRefresh')  # time at next scr refresh
        ThankyouMssg.setAutoDraw(True)
    if ThankyouMssg.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > ThankyouMssg.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            ThankyouMssg.tStop = t  # not accounting for scr refresh
            ThankyouMssg.frameNStop = frameN  # exact frame index
            win.timeOnFlip(ThankyouMssg, 'tStopRefresh')  # time at next scr refresh
            ThankyouMssg.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "End"-------
for thisComponent in EndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('ThankyouMssg.started', ThankyouMssg.tStartRefresh)
thisExp.addData('ThankyouMssg.stopped', ThankyouMssg.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
