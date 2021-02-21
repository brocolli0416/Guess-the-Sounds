#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.10),
    on February 20, 2021, at 14:58
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
    text="Welcome to 'Sound Memory Test'!\n\n\nThis experiment involves audio stimuli and requires you to wear headphones. Before we begin, please make sure that you're in a quiet listening environment, that you are wearing headphones, and that your volume is turned on.\n\n\n",
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

# Initialize components for Routine "StartAdjustment"
StartAdjustmentClock = core.Clock()
VolumeBeginTxt = visual.TextStim(win=win, name='VolumeBeginTxt',
    text='We will begin with a quick volume calibration and headphone check. \n\nFirst, we will play some music to make sure that your sound volume is at a comfortable level.\n\n\n\nPress SPACE to begin the volume calibration \n\n',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
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

# Initialize components for Routine "HeadphoneCheck"
HeadphoneCheckClock = core.Clock()
HeadphoneCheckBeing = visual.TextStim(win=win, name='HeadphoneCheckBeing',
    text='Next, we will do a short headphone check.\n\nOn each trial, you will hear three tones. One of these tones will be quieter than the others. You will identify whether the quiet tone occurred first, second, or third.\n\nThere are six trials in total.',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
HeadphoneContinue = visual.TextStim(win=win, name='HeadphoneContinue',
    text='Press SPACE to continue',
    font='Arial',
    pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
HeadphoneContinueKey = keyboard.Keyboard()

# Initialize components for Routine "HeadphonePlay"
HeadphonePlayClock = core.Clock()
CheckSound = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='CheckSound')
CheckSound.setVolume(1)
counter = 0
checkcount = str(counter) + "/6"
QuestionTxt = visual.TextStim(win=win, name='QuestionTxt',
    text='Which tone was the quietest?\n(Press the corresponding number on your keyboard)\n\n1 = First  2 = Second  3 = Third',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
CheckTrial = visual.TextStim(win=win, name='CheckTrial',
    text='default text',
    font='Arial',
    pos=(0, 0.2), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
CrossHeadphone = visual.TextStim(win=win, name='CrossHeadphone',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
CheckResp = keyboard.Keyboard()

# Initialize components for Routine "HeadphoneFeedback"
HeadphoneFeedbackClock = core.Clock()
FeedbackTxt = visual.TextStim(win=win, name='FeedbackTxt',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Welcome1"
Welcome1Clock = core.Clock()
WelcomeTxt1 = visual.TextStim(win=win, name='WelcomeTxt1',
    text='In this experiment, you will be presented with different enviornmental sounds one by one. \nOccasionally, you will hear the same sound being played for the second time. There are also sounds that are similar but not identical to a previously played sound.',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
ContinueKey1 = visual.TextStim(win=win, name='ContinueKey1',
    text='Press SPACE to continue',
    font='Arial',
    pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
ContinueResp = keyboard.Keyboard()

# Initialize components for Routine "Welcome2"
Welcome2Clock = core.Clock()
Welcome2Txt = visual.TextStim(win=win, name='Welcome2Txt',
    text="Your task is to indicate whether a sound is a NEW sound that has never been presented before, a REPEAT of a previously presented sound, or a sound that is SIMILAR but different from a previously presented sound. \n\nPress '1' on your keyboard for REPEAT, '2' for SIMILAR, and '3' for NEW.",
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
Wel2ContinueKey = keyboard.Keyboard()
Continue2 = visual.TextStim(win=win, name='Continue2',
    text='Press SPACE to continue',
    font='Arial',
    pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "PracticeBegin"
PracticeBeginClock = core.Clock()
InstructionTxt2 = visual.TextStim(win=win, name='InstructionTxt2',
    text='We will first begin with a few practice trials to familiarize you with the task. During the practice, we will give you the correct answer.\n\n\n',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
WelcomeContinue2 = visual.TextStim(win=win, name='WelcomeContinue2',
    text='Press SPACE to begin practice\n',
    font='Arial',
    pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
WelcomeContinueKey2 = keyboard.Keyboard()
Tcount = 1
TrialCount = 'Trial ' + str(Tcount)

# Initialize components for Routine "Practice1"
Practice1Clock = core.Clock()
TrialNumber = visual.TextStim(win=win, name='TrialNumber',
    text='default text',
    font='Arial',
    pos=(0, 0.3), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
PracticeSound = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='PracticeSound')
PracticeSound.setVolume(1)
PracticeCross = visual.TextStim(win=win, name='PracticeCross',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "PracticeFeedback"
PracticeFeedbackClock = core.Clock()
Practice_resp = keyboard.Keyboard()
PracticeMssg = visual.TextStim(win=win, name='PracticeMssg',
    text='default text',
    font='Arial',
    pos=(0, 0.2), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
FeedbackCross = visual.TextStim(win=win, name='FeedbackCross',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
Continue = visual.TextStim(win=win, name='Continue',
    text='Press the correct number on your keyboard',
    font='Arial',
    pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
Options = visual.TextStim(win=win, name='Options',
    text='1 = REPEAT\n2 = SIMILAR\n3 = NEW',
    font='Arial',
    pos=(0, -0.2), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);

# Initialize components for Routine "PracticeFeedbackII"
PracticeFeedbackIIClock = core.Clock()
FeedbackMssg = visual.TextStim(win=win, name='FeedbackMssg',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Start"
StartClock = core.Clock()
StartTxt = visual.TextStim(win=win, name='StartTxt',
    text='This is the end of practice.\n\n\nWe will now begin the actual task. The sounds you heard in the practice are not part of the actual task.\nThere are 128 items in total. Listen to each sound carefully as they will play only once.',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
StartTast = keyboard.Keyboard()
ContinueStart = visual.TextStim(win=win, name='ContinueStart',
    text='Press SPACE to begin the task',
    font='Arial',
    pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "Count1"
Count1Clock = core.Clock()
no_3 = visual.TextStim(win=win, name='no_3',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "MSTSound"
MSTSoundClock = core.Clock()
TargetSound = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='TargetSound')
TargetSound.setVolume(1)
Cross = visual.TextStim(win=win, name='Cross',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
ItemNumber = visual.TextStim(win=win, name='ItemNumber',
    text='default text',
    font='Arial',
    pos=(0, 0.3), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "MST"
MSTClock = core.Clock()
MSTQuestion = visual.TextStim(win=win, name='MSTQuestion',
    text='(Press the corresponding number on your keyboard)\n\n1 = REPEAT (The exact same sound has been played before)\n\n2 = SIMILAR (This sound is similar but not identical to a previously played sound)\n\n3 = NEW (This is my first time hearing this sound in this experiment)\n',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
MSTResp = keyboard.Keyboard()

# Initialize components for Routine "End"
EndClock = core.Clock()
ThankyouMssg = visual.TextStim(win=win, name='ThankyouMssg',
    text='This is the end of the experiment.\n\nThank you for your participation!\n\n\n\nYour Completion Code is',
    font='Arial',
    pos=(0, 0.2), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
CompletionCode = visual.TextBox2(
     win, text='51DF249E', font='Arial',
     pos=(0, 0),     letterHeight=0.04,
     size=(0.25, 0.07), borderWidth=2.0,
     color='Black', colorSpace='rgb',
     opacity=1,
     bold=True, italic=False,
     lineSpacing=1.0,
     padding=None,
     anchor='center',
     fillColor='White', borderColor='Black',
     flipHoriz=False, flipVert=False,
     editable=False,
     name='CompletionCode',
     autoLog=True,
)
ExitTxt = visual.TextStim(win=win, name='ExitTxt',
    text='Press SPACE to exit the study',
    font='Arial',
    pos=(0, -0.4), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
ExitKey = keyboard.Keyboard()
CodeTxt = visual.TextStim(win=win, name='CodeTxt',
    text='Please write the code down so you can enter it when you return to Prolific. You may then exit the study by pressing SPACE.',
    font='Arial',
    pos=(0, -0.22), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

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

# ------Prepare to start Routine "StartAdjustment"-------
continueRoutine = True
# update component parameters for each repeat
VolumeContinueKey.keys = []
VolumeContinueKey.rt = []
_VolumeContinueKey_allKeys = []
# keep track of which components have finished
StartAdjustmentComponents = [VolumeBeginTxt, VolumeContinueKey]
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

# ------Prepare to start Routine "HeadphoneCheck"-------
continueRoutine = True
# update component parameters for each repeat
HeadphoneContinueKey.keys = []
HeadphoneContinueKey.rt = []
_HeadphoneContinueKey_allKeys = []
# keep track of which components have finished
HeadphoneCheckComponents = [HeadphoneCheckBeing, HeadphoneContinue, HeadphoneContinueKey]
for thisComponent in HeadphoneCheckComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
HeadphoneCheckClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "HeadphoneCheck"-------
while continueRoutine:
    # get current time
    t = HeadphoneCheckClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=HeadphoneCheckClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *HeadphoneCheckBeing* updates
    if HeadphoneCheckBeing.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        HeadphoneCheckBeing.frameNStart = frameN  # exact frame index
        HeadphoneCheckBeing.tStart = t  # local t and not account for scr refresh
        HeadphoneCheckBeing.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(HeadphoneCheckBeing, 'tStartRefresh')  # time at next scr refresh
        HeadphoneCheckBeing.setAutoDraw(True)
    
    # *HeadphoneContinue* updates
    if HeadphoneContinue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        HeadphoneContinue.frameNStart = frameN  # exact frame index
        HeadphoneContinue.tStart = t  # local t and not account for scr refresh
        HeadphoneContinue.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(HeadphoneContinue, 'tStartRefresh')  # time at next scr refresh
        HeadphoneContinue.setAutoDraw(True)
    
    # *HeadphoneContinueKey* updates
    waitOnFlip = False
    if HeadphoneContinueKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        HeadphoneContinueKey.frameNStart = frameN  # exact frame index
        HeadphoneContinueKey.tStart = t  # local t and not account for scr refresh
        HeadphoneContinueKey.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(HeadphoneContinueKey, 'tStartRefresh')  # time at next scr refresh
        HeadphoneContinueKey.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(HeadphoneContinueKey.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(HeadphoneContinueKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if HeadphoneContinueKey.status == STARTED and not waitOnFlip:
        theseKeys = HeadphoneContinueKey.getKeys(keyList=['space'], waitRelease=False)
        _HeadphoneContinueKey_allKeys.extend(theseKeys)
        if len(_HeadphoneContinueKey_allKeys):
            HeadphoneContinueKey.keys = _HeadphoneContinueKey_allKeys[-1].name  # just the last key pressed
            HeadphoneContinueKey.rt = _HeadphoneContinueKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in HeadphoneCheckComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "HeadphoneCheck"-------
for thisComponent in HeadphoneCheckComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('HeadphoneCheckBeing.started', HeadphoneCheckBeing.tStartRefresh)
thisExp.addData('HeadphoneCheckBeing.stopped', HeadphoneCheckBeing.tStopRefresh)
thisExp.addData('HeadphoneContinue.started', HeadphoneContinue.tStartRefresh)
thisExp.addData('HeadphoneContinue.stopped', HeadphoneContinue.tStopRefresh)
# check responses
if HeadphoneContinueKey.keys in ['', [], None]:  # No response was made
    HeadphoneContinueKey.keys = None
thisExp.addData('HeadphoneContinueKey.keys',HeadphoneContinueKey.keys)
if HeadphoneContinueKey.keys != None:  # we had a response
    thisExp.addData('HeadphoneContinueKey.rt', HeadphoneContinueKey.rt)
thisExp.addData('HeadphoneContinueKey.started', HeadphoneContinueKey.tStartRefresh)
thisExp.addData('HeadphoneContinueKey.stopped', HeadphoneContinueKey.tStopRefresh)
thisExp.nextEntry()
# the Routine "HeadphoneCheck" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Headphone_check.xlsx'),
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2:
        exec('{} = thisTrial_2[paramName]'.format(paramName))

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "HeadphonePlay"-------
    continueRoutine = True
    # update component parameters for each repeat
    CheckSound.setSound(File, hamming=True)
    CheckSound.setVolume(1, log=False)
    counter += 1
    checkcount = str(counter) + "/6"
    CheckTrial.setText(checkcount)
    CheckResp.keys = []
    CheckResp.rt = []
    _CheckResp_allKeys = []
    # keep track of which components have finished
    HeadphonePlayComponents = [CheckSound, QuestionTxt, CheckTrial, CrossHeadphone, CheckResp]
    for thisComponent in HeadphonePlayComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    HeadphonePlayClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "HeadphonePlay"-------
    while continueRoutine:
        # get current time
        t = HeadphonePlayClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=HeadphonePlayClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop CheckSound
        if CheckSound.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            CheckSound.frameNStart = frameN  # exact frame index
            CheckSound.tStart = t  # local t and not account for scr refresh
            CheckSound.tStartRefresh = tThisFlipGlobal  # on global time
            CheckSound.play(when=win)  # sync with win flip
        
        # *QuestionTxt* updates
        if QuestionTxt.status == NOT_STARTED and tThisFlip >= CheckSound.getDuration() + 0.5-frameTolerance:
            # keep track of start time/frame for later
            QuestionTxt.frameNStart = frameN  # exact frame index
            QuestionTxt.tStart = t  # local t and not account for scr refresh
            QuestionTxt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(QuestionTxt, 'tStartRefresh')  # time at next scr refresh
            QuestionTxt.setAutoDraw(True)
        
        # *CheckTrial* updates
        if CheckTrial.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            CheckTrial.frameNStart = frameN  # exact frame index
            CheckTrial.tStart = t  # local t and not account for scr refresh
            CheckTrial.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(CheckTrial, 'tStartRefresh')  # time at next scr refresh
            CheckTrial.setAutoDraw(True)
        if CheckTrial.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > CheckTrial.tStartRefresh + CheckSound.getDuration() + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                CheckTrial.tStop = t  # not accounting for scr refresh
                CheckTrial.frameNStop = frameN  # exact frame index
                win.timeOnFlip(CheckTrial, 'tStopRefresh')  # time at next scr refresh
                CheckTrial.setAutoDraw(False)
        
        # *CrossHeadphone* updates
        if CrossHeadphone.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            CrossHeadphone.frameNStart = frameN  # exact frame index
            CrossHeadphone.tStart = t  # local t and not account for scr refresh
            CrossHeadphone.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(CrossHeadphone, 'tStartRefresh')  # time at next scr refresh
            CrossHeadphone.setAutoDraw(True)
        if CrossHeadphone.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > CrossHeadphone.tStartRefresh + CheckSound.getDuration() + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                CrossHeadphone.tStop = t  # not accounting for scr refresh
                CrossHeadphone.frameNStop = frameN  # exact frame index
                win.timeOnFlip(CrossHeadphone, 'tStopRefresh')  # time at next scr refresh
                CrossHeadphone.setAutoDraw(False)
        
        # *CheckResp* updates
        waitOnFlip = False
        if CheckResp.status == NOT_STARTED and tThisFlip >= CheckSound.getDuration() + 0.5-frameTolerance:
            # keep track of start time/frame for later
            CheckResp.frameNStart = frameN  # exact frame index
            CheckResp.tStart = t  # local t and not account for scr refresh
            CheckResp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(CheckResp, 'tStartRefresh')  # time at next scr refresh
            CheckResp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(CheckResp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(CheckResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if CheckResp.status == STARTED and not waitOnFlip:
            theseKeys = CheckResp.getKeys(keyList=['1', '2', '3'], waitRelease=False)
            _CheckResp_allKeys.extend(theseKeys)
            if len(_CheckResp_allKeys):
                CheckResp.keys = _CheckResp_allKeys[-1].name  # just the last key pressed
                CheckResp.rt = _CheckResp_allKeys[-1].rt
                # was this correct?
                if (CheckResp.keys == str(Correct)) or (CheckResp.keys == Correct):
                    CheckResp.corr = 1
                else:
                    CheckResp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in HeadphonePlayComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "HeadphonePlay"-------
    for thisComponent in HeadphonePlayComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    CheckSound.stop()  # ensure sound has stopped at end of routine
    trials_2.addData('CheckSound.started', CheckSound.tStartRefresh)
    trials_2.addData('CheckSound.stopped', CheckSound.tStopRefresh)
    if CheckResp.corr == 1:
        message = "CORRECT"
    else:
        message = "INCORRECT"
    trials_2.addData('QuestionTxt.started', QuestionTxt.tStartRefresh)
    trials_2.addData('QuestionTxt.stopped', QuestionTxt.tStopRefresh)
    trials_2.addData('CheckTrial.started', CheckTrial.tStartRefresh)
    trials_2.addData('CheckTrial.stopped', CheckTrial.tStopRefresh)
    trials_2.addData('CrossHeadphone.started', CrossHeadphone.tStartRefresh)
    trials_2.addData('CrossHeadphone.stopped', CrossHeadphone.tStopRefresh)
    # check responses
    if CheckResp.keys in ['', [], None]:  # No response was made
        CheckResp.keys = None
        # was no response the correct answer?!
        if str(Correct).lower() == 'none':
           CheckResp.corr = 1;  # correct non-response
        else:
           CheckResp.corr = 0;  # failed to respond (incorrectly)
    # store data for trials_2 (TrialHandler)
    trials_2.addData('CheckResp.keys',CheckResp.keys)
    trials_2.addData('CheckResp.corr', CheckResp.corr)
    if CheckResp.keys != None:  # we had a response
        trials_2.addData('CheckResp.rt', CheckResp.rt)
    trials_2.addData('CheckResp.started', CheckResp.tStartRefresh)
    trials_2.addData('CheckResp.stopped', CheckResp.tStopRefresh)
    # the Routine "HeadphonePlay" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "HeadphoneFeedback"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    FeedbackTxt.setText(message)
    # keep track of which components have finished
    HeadphoneFeedbackComponents = [FeedbackTxt]
    for thisComponent in HeadphoneFeedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    HeadphoneFeedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "HeadphoneFeedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = HeadphoneFeedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=HeadphoneFeedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *FeedbackTxt* updates
        if FeedbackTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            FeedbackTxt.frameNStart = frameN  # exact frame index
            FeedbackTxt.tStart = t  # local t and not account for scr refresh
            FeedbackTxt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(FeedbackTxt, 'tStartRefresh')  # time at next scr refresh
            FeedbackTxt.setAutoDraw(True)
        if FeedbackTxt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > FeedbackTxt.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                FeedbackTxt.tStop = t  # not accounting for scr refresh
                FeedbackTxt.frameNStop = frameN  # exact frame index
                win.timeOnFlip(FeedbackTxt, 'tStopRefresh')  # time at next scr refresh
                FeedbackTxt.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in HeadphoneFeedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "HeadphoneFeedback"-------
    for thisComponent in HeadphoneFeedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_2.addData('FeedbackTxt.started', FeedbackTxt.tStartRefresh)
    trials_2.addData('FeedbackTxt.stopped', FeedbackTxt.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_2'


# ------Prepare to start Routine "Welcome1"-------
continueRoutine = True
# update component parameters for each repeat
ContinueResp.keys = []
ContinueResp.rt = []
_ContinueResp_allKeys = []
# keep track of which components have finished
Welcome1Components = [WelcomeTxt1, ContinueKey1, ContinueResp]
for thisComponent in Welcome1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Welcome1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Welcome1"-------
while continueRoutine:
    # get current time
    t = Welcome1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Welcome1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *WelcomeTxt1* updates
    if WelcomeTxt1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        WelcomeTxt1.frameNStart = frameN  # exact frame index
        WelcomeTxt1.tStart = t  # local t and not account for scr refresh
        WelcomeTxt1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(WelcomeTxt1, 'tStartRefresh')  # time at next scr refresh
        WelcomeTxt1.setAutoDraw(True)
    
    # *ContinueKey1* updates
    if ContinueKey1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ContinueKey1.frameNStart = frameN  # exact frame index
        ContinueKey1.tStart = t  # local t and not account for scr refresh
        ContinueKey1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ContinueKey1, 'tStartRefresh')  # time at next scr refresh
        ContinueKey1.setAutoDraw(True)
    
    # *ContinueResp* updates
    waitOnFlip = False
    if ContinueResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ContinueResp.frameNStart = frameN  # exact frame index
        ContinueResp.tStart = t  # local t and not account for scr refresh
        ContinueResp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ContinueResp, 'tStartRefresh')  # time at next scr refresh
        ContinueResp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(ContinueResp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(ContinueResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if ContinueResp.status == STARTED and not waitOnFlip:
        theseKeys = ContinueResp.getKeys(keyList=['space'], waitRelease=False)
        _ContinueResp_allKeys.extend(theseKeys)
        if len(_ContinueResp_allKeys):
            ContinueResp.keys = _ContinueResp_allKeys[-1].name  # just the last key pressed
            ContinueResp.rt = _ContinueResp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Welcome1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Welcome1"-------
for thisComponent in Welcome1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('WelcomeTxt1.started', WelcomeTxt1.tStartRefresh)
thisExp.addData('WelcomeTxt1.stopped', WelcomeTxt1.tStopRefresh)
thisExp.addData('ContinueKey1.started', ContinueKey1.tStartRefresh)
thisExp.addData('ContinueKey1.stopped', ContinueKey1.tStopRefresh)
# check responses
if ContinueResp.keys in ['', [], None]:  # No response was made
    ContinueResp.keys = None
thisExp.addData('ContinueResp.keys',ContinueResp.keys)
if ContinueResp.keys != None:  # we had a response
    thisExp.addData('ContinueResp.rt', ContinueResp.rt)
thisExp.addData('ContinueResp.started', ContinueResp.tStartRefresh)
thisExp.addData('ContinueResp.stopped', ContinueResp.tStopRefresh)
thisExp.nextEntry()
# the Routine "Welcome1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Welcome2"-------
continueRoutine = True
# update component parameters for each repeat
Wel2ContinueKey.keys = []
Wel2ContinueKey.rt = []
_Wel2ContinueKey_allKeys = []
# keep track of which components have finished
Welcome2Components = [Welcome2Txt, Wel2ContinueKey, Continue2]
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
    
    # *Welcome2Txt* updates
    if Welcome2Txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Welcome2Txt.frameNStart = frameN  # exact frame index
        Welcome2Txt.tStart = t  # local t and not account for scr refresh
        Welcome2Txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Welcome2Txt, 'tStartRefresh')  # time at next scr refresh
        Welcome2Txt.setAutoDraw(True)
    
    # *Wel2ContinueKey* updates
    waitOnFlip = False
    if Wel2ContinueKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Wel2ContinueKey.frameNStart = frameN  # exact frame index
        Wel2ContinueKey.tStart = t  # local t and not account for scr refresh
        Wel2ContinueKey.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Wel2ContinueKey, 'tStartRefresh')  # time at next scr refresh
        Wel2ContinueKey.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Wel2ContinueKey.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Wel2ContinueKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Wel2ContinueKey.status == STARTED and not waitOnFlip:
        theseKeys = Wel2ContinueKey.getKeys(keyList=['space'], waitRelease=False)
        _Wel2ContinueKey_allKeys.extend(theseKeys)
        if len(_Wel2ContinueKey_allKeys):
            Wel2ContinueKey.keys = _Wel2ContinueKey_allKeys[-1].name  # just the last key pressed
            Wel2ContinueKey.rt = _Wel2ContinueKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *Continue2* updates
    if Continue2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Continue2.frameNStart = frameN  # exact frame index
        Continue2.tStart = t  # local t and not account for scr refresh
        Continue2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Continue2, 'tStartRefresh')  # time at next scr refresh
        Continue2.setAutoDraw(True)
    
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
thisExp.addData('Welcome2Txt.started', Welcome2Txt.tStartRefresh)
thisExp.addData('Welcome2Txt.stopped', Welcome2Txt.tStopRefresh)
# check responses
if Wel2ContinueKey.keys in ['', [], None]:  # No response was made
    Wel2ContinueKey.keys = None
thisExp.addData('Wel2ContinueKey.keys',Wel2ContinueKey.keys)
if Wel2ContinueKey.keys != None:  # we had a response
    thisExp.addData('Wel2ContinueKey.rt', Wel2ContinueKey.rt)
thisExp.addData('Wel2ContinueKey.started', Wel2ContinueKey.tStartRefresh)
thisExp.addData('Wel2ContinueKey.stopped', Wel2ContinueKey.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('Continue2.started', Continue2.tStartRefresh)
thisExp.addData('Continue2.stopped', Continue2.tStopRefresh)
# the Routine "Welcome2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "PracticeBegin"-------
continueRoutine = True
# update component parameters for each repeat
WelcomeContinueKey2.keys = []
WelcomeContinueKey2.rt = []
_WelcomeContinueKey2_allKeys = []
# keep track of which components have finished
PracticeBeginComponents = [InstructionTxt2, WelcomeContinue2, WelcomeContinueKey2]
for thisComponent in PracticeBeginComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
PracticeBeginClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "PracticeBegin"-------
while continueRoutine:
    # get current time
    t = PracticeBeginClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=PracticeBeginClock)
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
    for thisComponent in PracticeBeginComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "PracticeBegin"-------
for thisComponent in PracticeBeginComponents:
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
# the Routine "PracticeBegin" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
PracticeTrials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('GuessSounds_conditions.xlsx', selection='0:5'),
    seed=None, name='PracticeTrials')
thisExp.addLoop(PracticeTrials)  # add the loop to the experiment
thisPracticeTrial = PracticeTrials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPracticeTrial.rgb)
if thisPracticeTrial != None:
    for paramName in thisPracticeTrial:
        exec('{} = thisPracticeTrial[paramName]'.format(paramName))

for thisPracticeTrial in PracticeTrials:
    currentLoop = PracticeTrials
    # abbreviate parameter names if possible (e.g. rgb = thisPracticeTrial.rgb)
    if thisPracticeTrial != None:
        for paramName in thisPracticeTrial:
            exec('{} = thisPracticeTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Practice1"-------
    continueRoutine = True
    # update component parameters for each repeat
    TrialNumber.setText(TrialCount)
    PracticeSound.setSound(SoundFile, hamming=True)
    PracticeSound.setVolume(1, log=False)
    # keep track of which components have finished
    Practice1Components = [TrialNumber, PracticeSound, PracticeCross]
    for thisComponent in Practice1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Practice1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Practice1"-------
    while continueRoutine:
        # get current time
        t = Practice1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Practice1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *TrialNumber* updates
        if TrialNumber.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            TrialNumber.frameNStart = frameN  # exact frame index
            TrialNumber.tStart = t  # local t and not account for scr refresh
            TrialNumber.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TrialNumber, 'tStartRefresh')  # time at next scr refresh
            TrialNumber.setAutoDraw(True)
        if TrialNumber.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > TrialNumber.tStartRefresh + PracticeSound.getDuration()-frameTolerance:
                # keep track of stop time/frame for later
                TrialNumber.tStop = t  # not accounting for scr refresh
                TrialNumber.frameNStop = frameN  # exact frame index
                win.timeOnFlip(TrialNumber, 'tStopRefresh')  # time at next scr refresh
                TrialNumber.setAutoDraw(False)
        # start/stop PracticeSound
        if PracticeSound.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            PracticeSound.frameNStart = frameN  # exact frame index
            PracticeSound.tStart = t  # local t and not account for scr refresh
            PracticeSound.tStartRefresh = tThisFlipGlobal  # on global time
            PracticeSound.play(when=win)  # sync with win flip
        
        # *PracticeCross* updates
        if PracticeCross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            PracticeCross.frameNStart = frameN  # exact frame index
            PracticeCross.tStart = t  # local t and not account for scr refresh
            PracticeCross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(PracticeCross, 'tStartRefresh')  # time at next scr refresh
            PracticeCross.setAutoDraw(True)
        if PracticeCross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > PracticeCross.tStartRefresh + PracticeSound.getDuration()-frameTolerance:
                # keep track of stop time/frame for later
                PracticeCross.tStop = t  # not accounting for scr refresh
                PracticeCross.frameNStop = frameN  # exact frame index
                win.timeOnFlip(PracticeCross, 'tStopRefresh')  # time at next scr refresh
                PracticeCross.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Practice1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Practice1"-------
    for thisComponent in Practice1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    PracticeTrials.addData('TrialNumber.started', TrialNumber.tStartRefresh)
    PracticeTrials.addData('TrialNumber.stopped', TrialNumber.tStopRefresh)
    PracticeSound.stop()  # ensure sound has stopped at end of routine
    PracticeTrials.addData('PracticeSound.started', PracticeSound.tStartRefresh)
    PracticeTrials.addData('PracticeSound.stopped', PracticeSound.tStopRefresh)
    PracticeTrials.addData('PracticeCross.started', PracticeCross.tStartRefresh)
    PracticeTrials.addData('PracticeCross.stopped', PracticeCross.tStopRefresh)
    Tcount += 1
    TrialCount = 'Trial ' + str(Tcount)
    
    #if Type == 'NEW':
    #    message = "This is a NEW word. \nThis is your first time hearing this sound."
    #elif Type == 'SIMILAR':
    #    message = "This is a NEW word. \nNotice that this one sounds similar to the previous sound but is not exactly the same."
    #elif Type == 'OLD':
    #    message = "This is an OLD word. \nThis sound is exactly the same as the first sound."
    # the Routine "Practice1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "PracticeFeedback"-------
    continueRoutine = True
    # update component parameters for each repeat
    #Tcount += 1
    #TrialCount = 'Trial ' + str(Tcount)
    if Correct2 == 3:
        message = "This is a NEW sound. \nThis sound has never been played before."
    elif Correct2 == 2:
        message = "This is a SIMILAR sound. \nThis sound is similar but not identical to a previously played sound."
    elif Correct2 == 1:
        message = "This is a REPEAT sound. \nThe exact same sound has been played previously."
    
    Practice_resp.keys = []
    Practice_resp.rt = []
    _Practice_resp_allKeys = []
    PracticeMssg.setText(message)
    # keep track of which components have finished
    PracticeFeedbackComponents = [Practice_resp, PracticeMssg, FeedbackCross, Continue, Options]
    for thisComponent in PracticeFeedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    PracticeFeedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "PracticeFeedback"-------
    while continueRoutine:
        # get current time
        t = PracticeFeedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=PracticeFeedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Practice_resp* updates
        waitOnFlip = False
        if Practice_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Practice_resp.frameNStart = frameN  # exact frame index
            Practice_resp.tStart = t  # local t and not account for scr refresh
            Practice_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Practice_resp, 'tStartRefresh')  # time at next scr refresh
            Practice_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Practice_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Practice_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Practice_resp.status == STARTED and not waitOnFlip:
            theseKeys = Practice_resp.getKeys(keyList=['1', '2', '3'], waitRelease=False)
            _Practice_resp_allKeys.extend(theseKeys)
            if len(_Practice_resp_allKeys):
                Practice_resp.keys = _Practice_resp_allKeys[-1].name  # just the last key pressed
                Practice_resp.rt = _Practice_resp_allKeys[-1].rt
                # was this correct?
                if (Practice_resp.keys == str(Correct2)) or (Practice_resp.keys == Correct2):
                    Practice_resp.corr = 1
                else:
                    Practice_resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *PracticeMssg* updates
        if PracticeMssg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            PracticeMssg.frameNStart = frameN  # exact frame index
            PracticeMssg.tStart = t  # local t and not account for scr refresh
            PracticeMssg.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(PracticeMssg, 'tStartRefresh')  # time at next scr refresh
            PracticeMssg.setAutoDraw(True)
        
        # *FeedbackCross* updates
        if FeedbackCross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            FeedbackCross.frameNStart = frameN  # exact frame index
            FeedbackCross.tStart = t  # local t and not account for scr refresh
            FeedbackCross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(FeedbackCross, 'tStartRefresh')  # time at next scr refresh
            FeedbackCross.setAutoDraw(True)
        
        # *Continue* updates
        if Continue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Continue.frameNStart = frameN  # exact frame index
            Continue.tStart = t  # local t and not account for scr refresh
            Continue.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Continue, 'tStartRefresh')  # time at next scr refresh
            Continue.setAutoDraw(True)
        
        # *Options* updates
        if Options.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Options.frameNStart = frameN  # exact frame index
            Options.tStart = t  # local t and not account for scr refresh
            Options.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Options, 'tStartRefresh')  # time at next scr refresh
            Options.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in PracticeFeedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "PracticeFeedback"-------
    for thisComponent in PracticeFeedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    if Practice_resp.corr == 1:
        feedback = 'CORRECT'
    else:
        feedback = 'INCORRECT'
    # check responses
    if Practice_resp.keys in ['', [], None]:  # No response was made
        Practice_resp.keys = None
        # was no response the correct answer?!
        if str(Correct2).lower() == 'none':
           Practice_resp.corr = 1;  # correct non-response
        else:
           Practice_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for PracticeTrials (TrialHandler)
    PracticeTrials.addData('Practice_resp.keys',Practice_resp.keys)
    PracticeTrials.addData('Practice_resp.corr', Practice_resp.corr)
    if Practice_resp.keys != None:  # we had a response
        PracticeTrials.addData('Practice_resp.rt', Practice_resp.rt)
    PracticeTrials.addData('Practice_resp.started', Practice_resp.tStartRefresh)
    PracticeTrials.addData('Practice_resp.stopped', Practice_resp.tStopRefresh)
    PracticeTrials.addData('PracticeMssg.started', PracticeMssg.tStartRefresh)
    PracticeTrials.addData('PracticeMssg.stopped', PracticeMssg.tStopRefresh)
    PracticeTrials.addData('FeedbackCross.started', FeedbackCross.tStartRefresh)
    PracticeTrials.addData('FeedbackCross.stopped', FeedbackCross.tStopRefresh)
    PracticeTrials.addData('Continue.started', Continue.tStartRefresh)
    PracticeTrials.addData('Continue.stopped', Continue.tStopRefresh)
    PracticeTrials.addData('Options.started', Options.tStartRefresh)
    PracticeTrials.addData('Options.stopped', Options.tStopRefresh)
    # the Routine "PracticeFeedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "PracticeFeedbackII"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    FeedbackMssg.setText(feedback)
    # keep track of which components have finished
    PracticeFeedbackIIComponents = [FeedbackMssg]
    for thisComponent in PracticeFeedbackIIComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    PracticeFeedbackIIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "PracticeFeedbackII"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = PracticeFeedbackIIClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=PracticeFeedbackIIClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *FeedbackMssg* updates
        if FeedbackMssg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            FeedbackMssg.frameNStart = frameN  # exact frame index
            FeedbackMssg.tStart = t  # local t and not account for scr refresh
            FeedbackMssg.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(FeedbackMssg, 'tStartRefresh')  # time at next scr refresh
            FeedbackMssg.setAutoDraw(True)
        if FeedbackMssg.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > FeedbackMssg.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                FeedbackMssg.tStop = t  # not accounting for scr refresh
                FeedbackMssg.frameNStop = frameN  # exact frame index
                win.timeOnFlip(FeedbackMssg, 'tStopRefresh')  # time at next scr refresh
                FeedbackMssg.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in PracticeFeedbackIIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "PracticeFeedbackII"-------
    for thisComponent in PracticeFeedbackIIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    PracticeTrials.addData('FeedbackMssg.started', FeedbackMssg.tStartRefresh)
    PracticeTrials.addData('FeedbackMssg.stopped', FeedbackMssg.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'PracticeTrials'


# ------Prepare to start Routine "Start"-------
continueRoutine = True
# update component parameters for each repeat
StartTast.keys = []
StartTast.rt = []
_StartTast_allKeys = []
# keep track of which components have finished
StartComponents = [StartTxt, StartTast, ContinueStart]
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
while continueRoutine:
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
    
    # *StartTast* updates
    waitOnFlip = False
    if StartTast.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        StartTast.frameNStart = frameN  # exact frame index
        StartTast.tStart = t  # local t and not account for scr refresh
        StartTast.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(StartTast, 'tStartRefresh')  # time at next scr refresh
        StartTast.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(StartTast.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(StartTast.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if StartTast.status == STARTED and not waitOnFlip:
        theseKeys = StartTast.getKeys(keyList=['space'], waitRelease=False)
        _StartTast_allKeys.extend(theseKeys)
        if len(_StartTast_allKeys):
            StartTast.keys = _StartTast_allKeys[-1].name  # just the last key pressed
            StartTast.rt = _StartTast_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *ContinueStart* updates
    if ContinueStart.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ContinueStart.frameNStart = frameN  # exact frame index
        ContinueStart.tStart = t  # local t and not account for scr refresh
        ContinueStart.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ContinueStart, 'tStartRefresh')  # time at next scr refresh
        ContinueStart.setAutoDraw(True)
    
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
# check responses
if StartTast.keys in ['', [], None]:  # No response was made
    StartTast.keys = None
thisExp.addData('StartTast.keys',StartTast.keys)
if StartTast.keys != None:  # we had a response
    thisExp.addData('StartTast.rt', StartTast.rt)
thisExp.addData('StartTast.started', StartTast.tStartRefresh)
thisExp.addData('StartTast.stopped', StartTast.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('ContinueStart.started', ContinueStart.tStartRefresh)
thisExp.addData('ContinueStart.stopped', ContinueStart.tStopRefresh)
# the Routine "Start" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('GuessSounds_conditions.xlsx', selection='5:149'),
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
    
    # ------Prepare to start Routine "Count1"-------
    continueRoutine = True
    routineTimer.add(1.500000)
    # update component parameters for each repeat
    count += 1
    number = str(count) + "/128"
    
    
    # keep track of which components have finished
    Count1Components = [no_3]
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
        
        # *no_3* updates
        if no_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            no_3.frameNStart = frameN  # exact frame index
            no_3.tStart = t  # local t and not account for scr refresh
            no_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(no_3, 'tStartRefresh')  # time at next scr refresh
            no_3.setAutoDraw(True)
        if no_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > no_3.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                no_3.tStop = t  # not accounting for scr refresh
                no_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(no_3, 'tStopRefresh')  # time at next scr refresh
                no_3.setAutoDraw(False)
        
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
    trials.addData('no_3.started', no_3.tStartRefresh)
    trials.addData('no_3.stopped', no_3.tStopRefresh)
    
    # ------Prepare to start Routine "MSTSound"-------
    continueRoutine = True
    # update component parameters for each repeat
    TargetSound.setSound(SoundFile, hamming=True)
    TargetSound.setVolume(1, log=False)
    ItemNumber.setText(number)
    # keep track of which components have finished
    MSTSoundComponents = [TargetSound, Cross, ItemNumber]
    for thisComponent in MSTSoundComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    MSTSoundClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "MSTSound"-------
    while continueRoutine:
        # get current time
        t = MSTSoundClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=MSTSoundClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop TargetSound
        if TargetSound.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            TargetSound.frameNStart = frameN  # exact frame index
            TargetSound.tStart = t  # local t and not account for scr refresh
            TargetSound.tStartRefresh = tThisFlipGlobal  # on global time
            TargetSound.play(when=win)  # sync with win flip
        
        # *Cross* updates
        if Cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Cross.frameNStart = frameN  # exact frame index
            Cross.tStart = t  # local t and not account for scr refresh
            Cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Cross, 'tStartRefresh')  # time at next scr refresh
            Cross.setAutoDraw(True)
        if Cross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Cross.tStartRefresh + TargetSound.getDuration() + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                Cross.tStop = t  # not accounting for scr refresh
                Cross.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Cross, 'tStopRefresh')  # time at next scr refresh
                Cross.setAutoDraw(False)
        
        # *ItemNumber* updates
        if ItemNumber.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ItemNumber.frameNStart = frameN  # exact frame index
            ItemNumber.tStart = t  # local t and not account for scr refresh
            ItemNumber.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ItemNumber, 'tStartRefresh')  # time at next scr refresh
            ItemNumber.setAutoDraw(True)
        if ItemNumber.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ItemNumber.tStartRefresh + TargetSound.getDuration() + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                ItemNumber.tStop = t  # not accounting for scr refresh
                ItemNumber.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ItemNumber, 'tStopRefresh')  # time at next scr refresh
                ItemNumber.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in MSTSoundComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "MSTSound"-------
    for thisComponent in MSTSoundComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    TargetSound.stop()  # ensure sound has stopped at end of routine
    trials.addData('TargetSound.started', TargetSound.tStartRefresh)
    trials.addData('TargetSound.stopped', TargetSound.tStopRefresh)
    trials.addData('Cross.started', Cross.tStartRefresh)
    trials.addData('Cross.stopped', Cross.tStopRefresh)
    trials.addData('ItemNumber.started', ItemNumber.tStartRefresh)
    trials.addData('ItemNumber.stopped', ItemNumber.tStopRefresh)
    # the Routine "MSTSound" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "MST"-------
    continueRoutine = True
    # update component parameters for each repeat
    MSTResp.keys = []
    MSTResp.rt = []
    _MSTResp_allKeys = []
    # keep track of which components have finished
    MSTComponents = [MSTQuestion, MSTResp]
    for thisComponent in MSTComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    MSTClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "MST"-------
    while continueRoutine:
        # get current time
        t = MSTClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=MSTClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *MSTQuestion* updates
        if MSTQuestion.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            MSTQuestion.frameNStart = frameN  # exact frame index
            MSTQuestion.tStart = t  # local t and not account for scr refresh
            MSTQuestion.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(MSTQuestion, 'tStartRefresh')  # time at next scr refresh
            MSTQuestion.setAutoDraw(True)
        
        # *MSTResp* updates
        waitOnFlip = False
        if MSTResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            MSTResp.frameNStart = frameN  # exact frame index
            MSTResp.tStart = t  # local t and not account for scr refresh
            MSTResp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(MSTResp, 'tStartRefresh')  # time at next scr refresh
            MSTResp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(MSTResp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(MSTResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if MSTResp.status == STARTED and not waitOnFlip:
            theseKeys = MSTResp.getKeys(keyList=['1', '2', '3'], waitRelease=False)
            _MSTResp_allKeys.extend(theseKeys)
            if len(_MSTResp_allKeys):
                MSTResp.keys = _MSTResp_allKeys[-1].name  # just the last key pressed
                MSTResp.rt = _MSTResp_allKeys[-1].rt
                # was this correct?
                if (MSTResp.keys == str(Correct2)) or (MSTResp.keys == Correct2):
                    MSTResp.corr = 1
                else:
                    MSTResp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in MSTComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "MST"-------
    for thisComponent in MSTComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('MSTQuestion.started', MSTQuestion.tStartRefresh)
    trials.addData('MSTQuestion.stopped', MSTQuestion.tStopRefresh)
    # check responses
    if MSTResp.keys in ['', [], None]:  # No response was made
        MSTResp.keys = None
        # was no response the correct answer?!
        if str(Correct2).lower() == 'none':
           MSTResp.corr = 1;  # correct non-response
        else:
           MSTResp.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('MSTResp.keys',MSTResp.keys)
    trials.addData('MSTResp.corr', MSTResp.corr)
    if MSTResp.keys != None:  # we had a response
        trials.addData('MSTResp.rt', MSTResp.rt)
    trials.addData('MSTResp.started', MSTResp.tStartRefresh)
    trials.addData('MSTResp.stopped', MSTResp.tStopRefresh)
    # the Routine "MST" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


# ------Prepare to start Routine "End"-------
continueRoutine = True
# update component parameters for each repeat
ExitKey.keys = []
ExitKey.rt = []
_ExitKey_allKeys = []
# keep track of which components have finished
EndComponents = [ThankyouMssg, CompletionCode, ExitTxt, ExitKey, CodeTxt]
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
while continueRoutine:
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
    
    # *CompletionCode* updates
    if CompletionCode.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        CompletionCode.frameNStart = frameN  # exact frame index
        CompletionCode.tStart = t  # local t and not account for scr refresh
        CompletionCode.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(CompletionCode, 'tStartRefresh')  # time at next scr refresh
        CompletionCode.setAutoDraw(True)
    
    # *ExitTxt* updates
    if ExitTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ExitTxt.frameNStart = frameN  # exact frame index
        ExitTxt.tStart = t  # local t and not account for scr refresh
        ExitTxt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ExitTxt, 'tStartRefresh')  # time at next scr refresh
        ExitTxt.setAutoDraw(True)
    
    # *ExitKey* updates
    waitOnFlip = False
    if ExitKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ExitKey.frameNStart = frameN  # exact frame index
        ExitKey.tStart = t  # local t and not account for scr refresh
        ExitKey.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ExitKey, 'tStartRefresh')  # time at next scr refresh
        ExitKey.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(ExitKey.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(ExitKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if ExitKey.status == STARTED and not waitOnFlip:
        theseKeys = ExitKey.getKeys(keyList=['space'], waitRelease=False)
        _ExitKey_allKeys.extend(theseKeys)
        if len(_ExitKey_allKeys):
            ExitKey.keys = _ExitKey_allKeys[-1].name  # just the last key pressed
            ExitKey.rt = _ExitKey_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *CodeTxt* updates
    if CodeTxt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        CodeTxt.frameNStart = frameN  # exact frame index
        CodeTxt.tStart = t  # local t and not account for scr refresh
        CodeTxt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(CodeTxt, 'tStartRefresh')  # time at next scr refresh
        CodeTxt.setAutoDraw(True)
    
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
thisExp.addData('CompletionCode.started', CompletionCode.tStartRefresh)
thisExp.addData('CompletionCode.stopped', CompletionCode.tStopRefresh)
thisExp.addData('ExitTxt.started', ExitTxt.tStartRefresh)
thisExp.addData('ExitTxt.stopped', ExitTxt.tStopRefresh)
# check responses
if ExitKey.keys in ['', [], None]:  # No response was made
    ExitKey.keys = None
thisExp.addData('ExitKey.keys',ExitKey.keys)
if ExitKey.keys != None:  # we had a response
    thisExp.addData('ExitKey.rt', ExitKey.rt)
thisExp.addData('ExitKey.started', ExitKey.tStartRefresh)
thisExp.addData('ExitKey.stopped', ExitKey.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('CodeTxt.started', CodeTxt.tStartRefresh)
thisExp.addData('CodeTxt.stopped', CodeTxt.tStopRefresh)
# the Routine "End" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

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
