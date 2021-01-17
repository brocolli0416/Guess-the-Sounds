#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.10),
    on January 17, 2021, at 13:36
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

Tcount = 1
TrialCount = 'Trial ' + str(Tcount)


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

# Initialize components for Routine "MSTSound"
MSTSoundClock = core.Clock()
TargetSound = sound.Sound('A', secs=-1, stereo=True, hamming=False,
    name='TargetSound')
TargetSound.setVolume(1)

# Initialize components for Routine "MST"
MSTClock = core.Clock()
MSTQuestion = visual.TextStim(win=win, name='MSTQuestion',
    text='1 = REPEAT\n\n2 = SIMILAR\n\n3 = NEW\n',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
MSTResp = keyboard.Keyboard()

# Initialize components for Routine "Welcome"
WelcomeClock = core.Clock()
InstructionTxt = visual.TextStim(win=win, name='InstructionTxt',
    text="Welcome to 'Sound Memory Test'!\n\n\nIn this experiment, we will test your memory for different sound items. \n\n\n",
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

# Initialize components for Routine "Welcome1"
Welcome1Clock = core.Clock()
WelcomeTxt1 = visual.TextStim(win=win, name='WelcomeTxt1',
    text="In this task, you will be presented with different enviornmental sounds one by one. For each sound you hear, please indicate whether it is a NEW sound that has never been presented before, a REPEAT of a previously presented sound, or a sound that is SIMILAR but different from a previously presented sound. \n\nPress '1' on your keyboard for REPEAT, '2' for SIMILAR, and '3' for NEW.",
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

# Initialize components for Routine "PracticeBegin"
PracticeBeginClock = core.Clock()
InstructionTxt2 = visual.TextStim(win=win, name='InstructionTxt2',
    text="Let's begin with a few practice trials. \n\n\n",
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
    text='Press the right key on your keyboard',
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

# Initialize components for Routine "Start"
StartClock = core.Clock()
StartTxt = visual.TextStim(win=win, name='StartTxt',
    text='This is the end of practice.\n\n\nWe will now begin the actual task.\nThere are 80 items in total. Listen to each sound carefully as they will play once.',
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
no1 = visual.TextStim(win=win, name='no1',
    text='1',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
no_2 = visual.TextStim(win=win, name='no_2',
    text='2',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
no_3 = visual.TextStim(win=win, name='no_3',
    text='3',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "MSTSound"
MSTSoundClock = core.Clock()
TargetSound = sound.Sound('A', secs=-1, stereo=True, hamming=False,
    name='TargetSound')
TargetSound.setVolume(1)

# Initialize components for Routine "MST"
MSTClock = core.Clock()
MSTQuestion = visual.TextStim(win=win, name='MSTQuestion',
    text='1 = REPEAT\n\n2 = SIMILAR\n\n3 = NEW\n',
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

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('GuessSounds_conditions.xlsx', selection='5:85'),
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
    
    # ------Prepare to start Routine "Study"-------
    continueRoutine = True
    # update component parameters for each repeat
    ResponseBox.setText('\n\n')
    # setup some python lists for storing info about the SubmitClick
    SubmitClick.clicked_name = []
    gotValidClick = False  # until a click is received
    SoundItem.setSound(SoundFiles3, hamming=True)
    SoundItem.setVolume(1.1, log=False)
    # keep track of which components have finished
    StudyComponents = [Question, ResponseBox, SubmitClick, ClickTheButton, SoundItem, Submit]
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
    trials_2.addData('Question.started', Question.tStartRefresh)
    trials_2.addData('Question.stopped', Question.tStopRefresh)
    trials_2.addData('ResponseBox.text',ResponseBox.text)
    ResponseBox.reset()
    trials_2.addData('ResponseBox.started', ResponseBox.tStartRefresh)
    trials_2.addData('ResponseBox.stopped', ResponseBox.tStopRefresh)
    # store data for trials_2 (TrialHandler)
    trials_2.addData('SubmitClick.started', SubmitClick.tStart)
    trials_2.addData('SubmitClick.stopped', SubmitClick.tStop)
    trials_2.addData('ClickTheButton.started', ClickTheButton.tStartRefresh)
    trials_2.addData('ClickTheButton.stopped', ClickTheButton.tStopRefresh)
    SoundItem.stop()  # ensure sound has stopped at end of routine
    trials_2.addData('SoundItem.started', SoundItem.tStartRefresh)
    trials_2.addData('SoundItem.stopped', SoundItem.tStopRefresh)
    #if trials.thisN == 2: # i.e. trials 0, 1, 2 have been completed
     #   trials.finished = True # end the loop early
     
    
    #if count == 60:
    #    trials.finished = True
    #    #trials.status = PsychoJS.Status.FINISHED
    trials_2.addData('Submit.started', Submit.tStartRefresh)
    trials_2.addData('Submit.stopped', Submit.tStopRefresh)
    # the Routine "Study" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "MSTSound"-------
    continueRoutine = True
    # update component parameters for each repeat
    TargetSound.setSound(SoundFiles3, hamming=False)
    TargetSound.setVolume(1, log=False)
    # keep track of which components have finished
    MSTSoundComponents = [TargetSound]
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
    trials_2.addData('TargetSound.started', TargetSound.tStartRefresh)
    trials_2.addData('TargetSound.stopped', TargetSound.tStopRefresh)
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
                if (MSTResp.keys == str(Correct)) or (MSTResp.keys == Correct):
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
    trials_2.addData('MSTQuestion.started', MSTQuestion.tStartRefresh)
    trials_2.addData('MSTQuestion.stopped', MSTQuestion.tStopRefresh)
    # check responses
    if MSTResp.keys in ['', [], None]:  # No response was made
        MSTResp.keys = None
        # was no response the correct answer?!
        if str(Correct).lower() == 'none':
           MSTResp.corr = 1;  # correct non-response
        else:
           MSTResp.corr = 0;  # failed to respond (incorrectly)
    # store data for trials_2 (TrialHandler)
    trials_2.addData('MSTResp.keys',MSTResp.keys)
    trials_2.addData('MSTResp.corr', MSTResp.corr)
    if MSTResp.keys != None:  # we had a response
        trials_2.addData('MSTResp.rt', MSTResp.rt)
    trials_2.addData('MSTResp.started', MSTResp.tStartRefresh)
    trials_2.addData('MSTResp.stopped', MSTResp.tStopRefresh)
    # the Routine "MST" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_2'


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
    PracticeSound.setSound(SoundFiles3, hamming=True)
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
    # the Routine "Practice1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "PracticeFeedback"-------
    continueRoutine = True
    # update component parameters for each repeat
    Tcount += 1
    TrialCount = 'Trial ' + str(Tcount)
    if Correct == 3:
        message = "This is a NEW sound. \nThis sound has never been presented before."
    elif Correct == 2:
        message = "This is a SIMILAR sound. \nThis sound is similar but not identical to a previously presented sound."
    elif Correct == 1:
        message = "This is a REPEAT sound. \nThe exact same sound has been presented previously."
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
                if (Practice_resp.keys == str(Correct)) or (Practice_resp.keys == Correct):
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
    # check responses
    if Practice_resp.keys in ['', [], None]:  # No response was made
        Practice_resp.keys = None
        # was no response the correct answer?!
        if str(Correct).lower() == 'none':
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
    trialList=data.importConditions('GuessSounds_conditions.xlsx', selection='5:85'),
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
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    count += 1
    number = str(count) + "/80"
    
    
    # keep track of which components have finished
    Count1Components = [no1, no_2, no_3]
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
        if no1.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            no1.frameNStart = frameN  # exact frame index
            no1.tStart = t  # local t and not account for scr refresh
            no1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(no1, 'tStartRefresh')  # time at next scr refresh
            no1.setAutoDraw(True)
        if no1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > no1.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                no1.tStop = t  # not accounting for scr refresh
                no1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(no1, 'tStopRefresh')  # time at next scr refresh
                no1.setAutoDraw(False)
        
        # *no_2* updates
        if no_2.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            no_2.frameNStart = frameN  # exact frame index
            no_2.tStart = t  # local t and not account for scr refresh
            no_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(no_2, 'tStartRefresh')  # time at next scr refresh
            no_2.setAutoDraw(True)
        if no_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > no_2.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                no_2.tStop = t  # not accounting for scr refresh
                no_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(no_2, 'tStopRefresh')  # time at next scr refresh
                no_2.setAutoDraw(False)
        
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
            if tThisFlipGlobal > no_3.tStartRefresh + 1.0-frameTolerance:
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
    trials.addData('no1.started', no1.tStartRefresh)
    trials.addData('no1.stopped', no1.tStopRefresh)
    trials.addData('no_2.started', no_2.tStartRefresh)
    trials.addData('no_2.stopped', no_2.tStopRefresh)
    trials.addData('no_3.started', no_3.tStartRefresh)
    trials.addData('no_3.stopped', no_3.tStopRefresh)
    
    # ------Prepare to start Routine "MSTSound"-------
    continueRoutine = True
    # update component parameters for each repeat
    TargetSound.setSound(SoundFiles3, hamming=False)
    TargetSound.setVolume(1, log=False)
    # keep track of which components have finished
    MSTSoundComponents = [TargetSound]
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
                if (MSTResp.keys == str(Correct)) or (MSTResp.keys == Correct):
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
        if str(Correct).lower() == 'none':
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
