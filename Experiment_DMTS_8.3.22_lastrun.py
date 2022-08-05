#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.2),
    on Wed Aug  3 14:51:23 2022
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
prefs.hardware['audioLib'] = 'ptb'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.2'
expName = 'Experiment_DMTS'  # from the Builder filename that created this script
expInfo = {'participant': ''}
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
    originPath='/Users/ajennings/Documents/698/Experiment_DMTS_8.3.22_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.DEBUG)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1440, 900], fullscr=True, screen=0, 
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

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "instructions1"
instructions1Clock = core.Clock()
readyResp = keyboard.Keyboard()
instrText = visual.TextStim(win=win, name='instrText',
    text='Greetings!\n\nIn this experiment you will learn to match black and white images. First an image will briefly appear in the upper half of the screen. Next there will be three images below. \n\nUse the left, up, and right arrows to select which image you think matches. \n\nPay attention to the feedback to learn which images go together. \n\nPress any key to begin.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
sample = visual.ImageStim(
    win=win,
    name='sample', units='norm', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0.35), size=(0.35, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
cmp1 = visual.ImageStim(
    win=win,
    name='cmp1', units='norm', 
    image='sin', mask=None,
    ori=0.0, pos=(-0.5, -0.4), size=(0.35, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
cmp2 = visual.ImageStim(
    win=win,
    name='cmp2', units='norm', 
    image='sin', mask=None,
    ori=0.0, pos=(0, -0.4), size=(0.35, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
cmp3 = visual.ImageStim(
    win=win,
    name='cmp3', units='norm', 
    image='sin', mask=None,
    ori=0.0, pos=(0.5, -0.4), size=(0.35, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
resp = keyboard.Keyboard()

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
msg = ' '
correct_incorrect = []
feedbackText = visual.TextStim(win=win, name='feedbackText',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "instructions2"
instructions2Clock = core.Clock()
readyResp2 = keyboard.Keyboard()
text = visual.TextStim(win=win, name='text',
    text='Nice work, you have successfully learned which images go together! Now you will complete the same task except feedback will not be provided. \n\nPress any key to begin. Good luck! ',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
sample = visual.ImageStim(
    win=win,
    name='sample', units='norm', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0.35), size=(0.35, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
cmp1 = visual.ImageStim(
    win=win,
    name='cmp1', units='norm', 
    image='sin', mask=None,
    ori=0.0, pos=(-0.5, -0.4), size=(0.35, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
cmp2 = visual.ImageStim(
    win=win,
    name='cmp2', units='norm', 
    image='sin', mask=None,
    ori=0.0, pos=(0, -0.4), size=(0.35, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
cmp3 = visual.ImageStim(
    win=win,
    name='cmp3', units='norm', 
    image='sin', mask=None,
    ori=0.0, pos=(0.5, -0.4), size=(0.35, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
resp = keyboard.Keyboard()

# Initialize components for Routine "thankyou"
thankyouClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='Thank you for your participation!',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instructions1"-------
continueRoutine = True
# update component parameters for each repeat
readyResp.keys = []
readyResp.rt = []
_readyResp_allKeys = []
# keep track of which components have finished
instructions1Components = [readyResp, instrText]
for thisComponent in instructions1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructions1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instructions1"-------
while continueRoutine:
    # get current time
    t = instructions1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructions1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *readyResp* updates
    waitOnFlip = False
    if readyResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        readyResp.frameNStart = frameN  # exact frame index
        readyResp.tStart = t  # local t and not account for scr refresh
        readyResp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(readyResp, 'tStartRefresh')  # time at next scr refresh
        readyResp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(readyResp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(readyResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if readyResp.status == STARTED and not waitOnFlip:
        theseKeys = readyResp.getKeys(keyList=None, waitRelease=False)
        _readyResp_allKeys.extend(theseKeys)
        if len(_readyResp_allKeys):
            readyResp.keys = _readyResp_allKeys[-1].name  # just the last key pressed
            readyResp.rt = _readyResp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *instrText* updates
    if instrText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instrText.frameNStart = frameN  # exact frame index
        instrText.tStart = t  # local t and not account for scr refresh
        instrText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instrText, 'tStartRefresh')  # time at next scr refresh
        instrText.setAutoDraw(True)
    if instrText.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > instrText.tStartRefresh + 10.0-frameTolerance:
            # keep track of stop time/frame for later
            instrText.tStop = t  # not accounting for scr refresh
            instrText.frameNStop = frameN  # exact frame index
            win.timeOnFlip(instrText, 'tStopRefresh')  # time at next scr refresh
            instrText.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions1"-------
for thisComponent in instructions1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if readyResp.keys in ['', [], None]:  # No response was made
    readyResp.keys = None
thisExp.addData('readyResp.keys',readyResp.keys)
if readyResp.keys != None:  # we had a response
    thisExp.addData('readyResp.rt', readyResp.rt)
thisExp.addData('readyResp.started', readyResp.tStartRefresh)
thisExp.addData('readyResp.stopped', readyResp.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('instrText.started', instrText.tStartRefresh)
thisExp.addData('instrText.stopped', instrText.tStopRefresh)
# the Routine "instructions1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
training = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('exp3.xlsx'),
    seed=None, name='training')
thisExp.addLoop(training)  # add the loop to the experiment
thisTraining = training.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTraining.rgb)
if thisTraining != None:
    for paramName in thisTraining:
        exec('{} = thisTraining[paramName]'.format(paramName))

for thisTraining in training:
    currentLoop = training
    # abbreviate parameter names if possible (e.g. rgb = thisTraining.rgb)
    if thisTraining != None:
        for paramName in thisTraining:
            exec('{} = thisTraining[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    # update component parameters for each repeat
    sample.setImage(_sample)
    cmp1.setImage(_cmp1)
    cmp2.setImage(_cmp2)
    cmp3.setImage(_cmp3)
    resp.keys = []
    resp.rt = []
    _resp_allKeys = []
    # keep track of which components have finished
    trialComponents = [sample, cmp1, cmp2, cmp3, resp]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *sample* updates
        if sample.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sample.frameNStart = frameN  # exact frame index
            sample.tStart = t  # local t and not account for scr refresh
            sample.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sample, 'tStartRefresh')  # time at next scr refresh
            sample.setAutoDraw(True)
        if sample.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sample.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                sample.tStop = t  # not accounting for scr refresh
                sample.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sample, 'tStopRefresh')  # time at next scr refresh
                sample.setAutoDraw(False)
        
        # *cmp1* updates
        if cmp1.status == NOT_STARTED and tThisFlip >= 3.5-frameTolerance:
            # keep track of start time/frame for later
            cmp1.frameNStart = frameN  # exact frame index
            cmp1.tStart = t  # local t and not account for scr refresh
            cmp1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cmp1, 'tStartRefresh')  # time at next scr refresh
            cmp1.setAutoDraw(True)
        
        # *cmp2* updates
        if cmp2.status == NOT_STARTED and tThisFlip >= 3.5-frameTolerance:
            # keep track of start time/frame for later
            cmp2.frameNStart = frameN  # exact frame index
            cmp2.tStart = t  # local t and not account for scr refresh
            cmp2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cmp2, 'tStartRefresh')  # time at next scr refresh
            cmp2.setAutoDraw(True)
        
        # *cmp3* updates
        if cmp3.status == NOT_STARTED and tThisFlip >= 3.5-frameTolerance:
            # keep track of start time/frame for later
            cmp3.frameNStart = frameN  # exact frame index
            cmp3.tStart = t  # local t and not account for scr refresh
            cmp3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cmp3, 'tStartRefresh')  # time at next scr refresh
            cmp3.setAutoDraw(True)
        
        # *resp* updates
        waitOnFlip = False
        if resp.status == NOT_STARTED and tThisFlip >= 3.5-frameTolerance:
            # keep track of start time/frame for later
            resp.frameNStart = frameN  # exact frame index
            resp.tStart = t  # local t and not account for scr refresh
            resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(resp, 'tStartRefresh')  # time at next scr refresh
            resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if resp.status == STARTED and not waitOnFlip:
            theseKeys = resp.getKeys(keyList=['up', 'left', 'right'], waitRelease=False)
            _resp_allKeys.extend(theseKeys)
            if len(_resp_allKeys):
                resp.keys = _resp_allKeys[-1].name  # just the last key pressed
                resp.rt = _resp_allKeys[-1].rt
                # was this correct?
                if (resp.keys == str(corrAns)) or (resp.keys == corrAns):
                    resp.corr = 1
                else:
                    resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    training.addData('sample.started', sample.tStartRefresh)
    training.addData('sample.stopped', sample.tStopRefresh)
    training.addData('cmp1.started', cmp1.tStartRefresh)
    training.addData('cmp1.stopped', cmp1.tStopRefresh)
    training.addData('cmp2.started', cmp2.tStartRefresh)
    training.addData('cmp2.stopped', cmp2.tStopRefresh)
    training.addData('cmp3.started', cmp3.tStartRefresh)
    training.addData('cmp3.stopped', cmp3.tStopRefresh)
    # check responses
    if resp.keys in ['', [], None]:  # No response was made
        resp.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           resp.corr = 1;  # correct non-response
        else:
           resp.corr = 0;  # failed to respond (incorrectly)
    # store data for training (TrialHandler)
    training.addData('resp.keys',resp.keys)
    training.addData('resp.corr', resp.corr)
    if resp.keys != None:  # we had a response
        training.addData('resp.rt', resp.rt)
    training.addData('resp.started', resp.tStartRefresh)
    training.addData('resp.stopped', resp.tStopRefresh)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "feedback"-------
    continueRoutine = True
    routineTimer.add(1.500000)
    # update component parameters for each repeat
    if resp.corr:
            msg = "Yas! "
            msgColor = "green"
            correct_incorrect.append(1)
    else:
            msg = "Nope "
            msgColor = "red"
            correct_incorrect.append(0)
    #end trial block after scoring 100% correct on 6 consecutive trials
    nCorr = sum(correct_incorrect[-6:])
    nResps = len(correct_incorrect[-6:])
    
    print(str(nCorr)+" this is number correct")
    print(str(nResps)+" this is number of responses")
    print("*"*50)
    
    
    feedbackText.setColor(msgColor, colorSpace='rgb')
    feedbackText.setText(msg)
    # keep track of which components have finished
    feedbackComponents = [feedbackText]
    for thisComponent in feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "feedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *feedbackText* updates
        if feedbackText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedbackText.frameNStart = frameN  # exact frame index
            feedbackText.tStart = t  # local t and not account for scr refresh
            feedbackText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedbackText, 'tStartRefresh')  # time at next scr refresh
            feedbackText.setAutoDraw(True)
        if feedbackText.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedbackText.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                feedbackText.tStop = t  # not accounting for scr refresh
                feedbackText.frameNStop = frameN  # exact frame index
                win.timeOnFlip(feedbackText, 'tStopRefresh')  # time at next scr refresh
                feedbackText.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedback"-------
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    if nCorr >= 6:
        print("you got one right")
        training.finished = True
        else:
        training.finished = False
       
    training.addData('feedbackText.started', feedbackText.tStartRefresh)
    training.addData('feedbackText.stopped', feedbackText.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'training'


# ------Prepare to start Routine "instructions2"-------
continueRoutine = True
# update component parameters for each repeat
readyResp2.keys = []
readyResp2.rt = []
_readyResp2_allKeys = []
# keep track of which components have finished
instructions2Components = [readyResp2, text]
for thisComponent in instructions2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructions2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instructions2"-------
while continueRoutine:
    # get current time
    t = instructions2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructions2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *readyResp2* updates
    waitOnFlip = False
    if readyResp2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        readyResp2.frameNStart = frameN  # exact frame index
        readyResp2.tStart = t  # local t and not account for scr refresh
        readyResp2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(readyResp2, 'tStartRefresh')  # time at next scr refresh
        readyResp2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(readyResp2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(readyResp2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if readyResp2.status == STARTED and not waitOnFlip:
        theseKeys = readyResp2.getKeys(keyList=None, waitRelease=False)
        _readyResp2_allKeys.extend(theseKeys)
        if len(_readyResp2_allKeys):
            readyResp2.keys = _readyResp2_allKeys[-1].name  # just the last key pressed
            readyResp2.rt = _readyResp2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    if text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text.tStartRefresh + 10.0-frameTolerance:
            # keep track of stop time/frame for later
            text.tStop = t  # not accounting for scr refresh
            text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
            text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions2"-------
for thisComponent in instructions2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if readyResp2.keys in ['', [], None]:  # No response was made
    readyResp2.keys = None
thisExp.addData('readyResp2.keys',readyResp2.keys)
if readyResp2.keys != None:  # we had a response
    thisExp.addData('readyResp2.rt', readyResp2.rt)
thisExp.addData('readyResp2.started', readyResp2.tStartRefresh)
thisExp.addData('readyResp2.stopped', readyResp2.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
# the Routine "instructions2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
test = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('exp3.xlsx'),
    seed=None, name='test')
thisExp.addLoop(test)  # add the loop to the experiment
thisTest = test.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTest.rgb)
if thisTest != None:
    for paramName in thisTest:
        exec('{} = thisTest[paramName]'.format(paramName))

for thisTest in test:
    currentLoop = test
    # abbreviate parameter names if possible (e.g. rgb = thisTest.rgb)
    if thisTest != None:
        for paramName in thisTest:
            exec('{} = thisTest[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    # update component parameters for each repeat
    sample.setImage(_sample)
    cmp1.setImage(_cmp1)
    cmp2.setImage(_cmp2)
    cmp3.setImage(_cmp3)
    resp.keys = []
    resp.rt = []
    _resp_allKeys = []
    # keep track of which components have finished
    trialComponents = [sample, cmp1, cmp2, cmp3, resp]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *sample* updates
        if sample.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sample.frameNStart = frameN  # exact frame index
            sample.tStart = t  # local t and not account for scr refresh
            sample.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sample, 'tStartRefresh')  # time at next scr refresh
            sample.setAutoDraw(True)
        if sample.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sample.tStartRefresh + 3.0-frameTolerance:
                # keep track of stop time/frame for later
                sample.tStop = t  # not accounting for scr refresh
                sample.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sample, 'tStopRefresh')  # time at next scr refresh
                sample.setAutoDraw(False)
        
        # *cmp1* updates
        if cmp1.status == NOT_STARTED and tThisFlip >= 3.5-frameTolerance:
            # keep track of start time/frame for later
            cmp1.frameNStart = frameN  # exact frame index
            cmp1.tStart = t  # local t and not account for scr refresh
            cmp1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cmp1, 'tStartRefresh')  # time at next scr refresh
            cmp1.setAutoDraw(True)
        
        # *cmp2* updates
        if cmp2.status == NOT_STARTED and tThisFlip >= 3.5-frameTolerance:
            # keep track of start time/frame for later
            cmp2.frameNStart = frameN  # exact frame index
            cmp2.tStart = t  # local t and not account for scr refresh
            cmp2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cmp2, 'tStartRefresh')  # time at next scr refresh
            cmp2.setAutoDraw(True)
        
        # *cmp3* updates
        if cmp3.status == NOT_STARTED and tThisFlip >= 3.5-frameTolerance:
            # keep track of start time/frame for later
            cmp3.frameNStart = frameN  # exact frame index
            cmp3.tStart = t  # local t and not account for scr refresh
            cmp3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(cmp3, 'tStartRefresh')  # time at next scr refresh
            cmp3.setAutoDraw(True)
        
        # *resp* updates
        waitOnFlip = False
        if resp.status == NOT_STARTED and tThisFlip >= 3.5-frameTolerance:
            # keep track of start time/frame for later
            resp.frameNStart = frameN  # exact frame index
            resp.tStart = t  # local t and not account for scr refresh
            resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(resp, 'tStartRefresh')  # time at next scr refresh
            resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if resp.status == STARTED and not waitOnFlip:
            theseKeys = resp.getKeys(keyList=['up', 'left', 'right'], waitRelease=False)
            _resp_allKeys.extend(theseKeys)
            if len(_resp_allKeys):
                resp.keys = _resp_allKeys[-1].name  # just the last key pressed
                resp.rt = _resp_allKeys[-1].rt
                # was this correct?
                if (resp.keys == str(corrAns)) or (resp.keys == corrAns):
                    resp.corr = 1
                else:
                    resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    test.addData('sample.started', sample.tStartRefresh)
    test.addData('sample.stopped', sample.tStopRefresh)
    test.addData('cmp1.started', cmp1.tStartRefresh)
    test.addData('cmp1.stopped', cmp1.tStopRefresh)
    test.addData('cmp2.started', cmp2.tStartRefresh)
    test.addData('cmp2.stopped', cmp2.tStopRefresh)
    test.addData('cmp3.started', cmp3.tStartRefresh)
    test.addData('cmp3.stopped', cmp3.tStopRefresh)
    # check responses
    if resp.keys in ['', [], None]:  # No response was made
        resp.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           resp.corr = 1;  # correct non-response
        else:
           resp.corr = 0;  # failed to respond (incorrectly)
    # store data for test (TrialHandler)
    test.addData('resp.keys',resp.keys)
    test.addData('resp.corr', resp.corr)
    if resp.keys != None:  # we had a response
        test.addData('resp.rt', resp.rt)
    test.addData('resp.started', resp.tStartRefresh)
    test.addData('resp.stopped', resp.tStopRefresh)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'test'


# ------Prepare to start Routine "thankyou"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
thankyouComponents = [text_2]
for thisComponent in thankyouComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
thankyouClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "thankyou"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = thankyouClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=thankyouClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    if text_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_2.tStartRefresh + 3.0-frameTolerance:
            # keep track of stop time/frame for later
            text_2.tStop = t  # not accounting for scr refresh
            text_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
            text_2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in thankyouComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "thankyou"-------
for thisComponent in thankyouComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)

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
