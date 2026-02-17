#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2024.2.1post4),
    on February 16, 2026, at 12:26
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2024.2.1post4'
expName = 'turtles_categorization'  # from the Builder filename that created this script
# information about this experiment
expInfo = {
    'participant': '',
    'computer_number': '',
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = True
_winSize = [1680, 1050]
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='D:\\turtles_task_switching\\turtles_categorization_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # set how much information should be printed to the console / app
    if PILOTING:
        logging.console.setLevel(
            prefs.piloting['pilotConsoleLoggingLevel']
        )
    else:
        logging.console.setLevel('warning')
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log')
    if PILOTING:
        logFile.setLevel(
            prefs.piloting['pilotLoggingLevel']
        )
    else:
        logFile.setLevel(
            logging.getLevel('info')
        )
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if PILOTING:
        logging.debug('Fullscreen settings ignored as running in pilot mode.')
    
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=0,
            winType='pyglet', allowStencil=False,
            monitor='testMonitor', color=[0.6549, 0.6549, 0.6549], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='pix', 
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0.6549, 0.6549, 0.6549]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'pix'
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win._monitorFrameRate = win.getActualFrameRate(infoMsg='STARTING EXPERIMENT')
        expInfo['frameRate'] = win._monitorFrameRate
    win.mouseVisible = True
    win.hideMessage()
    # show a visual indicator if we're in piloting mode
    if PILOTING and prefs.piloting['showPilotingIndicator']:
        win.showPilotingIndicator()
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    # Setup iohub experiment
    ioConfig['Experiment'] = dict(filename=thisExp.dataFileName)
    
    # Start ioHub server
    ioServer = io.launchHubServer(window=win, **ioConfig)
    
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='iohub'
        )
    if deviceManager.getDevice('key_resp_7') is None:
        # initialise key_resp_7
        key_resp_7 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_7',
        )
    if deviceManager.getDevice('key_resp_8') is None:
        # initialise key_resp_8
        key_resp_8 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_8',
        )
    if deviceManager.getDevice('key_resp_9') is None:
        # initialise key_resp_9
        key_resp_9 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_9',
        )
    if deviceManager.getDevice('key_resp_10') is None:
        # initialise key_resp_10
        key_resp_10 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_10',
        )
    if deviceManager.getDevice('key_resp_11') is None:
        # initialise key_resp_11
        key_resp_11 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_11',
        )
    if deviceManager.getDevice('key_resp_12') is None:
        # initialise key_resp_12
        key_resp_12 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_12',
        )
    if deviceManager.getDevice('key_resp_13') is None:
        # initialise key_resp_13
        key_resp_13 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_13',
        )
    if deviceManager.getDevice('key_resp_14') is None:
        # initialise key_resp_14
        key_resp_14 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_14',
        )
    if deviceManager.getDevice('key_resp_training') is None:
        # initialise key_resp_training
        key_resp_training = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_training',
        )
    if deviceManager.getDevice('key_resp') is None:
        # initialise key_resp
        key_resp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp',
        )
    if deviceManager.getDevice('key_resp_2') is None:
        # initialise key_resp_2
        key_resp_2 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_2',
        )
    if deviceManager.getDevice('key_resp_3') is None:
        # initialise key_resp_3
        key_resp_3 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_3',
        )
    if deviceManager.getDevice('key_resp_4') is None:
        # initialise key_resp_4
        key_resp_4 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_4',
        )
    if deviceManager.getDevice('key_resp_5') is None:
        # initialise key_resp_5
        key_resp_5 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_5',
        )
    if deviceManager.getDevice('key_resp_6') is None:
        # initialise key_resp_6
        key_resp_6 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_6',
        )
    if deviceManager.getDevice('key_resp_size_judgment') is None:
        # initialise key_resp_size_judgment
        key_resp_size_judgment = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_size_judgment',
        )
    if deviceManager.getDevice('space_8') is None:
        # initialise space_8
        space_8 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='space_8',
        )
    if deviceManager.getDevice('space_10') is None:
        # initialise space_10
        space_10 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='space_10',
        )
    if deviceManager.getDevice('space_12') is None:
        # initialise space_12
        space_12 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='space_12',
        )
    if deviceManager.getDevice('key_resp_transfer_standard') is None:
        # initialise key_resp_transfer_standard
        key_resp_transfer_standard = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_transfer_standard',
        )
    if deviceManager.getDevice('space_14') is None:
        # initialise space_14
        space_14 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='space_14',
        )
    if deviceManager.getDevice('space_16') is None:
        # initialise space_16
        space_16 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='space_16',
        )
    if deviceManager.getDevice('space_18') is None:
        # initialise space_18
        space_18 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='space_18',
        )
    if deviceManager.getDevice('space_to_begin_switch') is None:
        # initialise space_to_begin_switch
        space_to_begin_switch = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='space_to_begin_switch',
        )
    if deviceManager.getDevice('key_resp_transfer_switch') is None:
        # initialise key_resp_transfer_switch
        key_resp_transfer_switch = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_transfer_switch',
        )
    if deviceManager.getDevice('space_to_begin_debrief') is None:
        # initialise space_to_begin_debrief
        space_to_begin_debrief = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='space_to_begin_debrief',
        )
    if deviceManager.getDevice('space_to_end') is None:
        # initialise space_to_end
        space_to_end = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='space_to_end',
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # start a timer to figure out how long we're paused for
    pauseTimer = core.Clock()
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='ioHub',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # sleep 1ms so other threads can execute
        clock.time.sleep(0.001)
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # reset any timers
    for timer in timers:
        timer.addTime(-pauseTimer.getTime())


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ioHub'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "consent" ---
    agree_button = visual.ButtonStim(win, 
        text='By clicking this box, I agee to take part in this survey and understand the information above about my participation.', font='Arial',
        pos=(400, -200),
        letterHeight=15.0,
        size=[200,200], 
        ori=0.0
        ,borderWidth=0.0,
        fillColor='darkgrey', borderColor=None,
        color='black', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='agree_button',
        depth=0
    )
    agree_button.buttonClock = core.Clock()
    decline_button = visual.ButtonStim(win, 
        text='I do not agree to participate.', font='Arial',
        pos=[400,-400],
        letterHeight=15.0,
        size=[150,150], 
        ori=0.0
        ,borderWidth=0.0,
        fillColor='darkgrey', borderColor=None,
        color='black', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='decline_button',
        depth=-1
    )
    decline_button.buttonClock = core.Clock()
    consent1_img = visual.ImageStim(
        win=win,
        name='consent1_img', 
        image='consent_p1.png', mask=None, anchor='bottom-center',
        ori=0.0, pos=(-350, -475), draggable=False, size=[825,1000],
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    mouse = event.Mouse(win=win)
    x, y = [None, None]
    mouse.mouseClock = core.Clock()
    consent2_img = visual.ImageStim(
        win=win,
        name='consent2_img', 
        image='consent_p2.png', mask=None, anchor='bottom-center',
        ori=0.0, pos=(400, -100), draggable=False, size=[700,600],
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-4.0)
    
    # --- Initialize components for Routine "age_check" ---
    age_yes = visual.ButtonStim(win, 
        text='By clicking this box, I state that I am 18 years of age or older.', font='Arial',
        pos=[0,0],
        letterHeight=15.0,
        size=[200,200], 
        ori=0.0
        ,borderWidth=0.0,
        fillColor='darkgrey', borderColor=None,
        color='black', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='age_yes',
        depth=0
    )
    age_yes.buttonClock = core.Clock()
    age_no = visual.ButtonStim(win, 
        text='I am NOT 18 years of age or older.', font='Arial',
        pos=[0,-300],
        letterHeight=15.0,
        size=[200,200], 
        ori=0.0
        ,borderWidth=0.0,
        fillColor='darkgrey', borderColor=None,
        color='black', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='age_no',
        depth=-1
    )
    age_no.buttonClock = core.Clock()
    
    # --- Initialize components for Routine "exp_setup" ---
    # Run 'Begin Experiment' code from setup
    import numpy as np
    participant_number=int(expInfo['participant'])
    num_transfer_blocks=4
    num_train_blocks=4
    num_size_blocks=2
    max_transfer_rt=5
    
    if participant_number % 2 == 0:
        condition="switch/standard"
    elif participant_number % 2 !=0:
        condition="standard/switch"
    
    category_labels=np.array(['f','j'])
    np.random.shuffle(category_labels)
    category_A_label=category_labels[0]
    category_B_label=category_labels[1]
    
    # add data
    thisExp.addData('condition',condition)
    thisExp.addData('category_A_label',category_A_label)
    thisExp.addData('category_B_label',category_B_label)
    
    # --- Initialize components for Routine "turtle_param_functions" ---
    # Run 'Begin Experiment' code from turtle_functions
    import numpy as np
    
    def get_turtle_halfcircle_vertices(radius):
        n_points = 300
        angles = np.linspace(0, np.pi, n_points)
        arc_x = radius*np.cos(angles)
        arc_y = radius*np.sin(angles)
        verts=np.column_stack([arc_x,arc_y])
        verts=np.vstack(([-radius,0],
                         verts,
                         [radius,0]))
        return verts
    
    def get_turtle_wedge_vertices(angle):
        radius=150 # DO NOT CHANGE
        n_points = 300
        angle_rad = np.deg2rad(angle)
        angles = np.linspace(0, angle_rad, n_points)
        arc_x=radius*np.cos(angles)
        arc_y=radius*np.sin(angles)
        verts=np.column_stack([arc_x,arc_y])
        verts=np.vstack(([0,0],
                        verts,
                        [0,0]))
        return verts
    
    # --- Initialize components for Routine "categorization_instructions_p1" ---
    categorization_instructions_text_1 = visual.TextStim(win=win, name='categorization_instructions_text_1',
        text='Welcome to the experiment!\n\nPress space to continue.',
        font='Arial',
        pos=(0, 0), draggable=False, height=20.0, wrapWidth=None, ori=0.0, 
        color=(-1.0000, -1.0000, -1.0000), colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_7 = keyboard.Keyboard(deviceName='key_resp_7')
    
    # --- Initialize components for Routine "categorization_instructions_p2" ---
    categorization_instructions_text_2 = visual.TextStim(win=win, name='categorization_instructions_text_2',
        text='The stimuli:\n\nIn this experiment you will be making judgments about turtles!\n\nHere is an example:\n',
        font='Arial',
        pos=(0, 0), draggable=False, height=20.0, wrapWidth=None, ori=0.0, 
        color=(-1.0000, -1.0000, -1.0000), colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    turtle_halfcircle_for_categorization_instructions = visual.ShapeStim(
        win=win, name='turtle_halfcircle_for_categorization_instructions',
        size=(1,1), vertices='triangle',
        ori=0.0, pos=(0, -200), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[-1.0000, 0.0039, -1.0000], fillColor=[-1.0000, 0.0039, -1.0000],
        opacity=None, depth=-2.0, interpolate=True)
    turtle_wedge_for_categorization_instructions = visual.ShapeStim(
        win=win, name='turtle_wedge_for_categorization_instructions',
        size=(1,1), vertices='triangle',
        ori=0.0, pos=(0, -201), draggable=False, anchor='center',
        lineWidth=0.0,
        colorSpace='rgb', lineColor=[1.0000, 0.5059, -1.0000], fillColor=[1.0000, 0.5059, -1.0000],
        opacity=None, depth=-3.0, interpolate=True)
    turtle_wedge_boundary_for_categorization_instructions = visual.Line(
        win=win, name='turtle_wedge_boundary_for_categorization_instructions',
        size=(150, 1),
        ori=0.0, pos=(0,-200), draggable=False, anchor='bottom-left',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[1.0000, 0.5059, -1.0000], fillColor=[1.0000, 0.5059, -1.0000],
        opacity=None, depth=-4.0, interpolate=True)
    space = visual.TextStim(win=win, name='space',
        text='Press space to continue',
        font='Arial',
        pos=(0, -400), draggable=False, height=20.0, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-5.0);
    key_resp_8 = keyboard.Keyboard(deviceName='key_resp_8')
    
    # --- Initialize components for Routine "categorization_instructions_p3" ---
    categorization_instructions_text_3 = visual.TextStim(win=win, name='categorization_instructions_text_3',
        text='Here is another example:\n',
        font='Arial',
        pos=(0, 0), draggable=False, height=20.0, wrapWidth=None, ori=0.0, 
        color=(-1.0000, -1.0000, -1.0000), colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    turtle_halfcircle_for_categorization_instructions_2 = visual.ShapeStim(
        win=win, name='turtle_halfcircle_for_categorization_instructions_2',
        size=(1,1), vertices='triangle',
        ori=0.0, pos=(0, -200), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[-1.0000, 0.0039, -1.0000], fillColor=[-1.0000, 0.0039, -1.0000],
        opacity=None, depth=-2.0, interpolate=True)
    space_2 = visual.TextStim(win=win, name='space_2',
        text='Press space to continue',
        font='Arial',
        pos=(0, -400), draggable=False, height=20.0, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    key_resp_9 = keyboard.Keyboard(deviceName='key_resp_9')
    turtle_wedge_for_categorization_instructions_2 = visual.ShapeStim(
        win=win, name='turtle_wedge_for_categorization_instructions_2',
        size=(1,1), vertices='triangle',
        ori=0.0, pos=(0, -201), draggable=False, anchor='center',
        lineWidth=0.0,
        colorSpace='rgb', lineColor=[1.0000, 0.5059, -1.0000], fillColor=[1.0000, 0.5059, -1.0000],
        opacity=None, depth=-5.0, interpolate=True)
    turtle_wedge_boundary_for_categorization_instructions_2 = visual.Line(
        win=win, name='turtle_wedge_boundary_for_categorization_instructions_2',
        size=(150, 1),
        ori=0.0, pos=(0,-200), draggable=False, anchor='bottom-left',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[1.0000, 0.5059, -1.0000], fillColor=[1.0000, 0.5059, -1.0000],
        opacity=None, depth=-6.0, interpolate=True)
    
    # --- Initialize components for Routine "categorization_instructions_p4" ---
    categorization_instructions_text = visual.TextStim(win=win, name='categorization_instructions_text',
        text='First, you are tasked with determining which turtle belongs to Species F or Species J. \n\nThere are TWO components related to the turtles’ species classification. You should consider both \n-   the height of the green shell AND\n\n-   the angle of the yellow head\n',
        font='Arial',
        pos=(0, 0), draggable=False, height=20.0, wrapWidth=None, ori=0.0, 
        color=(-1.0000, -1.0000, -1.0000), colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    turtle_halfcircle_for_categorization_instructions_3 = visual.ShapeStim(
        win=win, name='turtle_halfcircle_for_categorization_instructions_3',
        size=(1,1), vertices='triangle',
        ori=0.0, pos=(0, -200), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[-1.0000, 0.0039, -1.0000], fillColor=[-1.0000, 0.0039, -1.0000],
        opacity=None, depth=-1.0, interpolate=True)
    turtle_wedge_for_categorization_instructions_3 = visual.ShapeStim(
        win=win, name='turtle_wedge_for_categorization_instructions_3',
        size=(1,1), vertices='triangle',
        ori=0.0, pos=(0, -201), draggable=False, anchor='center',
        lineWidth=0.0,
        colorSpace='rgb', lineColor=[1.0000, 0.5059, -1.0000], fillColor=[1.0000, 0.5059, -1.0000],
        opacity=None, depth=-2.0, interpolate=True)
    space_3 = visual.TextStim(win=win, name='space_3',
        text='Press space to continue',
        font='Arial',
        pos=(0, -400), draggable=False, height=20.0, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    turtle_wedge_boundary_for_categorization_instructions_3 = visual.Line(
        win=win, name='turtle_wedge_boundary_for_categorization_instructions_3',
        size=(150, 1),
        ori=0.0, pos=(0,-200), draggable=False, anchor='bottom-left',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[1.0000, 0.5059, -1.0000], fillColor=[1.0000, 0.5059, -1.0000],
        opacity=None, depth=-4.0, interpolate=True)
    key_resp_10 = keyboard.Keyboard(deviceName='key_resp_10')
    
    # --- Initialize components for Routine "categorization_instructions_p5" ---
    categorization_instructions_text_4 = visual.TextStim(win=win, name='categorization_instructions_text_4',
        text='For now, you will learn to classify a single turtle on each trial.\n\n\nBefore each trial, you will see a plus sign. This will let you know that you are about to see a new turtle.\n\n\nWhen the trial begins, you will be shown a turtle.\n\n',
        font='Arial',
        pos=(0, 0), draggable=False, height=20.0, wrapWidth=None, ori=0.0, 
        color=(-1.0000, -1.0000, -1.0000), colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    turtle_halfcircle_for_categorization_instructions_4 = visual.ShapeStim(
        win=win, name='turtle_halfcircle_for_categorization_instructions_4',
        size=(1,1), vertices='triangle',
        ori=0.0, pos=(0, -200), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[-1.0000, 0.0039, -1.0000], fillColor=[-1.0000, 0.0039, -1.0000],
        opacity=None, depth=-1.0, interpolate=True)
    turtle_wedge_for_categorization_instructions_4 = visual.ShapeStim(
        win=win, name='turtle_wedge_for_categorization_instructions_4',
        size=(1,1), vertices='triangle',
        ori=0.0, pos=(0, -201), draggable=False, anchor='center',
        lineWidth=0.0,
        colorSpace='rgb', lineColor=[1.0000, 0.5059, -1.0000], fillColor=[1.0000, 0.5059, -1.0000],
        opacity=None, depth=-2.0, interpolate=True)
    space_4 = visual.TextStim(win=win, name='space_4',
        text='Press space to continue',
        font='Arial',
        pos=(0, -400), draggable=False, height=20.0, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    turtle_wedge_boundary_for_categorization_instructions_4 = visual.Line(
        win=win, name='turtle_wedge_boundary_for_categorization_instructions_4',
        size=(150, 1),
        ori=0.0, pos=(0,-200), draggable=False, anchor='bottom-left',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[1.0000, 0.5059, -1.0000], fillColor=[1.0000, 0.5059, -1.0000],
        opacity=None, depth=-4.0, interpolate=True)
    key_resp_11 = keyboard.Keyboard(deviceName='key_resp_11')
    
    # --- Initialize components for Routine "categorization_instructions_p6" ---
    categorization_instructions_text_5 = visual.TextStim(win=win, name='categorization_instructions_text_5',
        text='Press “f” on the keyboard if the turtle belongs to Species F, and “j” if it belongs to Species J.\n\n\nAfter each response you will be told whether or not your answer was correct.\n\n\nAt first you will be guessing, however, the feedback will help you get better at classifying these turtles.\n\n',
        font='Arial',
        pos=(0, 0), draggable=False, height=20.0, wrapWidth=None, ori=0.0, 
        color=(-1.0000, -1.0000, -1.0000), colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    turtle_halfcircle_for_categorization_instructions_5 = visual.ShapeStim(
        win=win, name='turtle_halfcircle_for_categorization_instructions_5',
        size=(1,1), vertices='triangle',
        ori=0.0, pos=(0, -200), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[-1.0000, 0.0039, -1.0000], fillColor=[-1.0000, 0.0039, -1.0000],
        opacity=None, depth=-1.0, interpolate=True)
    turtle_wedge_for_categorization_instructions_5 = visual.ShapeStim(
        win=win, name='turtle_wedge_for_categorization_instructions_5',
        size=(1,1), vertices='triangle',
        ori=0.0, pos=(0, -201), draggable=False, anchor='center',
        lineWidth=0.0,
        colorSpace='rgb', lineColor=[1.0000, 0.5059, -1.0000], fillColor=[1.0000, 0.5059, -1.0000],
        opacity=None, depth=-2.0, interpolate=True)
    turtle_wedge_boundary_for_categorization_instructions_5 = visual.Line(
        win=win, name='turtle_wedge_boundary_for_categorization_instructions_5',
        size=(150, 1),
        ori=0.0, pos=(0,-200), draggable=False, anchor='bottom-left',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[1.0000, 0.5059, -1.0000], fillColor=[1.0000, 0.5059, -1.0000],
        opacity=None, depth=-3.0, interpolate=True)
    space_5 = visual.TextStim(win=win, name='space_5',
        text='Press space to continue',
        font='Arial',
        pos=(0, -400), draggable=False, height=20.0, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    key_resp_12 = keyboard.Keyboard(deviceName='key_resp_12')
    
    # --- Initialize components for Routine "categorization_instructions_p7" ---
    categorization_instructions_text_6 = visual.TextStim(win=win, name='categorization_instructions_text_6',
        text='There will be other parts to this experiment, but instructions for those will come later.',
        font='Arial',
        pos=(0, 0), draggable=False, height=20.0, wrapWidth=None, ori=0.0, 
        color=(-1.0000, -1.0000, -1.0000), colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    turtle_halfcircle_for_categorization_instructions_6 = visual.ShapeStim(
        win=win, name='turtle_halfcircle_for_categorization_instructions_6',
        size=(1,1), vertices='triangle',
        ori=0.0, pos=(0, -200), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[-1.0000, 0.0039, -1.0000], fillColor=[-1.0000, 0.0039, -1.0000],
        opacity=None, depth=-1.0, interpolate=True)
    turtle_wedge_for_categorization_instructions_6 = visual.ShapeStim(
        win=win, name='turtle_wedge_for_categorization_instructions_6',
        size=(1,1), vertices='triangle',
        ori=0.0, pos=(0, -201), draggable=False, anchor='center',
        lineWidth=0.0,
        colorSpace='rgb', lineColor=[1.0000, 0.5059, -1.0000], fillColor=[1.0000, 0.5059, -1.0000],
        opacity=None, depth=-2.0, interpolate=True)
    turtle_wedge_boundary_for_categorization_instructions_6 = visual.Line(
        win=win, name='turtle_wedge_boundary_for_categorization_instructions_6',
        size=(150, 1),
        ori=0.0, pos=(0,-200), draggable=False, anchor='bottom-left',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[1.0000, 0.5059, -1.0000], fillColor=[1.0000, 0.5059, -1.0000],
        opacity=None, depth=-3.0, interpolate=True)
    space_6 = visual.TextStim(win=win, name='space_6',
        text='Press space to continue',
        font='Arial',
        pos=(0, -400), draggable=False, height=20.0, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    key_resp_13 = keyboard.Keyboard(deviceName='key_resp_13')
    
    # --- Initialize components for Routine "categorization_instructions_p8" ---
    space_to_begin_exp = visual.TextStim(win=win, name='space_to_begin_exp',
        text='Press space to begin classifying turtles.',
        font='Arial',
        pos=(0, 0), draggable=False, height=20.0, wrapWidth=None, ori=0.0, 
        color=(-1.0000, -1.0000, -1.0000), colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_14 = keyboard.Keyboard(deviceName='key_resp_14')
    
    # --- Initialize components for Routine "fixation_cross" ---
    fixation_cross_1 = visual.ShapeStim(
        win=win, name='fixation_cross_1', vertices='cross',
        size=(30, 30),
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[-1.0000, -1.0000, -1.0000], fillColor=[-1.0000, -1.0000, -1.0000],
        opacity=None, depth=0.0, interpolate=True)
    
    # --- Initialize components for Routine "blank" ---
    text_2 = visual.TextStim(win=win, name='text_2',
        text=None,
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "get_turtle_params_training" ---
    
    # --- Initialize components for Routine "training_response" ---
    key_resp_training = keyboard.Keyboard(deviceName='key_resp_training')
    turtle_halfcircle = visual.ShapeStim(
        win=win, name='turtle_halfcircle',
        size=(1,1), vertices='triangle',
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[-1.0000, 0.0039, -1.0000], fillColor=[-1.0000, 0.0039, -1.0000],
        opacity=None, depth=-1.0, interpolate=True)
    turtle_wedge = visual.ShapeStim(
        win=win, name='turtle_wedge',
        size=(1,1), vertices='triangle',
        ori=0.0, pos=(0, -1), draggable=False, anchor='center',
        lineWidth=0.0,
        colorSpace='rgb', lineColor=[1.0000, 0.5059, -1.0000], fillColor=[1.0000, 0.5059, -1.0000],
        opacity=None, depth=-2.0, interpolate=True)
    turtle_wedge_boundary = visual.Line(
        win=win, name='turtle_wedge_boundary',
        size=(150, 1),
        ori=0.0, pos=(0,-1), draggable=False, anchor='bottom-left',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[1.0000, 0.5059, -1.0000], fillColor=[1.0000, 0.5059, -1.0000],
        opacity=None, depth=-3.0, interpolate=True)
    training_prompt = visual.TextStim(win=win, name='training_prompt',
        text='',
        font='Arial',
        pos=(0, -100), draggable=False, height=20.0, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=1.0, 
        languageStyle='LTR',
        depth=-4.0);
    
    # --- Initialize components for Routine "train_feedback_code_checks" ---
    
    # --- Initialize components for Routine "training_feedback" ---
    train_feedback_text_display = visual.TextStim(win=win, name='train_feedback_text_display',
        text='',
        font='Arial',
        pos=(0, -100), draggable=False, height=20.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    turtle_halfcircle_for_feedback = visual.ShapeStim(
        win=win, name='turtle_halfcircle_for_feedback',
        size=(1,1), vertices='triangle',
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[-1.0000, 0.0039, -1.0000], fillColor=[-1.0000, 0.0039, -1.0000],
        opacity=None, depth=-1.0, interpolate=True)
    turtle_wedge_for_feedback = visual.ShapeStim(
        win=win, name='turtle_wedge_for_feedback',
        size=(1,1), vertices='triangle',
        ori=0.0, pos=(0, -1), draggable=False, anchor='center',
        lineWidth=0.0,
        colorSpace='rgb', lineColor=[1.0000, 0.5059, -1.0000], fillColor=[1.0000, 0.5059, -1.0000],
        opacity=None, depth=-2.0, interpolate=True)
    turtle_wedge_boundary_for_feedback = visual.Line(
        win=win, name='turtle_wedge_boundary_for_feedback',
        size=(150, 1),
        ori=0.0, pos=(0,-1), draggable=False, anchor='bottom-left',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[1.0000, 0.5059, -1.0000], fillColor=[1.0000, 0.5059, -1.0000],
        opacity=None, depth=-3.0, interpolate=True)
    
    # --- Initialize components for Routine "blank" ---
    text_2 = visual.TextStim(win=win, name='text_2',
        text=None,
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "del_corr_resp" ---
    
    # --- Initialize components for Routine "avg_turtle_setup" ---
    # Run 'Begin Experiment' code from get_avg_turtle
    import pandas as pd
    avg_turtle=pd.read_csv('stim/stim_avg_turtle.csv')
    avg_turtle_radius=avg_turtle['radius'][0]
    avg_turtle_angle=avg_turtle['angle'][0]
    avg_turtle_halfcircle_vertices = get_turtle_halfcircle_vertices(avg_turtle_radius)
    avg_turtle_wedge_vertices = get_turtle_wedge_vertices(avg_turtle_angle)
    avg_turtle_area = avg_turtle['area'][0]
    
    
    # --- Initialize components for Routine "size_judgment_instructions_p1" ---
    avg_turtle_instr_1 = visual.TextStim(win=win, name='avg_turtle_instr_1',
        text='You have completed the first phase of the experiment.\n\nPress space to continue.',
        font='Arial',
        pos=(0, 0), draggable=False, height=20.0, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp = keyboard.Keyboard(deviceName='key_resp')
    
    # --- Initialize components for Routine "size_judgment_instructions_p2" ---
    avg_turtle_instr_2 = visual.TextStim(win=win, name='avg_turtle_instr_2',
        text='In the next phase, we are going to ask you to learn something else about the turtles. \n\nHowever, make sure not to forget the turtle species names you just learned.\n\nPress space to continue.',
        font='Arial',
        pos=(0, 0), draggable=False, height=20.0, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_2 = keyboard.Keyboard(deviceName='key_resp_2')
    
    # --- Initialize components for Routine "size_judgment_instructions_p3" ---
    turtle_halfcircle_for_size_instructions = visual.ShapeStim(
        win=win, name='turtle_halfcircle_for_size_instructions',
        size=(1,1), vertices='triangle',
        ori=0.0, pos=(0, -200), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[-1.0000, 0.0039, -1.0000], fillColor=[-1.0000, 0.0039, -1.0000],
        opacity=None, depth=0.0, interpolate=True)
    turtle_wedge_for_size_instructions = visual.ShapeStim(
        win=win, name='turtle_wedge_for_size_instructions',
        size=(1,1), vertices='triangle',
        ori=0.0, pos=(0, -201), draggable=False, anchor='center',
        lineWidth=0.0,
        colorSpace='rgb', lineColor=[1.0000, 0.5059, -1.0000], fillColor=[1.0000, 0.5059, -1.0000],
        opacity=None, depth=-1.0, interpolate=True)
    turtle_wedge_boundary_for_instructions = visual.Line(
        win=win, name='turtle_wedge_boundary_for_instructions',
        size=(150, 1),
        ori=0.0, pos=(0,-200), draggable=False, anchor='bottom-left',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[1.0000, 0.5059, -1.0000], fillColor=[1.0000, 0.5059, -1.0000],
        opacity=None, depth=-2.0, interpolate=True)
    avg_turtle_instr_3 = visual.TextStim(win=win, name='avg_turtle_instr_3',
        text='Here is an average turtle. This turtle’s size - the total area taken up by its shell and head - is very average compared to the other turtles you have seen so far.\n\npress space to continue',
        font='Arial',
        pos=(0, 0), draggable=False, height=20.0, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    key_resp_3 = keyboard.Keyboard(deviceName='key_resp_3')
    
    # --- Initialize components for Routine "size_judgment_instructions_p4" ---
    turtle_halfcircle_for_size_instructions_2 = visual.ShapeStim(
        win=win, name='turtle_halfcircle_for_size_instructions_2',
        size=(1,1), vertices='triangle',
        ori=0.0, pos=(0, -200), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[-1.0000, 0.0039, -1.0000], fillColor=[-1.0000, 0.0039, -1.0000],
        opacity=None, depth=0.0, interpolate=True)
    turtle_wedge_for_size_instructions_2 = visual.ShapeStim(
        win=win, name='turtle_wedge_for_size_instructions_2',
        size=(1,1), vertices='triangle',
        ori=0.0, pos=(0, -201), draggable=False, anchor='center',
        lineWidth=0.0,
        colorSpace='rgb', lineColor=[1.0000, 0.5059, -1.0000], fillColor=[1.0000, 0.5059, -1.0000],
        opacity=None, depth=-1.0, interpolate=True)
    turtle_wedge_boundary_for_instructions_2 = visual.Line(
        win=win, name='turtle_wedge_boundary_for_instructions_2',
        size=(150, 1),
        ori=0.0, pos=(0,-200), draggable=False, anchor='bottom-left',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[1.0000, 0.5059, -1.0000], fillColor=[1.0000, 0.5059, -1.0000],
        opacity=None, depth=-2.0, interpolate=True)
    avg_turtle_instr = visual.TextStim(win=win, name='avg_turtle_instr',
        text='Your task, in the next part of the experiment, is to determine whether each turtle you see is smaller or larger than this average turtle.\n\nYou will still use the f and j keys - f for smaller, j for larger.\n\nPress space to continue.',
        font='Arial',
        pos=(0, 0), draggable=False, height=20.0, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    key_resp_4 = keyboard.Keyboard(deviceName='key_resp_4')
    
    # --- Initialize components for Routine "size_jugment_instructions_p5" ---
    turtle_halfcircle_for_size_instructions_3 = visual.ShapeStim(
        win=win, name='turtle_halfcircle_for_size_instructions_3',
        size=(1,1), vertices='triangle',
        ori=0.0, pos=(0, -200), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[-1.0000, 0.0039, -1.0000], fillColor=[-1.0000, 0.0039, -1.0000],
        opacity=None, depth=0.0, interpolate=True)
    turtle_wedge_for_size_instructions_3 = visual.ShapeStim(
        win=win, name='turtle_wedge_for_size_instructions_3',
        size=(1,1), vertices='triangle',
        ori=0.0, pos=(0, -201), draggable=False, anchor='center',
        lineWidth=0.0,
        colorSpace='rgb', lineColor=[1.0000, 0.5059, -1.0000], fillColor=[1.0000, 0.5059, -1.0000],
        opacity=None, depth=-1.0, interpolate=True)
    turtle_wedge_boundary_for_instructions_3 = visual.Line(
        win=win, name='turtle_wedge_boundary_for_instructions_3',
        size=(150, 1),
        ori=0.0, pos=(0,-200), draggable=False, anchor='bottom-left',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[1.0000, 0.5059, -1.0000], fillColor=[1.0000, 0.5059, -1.0000],
        opacity=None, depth=-2.0, interpolate=True)
    avg_turtle_instr_4 = visual.TextStim(win=win, name='avg_turtle_instr_4',
        text='We will still give you feedback on your answer.\n\nSome trials will be harder than others; we simply ask you to please try your best.\n\nPress space to continue.',
        font='Arial',
        pos=(0, 0), draggable=False, height=20.0, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    key_resp_5 = keyboard.Keyboard(deviceName='key_resp_5')
    
    # --- Initialize components for Routine "size_judgment_instructions_p6" ---
    turtle_halfcircle_for_size_instructions_4 = visual.ShapeStim(
        win=win, name='turtle_halfcircle_for_size_instructions_4',
        size=(1,1), vertices='triangle',
        ori=0.0, pos=(0, -200), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[-1.0000, 0.0039, -1.0000], fillColor=[-1.0000, 0.0039, -1.0000],
        opacity=None, depth=0.0, interpolate=True)
    turtle_wedge_for_size_instructions_4 = visual.ShapeStim(
        win=win, name='turtle_wedge_for_size_instructions_4',
        size=(1,1), vertices='triangle',
        ori=0.0, pos=(0, -201), draggable=False, anchor='center',
        lineWidth=0.0,
        colorSpace='rgb', lineColor=[1.0000, 0.5059, -1.0000], fillColor=[1.0000, 0.5059, -1.0000],
        opacity=None, depth=-1.0, interpolate=True)
    turtle_wedge_boundary_for_instructions_4 = visual.Line(
        win=win, name='turtle_wedge_boundary_for_instructions_4',
        size=(150, 1),
        ori=0.0, pos=(0,-200), draggable=False, anchor='bottom-left',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[1.0000, 0.5059, -1.0000], fillColor=[1.0000, 0.5059, -1.0000],
        opacity=None, depth=-2.0, interpolate=True)
    avg_turtle_instr_5 = visual.TextStim(win=win, name='avg_turtle_instr_5',
        text='The next part of the experiment will now begin.\n\nPress space to continue.',
        font='Arial',
        pos=(0, 0), draggable=False, height=20.0, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    key_resp_6 = keyboard.Keyboard(deviceName='key_resp_6')
    
    # --- Initialize components for Routine "fixation_cross" ---
    fixation_cross_1 = visual.ShapeStim(
        win=win, name='fixation_cross_1', vertices='cross',
        size=(30, 30),
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[-1.0000, -1.0000, -1.0000], fillColor=[-1.0000, -1.0000, -1.0000],
        opacity=None, depth=0.0, interpolate=True)
    
    # --- Initialize components for Routine "blank" ---
    text_2 = visual.TextStim(win=win, name='text_2',
        text=None,
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "size_judgment_params" ---
    
    # --- Initialize components for Routine "size_judgment_response" ---
    turtle_half_circle_for_size_judgment = visual.ShapeStim(
        win=win, name='turtle_half_circle_for_size_judgment',
        size=(1,1), vertices='triangle',
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[-1.0000, 0.0039, -1.0000], fillColor=[-1.0000, 0.0039, -1.0000],
        opacity=None, depth=0.0, interpolate=True)
    turtle_wedge_for_size_judgment = visual.ShapeStim(
        win=win, name='turtle_wedge_for_size_judgment',
        size=(1,1), vertices='triangle',
        ori=0.0, pos=(0, -1), draggable=False, anchor='center',
        lineWidth=0.0,
        colorSpace='rgb', lineColor=[1.0000, 0.5059, -1.0000], fillColor=[1.0000, 0.5059, -1.0000],
        opacity=None, depth=-1.0, interpolate=True)
    turtle_boundary_for_size_judgment = visual.Line(
        win=win, name='turtle_boundary_for_size_judgment',
        size=(150, 1),
        ori=0.0, pos=(0,-1), draggable=False, anchor='bottom-left',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[1.0000, 0.5059, -1.0000], fillColor=[1.0000, 0.5059, -1.0000],
        opacity=None, depth=-2.0, interpolate=True)
    size_judgment_prompt = visual.TextStim(win=win, name='size_judgment_prompt',
        text='Is this turtle smaller or larger than the average turtle?\n\nF - smaller, J - larger',
        font='Arial',
        pos=(0, -100), draggable=False, height=20.0, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=1.0, 
        languageStyle='LTR',
        depth=-3.0);
    key_resp_size_judgment = keyboard.Keyboard(deviceName='key_resp_size_judgment')
    
    # --- Initialize components for Routine "size_jugment_code_check" ---
    
    # --- Initialize components for Routine "size_judgment_feedback" ---
    turtle_half_circle_for_size_judgment_feedback = visual.ShapeStim(
        win=win, name='turtle_half_circle_for_size_judgment_feedback',
        size=(1,1), vertices='triangle',
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[-1.0000, 0.0039, -1.0000], fillColor=[-1.0000, 0.0039, -1.0000],
        opacity=None, depth=0.0, interpolate=True)
    turtle_wedge_for_size_judgment_feedback = visual.ShapeStim(
        win=win, name='turtle_wedge_for_size_judgment_feedback',
        size=(1,1), vertices='triangle',
        ori=0.0, pos=(0, -1), draggable=False, anchor='center',
        lineWidth=0.0,
        colorSpace='rgb', lineColor=[1.0000, 0.5059, -1.0000], fillColor=[1.0000, 0.5059, -1.0000],
        opacity=None, depth=-1.0, interpolate=True)
    turtle_boundary_for_size_judgment_feedback = visual.Line(
        win=win, name='turtle_boundary_for_size_judgment_feedback',
        size=(150, 1),
        ori=0.0, pos=(0,-1), draggable=False, anchor='bottom-left',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[1.0000, 0.5059, -1.0000], fillColor=[1.0000, 0.5059, -1.0000],
        opacity=None, depth=-2.0, interpolate=True)
    size_feedback_text_display = visual.TextStim(win=win, name='size_feedback_text_display',
        text='',
        font='Arial',
        pos=(0, -100), draggable=False, height=20.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    
    # --- Initialize components for Routine "blank" ---
    text_2 = visual.TextStim(win=win, name='text_2',
        text=None,
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "del_corr_size_resp_tmp" ---
    
    # --- Initialize components for Routine "index" ---
    
    # --- Initialize components for Routine "transfer_loop_setup" ---
    
    # --- Initialize components for Routine "transfer_standard_instructions_p1" ---
    transfer_standard_instructions_text_1 = visual.TextStim(win=win, name='transfer_standard_instructions_text_1',
        text='Now you will be asked to categorize some turtles again, using your knowledge of what makes a turtle belong to Species F or Species J. \n\nWe will not be asking you about size right now.',
        font='Arial',
        pos=(0, 0), draggable=False, height=20.0, wrapWidth=None, ori=0.0, 
        color=(-1.0000, -1.0000, -1.0000), colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    space_7 = visual.TextStim(win=win, name='space_7',
        text='Press space to continue',
        font='Arial',
        pos=(0, -400), draggable=False, height=20.0, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    space_8 = keyboard.Keyboard(deviceName='space_8')
    
    # --- Initialize components for Routine "transfer_standard_instructions_p2" ---
    transfer_standard_instructions_text = visual.TextStim(win=win, name='transfer_standard_instructions_text',
        text='You will not receive feedback after your responses.\n\nHowever, please make sure to respond carefully.',
        font='Arial',
        pos=(0, 0), draggable=False, height=20.0, wrapWidth=None, ori=0.0, 
        color=(-1.0000, -1.0000, -1.0000), colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    space_9 = visual.TextStim(win=win, name='space_9',
        text='Press space to continue',
        font='Arial',
        pos=(0, -400), draggable=False, height=20.0, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    space_10 = keyboard.Keyboard(deviceName='space_10')
    
    # --- Initialize components for Routine "transfer_standard_instructions_p3" ---
    transfer_standard_instructions_text_2 = visual.TextStim(win=win, name='transfer_standard_instructions_text_2',
        text='Press space to start the next phase of the experiment.\n',
        font='Arial',
        pos=(0, 0), draggable=False, height=20.0, wrapWidth=None, ori=0.0, 
        color=(-1.0000, -1.0000, -1.0000), colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    space_11 = visual.TextStim(win=win, name='space_11',
        text='Press space to continue',
        font='Arial',
        pos=(0, -400), draggable=False, height=20.0, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    space_12 = keyboard.Keyboard(deviceName='space_12')
    
    # --- Initialize components for Routine "fixation_cross" ---
    fixation_cross_1 = visual.ShapeStim(
        win=win, name='fixation_cross_1', vertices='cross',
        size=(30, 30),
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[-1.0000, -1.0000, -1.0000], fillColor=[-1.0000, -1.0000, -1.0000],
        opacity=None, depth=0.0, interpolate=True)
    
    # --- Initialize components for Routine "blank" ---
    text_2 = visual.TextStim(win=win, name='text_2',
        text=None,
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "transfer_response_standard" ---
    transfer_prompt_standard_trials = visual.TextStim(win=win, name='transfer_prompt_standard_trials',
        text='',
        font='Arial',
        pos=(0, -100), draggable=False, height=20.0, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    key_resp_transfer_standard = keyboard.Keyboard(deviceName='key_resp_transfer_standard')
    turtle_halfcircle_standard = visual.ShapeStim(
        win=win, name='turtle_halfcircle_standard',
        size=(1,1), vertices='triangle',
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[-1.0000, 0.0039, -1.0000], fillColor=[-1.0000, 0.0039, -1.0000],
        opacity=None, depth=-3.0, interpolate=True)
    turtle_wedge_standard = visual.ShapeStim(
        win=win, name='turtle_wedge_standard',
        size=(1,1), vertices='triangle',
        ori=0.0, pos=(0, -1), draggable=False, anchor='center',
        lineWidth=0.0,
        colorSpace='rgb', lineColor=[1.0000, 0.5059, -1.0000], fillColor=[1.0000, 0.5059, -1.0000],
        opacity=None, depth=-4.0, interpolate=True)
    turtle_wedge_boundary_standard = visual.Line(
        win=win, name='turtle_wedge_boundary_standard',
        size=(150, 1),
        ori=0.0, pos=(0,-1), draggable=False, anchor='bottom-left',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[1.0000, 0.5059, -1.0000], fillColor=[1.0000, 0.5059, -1.0000],
        opacity=None, depth=-5.0, interpolate=True)
    
    # --- Initialize components for Routine "blank" ---
    text_2 = visual.TextStim(win=win, name='text_2',
        text=None,
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "transfer_switch_instructions_p1" ---
    transfer_switch_instructions_text_1 = visual.TextStim(win=win, name='transfer_switch_instructions_text_1',
        text='In this next phase, you will be asked to both categorize turtles into species, and to make judgments about their size.',
        font='Arial',
        pos=(0, 0), draggable=False, height=20.0, wrapWidth=None, ori=0.0, 
        color=(-1.0000, -1.0000, -1.0000), colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    space_13 = visual.TextStim(win=win, name='space_13',
        text='Press space to continue',
        font='Arial',
        pos=(0, -400), draggable=False, height=20.0, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    space_14 = keyboard.Keyboard(deviceName='space_14')
    
    # --- Initialize components for Routine "transfer_switch_instructions_p2" ---
    transfer_switch_instructions_text_2 = visual.TextStim(win=win, name='transfer_switch_instructions_text_2',
        text='We will usually ask you about the species, but sometimes we will ask you about size.',
        font='Arial',
        pos=(0, 0), draggable=False, height=20.0, wrapWidth=None, ori=0.0, 
        color=(-1.0000, -1.0000, -1.0000), colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    space_15 = visual.TextStim(win=win, name='space_15',
        text='Press space to continue',
        font='Arial',
        pos=(0, -400), draggable=False, height=20.0, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    space_16 = keyboard.Keyboard(deviceName='space_16')
    
    # --- Initialize components for Routine "transfer_switch_instructions_p3" ---
    transfer_switch_instructions_text = visual.TextStim(win=win, name='transfer_switch_instructions_text',
        text='You will not receive feedback after your responses.\n\nHowever, please make sure to respond carefully.',
        font='Arial',
        pos=(0, 0), draggable=False, height=20.0, wrapWidth=None, ori=0.0, 
        color=(-1.0000, -1.0000, -1.0000), colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    space_17 = visual.TextStim(win=win, name='space_17',
        text='Press space to continue',
        font='Arial',
        pos=(0, -400), draggable=False, height=20.0, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    space_18 = keyboard.Keyboard(deviceName='space_18')
    
    # --- Initialize components for Routine "transfer_switch_instructions_p4" ---
    transfer_switch_instructions_text_3 = visual.TextStim(win=win, name='transfer_switch_instructions_text_3',
        text='Press space to begin the next phase of the experiment.',
        font='Arial',
        pos=(0, 0), draggable=False, height=20.0, wrapWidth=None, ori=0.0, 
        color=(-1.0000, -1.0000, -1.0000), colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    space_to_begin_switch = keyboard.Keyboard(deviceName='space_to_begin_switch')
    
    # --- Initialize components for Routine "blank" ---
    text_2 = visual.TextStim(win=win, name='text_2',
        text=None,
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "randomize_switch_trials" ---
    
    # --- Initialize components for Routine "fixation_cross" ---
    fixation_cross_1 = visual.ShapeStim(
        win=win, name='fixation_cross_1', vertices='cross',
        size=(30, 30),
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[-1.0000, -1.0000, -1.0000], fillColor=[-1.0000, -1.0000, -1.0000],
        opacity=None, depth=0.0, interpolate=True)
    
    # --- Initialize components for Routine "blank" ---
    text_2 = visual.TextStim(win=win, name='text_2',
        text=None,
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "transfer_response_switch" ---
    turtle_halfcircle_switch = visual.ShapeStim(
        win=win, name='turtle_halfcircle_switch',
        size=(1,1), vertices='triangle',
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[-1.0000, 0.0039, -1.0000], fillColor=[-1.0000, 0.0039, -1.0000],
        opacity=None, depth=-1.0, interpolate=True)
    turtle_wedge_switch = visual.ShapeStim(
        win=win, name='turtle_wedge_switch',
        size=(1,1), vertices='triangle',
        ori=0.0, pos=(0, -1), draggable=False, anchor='center',
        lineWidth=0.0,
        colorSpace='rgb', lineColor=[1.0000, 0.5059, -1.0000], fillColor=[1.0000, 0.5059, -1.0000],
        opacity=None, depth=-2.0, interpolate=True)
    turtle_wedge_boundary_switch = visual.Line(
        win=win, name='turtle_wedge_boundary_switch',
        size=(150, 1),
        ori=0.0, pos=(0,-1), draggable=False, anchor='bottom-left',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[1.0000, 0.5059, -1.0000], fillColor=[1.0000, 0.5059, -1.0000],
        opacity=None, depth=-3.0, interpolate=True)
    transfer_prompt_switch_trials = visual.TextStim(win=win, name='transfer_prompt_switch_trials',
        text='',
        font='Arial',
        pos=(0, -100), draggable=False, height=20.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    key_resp_transfer_switch = keyboard.Keyboard(deviceName='key_resp_transfer_switch')
    
    # --- Initialize components for Routine "blank" ---
    text_2 = visual.TextStim(win=win, name='text_2',
        text=None,
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "delete_switch_order" ---
    
    # --- Initialize components for Routine "begin_debrief" ---
    begin_debrief_text = visual.TextStim(win=win, name='begin_debrief_text',
        text='The experiment has now finished. On the next page, you will see a debriefing form explaining the purpose of our study and providing you with more information. After you finish reading this form, press space and the experiment will end. \n\nYou can then tell the researcher, and you are free to go.',
        font='Arial',
        pos=(0, 0), draggable=False, height=20.0, wrapWidth=None, ori=0.0, 
        color=(-1.0000, -1.0000, -1.0000), colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    space_20 = visual.TextStim(win=win, name='space_20',
        text='Press space to continue',
        font='Arial',
        pos=(0, -400), draggable=False, height=20.0, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    space_to_begin_debrief = keyboard.Keyboard(deviceName='space_to_begin_debrief')
    
    # --- Initialize components for Routine "debrief" ---
    debrief_img = visual.ImageStim(
        win=win,
        name='debrief_img', 
        image='debrief.png', mask=None, anchor='bottom-center',
        ori=0.0, pos=(0,-500), draggable=False, size=[800,1000],
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    space_to_end = keyboard.Keyboard(deviceName='space_to_end')
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "consent" ---
    # create an object to store info about Routine consent
    consent = data.Routine(
        name='consent',
        components=[agree_button, decline_button, consent1_img, mouse, consent2_img],
    )
    consent.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # reset agree_button to account for continued clicks & clear times on/off
    agree_button.reset()
    # reset decline_button to account for continued clicks & clear times on/off
    decline_button.reset()
    # setup some python lists for storing info about the mouse
    mouse.x = []
    mouse.y = []
    mouse.leftButton = []
    mouse.midButton = []
    mouse.rightButton = []
    mouse.time = []
    mouse.clicked_name = []
    gotValidClick = False  # until a click is received
    # store start times for consent
    consent.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    consent.tStart = globalClock.getTime(format='float')
    consent.status = STARTED
    thisExp.addData('consent.started', consent.tStart)
    consent.maxDuration = None
    win.color = [1.0000, 1.0000, 1.0000]
    win.colorSpace = 'rgb'
    win.backgroundImage = ''
    win.backgroundFit = 'none'
    # keep track of which components have finished
    consentComponents = consent.components
    for thisComponent in consent.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "consent" ---
    consent.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *agree_button* updates
        
        # if agree_button is starting this frame...
        if agree_button.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            agree_button.frameNStart = frameN  # exact frame index
            agree_button.tStart = t  # local t and not account for scr refresh
            agree_button.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(agree_button, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'agree_button.started')
            # update status
            agree_button.status = STARTED
            win.callOnFlip(agree_button.buttonClock.reset)
            agree_button.setAutoDraw(True)
        
        # if agree_button is active this frame...
        if agree_button.status == STARTED:
            # update params
            pass
            # check whether agree_button has been pressed
            if agree_button.isClicked:
                if not agree_button.wasClicked:
                    # if this is a new click, store time of first click and clicked until
                    agree_button.timesOn.append(agree_button.buttonClock.getTime())
                    agree_button.timesOff.append(agree_button.buttonClock.getTime())
                elif len(agree_button.timesOff):
                    # if click is continuing from last frame, update time of clicked until
                    agree_button.timesOff[-1] = agree_button.buttonClock.getTime()
                if not agree_button.wasClicked:
                    # end routine when agree_button is clicked
                    continueRoutine = False
                if not agree_button.wasClicked:
                    # run callback code when agree_button is clicked
                    pass
        # take note of whether agree_button was clicked, so that next frame we know if clicks are new
        agree_button.wasClicked = agree_button.isClicked and agree_button.status == STARTED
        # *decline_button* updates
        
        # if decline_button is starting this frame...
        if decline_button.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            decline_button.frameNStart = frameN  # exact frame index
            decline_button.tStart = t  # local t and not account for scr refresh
            decline_button.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(decline_button, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'decline_button.started')
            # update status
            decline_button.status = STARTED
            win.callOnFlip(decline_button.buttonClock.reset)
            decline_button.setAutoDraw(True)
        
        # if decline_button is active this frame...
        if decline_button.status == STARTED:
            # update params
            pass
            # check whether decline_button has been pressed
            if decline_button.isClicked:
                if not decline_button.wasClicked:
                    # if this is a new click, store time of first click and clicked until
                    decline_button.timesOn.append(decline_button.buttonClock.getTime())
                    decline_button.timesOff.append(decline_button.buttonClock.getTime())
                elif len(decline_button.timesOff):
                    # if click is continuing from last frame, update time of clicked until
                    decline_button.timesOff[-1] = decline_button.buttonClock.getTime()
                if not decline_button.wasClicked:
                    # end routine when decline_button is clicked
                    continueRoutine = False
                if not decline_button.wasClicked:
                    # run callback code when decline_button is clicked
                    pass
        # take note of whether decline_button was clicked, so that next frame we know if clicks are new
        decline_button.wasClicked = decline_button.isClicked and decline_button.status == STARTED
        
        # *consent1_img* updates
        
        # if consent1_img is starting this frame...
        if consent1_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            consent1_img.frameNStart = frameN  # exact frame index
            consent1_img.tStart = t  # local t and not account for scr refresh
            consent1_img.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(consent1_img, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'consent1_img.started')
            # update status
            consent1_img.status = STARTED
            consent1_img.setAutoDraw(True)
        
        # if consent1_img is active this frame...
        if consent1_img.status == STARTED:
            # update params
            pass
        # *mouse* updates
        
        # if mouse is starting this frame...
        if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse.frameNStart = frameN  # exact frame index
            mouse.tStart = t  # local t and not account for scr refresh
            mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse.started', t)
            # update status
            mouse.status = STARTED
            mouse.mouseClock.reset()
            prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
        if mouse.status == STARTED:  # only update if started and not finished!
            buttons = mouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames([agree_button, decline_button], namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(mouse):
                            gotValidClick = True
                            mouse.clicked_name.append(obj.name)
                    if not gotValidClick:
                        mouse.clicked_name.append(None)
                    x, y = mouse.getPos()
                    mouse.x.append(x)
                    mouse.y.append(y)
                    buttons = mouse.getPressed()
                    mouse.leftButton.append(buttons[0])
                    mouse.midButton.append(buttons[1])
                    mouse.rightButton.append(buttons[2])
                    mouse.time.append(mouse.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # end routine on response
        
        # *consent2_img* updates
        
        # if consent2_img is starting this frame...
        if consent2_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            consent2_img.frameNStart = frameN  # exact frame index
            consent2_img.tStart = t  # local t and not account for scr refresh
            consent2_img.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(consent2_img, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'consent2_img.started')
            # update status
            consent2_img.status = STARTED
            consent2_img.setAutoDraw(True)
        
        # if consent2_img is active this frame...
        if consent2_img.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            consent.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in consent.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "consent" ---
    for thisComponent in consent.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for consent
    consent.tStop = globalClock.getTime(format='float')
    consent.tStopRefresh = tThisFlipGlobal
    thisExp.addData('consent.stopped', consent.tStop)
    setupWindow(expInfo=expInfo, win=win)
    thisExp.addData('agree_button.numClicks', agree_button.numClicks)
    if agree_button.numClicks:
       thisExp.addData('agree_button.timesOn', agree_button.timesOn)
       thisExp.addData('agree_button.timesOff', agree_button.timesOff)
    else:
       thisExp.addData('agree_button.timesOn', "")
       thisExp.addData('agree_button.timesOff', "")
    thisExp.addData('decline_button.numClicks', decline_button.numClicks)
    if decline_button.numClicks:
       thisExp.addData('decline_button.timesOn', decline_button.timesOn)
       thisExp.addData('decline_button.timesOff', decline_button.timesOff)
    else:
       thisExp.addData('decline_button.timesOn', "")
       thisExp.addData('decline_button.timesOff', "")
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('mouse.x', mouse.x)
    thisExp.addData('mouse.y', mouse.y)
    thisExp.addData('mouse.leftButton', mouse.leftButton)
    thisExp.addData('mouse.midButton', mouse.midButton)
    thisExp.addData('mouse.rightButton', mouse.rightButton)
    thisExp.addData('mouse.time', mouse.time)
    thisExp.addData('mouse.clicked_name', mouse.clicked_name)
    # Run 'End Routine' code from check_consent
    if decline_button.numClicks==1:
        core.quit()
    thisExp.nextEntry()
    # the Routine "consent" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "age_check" ---
    # create an object to store info about Routine age_check
    age_check = data.Routine(
        name='age_check',
        components=[age_yes, age_no],
    )
    age_check.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # reset age_yes to account for continued clicks & clear times on/off
    age_yes.reset()
    # reset age_no to account for continued clicks & clear times on/off
    age_no.reset()
    # store start times for age_check
    age_check.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    age_check.tStart = globalClock.getTime(format='float')
    age_check.status = STARTED
    thisExp.addData('age_check.started', age_check.tStart)
    age_check.maxDuration = None
    # keep track of which components have finished
    age_checkComponents = age_check.components
    for thisComponent in age_check.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "age_check" ---
    age_check.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *age_yes* updates
        
        # if age_yes is starting this frame...
        if age_yes.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            age_yes.frameNStart = frameN  # exact frame index
            age_yes.tStart = t  # local t and not account for scr refresh
            age_yes.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(age_yes, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'age_yes.started')
            # update status
            age_yes.status = STARTED
            win.callOnFlip(age_yes.buttonClock.reset)
            age_yes.setAutoDraw(True)
        
        # if age_yes is active this frame...
        if age_yes.status == STARTED:
            # update params
            pass
            # check whether age_yes has been pressed
            if age_yes.isClicked:
                if not age_yes.wasClicked:
                    # if this is a new click, store time of first click and clicked until
                    age_yes.timesOn.append(age_yes.buttonClock.getTime())
                    age_yes.timesOff.append(age_yes.buttonClock.getTime())
                elif len(age_yes.timesOff):
                    # if click is continuing from last frame, update time of clicked until
                    age_yes.timesOff[-1] = age_yes.buttonClock.getTime()
                if not age_yes.wasClicked:
                    # end routine when age_yes is clicked
                    continueRoutine = False
                if not age_yes.wasClicked:
                    # run callback code when age_yes is clicked
                    pass
        # take note of whether age_yes was clicked, so that next frame we know if clicks are new
        age_yes.wasClicked = age_yes.isClicked and age_yes.status == STARTED
        # *age_no* updates
        
        # if age_no is starting this frame...
        if age_no.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            age_no.frameNStart = frameN  # exact frame index
            age_no.tStart = t  # local t and not account for scr refresh
            age_no.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(age_no, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'age_no.started')
            # update status
            age_no.status = STARTED
            win.callOnFlip(age_no.buttonClock.reset)
            age_no.setAutoDraw(True)
        
        # if age_no is active this frame...
        if age_no.status == STARTED:
            # update params
            pass
            # check whether age_no has been pressed
            if age_no.isClicked:
                if not age_no.wasClicked:
                    # if this is a new click, store time of first click and clicked until
                    age_no.timesOn.append(age_no.buttonClock.getTime())
                    age_no.timesOff.append(age_no.buttonClock.getTime())
                elif len(age_no.timesOff):
                    # if click is continuing from last frame, update time of clicked until
                    age_no.timesOff[-1] = age_no.buttonClock.getTime()
                if not age_no.wasClicked:
                    # end routine when age_no is clicked
                    continueRoutine = False
                if not age_no.wasClicked:
                    # run callback code when age_no is clicked
                    pass
        # take note of whether age_no was clicked, so that next frame we know if clicks are new
        age_no.wasClicked = age_no.isClicked and age_no.status == STARTED
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            age_check.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in age_check.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "age_check" ---
    for thisComponent in age_check.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for age_check
    age_check.tStop = globalClock.getTime(format='float')
    age_check.tStopRefresh = tThisFlipGlobal
    thisExp.addData('age_check.stopped', age_check.tStop)
    thisExp.addData('age_yes.numClicks', age_yes.numClicks)
    if age_yes.numClicks:
       thisExp.addData('age_yes.timesOn', age_yes.timesOn)
       thisExp.addData('age_yes.timesOff', age_yes.timesOff)
    else:
       thisExp.addData('age_yes.timesOn', "")
       thisExp.addData('age_yes.timesOff', "")
    thisExp.addData('age_no.numClicks', age_no.numClicks)
    if age_no.numClicks:
       thisExp.addData('age_no.timesOn', age_no.timesOn)
       thisExp.addData('age_no.timesOff', age_no.timesOff)
    else:
       thisExp.addData('age_no.timesOn', "")
       thisExp.addData('age_no.timesOff', "")
    # Run 'End Routine' code from age_check_code
    if age_no.numClicks==1:
        delete_data=True
    else:
        delete_data=False
    thisExp.nextEntry()
    # the Routine "age_check" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "exp_setup" ---
    # create an object to store info about Routine exp_setup
    exp_setup = data.Routine(
        name='exp_setup',
        components=[],
    )
    exp_setup.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for exp_setup
    exp_setup.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    exp_setup.tStart = globalClock.getTime(format='float')
    exp_setup.status = STARTED
    thisExp.addData('exp_setup.started', exp_setup.tStart)
    exp_setup.maxDuration = None
    # keep track of which components have finished
    exp_setupComponents = exp_setup.components
    for thisComponent in exp_setup.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "exp_setup" ---
    exp_setup.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            exp_setup.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in exp_setup.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "exp_setup" ---
    for thisComponent in exp_setup.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for exp_setup
    exp_setup.tStop = globalClock.getTime(format='float')
    exp_setup.tStopRefresh = tThisFlipGlobal
    thisExp.addData('exp_setup.stopped', exp_setup.tStop)
    thisExp.nextEntry()
    # the Routine "exp_setup" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "turtle_param_functions" ---
    # create an object to store info about Routine turtle_param_functions
    turtle_param_functions = data.Routine(
        name='turtle_param_functions',
        components=[],
    )
    turtle_param_functions.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for turtle_param_functions
    turtle_param_functions.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    turtle_param_functions.tStart = globalClock.getTime(format='float')
    turtle_param_functions.status = STARTED
    thisExp.addData('turtle_param_functions.started', turtle_param_functions.tStart)
    turtle_param_functions.maxDuration = None
    # keep track of which components have finished
    turtle_param_functionsComponents = turtle_param_functions.components
    for thisComponent in turtle_param_functions.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "turtle_param_functions" ---
    turtle_param_functions.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            turtle_param_functions.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in turtle_param_functions.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "turtle_param_functions" ---
    for thisComponent in turtle_param_functions.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for turtle_param_functions
    turtle_param_functions.tStop = globalClock.getTime(format='float')
    turtle_param_functions.tStopRefresh = tThisFlipGlobal
    thisExp.addData('turtle_param_functions.stopped', turtle_param_functions.tStop)
    thisExp.nextEntry()
    # the Routine "turtle_param_functions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    categorization_instructions = data.TrialHandler2(
        name='categorization_instructions',
        nReps=0.0, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=[None], 
        seed=None, 
    )
    thisExp.addLoop(categorization_instructions)  # add the loop to the experiment
    thisCategorization_instruction = categorization_instructions.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisCategorization_instruction.rgb)
    if thisCategorization_instruction != None:
        for paramName in thisCategorization_instruction:
            globals()[paramName] = thisCategorization_instruction[paramName]
    
    for thisCategorization_instruction in categorization_instructions:
        currentLoop = categorization_instructions
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # abbreviate parameter names if possible (e.g. rgb = thisCategorization_instruction.rgb)
        if thisCategorization_instruction != None:
            for paramName in thisCategorization_instruction:
                globals()[paramName] = thisCategorization_instruction[paramName]
        
        # --- Prepare to start Routine "categorization_instructions_p1" ---
        # create an object to store info about Routine categorization_instructions_p1
        categorization_instructions_p1 = data.Routine(
            name='categorization_instructions_p1',
            components=[categorization_instructions_text_1, key_resp_7],
        )
        categorization_instructions_p1.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # create starting attributes for key_resp_7
        key_resp_7.keys = []
        key_resp_7.rt = []
        _key_resp_7_allKeys = []
        # store start times for categorization_instructions_p1
        categorization_instructions_p1.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        categorization_instructions_p1.tStart = globalClock.getTime(format='float')
        categorization_instructions_p1.status = STARTED
        thisExp.addData('categorization_instructions_p1.started', categorization_instructions_p1.tStart)
        categorization_instructions_p1.maxDuration = None
        # keep track of which components have finished
        categorization_instructions_p1Components = categorization_instructions_p1.components
        for thisComponent in categorization_instructions_p1.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "categorization_instructions_p1" ---
        # if trial has changed, end Routine now
        if isinstance(categorization_instructions, data.TrialHandler2) and thisCategorization_instruction.thisN != categorization_instructions.thisTrial.thisN:
            continueRoutine = False
        categorization_instructions_p1.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *categorization_instructions_text_1* updates
            
            # if categorization_instructions_text_1 is starting this frame...
            if categorization_instructions_text_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                categorization_instructions_text_1.frameNStart = frameN  # exact frame index
                categorization_instructions_text_1.tStart = t  # local t and not account for scr refresh
                categorization_instructions_text_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(categorization_instructions_text_1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'categorization_instructions_text_1.started')
                # update status
                categorization_instructions_text_1.status = STARTED
                categorization_instructions_text_1.setAutoDraw(True)
            
            # if categorization_instructions_text_1 is active this frame...
            if categorization_instructions_text_1.status == STARTED:
                # update params
                pass
            
            # *key_resp_7* updates
            waitOnFlip = False
            
            # if key_resp_7 is starting this frame...
            if key_resp_7.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                key_resp_7.frameNStart = frameN  # exact frame index
                key_resp_7.tStart = t  # local t and not account for scr refresh
                key_resp_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_7.started')
                # update status
                key_resp_7.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_7.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_7.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_7_allKeys.extend(theseKeys)
                if len(_key_resp_7_allKeys):
                    key_resp_7.keys = _key_resp_7_allKeys[-1].name  # just the last key pressed
                    key_resp_7.rt = _key_resp_7_allKeys[-1].rt
                    key_resp_7.duration = _key_resp_7_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                categorization_instructions_p1.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in categorization_instructions_p1.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "categorization_instructions_p1" ---
        for thisComponent in categorization_instructions_p1.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for categorization_instructions_p1
        categorization_instructions_p1.tStop = globalClock.getTime(format='float')
        categorization_instructions_p1.tStopRefresh = tThisFlipGlobal
        thisExp.addData('categorization_instructions_p1.stopped', categorization_instructions_p1.tStop)
        # check responses
        if key_resp_7.keys in ['', [], None]:  # No response was made
            key_resp_7.keys = None
        categorization_instructions.addData('key_resp_7.keys',key_resp_7.keys)
        if key_resp_7.keys != None:  # we had a response
            categorization_instructions.addData('key_resp_7.rt', key_resp_7.rt)
            categorization_instructions.addData('key_resp_7.duration', key_resp_7.duration)
        # the Routine "categorization_instructions_p1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "categorization_instructions_p2" ---
        # create an object to store info about Routine categorization_instructions_p2
        categorization_instructions_p2 = data.Routine(
            name='categorization_instructions_p2',
            components=[categorization_instructions_text_2, turtle_halfcircle_for_categorization_instructions, turtle_wedge_for_categorization_instructions, turtle_wedge_boundary_for_categorization_instructions, space, key_resp_8],
        )
        categorization_instructions_p2.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from turtle_setup_for_categorization_instructions
        example_turtle_radius=113
        example_turtle_angle=25
        example_turtle_halfcircle_vertices = get_turtle_halfcircle_vertices(example_turtle_radius)
        example_turtle_wedge_vertices = get_turtle_wedge_vertices(example_turtle_angle)
        
        turtle_halfcircle_for_categorization_instructions.setVertices(example_turtle_halfcircle_vertices)
        turtle_wedge_for_categorization_instructions.setVertices(example_turtle_wedge_vertices)
        # create starting attributes for key_resp_8
        key_resp_8.keys = []
        key_resp_8.rt = []
        _key_resp_8_allKeys = []
        # store start times for categorization_instructions_p2
        categorization_instructions_p2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        categorization_instructions_p2.tStart = globalClock.getTime(format='float')
        categorization_instructions_p2.status = STARTED
        thisExp.addData('categorization_instructions_p2.started', categorization_instructions_p2.tStart)
        categorization_instructions_p2.maxDuration = None
        # keep track of which components have finished
        categorization_instructions_p2Components = categorization_instructions_p2.components
        for thisComponent in categorization_instructions_p2.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "categorization_instructions_p2" ---
        # if trial has changed, end Routine now
        if isinstance(categorization_instructions, data.TrialHandler2) and thisCategorization_instruction.thisN != categorization_instructions.thisTrial.thisN:
            continueRoutine = False
        categorization_instructions_p2.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *categorization_instructions_text_2* updates
            
            # if categorization_instructions_text_2 is starting this frame...
            if categorization_instructions_text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                categorization_instructions_text_2.frameNStart = frameN  # exact frame index
                categorization_instructions_text_2.tStart = t  # local t and not account for scr refresh
                categorization_instructions_text_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(categorization_instructions_text_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'categorization_instructions_text_2.started')
                # update status
                categorization_instructions_text_2.status = STARTED
                categorization_instructions_text_2.setAutoDraw(True)
            
            # if categorization_instructions_text_2 is active this frame...
            if categorization_instructions_text_2.status == STARTED:
                # update params
                pass
            
            # *turtle_halfcircle_for_categorization_instructions* updates
            
            # if turtle_halfcircle_for_categorization_instructions is starting this frame...
            if turtle_halfcircle_for_categorization_instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                turtle_halfcircle_for_categorization_instructions.frameNStart = frameN  # exact frame index
                turtle_halfcircle_for_categorization_instructions.tStart = t  # local t and not account for scr refresh
                turtle_halfcircle_for_categorization_instructions.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(turtle_halfcircle_for_categorization_instructions, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'turtle_halfcircle_for_categorization_instructions.started')
                # update status
                turtle_halfcircle_for_categorization_instructions.status = STARTED
                turtle_halfcircle_for_categorization_instructions.setAutoDraw(True)
            
            # if turtle_halfcircle_for_categorization_instructions is active this frame...
            if turtle_halfcircle_for_categorization_instructions.status == STARTED:
                # update params
                pass
            
            # *turtle_wedge_for_categorization_instructions* updates
            
            # if turtle_wedge_for_categorization_instructions is starting this frame...
            if turtle_wedge_for_categorization_instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                turtle_wedge_for_categorization_instructions.frameNStart = frameN  # exact frame index
                turtle_wedge_for_categorization_instructions.tStart = t  # local t and not account for scr refresh
                turtle_wedge_for_categorization_instructions.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(turtle_wedge_for_categorization_instructions, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'turtle_wedge_for_categorization_instructions.started')
                # update status
                turtle_wedge_for_categorization_instructions.status = STARTED
                turtle_wedge_for_categorization_instructions.setAutoDraw(True)
            
            # if turtle_wedge_for_categorization_instructions is active this frame...
            if turtle_wedge_for_categorization_instructions.status == STARTED:
                # update params
                pass
            
            # *turtle_wedge_boundary_for_categorization_instructions* updates
            
            # if turtle_wedge_boundary_for_categorization_instructions is starting this frame...
            if turtle_wedge_boundary_for_categorization_instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                turtle_wedge_boundary_for_categorization_instructions.frameNStart = frameN  # exact frame index
                turtle_wedge_boundary_for_categorization_instructions.tStart = t  # local t and not account for scr refresh
                turtle_wedge_boundary_for_categorization_instructions.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(turtle_wedge_boundary_for_categorization_instructions, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'turtle_wedge_boundary_for_categorization_instructions.started')
                # update status
                turtle_wedge_boundary_for_categorization_instructions.status = STARTED
                turtle_wedge_boundary_for_categorization_instructions.setAutoDraw(True)
            
            # if turtle_wedge_boundary_for_categorization_instructions is active this frame...
            if turtle_wedge_boundary_for_categorization_instructions.status == STARTED:
                # update params
                pass
            
            # *space* updates
            
            # if space is starting this frame...
            if space.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                # keep track of start time/frame for later
                space.frameNStart = frameN  # exact frame index
                space.tStart = t  # local t and not account for scr refresh
                space.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(space, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'space.started')
                # update status
                space.status = STARTED
                space.setAutoDraw(True)
            
            # if space is active this frame...
            if space.status == STARTED:
                # update params
                pass
            
            # *key_resp_8* updates
            waitOnFlip = False
            
            # if key_resp_8 is starting this frame...
            if key_resp_8.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                # keep track of start time/frame for later
                key_resp_8.frameNStart = frameN  # exact frame index
                key_resp_8.tStart = t  # local t and not account for scr refresh
                key_resp_8.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_8, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_8.started')
                # update status
                key_resp_8.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_8.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_8.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_8_allKeys.extend(theseKeys)
                if len(_key_resp_8_allKeys):
                    key_resp_8.keys = _key_resp_8_allKeys[-1].name  # just the last key pressed
                    key_resp_8.rt = _key_resp_8_allKeys[-1].rt
                    key_resp_8.duration = _key_resp_8_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                categorization_instructions_p2.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in categorization_instructions_p2.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "categorization_instructions_p2" ---
        for thisComponent in categorization_instructions_p2.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for categorization_instructions_p2
        categorization_instructions_p2.tStop = globalClock.getTime(format='float')
        categorization_instructions_p2.tStopRefresh = tThisFlipGlobal
        thisExp.addData('categorization_instructions_p2.stopped', categorization_instructions_p2.tStop)
        # check responses
        if key_resp_8.keys in ['', [], None]:  # No response was made
            key_resp_8.keys = None
        categorization_instructions.addData('key_resp_8.keys',key_resp_8.keys)
        if key_resp_8.keys != None:  # we had a response
            categorization_instructions.addData('key_resp_8.rt', key_resp_8.rt)
            categorization_instructions.addData('key_resp_8.duration', key_resp_8.duration)
        # the Routine "categorization_instructions_p2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "categorization_instructions_p3" ---
        # create an object to store info about Routine categorization_instructions_p3
        categorization_instructions_p3 = data.Routine(
            name='categorization_instructions_p3',
            components=[categorization_instructions_text_3, turtle_halfcircle_for_categorization_instructions_2, space_2, key_resp_9, turtle_wedge_for_categorization_instructions_2, turtle_wedge_boundary_for_categorization_instructions_2],
        )
        categorization_instructions_p3.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from turtle_setup_for_categorization_instructions_2
        example_turtle_radius=40
        example_turtle_angle=30
        example_turtle_halfcircle_vertices = get_turtle_halfcircle_vertices(example_turtle_radius)
        example_turtle_wedge_vertices = get_turtle_wedge_vertices(example_turtle_angle)
        
        turtle_halfcircle_for_categorization_instructions_2.setVertices(example_turtle_halfcircle_vertices)
        # create starting attributes for key_resp_9
        key_resp_9.keys = []
        key_resp_9.rt = []
        _key_resp_9_allKeys = []
        turtle_wedge_for_categorization_instructions_2.setVertices(example_turtle_wedge_vertices)
        # store start times for categorization_instructions_p3
        categorization_instructions_p3.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        categorization_instructions_p3.tStart = globalClock.getTime(format='float')
        categorization_instructions_p3.status = STARTED
        thisExp.addData('categorization_instructions_p3.started', categorization_instructions_p3.tStart)
        categorization_instructions_p3.maxDuration = None
        # keep track of which components have finished
        categorization_instructions_p3Components = categorization_instructions_p3.components
        for thisComponent in categorization_instructions_p3.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "categorization_instructions_p3" ---
        # if trial has changed, end Routine now
        if isinstance(categorization_instructions, data.TrialHandler2) and thisCategorization_instruction.thisN != categorization_instructions.thisTrial.thisN:
            continueRoutine = False
        categorization_instructions_p3.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *categorization_instructions_text_3* updates
            
            # if categorization_instructions_text_3 is starting this frame...
            if categorization_instructions_text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                categorization_instructions_text_3.frameNStart = frameN  # exact frame index
                categorization_instructions_text_3.tStart = t  # local t and not account for scr refresh
                categorization_instructions_text_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(categorization_instructions_text_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'categorization_instructions_text_3.started')
                # update status
                categorization_instructions_text_3.status = STARTED
                categorization_instructions_text_3.setAutoDraw(True)
            
            # if categorization_instructions_text_3 is active this frame...
            if categorization_instructions_text_3.status == STARTED:
                # update params
                pass
            
            # *turtle_halfcircle_for_categorization_instructions_2* updates
            
            # if turtle_halfcircle_for_categorization_instructions_2 is starting this frame...
            if turtle_halfcircle_for_categorization_instructions_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                turtle_halfcircle_for_categorization_instructions_2.frameNStart = frameN  # exact frame index
                turtle_halfcircle_for_categorization_instructions_2.tStart = t  # local t and not account for scr refresh
                turtle_halfcircle_for_categorization_instructions_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(turtle_halfcircle_for_categorization_instructions_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'turtle_halfcircle_for_categorization_instructions_2.started')
                # update status
                turtle_halfcircle_for_categorization_instructions_2.status = STARTED
                turtle_halfcircle_for_categorization_instructions_2.setAutoDraw(True)
            
            # if turtle_halfcircle_for_categorization_instructions_2 is active this frame...
            if turtle_halfcircle_for_categorization_instructions_2.status == STARTED:
                # update params
                pass
            
            # *space_2* updates
            
            # if space_2 is starting this frame...
            if space_2.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                # keep track of start time/frame for later
                space_2.frameNStart = frameN  # exact frame index
                space_2.tStart = t  # local t and not account for scr refresh
                space_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(space_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'space_2.started')
                # update status
                space_2.status = STARTED
                space_2.setAutoDraw(True)
            
            # if space_2 is active this frame...
            if space_2.status == STARTED:
                # update params
                pass
            
            # *key_resp_9* updates
            waitOnFlip = False
            
            # if key_resp_9 is starting this frame...
            if key_resp_9.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                # keep track of start time/frame for later
                key_resp_9.frameNStart = frameN  # exact frame index
                key_resp_9.tStart = t  # local t and not account for scr refresh
                key_resp_9.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_9, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_9.started')
                # update status
                key_resp_9.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_9.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_9.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_9.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_9_allKeys.extend(theseKeys)
                if len(_key_resp_9_allKeys):
                    key_resp_9.keys = _key_resp_9_allKeys[-1].name  # just the last key pressed
                    key_resp_9.rt = _key_resp_9_allKeys[-1].rt
                    key_resp_9.duration = _key_resp_9_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # *turtle_wedge_for_categorization_instructions_2* updates
            
            # if turtle_wedge_for_categorization_instructions_2 is starting this frame...
            if turtle_wedge_for_categorization_instructions_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                turtle_wedge_for_categorization_instructions_2.frameNStart = frameN  # exact frame index
                turtle_wedge_for_categorization_instructions_2.tStart = t  # local t and not account for scr refresh
                turtle_wedge_for_categorization_instructions_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(turtle_wedge_for_categorization_instructions_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'turtle_wedge_for_categorization_instructions_2.started')
                # update status
                turtle_wedge_for_categorization_instructions_2.status = STARTED
                turtle_wedge_for_categorization_instructions_2.setAutoDraw(True)
            
            # if turtle_wedge_for_categorization_instructions_2 is active this frame...
            if turtle_wedge_for_categorization_instructions_2.status == STARTED:
                # update params
                pass
            
            # *turtle_wedge_boundary_for_categorization_instructions_2* updates
            
            # if turtle_wedge_boundary_for_categorization_instructions_2 is starting this frame...
            if turtle_wedge_boundary_for_categorization_instructions_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                turtle_wedge_boundary_for_categorization_instructions_2.frameNStart = frameN  # exact frame index
                turtle_wedge_boundary_for_categorization_instructions_2.tStart = t  # local t and not account for scr refresh
                turtle_wedge_boundary_for_categorization_instructions_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(turtle_wedge_boundary_for_categorization_instructions_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'turtle_wedge_boundary_for_categorization_instructions_2.started')
                # update status
                turtle_wedge_boundary_for_categorization_instructions_2.status = STARTED
                turtle_wedge_boundary_for_categorization_instructions_2.setAutoDraw(True)
            
            # if turtle_wedge_boundary_for_categorization_instructions_2 is active this frame...
            if turtle_wedge_boundary_for_categorization_instructions_2.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                categorization_instructions_p3.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in categorization_instructions_p3.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "categorization_instructions_p3" ---
        for thisComponent in categorization_instructions_p3.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for categorization_instructions_p3
        categorization_instructions_p3.tStop = globalClock.getTime(format='float')
        categorization_instructions_p3.tStopRefresh = tThisFlipGlobal
        thisExp.addData('categorization_instructions_p3.stopped', categorization_instructions_p3.tStop)
        # check responses
        if key_resp_9.keys in ['', [], None]:  # No response was made
            key_resp_9.keys = None
        categorization_instructions.addData('key_resp_9.keys',key_resp_9.keys)
        if key_resp_9.keys != None:  # we had a response
            categorization_instructions.addData('key_resp_9.rt', key_resp_9.rt)
            categorization_instructions.addData('key_resp_9.duration', key_resp_9.duration)
        # the Routine "categorization_instructions_p3" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "categorization_instructions_p4" ---
        # create an object to store info about Routine categorization_instructions_p4
        categorization_instructions_p4 = data.Routine(
            name='categorization_instructions_p4',
            components=[categorization_instructions_text, turtle_halfcircle_for_categorization_instructions_3, turtle_wedge_for_categorization_instructions_3, space_3, turtle_wedge_boundary_for_categorization_instructions_3, key_resp_10],
        )
        categorization_instructions_p4.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        turtle_halfcircle_for_categorization_instructions_3.setVertices(example_turtle_halfcircle_vertices)
        turtle_wedge_for_categorization_instructions_3.setVertices(example_turtle_wedge_vertices)
        # create starting attributes for key_resp_10
        key_resp_10.keys = []
        key_resp_10.rt = []
        _key_resp_10_allKeys = []
        # store start times for categorization_instructions_p4
        categorization_instructions_p4.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        categorization_instructions_p4.tStart = globalClock.getTime(format='float')
        categorization_instructions_p4.status = STARTED
        thisExp.addData('categorization_instructions_p4.started', categorization_instructions_p4.tStart)
        categorization_instructions_p4.maxDuration = None
        # keep track of which components have finished
        categorization_instructions_p4Components = categorization_instructions_p4.components
        for thisComponent in categorization_instructions_p4.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "categorization_instructions_p4" ---
        # if trial has changed, end Routine now
        if isinstance(categorization_instructions, data.TrialHandler2) and thisCategorization_instruction.thisN != categorization_instructions.thisTrial.thisN:
            continueRoutine = False
        categorization_instructions_p4.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *categorization_instructions_text* updates
            
            # if categorization_instructions_text is starting this frame...
            if categorization_instructions_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                categorization_instructions_text.frameNStart = frameN  # exact frame index
                categorization_instructions_text.tStart = t  # local t and not account for scr refresh
                categorization_instructions_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(categorization_instructions_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'categorization_instructions_text.started')
                # update status
                categorization_instructions_text.status = STARTED
                categorization_instructions_text.setAutoDraw(True)
            
            # if categorization_instructions_text is active this frame...
            if categorization_instructions_text.status == STARTED:
                # update params
                pass
            
            # *turtle_halfcircle_for_categorization_instructions_3* updates
            
            # if turtle_halfcircle_for_categorization_instructions_3 is starting this frame...
            if turtle_halfcircle_for_categorization_instructions_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                turtle_halfcircle_for_categorization_instructions_3.frameNStart = frameN  # exact frame index
                turtle_halfcircle_for_categorization_instructions_3.tStart = t  # local t and not account for scr refresh
                turtle_halfcircle_for_categorization_instructions_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(turtle_halfcircle_for_categorization_instructions_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'turtle_halfcircle_for_categorization_instructions_3.started')
                # update status
                turtle_halfcircle_for_categorization_instructions_3.status = STARTED
                turtle_halfcircle_for_categorization_instructions_3.setAutoDraw(True)
            
            # if turtle_halfcircle_for_categorization_instructions_3 is active this frame...
            if turtle_halfcircle_for_categorization_instructions_3.status == STARTED:
                # update params
                pass
            
            # *turtle_wedge_for_categorization_instructions_3* updates
            
            # if turtle_wedge_for_categorization_instructions_3 is starting this frame...
            if turtle_wedge_for_categorization_instructions_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                turtle_wedge_for_categorization_instructions_3.frameNStart = frameN  # exact frame index
                turtle_wedge_for_categorization_instructions_3.tStart = t  # local t and not account for scr refresh
                turtle_wedge_for_categorization_instructions_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(turtle_wedge_for_categorization_instructions_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'turtle_wedge_for_categorization_instructions_3.started')
                # update status
                turtle_wedge_for_categorization_instructions_3.status = STARTED
                turtle_wedge_for_categorization_instructions_3.setAutoDraw(True)
            
            # if turtle_wedge_for_categorization_instructions_3 is active this frame...
            if turtle_wedge_for_categorization_instructions_3.status == STARTED:
                # update params
                pass
            
            # *space_3* updates
            
            # if space_3 is starting this frame...
            if space_3.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                # keep track of start time/frame for later
                space_3.frameNStart = frameN  # exact frame index
                space_3.tStart = t  # local t and not account for scr refresh
                space_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(space_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'space_3.started')
                # update status
                space_3.status = STARTED
                space_3.setAutoDraw(True)
            
            # if space_3 is active this frame...
            if space_3.status == STARTED:
                # update params
                pass
            
            # *turtle_wedge_boundary_for_categorization_instructions_3* updates
            
            # if turtle_wedge_boundary_for_categorization_instructions_3 is starting this frame...
            if turtle_wedge_boundary_for_categorization_instructions_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                turtle_wedge_boundary_for_categorization_instructions_3.frameNStart = frameN  # exact frame index
                turtle_wedge_boundary_for_categorization_instructions_3.tStart = t  # local t and not account for scr refresh
                turtle_wedge_boundary_for_categorization_instructions_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(turtle_wedge_boundary_for_categorization_instructions_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'turtle_wedge_boundary_for_categorization_instructions_3.started')
                # update status
                turtle_wedge_boundary_for_categorization_instructions_3.status = STARTED
                turtle_wedge_boundary_for_categorization_instructions_3.setAutoDraw(True)
            
            # if turtle_wedge_boundary_for_categorization_instructions_3 is active this frame...
            if turtle_wedge_boundary_for_categorization_instructions_3.status == STARTED:
                # update params
                pass
            
            # *key_resp_10* updates
            waitOnFlip = False
            
            # if key_resp_10 is starting this frame...
            if key_resp_10.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                # keep track of start time/frame for later
                key_resp_10.frameNStart = frameN  # exact frame index
                key_resp_10.tStart = t  # local t and not account for scr refresh
                key_resp_10.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_10, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_10.started')
                # update status
                key_resp_10.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_10.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_10.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_10.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_10.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_10_allKeys.extend(theseKeys)
                if len(_key_resp_10_allKeys):
                    key_resp_10.keys = _key_resp_10_allKeys[-1].name  # just the last key pressed
                    key_resp_10.rt = _key_resp_10_allKeys[-1].rt
                    key_resp_10.duration = _key_resp_10_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                categorization_instructions_p4.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in categorization_instructions_p4.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "categorization_instructions_p4" ---
        for thisComponent in categorization_instructions_p4.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for categorization_instructions_p4
        categorization_instructions_p4.tStop = globalClock.getTime(format='float')
        categorization_instructions_p4.tStopRefresh = tThisFlipGlobal
        thisExp.addData('categorization_instructions_p4.stopped', categorization_instructions_p4.tStop)
        # check responses
        if key_resp_10.keys in ['', [], None]:  # No response was made
            key_resp_10.keys = None
        categorization_instructions.addData('key_resp_10.keys',key_resp_10.keys)
        if key_resp_10.keys != None:  # we had a response
            categorization_instructions.addData('key_resp_10.rt', key_resp_10.rt)
            categorization_instructions.addData('key_resp_10.duration', key_resp_10.duration)
        # the Routine "categorization_instructions_p4" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "categorization_instructions_p5" ---
        # create an object to store info about Routine categorization_instructions_p5
        categorization_instructions_p5 = data.Routine(
            name='categorization_instructions_p5',
            components=[categorization_instructions_text_4, turtle_halfcircle_for_categorization_instructions_4, turtle_wedge_for_categorization_instructions_4, space_4, turtle_wedge_boundary_for_categorization_instructions_4, key_resp_11],
        )
        categorization_instructions_p5.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        turtle_halfcircle_for_categorization_instructions_4.setVertices(example_turtle_halfcircle_vertices)
        turtle_wedge_for_categorization_instructions_4.setVertices(example_turtle_wedge_vertices)
        # create starting attributes for key_resp_11
        key_resp_11.keys = []
        key_resp_11.rt = []
        _key_resp_11_allKeys = []
        # store start times for categorization_instructions_p5
        categorization_instructions_p5.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        categorization_instructions_p5.tStart = globalClock.getTime(format='float')
        categorization_instructions_p5.status = STARTED
        thisExp.addData('categorization_instructions_p5.started', categorization_instructions_p5.tStart)
        categorization_instructions_p5.maxDuration = None
        # keep track of which components have finished
        categorization_instructions_p5Components = categorization_instructions_p5.components
        for thisComponent in categorization_instructions_p5.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "categorization_instructions_p5" ---
        # if trial has changed, end Routine now
        if isinstance(categorization_instructions, data.TrialHandler2) and thisCategorization_instruction.thisN != categorization_instructions.thisTrial.thisN:
            continueRoutine = False
        categorization_instructions_p5.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *categorization_instructions_text_4* updates
            
            # if categorization_instructions_text_4 is starting this frame...
            if categorization_instructions_text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                categorization_instructions_text_4.frameNStart = frameN  # exact frame index
                categorization_instructions_text_4.tStart = t  # local t and not account for scr refresh
                categorization_instructions_text_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(categorization_instructions_text_4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'categorization_instructions_text_4.started')
                # update status
                categorization_instructions_text_4.status = STARTED
                categorization_instructions_text_4.setAutoDraw(True)
            
            # if categorization_instructions_text_4 is active this frame...
            if categorization_instructions_text_4.status == STARTED:
                # update params
                pass
            
            # *turtle_halfcircle_for_categorization_instructions_4* updates
            
            # if turtle_halfcircle_for_categorization_instructions_4 is starting this frame...
            if turtle_halfcircle_for_categorization_instructions_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                turtle_halfcircle_for_categorization_instructions_4.frameNStart = frameN  # exact frame index
                turtle_halfcircle_for_categorization_instructions_4.tStart = t  # local t and not account for scr refresh
                turtle_halfcircle_for_categorization_instructions_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(turtle_halfcircle_for_categorization_instructions_4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'turtle_halfcircle_for_categorization_instructions_4.started')
                # update status
                turtle_halfcircle_for_categorization_instructions_4.status = STARTED
                turtle_halfcircle_for_categorization_instructions_4.setAutoDraw(True)
            
            # if turtle_halfcircle_for_categorization_instructions_4 is active this frame...
            if turtle_halfcircle_for_categorization_instructions_4.status == STARTED:
                # update params
                pass
            
            # *turtle_wedge_for_categorization_instructions_4* updates
            
            # if turtle_wedge_for_categorization_instructions_4 is starting this frame...
            if turtle_wedge_for_categorization_instructions_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                turtle_wedge_for_categorization_instructions_4.frameNStart = frameN  # exact frame index
                turtle_wedge_for_categorization_instructions_4.tStart = t  # local t and not account for scr refresh
                turtle_wedge_for_categorization_instructions_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(turtle_wedge_for_categorization_instructions_4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'turtle_wedge_for_categorization_instructions_4.started')
                # update status
                turtle_wedge_for_categorization_instructions_4.status = STARTED
                turtle_wedge_for_categorization_instructions_4.setAutoDraw(True)
            
            # if turtle_wedge_for_categorization_instructions_4 is active this frame...
            if turtle_wedge_for_categorization_instructions_4.status == STARTED:
                # update params
                pass
            
            # *space_4* updates
            
            # if space_4 is starting this frame...
            if space_4.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                # keep track of start time/frame for later
                space_4.frameNStart = frameN  # exact frame index
                space_4.tStart = t  # local t and not account for scr refresh
                space_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(space_4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'space_4.started')
                # update status
                space_4.status = STARTED
                space_4.setAutoDraw(True)
            
            # if space_4 is active this frame...
            if space_4.status == STARTED:
                # update params
                pass
            
            # *turtle_wedge_boundary_for_categorization_instructions_4* updates
            
            # if turtle_wedge_boundary_for_categorization_instructions_4 is starting this frame...
            if turtle_wedge_boundary_for_categorization_instructions_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                turtle_wedge_boundary_for_categorization_instructions_4.frameNStart = frameN  # exact frame index
                turtle_wedge_boundary_for_categorization_instructions_4.tStart = t  # local t and not account for scr refresh
                turtle_wedge_boundary_for_categorization_instructions_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(turtle_wedge_boundary_for_categorization_instructions_4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'turtle_wedge_boundary_for_categorization_instructions_4.started')
                # update status
                turtle_wedge_boundary_for_categorization_instructions_4.status = STARTED
                turtle_wedge_boundary_for_categorization_instructions_4.setAutoDraw(True)
            
            # if turtle_wedge_boundary_for_categorization_instructions_4 is active this frame...
            if turtle_wedge_boundary_for_categorization_instructions_4.status == STARTED:
                # update params
                pass
            
            # *key_resp_11* updates
            waitOnFlip = False
            
            # if key_resp_11 is starting this frame...
            if key_resp_11.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                # keep track of start time/frame for later
                key_resp_11.frameNStart = frameN  # exact frame index
                key_resp_11.tStart = t  # local t and not account for scr refresh
                key_resp_11.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_11, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_11.started')
                # update status
                key_resp_11.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_11.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_11.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_11.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_11.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_11_allKeys.extend(theseKeys)
                if len(_key_resp_11_allKeys):
                    key_resp_11.keys = _key_resp_11_allKeys[-1].name  # just the last key pressed
                    key_resp_11.rt = _key_resp_11_allKeys[-1].rt
                    key_resp_11.duration = _key_resp_11_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                categorization_instructions_p5.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in categorization_instructions_p5.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "categorization_instructions_p5" ---
        for thisComponent in categorization_instructions_p5.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for categorization_instructions_p5
        categorization_instructions_p5.tStop = globalClock.getTime(format='float')
        categorization_instructions_p5.tStopRefresh = tThisFlipGlobal
        thisExp.addData('categorization_instructions_p5.stopped', categorization_instructions_p5.tStop)
        # check responses
        if key_resp_11.keys in ['', [], None]:  # No response was made
            key_resp_11.keys = None
        categorization_instructions.addData('key_resp_11.keys',key_resp_11.keys)
        if key_resp_11.keys != None:  # we had a response
            categorization_instructions.addData('key_resp_11.rt', key_resp_11.rt)
            categorization_instructions.addData('key_resp_11.duration', key_resp_11.duration)
        # the Routine "categorization_instructions_p5" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "categorization_instructions_p6" ---
        # create an object to store info about Routine categorization_instructions_p6
        categorization_instructions_p6 = data.Routine(
            name='categorization_instructions_p6',
            components=[categorization_instructions_text_5, turtle_halfcircle_for_categorization_instructions_5, turtle_wedge_for_categorization_instructions_5, turtle_wedge_boundary_for_categorization_instructions_5, space_5, key_resp_12],
        )
        categorization_instructions_p6.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        turtle_halfcircle_for_categorization_instructions_5.setVertices(example_turtle_halfcircle_vertices)
        turtle_wedge_for_categorization_instructions_5.setVertices(example_turtle_wedge_vertices)
        # create starting attributes for key_resp_12
        key_resp_12.keys = []
        key_resp_12.rt = []
        _key_resp_12_allKeys = []
        # store start times for categorization_instructions_p6
        categorization_instructions_p6.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        categorization_instructions_p6.tStart = globalClock.getTime(format='float')
        categorization_instructions_p6.status = STARTED
        thisExp.addData('categorization_instructions_p6.started', categorization_instructions_p6.tStart)
        categorization_instructions_p6.maxDuration = None
        # keep track of which components have finished
        categorization_instructions_p6Components = categorization_instructions_p6.components
        for thisComponent in categorization_instructions_p6.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "categorization_instructions_p6" ---
        # if trial has changed, end Routine now
        if isinstance(categorization_instructions, data.TrialHandler2) and thisCategorization_instruction.thisN != categorization_instructions.thisTrial.thisN:
            continueRoutine = False
        categorization_instructions_p6.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *categorization_instructions_text_5* updates
            
            # if categorization_instructions_text_5 is starting this frame...
            if categorization_instructions_text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                categorization_instructions_text_5.frameNStart = frameN  # exact frame index
                categorization_instructions_text_5.tStart = t  # local t and not account for scr refresh
                categorization_instructions_text_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(categorization_instructions_text_5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'categorization_instructions_text_5.started')
                # update status
                categorization_instructions_text_5.status = STARTED
                categorization_instructions_text_5.setAutoDraw(True)
            
            # if categorization_instructions_text_5 is active this frame...
            if categorization_instructions_text_5.status == STARTED:
                # update params
                pass
            
            # *turtle_halfcircle_for_categorization_instructions_5* updates
            
            # if turtle_halfcircle_for_categorization_instructions_5 is starting this frame...
            if turtle_halfcircle_for_categorization_instructions_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                turtle_halfcircle_for_categorization_instructions_5.frameNStart = frameN  # exact frame index
                turtle_halfcircle_for_categorization_instructions_5.tStart = t  # local t and not account for scr refresh
                turtle_halfcircle_for_categorization_instructions_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(turtle_halfcircle_for_categorization_instructions_5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'turtle_halfcircle_for_categorization_instructions_5.started')
                # update status
                turtle_halfcircle_for_categorization_instructions_5.status = STARTED
                turtle_halfcircle_for_categorization_instructions_5.setAutoDraw(True)
            
            # if turtle_halfcircle_for_categorization_instructions_5 is active this frame...
            if turtle_halfcircle_for_categorization_instructions_5.status == STARTED:
                # update params
                pass
            
            # *turtle_wedge_for_categorization_instructions_5* updates
            
            # if turtle_wedge_for_categorization_instructions_5 is starting this frame...
            if turtle_wedge_for_categorization_instructions_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                turtle_wedge_for_categorization_instructions_5.frameNStart = frameN  # exact frame index
                turtle_wedge_for_categorization_instructions_5.tStart = t  # local t and not account for scr refresh
                turtle_wedge_for_categorization_instructions_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(turtle_wedge_for_categorization_instructions_5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'turtle_wedge_for_categorization_instructions_5.started')
                # update status
                turtle_wedge_for_categorization_instructions_5.status = STARTED
                turtle_wedge_for_categorization_instructions_5.setAutoDraw(True)
            
            # if turtle_wedge_for_categorization_instructions_5 is active this frame...
            if turtle_wedge_for_categorization_instructions_5.status == STARTED:
                # update params
                pass
            
            # *turtle_wedge_boundary_for_categorization_instructions_5* updates
            
            # if turtle_wedge_boundary_for_categorization_instructions_5 is starting this frame...
            if turtle_wedge_boundary_for_categorization_instructions_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                turtle_wedge_boundary_for_categorization_instructions_5.frameNStart = frameN  # exact frame index
                turtle_wedge_boundary_for_categorization_instructions_5.tStart = t  # local t and not account for scr refresh
                turtle_wedge_boundary_for_categorization_instructions_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(turtle_wedge_boundary_for_categorization_instructions_5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'turtle_wedge_boundary_for_categorization_instructions_5.started')
                # update status
                turtle_wedge_boundary_for_categorization_instructions_5.status = STARTED
                turtle_wedge_boundary_for_categorization_instructions_5.setAutoDraw(True)
            
            # if turtle_wedge_boundary_for_categorization_instructions_5 is active this frame...
            if turtle_wedge_boundary_for_categorization_instructions_5.status == STARTED:
                # update params
                pass
            
            # *space_5* updates
            
            # if space_5 is starting this frame...
            if space_5.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                # keep track of start time/frame for later
                space_5.frameNStart = frameN  # exact frame index
                space_5.tStart = t  # local t and not account for scr refresh
                space_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(space_5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'space_5.started')
                # update status
                space_5.status = STARTED
                space_5.setAutoDraw(True)
            
            # if space_5 is active this frame...
            if space_5.status == STARTED:
                # update params
                pass
            
            # *key_resp_12* updates
            waitOnFlip = False
            
            # if key_resp_12 is starting this frame...
            if key_resp_12.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                # keep track of start time/frame for later
                key_resp_12.frameNStart = frameN  # exact frame index
                key_resp_12.tStart = t  # local t and not account for scr refresh
                key_resp_12.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_12, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_12.started')
                # update status
                key_resp_12.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_12.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_12.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_12.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_12.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_12_allKeys.extend(theseKeys)
                if len(_key_resp_12_allKeys):
                    key_resp_12.keys = _key_resp_12_allKeys[-1].name  # just the last key pressed
                    key_resp_12.rt = _key_resp_12_allKeys[-1].rt
                    key_resp_12.duration = _key_resp_12_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                categorization_instructions_p6.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in categorization_instructions_p6.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "categorization_instructions_p6" ---
        for thisComponent in categorization_instructions_p6.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for categorization_instructions_p6
        categorization_instructions_p6.tStop = globalClock.getTime(format='float')
        categorization_instructions_p6.tStopRefresh = tThisFlipGlobal
        thisExp.addData('categorization_instructions_p6.stopped', categorization_instructions_p6.tStop)
        # check responses
        if key_resp_12.keys in ['', [], None]:  # No response was made
            key_resp_12.keys = None
        categorization_instructions.addData('key_resp_12.keys',key_resp_12.keys)
        if key_resp_12.keys != None:  # we had a response
            categorization_instructions.addData('key_resp_12.rt', key_resp_12.rt)
            categorization_instructions.addData('key_resp_12.duration', key_resp_12.duration)
        # the Routine "categorization_instructions_p6" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "categorization_instructions_p7" ---
        # create an object to store info about Routine categorization_instructions_p7
        categorization_instructions_p7 = data.Routine(
            name='categorization_instructions_p7',
            components=[categorization_instructions_text_6, turtle_halfcircle_for_categorization_instructions_6, turtle_wedge_for_categorization_instructions_6, turtle_wedge_boundary_for_categorization_instructions_6, space_6, key_resp_13],
        )
        categorization_instructions_p7.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        turtle_halfcircle_for_categorization_instructions_6.setVertices(example_turtle_halfcircle_vertices)
        turtle_wedge_for_categorization_instructions_6.setVertices(example_turtle_wedge_vertices)
        # create starting attributes for key_resp_13
        key_resp_13.keys = []
        key_resp_13.rt = []
        _key_resp_13_allKeys = []
        # store start times for categorization_instructions_p7
        categorization_instructions_p7.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        categorization_instructions_p7.tStart = globalClock.getTime(format='float')
        categorization_instructions_p7.status = STARTED
        thisExp.addData('categorization_instructions_p7.started', categorization_instructions_p7.tStart)
        categorization_instructions_p7.maxDuration = None
        # keep track of which components have finished
        categorization_instructions_p7Components = categorization_instructions_p7.components
        for thisComponent in categorization_instructions_p7.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "categorization_instructions_p7" ---
        # if trial has changed, end Routine now
        if isinstance(categorization_instructions, data.TrialHandler2) and thisCategorization_instruction.thisN != categorization_instructions.thisTrial.thisN:
            continueRoutine = False
        categorization_instructions_p7.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *categorization_instructions_text_6* updates
            
            # if categorization_instructions_text_6 is starting this frame...
            if categorization_instructions_text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                categorization_instructions_text_6.frameNStart = frameN  # exact frame index
                categorization_instructions_text_6.tStart = t  # local t and not account for scr refresh
                categorization_instructions_text_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(categorization_instructions_text_6, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'categorization_instructions_text_6.started')
                # update status
                categorization_instructions_text_6.status = STARTED
                categorization_instructions_text_6.setAutoDraw(True)
            
            # if categorization_instructions_text_6 is active this frame...
            if categorization_instructions_text_6.status == STARTED:
                # update params
                pass
            
            # *turtle_halfcircle_for_categorization_instructions_6* updates
            
            # if turtle_halfcircle_for_categorization_instructions_6 is starting this frame...
            if turtle_halfcircle_for_categorization_instructions_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                turtle_halfcircle_for_categorization_instructions_6.frameNStart = frameN  # exact frame index
                turtle_halfcircle_for_categorization_instructions_6.tStart = t  # local t and not account for scr refresh
                turtle_halfcircle_for_categorization_instructions_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(turtle_halfcircle_for_categorization_instructions_6, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'turtle_halfcircle_for_categorization_instructions_6.started')
                # update status
                turtle_halfcircle_for_categorization_instructions_6.status = STARTED
                turtle_halfcircle_for_categorization_instructions_6.setAutoDraw(True)
            
            # if turtle_halfcircle_for_categorization_instructions_6 is active this frame...
            if turtle_halfcircle_for_categorization_instructions_6.status == STARTED:
                # update params
                pass
            
            # *turtle_wedge_for_categorization_instructions_6* updates
            
            # if turtle_wedge_for_categorization_instructions_6 is starting this frame...
            if turtle_wedge_for_categorization_instructions_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                turtle_wedge_for_categorization_instructions_6.frameNStart = frameN  # exact frame index
                turtle_wedge_for_categorization_instructions_6.tStart = t  # local t and not account for scr refresh
                turtle_wedge_for_categorization_instructions_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(turtle_wedge_for_categorization_instructions_6, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'turtle_wedge_for_categorization_instructions_6.started')
                # update status
                turtle_wedge_for_categorization_instructions_6.status = STARTED
                turtle_wedge_for_categorization_instructions_6.setAutoDraw(True)
            
            # if turtle_wedge_for_categorization_instructions_6 is active this frame...
            if turtle_wedge_for_categorization_instructions_6.status == STARTED:
                # update params
                pass
            
            # *turtle_wedge_boundary_for_categorization_instructions_6* updates
            
            # if turtle_wedge_boundary_for_categorization_instructions_6 is starting this frame...
            if turtle_wedge_boundary_for_categorization_instructions_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                turtle_wedge_boundary_for_categorization_instructions_6.frameNStart = frameN  # exact frame index
                turtle_wedge_boundary_for_categorization_instructions_6.tStart = t  # local t and not account for scr refresh
                turtle_wedge_boundary_for_categorization_instructions_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(turtle_wedge_boundary_for_categorization_instructions_6, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'turtle_wedge_boundary_for_categorization_instructions_6.started')
                # update status
                turtle_wedge_boundary_for_categorization_instructions_6.status = STARTED
                turtle_wedge_boundary_for_categorization_instructions_6.setAutoDraw(True)
            
            # if turtle_wedge_boundary_for_categorization_instructions_6 is active this frame...
            if turtle_wedge_boundary_for_categorization_instructions_6.status == STARTED:
                # update params
                pass
            
            # *space_6* updates
            
            # if space_6 is starting this frame...
            if space_6.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                # keep track of start time/frame for later
                space_6.frameNStart = frameN  # exact frame index
                space_6.tStart = t  # local t and not account for scr refresh
                space_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(space_6, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'space_6.started')
                # update status
                space_6.status = STARTED
                space_6.setAutoDraw(True)
            
            # if space_6 is active this frame...
            if space_6.status == STARTED:
                # update params
                pass
            
            # *key_resp_13* updates
            waitOnFlip = False
            
            # if key_resp_13 is starting this frame...
            if key_resp_13.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                # keep track of start time/frame for later
                key_resp_13.frameNStart = frameN  # exact frame index
                key_resp_13.tStart = t  # local t and not account for scr refresh
                key_resp_13.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_13, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_13.started')
                # update status
                key_resp_13.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_13.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_13.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_13.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_13.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_13_allKeys.extend(theseKeys)
                if len(_key_resp_13_allKeys):
                    key_resp_13.keys = _key_resp_13_allKeys[-1].name  # just the last key pressed
                    key_resp_13.rt = _key_resp_13_allKeys[-1].rt
                    key_resp_13.duration = _key_resp_13_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                categorization_instructions_p7.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in categorization_instructions_p7.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "categorization_instructions_p7" ---
        for thisComponent in categorization_instructions_p7.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for categorization_instructions_p7
        categorization_instructions_p7.tStop = globalClock.getTime(format='float')
        categorization_instructions_p7.tStopRefresh = tThisFlipGlobal
        thisExp.addData('categorization_instructions_p7.stopped', categorization_instructions_p7.tStop)
        # check responses
        if key_resp_13.keys in ['', [], None]:  # No response was made
            key_resp_13.keys = None
        categorization_instructions.addData('key_resp_13.keys',key_resp_13.keys)
        if key_resp_13.keys != None:  # we had a response
            categorization_instructions.addData('key_resp_13.rt', key_resp_13.rt)
            categorization_instructions.addData('key_resp_13.duration', key_resp_13.duration)
        # the Routine "categorization_instructions_p7" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "categorization_instructions_p8" ---
        # create an object to store info about Routine categorization_instructions_p8
        categorization_instructions_p8 = data.Routine(
            name='categorization_instructions_p8',
            components=[space_to_begin_exp, key_resp_14],
        )
        categorization_instructions_p8.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # create starting attributes for key_resp_14
        key_resp_14.keys = []
        key_resp_14.rt = []
        _key_resp_14_allKeys = []
        # store start times for categorization_instructions_p8
        categorization_instructions_p8.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        categorization_instructions_p8.tStart = globalClock.getTime(format='float')
        categorization_instructions_p8.status = STARTED
        thisExp.addData('categorization_instructions_p8.started', categorization_instructions_p8.tStart)
        categorization_instructions_p8.maxDuration = None
        # keep track of which components have finished
        categorization_instructions_p8Components = categorization_instructions_p8.components
        for thisComponent in categorization_instructions_p8.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "categorization_instructions_p8" ---
        # if trial has changed, end Routine now
        if isinstance(categorization_instructions, data.TrialHandler2) and thisCategorization_instruction.thisN != categorization_instructions.thisTrial.thisN:
            continueRoutine = False
        categorization_instructions_p8.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *space_to_begin_exp* updates
            
            # if space_to_begin_exp is starting this frame...
            if space_to_begin_exp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                space_to_begin_exp.frameNStart = frameN  # exact frame index
                space_to_begin_exp.tStart = t  # local t and not account for scr refresh
                space_to_begin_exp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(space_to_begin_exp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'space_to_begin_exp.started')
                # update status
                space_to_begin_exp.status = STARTED
                space_to_begin_exp.setAutoDraw(True)
            
            # if space_to_begin_exp is active this frame...
            if space_to_begin_exp.status == STARTED:
                # update params
                pass
            
            # *key_resp_14* updates
            waitOnFlip = False
            
            # if key_resp_14 is starting this frame...
            if key_resp_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_14.frameNStart = frameN  # exact frame index
                key_resp_14.tStart = t  # local t and not account for scr refresh
                key_resp_14.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_14, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_14.started')
                # update status
                key_resp_14.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_14.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_14.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_14.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_14.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_14_allKeys.extend(theseKeys)
                if len(_key_resp_14_allKeys):
                    key_resp_14.keys = _key_resp_14_allKeys[-1].name  # just the last key pressed
                    key_resp_14.rt = _key_resp_14_allKeys[-1].rt
                    key_resp_14.duration = _key_resp_14_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                categorization_instructions_p8.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in categorization_instructions_p8.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "categorization_instructions_p8" ---
        for thisComponent in categorization_instructions_p8.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for categorization_instructions_p8
        categorization_instructions_p8.tStop = globalClock.getTime(format='float')
        categorization_instructions_p8.tStopRefresh = tThisFlipGlobal
        thisExp.addData('categorization_instructions_p8.stopped', categorization_instructions_p8.tStop)
        # check responses
        if key_resp_14.keys in ['', [], None]:  # No response was made
            key_resp_14.keys = None
        categorization_instructions.addData('key_resp_14.keys',key_resp_14.keys)
        if key_resp_14.keys != None:  # we had a response
            categorization_instructions.addData('key_resp_14.rt', key_resp_14.rt)
            categorization_instructions.addData('key_resp_14.duration', key_resp_14.duration)
        # the Routine "categorization_instructions_p8" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    # completed 0.0 repeats of 'categorization_instructions'
    
    
    # set up handler to look after randomisation of conditions etc
    training = data.TrialHandler2(
        name='training',
        nReps=num_train_blocks, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('stim/stim_train.csv'), 
        seed=None, 
    )
    thisExp.addLoop(training)  # add the loop to the experiment
    thisTraining = training.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTraining.rgb)
    if thisTraining != None:
        for paramName in thisTraining:
            globals()[paramName] = thisTraining[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisTraining in training:
        currentLoop = training
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisTraining.rgb)
        if thisTraining != None:
            for paramName in thisTraining:
                globals()[paramName] = thisTraining[paramName]
        
        # --- Prepare to start Routine "fixation_cross" ---
        # create an object to store info about Routine fixation_cross
        fixation_cross = data.Routine(
            name='fixation_cross',
            components=[fixation_cross_1],
        )
        fixation_cross.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for fixation_cross
        fixation_cross.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        fixation_cross.tStart = globalClock.getTime(format='float')
        fixation_cross.status = STARTED
        thisExp.addData('fixation_cross.started', fixation_cross.tStart)
        fixation_cross.maxDuration = None
        # keep track of which components have finished
        fixation_crossComponents = fixation_cross.components
        for thisComponent in fixation_cross.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "fixation_cross" ---
        # if trial has changed, end Routine now
        if isinstance(training, data.TrialHandler2) and thisTraining.thisN != training.thisTrial.thisN:
            continueRoutine = False
        fixation_cross.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.4:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixation_cross_1* updates
            
            # if fixation_cross_1 is starting this frame...
            if fixation_cross_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation_cross_1.frameNStart = frameN  # exact frame index
                fixation_cross_1.tStart = t  # local t and not account for scr refresh
                fixation_cross_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation_cross_1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation_cross_1.started')
                # update status
                fixation_cross_1.status = STARTED
                fixation_cross_1.setAutoDraw(True)
            
            # if fixation_cross_1 is active this frame...
            if fixation_cross_1.status == STARTED:
                # update params
                pass
            
            # if fixation_cross_1 is stopping this frame...
            if fixation_cross_1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation_cross_1.tStartRefresh + .4-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation_cross_1.tStop = t  # not accounting for scr refresh
                    fixation_cross_1.tStopRefresh = tThisFlipGlobal  # on global time
                    fixation_cross_1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixation_cross_1.stopped')
                    # update status
                    fixation_cross_1.status = FINISHED
                    fixation_cross_1.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                fixation_cross.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fixation_cross.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "fixation_cross" ---
        for thisComponent in fixation_cross.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for fixation_cross
        fixation_cross.tStop = globalClock.getTime(format='float')
        fixation_cross.tStopRefresh = tThisFlipGlobal
        thisExp.addData('fixation_cross.stopped', fixation_cross.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if fixation_cross.maxDurationReached:
            routineTimer.addTime(-fixation_cross.maxDuration)
        elif fixation_cross.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.400000)
        
        # --- Prepare to start Routine "blank" ---
        # create an object to store info about Routine blank
        blank = data.Routine(
            name='blank',
            components=[text_2],
        )
        blank.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for blank
        blank.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        blank.tStart = globalClock.getTime(format='float')
        blank.status = STARTED
        thisExp.addData('blank.started', blank.tStart)
        blank.maxDuration = None
        # keep track of which components have finished
        blankComponents = blank.components
        for thisComponent in blank.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "blank" ---
        # if trial has changed, end Routine now
        if isinstance(training, data.TrialHandler2) and thisTraining.thisN != training.thisTrial.thisN:
            continueRoutine = False
        blank.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.2:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_2* updates
            
            # if text_2 is starting this frame...
            if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_2.frameNStart = frameN  # exact frame index
                text_2.tStart = t  # local t and not account for scr refresh
                text_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_2.started')
                # update status
                text_2.status = STARTED
                text_2.setAutoDraw(True)
            
            # if text_2 is active this frame...
            if text_2.status == STARTED:
                # update params
                pass
            
            # if text_2 is stopping this frame...
            if text_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_2.tStartRefresh + .2-frameTolerance:
                    # keep track of stop time/frame for later
                    text_2.tStop = t  # not accounting for scr refresh
                    text_2.tStopRefresh = tThisFlipGlobal  # on global time
                    text_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_2.stopped')
                    # update status
                    text_2.status = FINISHED
                    text_2.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                blank.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in blank.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "blank" ---
        for thisComponent in blank.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for blank
        blank.tStop = globalClock.getTime(format='float')
        blank.tStopRefresh = tThisFlipGlobal
        thisExp.addData('blank.stopped', blank.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if blank.maxDurationReached:
            routineTimer.addTime(-blank.maxDuration)
        elif blank.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.200000)
        
        # --- Prepare to start Routine "get_turtle_params_training" ---
        # create an object to store info about Routine get_turtle_params_training
        get_turtle_params_training = data.Routine(
            name='get_turtle_params_training',
            components=[],
        )
        get_turtle_params_training.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from get_turtle_params
        turtle_halfcircle_vertices = get_turtle_halfcircle_vertices(radius)
        turtle_wedge_vertices = get_turtle_wedge_vertices(angle)
        
        if category=="A":
            corr_resp_tmp=category_A_label
        elif category=="B":
            corr_resp_tmp=category_B_label
        # store start times for get_turtle_params_training
        get_turtle_params_training.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        get_turtle_params_training.tStart = globalClock.getTime(format='float')
        get_turtle_params_training.status = STARTED
        thisExp.addData('get_turtle_params_training.started', get_turtle_params_training.tStart)
        get_turtle_params_training.maxDuration = None
        # keep track of which components have finished
        get_turtle_params_trainingComponents = get_turtle_params_training.components
        for thisComponent in get_turtle_params_training.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "get_turtle_params_training" ---
        # if trial has changed, end Routine now
        if isinstance(training, data.TrialHandler2) and thisTraining.thisN != training.thisTrial.thisN:
            continueRoutine = False
        get_turtle_params_training.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from get_turtle_params
            #turtle_green = visual.Pie(
            #    win,
            #    fillColor=[0, 128, 0],
            #    colorSpace='rgb255',
            #    start=0,
            #    end=90,
            #    radius=100,
            #    pos=(0,200)
            #)
            #turtle_yellow = visual.Pie(
            #    win,
            #    fillColor=[255, 192, 0],
            #    lineColor=[255, 192, 0],
            #    colorSpace='rgb255',
            #    start=0,
            #    end=90,
            #    radius=200,
            #    pos=(0,200)
            #)
            #
            #turtle_yellow = visual.Pie(
            #    win=win,
            #    fillColor=[0, 0, 0],
            #    lineColor=[-1, -1, -1],
            #    start=0,
            #    end=90,
            #    radius=200,
            #    pos=(0,200)
            #)
            #
            #turtle_green.draw()
            #turtle_yellow.draw()
            #win.flip()
            #
            #circle = visual.Circle(
            #    win=win,
            #    units="pix",
            #    radius=150,
            #    fillColor=[0, 0, 0],
            #    lineColor=[-1, -1, -1]
            #)
            #
            #circle.draw()
            
            #win.flip()
            
            
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                get_turtle_params_training.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in get_turtle_params_training.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "get_turtle_params_training" ---
        for thisComponent in get_turtle_params_training.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for get_turtle_params_training
        get_turtle_params_training.tStop = globalClock.getTime(format='float')
        get_turtle_params_training.tStopRefresh = tThisFlipGlobal
        thisExp.addData('get_turtle_params_training.stopped', get_turtle_params_training.tStop)
        # the Routine "get_turtle_params_training" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "training_response" ---
        # create an object to store info about Routine training_response
        training_response = data.Routine(
            name='training_response',
            components=[key_resp_training, turtle_halfcircle, turtle_wedge, turtle_wedge_boundary, training_prompt],
        )
        training_response.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # create starting attributes for key_resp_training
        key_resp_training.keys = []
        key_resp_training.rt = []
        _key_resp_training_allKeys = []
        turtle_halfcircle.setVertices(turtle_halfcircle_vertices)
        turtle_wedge.setVertices(turtle_wedge_vertices)
        training_prompt.setText('Is this turtle in Species F or Species J? \n\nF - Species F, J - Species J')
        # store start times for training_response
        training_response.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        training_response.tStart = globalClock.getTime(format='float')
        training_response.status = STARTED
        thisExp.addData('training_response.started', training_response.tStart)
        training_response.maxDuration = None
        # keep track of which components have finished
        training_responseComponents = training_response.components
        for thisComponent in training_response.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "training_response" ---
        # if trial has changed, end Routine now
        if isinstance(training, data.TrialHandler2) and thisTraining.thisN != training.thisTrial.thisN:
            continueRoutine = False
        training_response.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *key_resp_training* updates
            waitOnFlip = False
            
            # if key_resp_training is starting this frame...
            if key_resp_training.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_training.frameNStart = frameN  # exact frame index
                key_resp_training.tStart = t  # local t and not account for scr refresh
                key_resp_training.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_training, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_training.started')
                # update status
                key_resp_training.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_training.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_training.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_training.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_training.getKeys(keyList=['f','j'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_training_allKeys.extend(theseKeys)
                if len(_key_resp_training_allKeys):
                    key_resp_training.keys = _key_resp_training_allKeys[-1].name  # just the last key pressed
                    key_resp_training.rt = _key_resp_training_allKeys[-1].rt
                    key_resp_training.duration = _key_resp_training_allKeys[-1].duration
                    # was this correct?
                    if (key_resp_training.keys == str(corr_resp_tmp)) or (key_resp_training.keys == corr_resp_tmp):
                        key_resp_training.corr = 1
                    else:
                        key_resp_training.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # *turtle_halfcircle* updates
            
            # if turtle_halfcircle is starting this frame...
            if turtle_halfcircle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                turtle_halfcircle.frameNStart = frameN  # exact frame index
                turtle_halfcircle.tStart = t  # local t and not account for scr refresh
                turtle_halfcircle.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(turtle_halfcircle, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'turtle_halfcircle.started')
                # update status
                turtle_halfcircle.status = STARTED
                turtle_halfcircle.setAutoDraw(True)
            
            # if turtle_halfcircle is active this frame...
            if turtle_halfcircle.status == STARTED:
                # update params
                pass
            
            # *turtle_wedge* updates
            
            # if turtle_wedge is starting this frame...
            if turtle_wedge.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                turtle_wedge.frameNStart = frameN  # exact frame index
                turtle_wedge.tStart = t  # local t and not account for scr refresh
                turtle_wedge.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(turtle_wedge, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'turtle_wedge.started')
                # update status
                turtle_wedge.status = STARTED
                turtle_wedge.setAutoDraw(True)
            
            # if turtle_wedge is active this frame...
            if turtle_wedge.status == STARTED:
                # update params
                pass
            
            # *turtle_wedge_boundary* updates
            
            # if turtle_wedge_boundary is starting this frame...
            if turtle_wedge_boundary.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                turtle_wedge_boundary.frameNStart = frameN  # exact frame index
                turtle_wedge_boundary.tStart = t  # local t and not account for scr refresh
                turtle_wedge_boundary.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(turtle_wedge_boundary, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'turtle_wedge_boundary.started')
                # update status
                turtle_wedge_boundary.status = STARTED
                turtle_wedge_boundary.setAutoDraw(True)
            
            # if turtle_wedge_boundary is active this frame...
            if turtle_wedge_boundary.status == STARTED:
                # update params
                pass
            
            # *training_prompt* updates
            
            # if training_prompt is starting this frame...
            if training_prompt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                training_prompt.frameNStart = frameN  # exact frame index
                training_prompt.tStart = t  # local t and not account for scr refresh
                training_prompt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(training_prompt, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'training_prompt.started')
                # update status
                training_prompt.status = STARTED
                training_prompt.setAutoDraw(True)
            
            # if training_prompt is active this frame...
            if training_prompt.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                training_response.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in training_response.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "training_response" ---
        for thisComponent in training_response.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for training_response
        training_response.tStop = globalClock.getTime(format='float')
        training_response.tStopRefresh = tThisFlipGlobal
        thisExp.addData('training_response.stopped', training_response.tStop)
        # check responses
        if key_resp_training.keys in ['', [], None]:  # No response was made
            key_resp_training.keys = None
            # was no response the correct answer?!
            if str(corr_resp_tmp).lower() == 'none':
               key_resp_training.corr = 1;  # correct non-response
            else:
               key_resp_training.corr = 0;  # failed to respond (incorrectly)
        # store data for training (TrialHandler)
        training.addData('key_resp_training.keys',key_resp_training.keys)
        training.addData('key_resp_training.corr', key_resp_training.corr)
        if key_resp_training.keys != None:  # we had a response
            training.addData('key_resp_training.rt', key_resp_training.rt)
            training.addData('key_resp_training.duration', key_resp_training.duration)
        # the Routine "training_response" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "train_feedback_code_checks" ---
        # create an object to store info about Routine train_feedback_code_checks
        train_feedback_code_checks = data.Routine(
            name='train_feedback_code_checks',
            components=[],
        )
        train_feedback_code_checks.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from train_feedback_text_code_2
        if key_resp_training.corr==1:
            train_feedback_dur=1;
            train_feedback_col="#008000"
            if category=="A":
                train_feedback_text="You were correct! This turtle belongs to species " + category_A_label.upper() + "."
            elif category=="B":
                train_feedback_text="You were correct! This turtle belongs to species " + category_B_label.upper() + "."
        elif key_resp_training.corr==0:
            train_feedback_dur=2;
            train_feedback_col="#FF0000"
            if category=="A":
                train_feedback_text="You were incorrect. This turtle belongs to species " + category_A_label.upper() + "."
            elif category=="B":
                train_feedback_text="You were incorrect. This turtle belongs to species " + category_B_label.upper() + "."
        # store start times for train_feedback_code_checks
        train_feedback_code_checks.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        train_feedback_code_checks.tStart = globalClock.getTime(format='float')
        train_feedback_code_checks.status = STARTED
        thisExp.addData('train_feedback_code_checks.started', train_feedback_code_checks.tStart)
        train_feedback_code_checks.maxDuration = None
        # keep track of which components have finished
        train_feedback_code_checksComponents = train_feedback_code_checks.components
        for thisComponent in train_feedback_code_checks.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "train_feedback_code_checks" ---
        # if trial has changed, end Routine now
        if isinstance(training, data.TrialHandler2) and thisTraining.thisN != training.thisTrial.thisN:
            continueRoutine = False
        train_feedback_code_checks.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                train_feedback_code_checks.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in train_feedback_code_checks.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "train_feedback_code_checks" ---
        for thisComponent in train_feedback_code_checks.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for train_feedback_code_checks
        train_feedback_code_checks.tStop = globalClock.getTime(format='float')
        train_feedback_code_checks.tStopRefresh = tThisFlipGlobal
        thisExp.addData('train_feedback_code_checks.stopped', train_feedback_code_checks.tStop)
        # the Routine "train_feedback_code_checks" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "training_feedback" ---
        # create an object to store info about Routine training_feedback
        training_feedback = data.Routine(
            name='training_feedback',
            components=[train_feedback_text_display, turtle_halfcircle_for_feedback, turtle_wedge_for_feedback, turtle_wedge_boundary_for_feedback],
        )
        training_feedback.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        train_feedback_text_display.setColor(train_feedback_col, colorSpace='rgb')
        train_feedback_text_display.setText(train_feedback_text)
        turtle_halfcircle_for_feedback.setVertices(turtle_halfcircle_vertices)
        turtle_wedge_for_feedback.setVertices(turtle_wedge_vertices)
        # store start times for training_feedback
        training_feedback.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        training_feedback.tStart = globalClock.getTime(format='float')
        training_feedback.status = STARTED
        thisExp.addData('training_feedback.started', training_feedback.tStart)
        training_feedback.maxDuration = None
        # keep track of which components have finished
        training_feedbackComponents = training_feedback.components
        for thisComponent in training_feedback.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "training_feedback" ---
        # if trial has changed, end Routine now
        if isinstance(training, data.TrialHandler2) and thisTraining.thisN != training.thisTrial.thisN:
            continueRoutine = False
        training_feedback.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *train_feedback_text_display* updates
            
            # if train_feedback_text_display is starting this frame...
            if train_feedback_text_display.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                train_feedback_text_display.frameNStart = frameN  # exact frame index
                train_feedback_text_display.tStart = t  # local t and not account for scr refresh
                train_feedback_text_display.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(train_feedback_text_display, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'train_feedback_text_display.started')
                # update status
                train_feedback_text_display.status = STARTED
                train_feedback_text_display.setAutoDraw(True)
            
            # if train_feedback_text_display is active this frame...
            if train_feedback_text_display.status == STARTED:
                # update params
                pass
            
            # if train_feedback_text_display is stopping this frame...
            if train_feedback_text_display.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > train_feedback_text_display.tStartRefresh + train_feedback_dur-frameTolerance:
                    # keep track of stop time/frame for later
                    train_feedback_text_display.tStop = t  # not accounting for scr refresh
                    train_feedback_text_display.tStopRefresh = tThisFlipGlobal  # on global time
                    train_feedback_text_display.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'train_feedback_text_display.stopped')
                    # update status
                    train_feedback_text_display.status = FINISHED
                    train_feedback_text_display.setAutoDraw(False)
            
            # *turtle_halfcircle_for_feedback* updates
            
            # if turtle_halfcircle_for_feedback is starting this frame...
            if turtle_halfcircle_for_feedback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                turtle_halfcircle_for_feedback.frameNStart = frameN  # exact frame index
                turtle_halfcircle_for_feedback.tStart = t  # local t and not account for scr refresh
                turtle_halfcircle_for_feedback.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(turtle_halfcircle_for_feedback, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'turtle_halfcircle_for_feedback.started')
                # update status
                turtle_halfcircle_for_feedback.status = STARTED
                turtle_halfcircle_for_feedback.setAutoDraw(True)
            
            # if turtle_halfcircle_for_feedback is active this frame...
            if turtle_halfcircle_for_feedback.status == STARTED:
                # update params
                pass
            
            # if turtle_halfcircle_for_feedback is stopping this frame...
            if turtle_halfcircle_for_feedback.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > turtle_halfcircle_for_feedback.tStartRefresh + train_feedback_dur-frameTolerance:
                    # keep track of stop time/frame for later
                    turtle_halfcircle_for_feedback.tStop = t  # not accounting for scr refresh
                    turtle_halfcircle_for_feedback.tStopRefresh = tThisFlipGlobal  # on global time
                    turtle_halfcircle_for_feedback.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'turtle_halfcircle_for_feedback.stopped')
                    # update status
                    turtle_halfcircle_for_feedback.status = FINISHED
                    turtle_halfcircle_for_feedback.setAutoDraw(False)
            
            # *turtle_wedge_for_feedback* updates
            
            # if turtle_wedge_for_feedback is starting this frame...
            if turtle_wedge_for_feedback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                turtle_wedge_for_feedback.frameNStart = frameN  # exact frame index
                turtle_wedge_for_feedback.tStart = t  # local t and not account for scr refresh
                turtle_wedge_for_feedback.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(turtle_wedge_for_feedback, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'turtle_wedge_for_feedback.started')
                # update status
                turtle_wedge_for_feedback.status = STARTED
                turtle_wedge_for_feedback.setAutoDraw(True)
            
            # if turtle_wedge_for_feedback is active this frame...
            if turtle_wedge_for_feedback.status == STARTED:
                # update params
                pass
            
            # if turtle_wedge_for_feedback is stopping this frame...
            if turtle_wedge_for_feedback.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > turtle_wedge_for_feedback.tStartRefresh + train_feedback_dur-frameTolerance:
                    # keep track of stop time/frame for later
                    turtle_wedge_for_feedback.tStop = t  # not accounting for scr refresh
                    turtle_wedge_for_feedback.tStopRefresh = tThisFlipGlobal  # on global time
                    turtle_wedge_for_feedback.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'turtle_wedge_for_feedback.stopped')
                    # update status
                    turtle_wedge_for_feedback.status = FINISHED
                    turtle_wedge_for_feedback.setAutoDraw(False)
            
            # *turtle_wedge_boundary_for_feedback* updates
            
            # if turtle_wedge_boundary_for_feedback is starting this frame...
            if turtle_wedge_boundary_for_feedback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                turtle_wedge_boundary_for_feedback.frameNStart = frameN  # exact frame index
                turtle_wedge_boundary_for_feedback.tStart = t  # local t and not account for scr refresh
                turtle_wedge_boundary_for_feedback.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(turtle_wedge_boundary_for_feedback, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'turtle_wedge_boundary_for_feedback.started')
                # update status
                turtle_wedge_boundary_for_feedback.status = STARTED
                turtle_wedge_boundary_for_feedback.setAutoDraw(True)
            
            # if turtle_wedge_boundary_for_feedback is active this frame...
            if turtle_wedge_boundary_for_feedback.status == STARTED:
                # update params
                pass
            
            # if turtle_wedge_boundary_for_feedback is stopping this frame...
            if turtle_wedge_boundary_for_feedback.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > turtle_wedge_boundary_for_feedback.tStartRefresh + train_feedback_dur-frameTolerance:
                    # keep track of stop time/frame for later
                    turtle_wedge_boundary_for_feedback.tStop = t  # not accounting for scr refresh
                    turtle_wedge_boundary_for_feedback.tStopRefresh = tThisFlipGlobal  # on global time
                    turtle_wedge_boundary_for_feedback.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'turtle_wedge_boundary_for_feedback.stopped')
                    # update status
                    turtle_wedge_boundary_for_feedback.status = FINISHED
                    turtle_wedge_boundary_for_feedback.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                training_feedback.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in training_feedback.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "training_feedback" ---
        for thisComponent in training_feedback.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for training_feedback
        training_feedback.tStop = globalClock.getTime(format='float')
        training_feedback.tStopRefresh = tThisFlipGlobal
        thisExp.addData('training_feedback.stopped', training_feedback.tStop)
        # the Routine "training_feedback" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "blank" ---
        # create an object to store info about Routine blank
        blank = data.Routine(
            name='blank',
            components=[text_2],
        )
        blank.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for blank
        blank.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        blank.tStart = globalClock.getTime(format='float')
        blank.status = STARTED
        thisExp.addData('blank.started', blank.tStart)
        blank.maxDuration = None
        # keep track of which components have finished
        blankComponents = blank.components
        for thisComponent in blank.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "blank" ---
        # if trial has changed, end Routine now
        if isinstance(training, data.TrialHandler2) and thisTraining.thisN != training.thisTrial.thisN:
            continueRoutine = False
        blank.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.2:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_2* updates
            
            # if text_2 is starting this frame...
            if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_2.frameNStart = frameN  # exact frame index
                text_2.tStart = t  # local t and not account for scr refresh
                text_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_2.started')
                # update status
                text_2.status = STARTED
                text_2.setAutoDraw(True)
            
            # if text_2 is active this frame...
            if text_2.status == STARTED:
                # update params
                pass
            
            # if text_2 is stopping this frame...
            if text_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_2.tStartRefresh + .2-frameTolerance:
                    # keep track of stop time/frame for later
                    text_2.tStop = t  # not accounting for scr refresh
                    text_2.tStopRefresh = tThisFlipGlobal  # on global time
                    text_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_2.stopped')
                    # update status
                    text_2.status = FINISHED
                    text_2.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                blank.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in blank.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "blank" ---
        for thisComponent in blank.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for blank
        blank.tStop = globalClock.getTime(format='float')
        blank.tStopRefresh = tThisFlipGlobal
        thisExp.addData('blank.stopped', blank.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if blank.maxDurationReached:
            routineTimer.addTime(-blank.maxDuration)
        elif blank.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.200000)
        
        # --- Prepare to start Routine "del_corr_resp" ---
        # create an object to store info about Routine del_corr_resp
        del_corr_resp = data.Routine(
            name='del_corr_resp',
            components=[],
        )
        del_corr_resp.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from delete_corr_resp_tmp_code_
        del corr_resp_tmp # bad programming but for safety deleting this
        # store start times for del_corr_resp
        del_corr_resp.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        del_corr_resp.tStart = globalClock.getTime(format='float')
        del_corr_resp.status = STARTED
        thisExp.addData('del_corr_resp.started', del_corr_resp.tStart)
        del_corr_resp.maxDuration = None
        # keep track of which components have finished
        del_corr_respComponents = del_corr_resp.components
        for thisComponent in del_corr_resp.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "del_corr_resp" ---
        # if trial has changed, end Routine now
        if isinstance(training, data.TrialHandler2) and thisTraining.thisN != training.thisTrial.thisN:
            continueRoutine = False
        del_corr_resp.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                del_corr_resp.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in del_corr_resp.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "del_corr_resp" ---
        for thisComponent in del_corr_resp.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for del_corr_resp
        del_corr_resp.tStop = globalClock.getTime(format='float')
        del_corr_resp.tStopRefresh = tThisFlipGlobal
        thisExp.addData('del_corr_resp.stopped', del_corr_resp.tStop)
        # the Routine "del_corr_resp" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed num_train_blocks repeats of 'training'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # set up handler to look after randomisation of conditions etc
    size_jugment_instructions_loop = data.TrialHandler2(
        name='size_jugment_instructions_loop',
        nReps=1.0, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=[None], 
        seed=None, 
    )
    thisExp.addLoop(size_jugment_instructions_loop)  # add the loop to the experiment
    thisSize_jugment_instructions_loop = size_jugment_instructions_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisSize_jugment_instructions_loop.rgb)
    if thisSize_jugment_instructions_loop != None:
        for paramName in thisSize_jugment_instructions_loop:
            globals()[paramName] = thisSize_jugment_instructions_loop[paramName]
    
    for thisSize_jugment_instructions_loop in size_jugment_instructions_loop:
        currentLoop = size_jugment_instructions_loop
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # abbreviate parameter names if possible (e.g. rgb = thisSize_jugment_instructions_loop.rgb)
        if thisSize_jugment_instructions_loop != None:
            for paramName in thisSize_jugment_instructions_loop:
                globals()[paramName] = thisSize_jugment_instructions_loop[paramName]
        
        # --- Prepare to start Routine "avg_turtle_setup" ---
        # create an object to store info about Routine avg_turtle_setup
        avg_turtle_setup = data.Routine(
            name='avg_turtle_setup',
            components=[],
        )
        avg_turtle_setup.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for avg_turtle_setup
        avg_turtle_setup.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        avg_turtle_setup.tStart = globalClock.getTime(format='float')
        avg_turtle_setup.status = STARTED
        thisExp.addData('avg_turtle_setup.started', avg_turtle_setup.tStart)
        avg_turtle_setup.maxDuration = None
        # keep track of which components have finished
        avg_turtle_setupComponents = avg_turtle_setup.components
        for thisComponent in avg_turtle_setup.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "avg_turtle_setup" ---
        # if trial has changed, end Routine now
        if isinstance(size_jugment_instructions_loop, data.TrialHandler2) and thisSize_jugment_instructions_loop.thisN != size_jugment_instructions_loop.thisTrial.thisN:
            continueRoutine = False
        avg_turtle_setup.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                avg_turtle_setup.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in avg_turtle_setup.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "avg_turtle_setup" ---
        for thisComponent in avg_turtle_setup.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for avg_turtle_setup
        avg_turtle_setup.tStop = globalClock.getTime(format='float')
        avg_turtle_setup.tStopRefresh = tThisFlipGlobal
        thisExp.addData('avg_turtle_setup.stopped', avg_turtle_setup.tStop)
        # the Routine "avg_turtle_setup" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "size_judgment_instructions_p1" ---
        # create an object to store info about Routine size_judgment_instructions_p1
        size_judgment_instructions_p1 = data.Routine(
            name='size_judgment_instructions_p1',
            components=[avg_turtle_instr_1, key_resp],
        )
        size_judgment_instructions_p1.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # create starting attributes for key_resp
        key_resp.keys = []
        key_resp.rt = []
        _key_resp_allKeys = []
        # store start times for size_judgment_instructions_p1
        size_judgment_instructions_p1.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        size_judgment_instructions_p1.tStart = globalClock.getTime(format='float')
        size_judgment_instructions_p1.status = STARTED
        thisExp.addData('size_judgment_instructions_p1.started', size_judgment_instructions_p1.tStart)
        size_judgment_instructions_p1.maxDuration = None
        # keep track of which components have finished
        size_judgment_instructions_p1Components = size_judgment_instructions_p1.components
        for thisComponent in size_judgment_instructions_p1.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "size_judgment_instructions_p1" ---
        # if trial has changed, end Routine now
        if isinstance(size_jugment_instructions_loop, data.TrialHandler2) and thisSize_jugment_instructions_loop.thisN != size_jugment_instructions_loop.thisTrial.thisN:
            continueRoutine = False
        size_judgment_instructions_p1.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *avg_turtle_instr_1* updates
            
            # if avg_turtle_instr_1 is starting this frame...
            if avg_turtle_instr_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                avg_turtle_instr_1.frameNStart = frameN  # exact frame index
                avg_turtle_instr_1.tStart = t  # local t and not account for scr refresh
                avg_turtle_instr_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(avg_turtle_instr_1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'avg_turtle_instr_1.started')
                # update status
                avg_turtle_instr_1.status = STARTED
                avg_turtle_instr_1.setAutoDraw(True)
            
            # if avg_turtle_instr_1 is active this frame...
            if avg_turtle_instr_1.status == STARTED:
                # update params
                pass
            
            # *key_resp* updates
            waitOnFlip = False
            
            # if key_resp is starting this frame...
            if key_resp.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                key_resp.frameNStart = frameN  # exact frame index
                key_resp.tStart = t  # local t and not account for scr refresh
                key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp.started')
                # update status
                key_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp.status == STARTED and not waitOnFlip:
                theseKeys = key_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_allKeys.extend(theseKeys)
                if len(_key_resp_allKeys):
                    key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                    key_resp.rt = _key_resp_allKeys[-1].rt
                    key_resp.duration = _key_resp_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                size_judgment_instructions_p1.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in size_judgment_instructions_p1.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "size_judgment_instructions_p1" ---
        for thisComponent in size_judgment_instructions_p1.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for size_judgment_instructions_p1
        size_judgment_instructions_p1.tStop = globalClock.getTime(format='float')
        size_judgment_instructions_p1.tStopRefresh = tThisFlipGlobal
        thisExp.addData('size_judgment_instructions_p1.stopped', size_judgment_instructions_p1.tStop)
        # check responses
        if key_resp.keys in ['', [], None]:  # No response was made
            key_resp.keys = None
        size_jugment_instructions_loop.addData('key_resp.keys',key_resp.keys)
        if key_resp.keys != None:  # we had a response
            size_jugment_instructions_loop.addData('key_resp.rt', key_resp.rt)
            size_jugment_instructions_loop.addData('key_resp.duration', key_resp.duration)
        # the Routine "size_judgment_instructions_p1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "size_judgment_instructions_p2" ---
        # create an object to store info about Routine size_judgment_instructions_p2
        size_judgment_instructions_p2 = data.Routine(
            name='size_judgment_instructions_p2',
            components=[avg_turtle_instr_2, key_resp_2],
        )
        size_judgment_instructions_p2.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # create starting attributes for key_resp_2
        key_resp_2.keys = []
        key_resp_2.rt = []
        _key_resp_2_allKeys = []
        # store start times for size_judgment_instructions_p2
        size_judgment_instructions_p2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        size_judgment_instructions_p2.tStart = globalClock.getTime(format='float')
        size_judgment_instructions_p2.status = STARTED
        thisExp.addData('size_judgment_instructions_p2.started', size_judgment_instructions_p2.tStart)
        size_judgment_instructions_p2.maxDuration = None
        # keep track of which components have finished
        size_judgment_instructions_p2Components = size_judgment_instructions_p2.components
        for thisComponent in size_judgment_instructions_p2.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "size_judgment_instructions_p2" ---
        # if trial has changed, end Routine now
        if isinstance(size_jugment_instructions_loop, data.TrialHandler2) and thisSize_jugment_instructions_loop.thisN != size_jugment_instructions_loop.thisTrial.thisN:
            continueRoutine = False
        size_judgment_instructions_p2.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *avg_turtle_instr_2* updates
            
            # if avg_turtle_instr_2 is starting this frame...
            if avg_turtle_instr_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                avg_turtle_instr_2.frameNStart = frameN  # exact frame index
                avg_turtle_instr_2.tStart = t  # local t and not account for scr refresh
                avg_turtle_instr_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(avg_turtle_instr_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'avg_turtle_instr_2.started')
                # update status
                avg_turtle_instr_2.status = STARTED
                avg_turtle_instr_2.setAutoDraw(True)
            
            # if avg_turtle_instr_2 is active this frame...
            if avg_turtle_instr_2.status == STARTED:
                # update params
                pass
            
            # *key_resp_2* updates
            waitOnFlip = False
            
            # if key_resp_2 is starting this frame...
            if key_resp_2.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                # keep track of start time/frame for later
                key_resp_2.frameNStart = frameN  # exact frame index
                key_resp_2.tStart = t  # local t and not account for scr refresh
                key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_2.started')
                # update status
                key_resp_2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_2.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_2.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_2_allKeys.extend(theseKeys)
                if len(_key_resp_2_allKeys):
                    key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                    key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                    key_resp_2.duration = _key_resp_2_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                size_judgment_instructions_p2.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in size_judgment_instructions_p2.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "size_judgment_instructions_p2" ---
        for thisComponent in size_judgment_instructions_p2.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for size_judgment_instructions_p2
        size_judgment_instructions_p2.tStop = globalClock.getTime(format='float')
        size_judgment_instructions_p2.tStopRefresh = tThisFlipGlobal
        thisExp.addData('size_judgment_instructions_p2.stopped', size_judgment_instructions_p2.tStop)
        # check responses
        if key_resp_2.keys in ['', [], None]:  # No response was made
            key_resp_2.keys = None
        size_jugment_instructions_loop.addData('key_resp_2.keys',key_resp_2.keys)
        if key_resp_2.keys != None:  # we had a response
            size_jugment_instructions_loop.addData('key_resp_2.rt', key_resp_2.rt)
            size_jugment_instructions_loop.addData('key_resp_2.duration', key_resp_2.duration)
        # the Routine "size_judgment_instructions_p2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "size_judgment_instructions_p3" ---
        # create an object to store info about Routine size_judgment_instructions_p3
        size_judgment_instructions_p3 = data.Routine(
            name='size_judgment_instructions_p3',
            components=[turtle_halfcircle_for_size_instructions, turtle_wedge_for_size_instructions, turtle_wedge_boundary_for_instructions, avg_turtle_instr_3, key_resp_3],
        )
        size_judgment_instructions_p3.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        turtle_halfcircle_for_size_instructions.setVertices(avg_turtle_halfcircle_vertices)
        turtle_wedge_for_size_instructions.setVertices(avg_turtle_wedge_vertices)
        # create starting attributes for key_resp_3
        key_resp_3.keys = []
        key_resp_3.rt = []
        _key_resp_3_allKeys = []
        # store start times for size_judgment_instructions_p3
        size_judgment_instructions_p3.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        size_judgment_instructions_p3.tStart = globalClock.getTime(format='float')
        size_judgment_instructions_p3.status = STARTED
        thisExp.addData('size_judgment_instructions_p3.started', size_judgment_instructions_p3.tStart)
        size_judgment_instructions_p3.maxDuration = None
        # keep track of which components have finished
        size_judgment_instructions_p3Components = size_judgment_instructions_p3.components
        for thisComponent in size_judgment_instructions_p3.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "size_judgment_instructions_p3" ---
        # if trial has changed, end Routine now
        if isinstance(size_jugment_instructions_loop, data.TrialHandler2) and thisSize_jugment_instructions_loop.thisN != size_jugment_instructions_loop.thisTrial.thisN:
            continueRoutine = False
        size_judgment_instructions_p3.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *turtle_halfcircle_for_size_instructions* updates
            
            # if turtle_halfcircle_for_size_instructions is starting this frame...
            if turtle_halfcircle_for_size_instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                turtle_halfcircle_for_size_instructions.frameNStart = frameN  # exact frame index
                turtle_halfcircle_for_size_instructions.tStart = t  # local t and not account for scr refresh
                turtle_halfcircle_for_size_instructions.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(turtle_halfcircle_for_size_instructions, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'turtle_halfcircle_for_size_instructions.started')
                # update status
                turtle_halfcircle_for_size_instructions.status = STARTED
                turtle_halfcircle_for_size_instructions.setAutoDraw(True)
            
            # if turtle_halfcircle_for_size_instructions is active this frame...
            if turtle_halfcircle_for_size_instructions.status == STARTED:
                # update params
                pass
            
            # *turtle_wedge_for_size_instructions* updates
            
            # if turtle_wedge_for_size_instructions is starting this frame...
            if turtle_wedge_for_size_instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                turtle_wedge_for_size_instructions.frameNStart = frameN  # exact frame index
                turtle_wedge_for_size_instructions.tStart = t  # local t and not account for scr refresh
                turtle_wedge_for_size_instructions.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(turtle_wedge_for_size_instructions, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'turtle_wedge_for_size_instructions.started')
                # update status
                turtle_wedge_for_size_instructions.status = STARTED
                turtle_wedge_for_size_instructions.setAutoDraw(True)
            
            # if turtle_wedge_for_size_instructions is active this frame...
            if turtle_wedge_for_size_instructions.status == STARTED:
                # update params
                pass
            
            # *turtle_wedge_boundary_for_instructions* updates
            
            # if turtle_wedge_boundary_for_instructions is starting this frame...
            if turtle_wedge_boundary_for_instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                turtle_wedge_boundary_for_instructions.frameNStart = frameN  # exact frame index
                turtle_wedge_boundary_for_instructions.tStart = t  # local t and not account for scr refresh
                turtle_wedge_boundary_for_instructions.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(turtle_wedge_boundary_for_instructions, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'turtle_wedge_boundary_for_instructions.started')
                # update status
                turtle_wedge_boundary_for_instructions.status = STARTED
                turtle_wedge_boundary_for_instructions.setAutoDraw(True)
            
            # if turtle_wedge_boundary_for_instructions is active this frame...
            if turtle_wedge_boundary_for_instructions.status == STARTED:
                # update params
                pass
            
            # *avg_turtle_instr_3* updates
            
            # if avg_turtle_instr_3 is starting this frame...
            if avg_turtle_instr_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                avg_turtle_instr_3.frameNStart = frameN  # exact frame index
                avg_turtle_instr_3.tStart = t  # local t and not account for scr refresh
                avg_turtle_instr_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(avg_turtle_instr_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'avg_turtle_instr_3.started')
                # update status
                avg_turtle_instr_3.status = STARTED
                avg_turtle_instr_3.setAutoDraw(True)
            
            # if avg_turtle_instr_3 is active this frame...
            if avg_turtle_instr_3.status == STARTED:
                # update params
                pass
            
            # *key_resp_3* updates
            waitOnFlip = False
            
            # if key_resp_3 is starting this frame...
            if key_resp_3.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
                # keep track of start time/frame for later
                key_resp_3.frameNStart = frameN  # exact frame index
                key_resp_3.tStart = t  # local t and not account for scr refresh
                key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_3.started')
                # update status
                key_resp_3.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_3.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_3.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_3_allKeys.extend(theseKeys)
                if len(_key_resp_3_allKeys):
                    key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
                    key_resp_3.rt = _key_resp_3_allKeys[-1].rt
                    key_resp_3.duration = _key_resp_3_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                size_judgment_instructions_p3.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in size_judgment_instructions_p3.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "size_judgment_instructions_p3" ---
        for thisComponent in size_judgment_instructions_p3.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for size_judgment_instructions_p3
        size_judgment_instructions_p3.tStop = globalClock.getTime(format='float')
        size_judgment_instructions_p3.tStopRefresh = tThisFlipGlobal
        thisExp.addData('size_judgment_instructions_p3.stopped', size_judgment_instructions_p3.tStop)
        # check responses
        if key_resp_3.keys in ['', [], None]:  # No response was made
            key_resp_3.keys = None
        size_jugment_instructions_loop.addData('key_resp_3.keys',key_resp_3.keys)
        if key_resp_3.keys != None:  # we had a response
            size_jugment_instructions_loop.addData('key_resp_3.rt', key_resp_3.rt)
            size_jugment_instructions_loop.addData('key_resp_3.duration', key_resp_3.duration)
        # the Routine "size_judgment_instructions_p3" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "size_judgment_instructions_p4" ---
        # create an object to store info about Routine size_judgment_instructions_p4
        size_judgment_instructions_p4 = data.Routine(
            name='size_judgment_instructions_p4',
            components=[turtle_halfcircle_for_size_instructions_2, turtle_wedge_for_size_instructions_2, turtle_wedge_boundary_for_instructions_2, avg_turtle_instr, key_resp_4],
        )
        size_judgment_instructions_p4.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        turtle_halfcircle_for_size_instructions_2.setVertices(avg_turtle_halfcircle_vertices)
        turtle_wedge_for_size_instructions_2.setVertices(avg_turtle_wedge_vertices)
        # create starting attributes for key_resp_4
        key_resp_4.keys = []
        key_resp_4.rt = []
        _key_resp_4_allKeys = []
        # store start times for size_judgment_instructions_p4
        size_judgment_instructions_p4.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        size_judgment_instructions_p4.tStart = globalClock.getTime(format='float')
        size_judgment_instructions_p4.status = STARTED
        thisExp.addData('size_judgment_instructions_p4.started', size_judgment_instructions_p4.tStart)
        size_judgment_instructions_p4.maxDuration = None
        # keep track of which components have finished
        size_judgment_instructions_p4Components = size_judgment_instructions_p4.components
        for thisComponent in size_judgment_instructions_p4.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "size_judgment_instructions_p4" ---
        # if trial has changed, end Routine now
        if isinstance(size_jugment_instructions_loop, data.TrialHandler2) and thisSize_jugment_instructions_loop.thisN != size_jugment_instructions_loop.thisTrial.thisN:
            continueRoutine = False
        size_judgment_instructions_p4.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *turtle_halfcircle_for_size_instructions_2* updates
            
            # if turtle_halfcircle_for_size_instructions_2 is starting this frame...
            if turtle_halfcircle_for_size_instructions_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                turtle_halfcircle_for_size_instructions_2.frameNStart = frameN  # exact frame index
                turtle_halfcircle_for_size_instructions_2.tStart = t  # local t and not account for scr refresh
                turtle_halfcircle_for_size_instructions_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(turtle_halfcircle_for_size_instructions_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'turtle_halfcircle_for_size_instructions_2.started')
                # update status
                turtle_halfcircle_for_size_instructions_2.status = STARTED
                turtle_halfcircle_for_size_instructions_2.setAutoDraw(True)
            
            # if turtle_halfcircle_for_size_instructions_2 is active this frame...
            if turtle_halfcircle_for_size_instructions_2.status == STARTED:
                # update params
                pass
            
            # *turtle_wedge_for_size_instructions_2* updates
            
            # if turtle_wedge_for_size_instructions_2 is starting this frame...
            if turtle_wedge_for_size_instructions_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                turtle_wedge_for_size_instructions_2.frameNStart = frameN  # exact frame index
                turtle_wedge_for_size_instructions_2.tStart = t  # local t and not account for scr refresh
                turtle_wedge_for_size_instructions_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(turtle_wedge_for_size_instructions_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'turtle_wedge_for_size_instructions_2.started')
                # update status
                turtle_wedge_for_size_instructions_2.status = STARTED
                turtle_wedge_for_size_instructions_2.setAutoDraw(True)
            
            # if turtle_wedge_for_size_instructions_2 is active this frame...
            if turtle_wedge_for_size_instructions_2.status == STARTED:
                # update params
                pass
            
            # *turtle_wedge_boundary_for_instructions_2* updates
            
            # if turtle_wedge_boundary_for_instructions_2 is starting this frame...
            if turtle_wedge_boundary_for_instructions_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                turtle_wedge_boundary_for_instructions_2.frameNStart = frameN  # exact frame index
                turtle_wedge_boundary_for_instructions_2.tStart = t  # local t and not account for scr refresh
                turtle_wedge_boundary_for_instructions_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(turtle_wedge_boundary_for_instructions_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'turtle_wedge_boundary_for_instructions_2.started')
                # update status
                turtle_wedge_boundary_for_instructions_2.status = STARTED
                turtle_wedge_boundary_for_instructions_2.setAutoDraw(True)
            
            # if turtle_wedge_boundary_for_instructions_2 is active this frame...
            if turtle_wedge_boundary_for_instructions_2.status == STARTED:
                # update params
                pass
            
            # *avg_turtle_instr* updates
            
            # if avg_turtle_instr is starting this frame...
            if avg_turtle_instr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                avg_turtle_instr.frameNStart = frameN  # exact frame index
                avg_turtle_instr.tStart = t  # local t and not account for scr refresh
                avg_turtle_instr.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(avg_turtle_instr, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'avg_turtle_instr.started')
                # update status
                avg_turtle_instr.status = STARTED
                avg_turtle_instr.setAutoDraw(True)
            
            # if avg_turtle_instr is active this frame...
            if avg_turtle_instr.status == STARTED:
                # update params
                pass
            
            # *key_resp_4* updates
            waitOnFlip = False
            
            # if key_resp_4 is starting this frame...
            if key_resp_4.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
                # keep track of start time/frame for later
                key_resp_4.frameNStart = frameN  # exact frame index
                key_resp_4.tStart = t  # local t and not account for scr refresh
                key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_4.started')
                # update status
                key_resp_4.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_4.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_4.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_4_allKeys.extend(theseKeys)
                if len(_key_resp_4_allKeys):
                    key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
                    key_resp_4.rt = _key_resp_4_allKeys[-1].rt
                    key_resp_4.duration = _key_resp_4_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                size_judgment_instructions_p4.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in size_judgment_instructions_p4.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "size_judgment_instructions_p4" ---
        for thisComponent in size_judgment_instructions_p4.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for size_judgment_instructions_p4
        size_judgment_instructions_p4.tStop = globalClock.getTime(format='float')
        size_judgment_instructions_p4.tStopRefresh = tThisFlipGlobal
        thisExp.addData('size_judgment_instructions_p4.stopped', size_judgment_instructions_p4.tStop)
        # check responses
        if key_resp_4.keys in ['', [], None]:  # No response was made
            key_resp_4.keys = None
        size_jugment_instructions_loop.addData('key_resp_4.keys',key_resp_4.keys)
        if key_resp_4.keys != None:  # we had a response
            size_jugment_instructions_loop.addData('key_resp_4.rt', key_resp_4.rt)
            size_jugment_instructions_loop.addData('key_resp_4.duration', key_resp_4.duration)
        # the Routine "size_judgment_instructions_p4" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "size_jugment_instructions_p5" ---
        # create an object to store info about Routine size_jugment_instructions_p5
        size_jugment_instructions_p5 = data.Routine(
            name='size_jugment_instructions_p5',
            components=[turtle_halfcircle_for_size_instructions_3, turtle_wedge_for_size_instructions_3, turtle_wedge_boundary_for_instructions_3, avg_turtle_instr_4, key_resp_5],
        )
        size_jugment_instructions_p5.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        turtle_halfcircle_for_size_instructions_3.setVertices(avg_turtle_halfcircle_vertices)
        turtle_wedge_for_size_instructions_3.setVertices(avg_turtle_wedge_vertices)
        # create starting attributes for key_resp_5
        key_resp_5.keys = []
        key_resp_5.rt = []
        _key_resp_5_allKeys = []
        # store start times for size_jugment_instructions_p5
        size_jugment_instructions_p5.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        size_jugment_instructions_p5.tStart = globalClock.getTime(format='float')
        size_jugment_instructions_p5.status = STARTED
        thisExp.addData('size_jugment_instructions_p5.started', size_jugment_instructions_p5.tStart)
        size_jugment_instructions_p5.maxDuration = None
        # keep track of which components have finished
        size_jugment_instructions_p5Components = size_jugment_instructions_p5.components
        for thisComponent in size_jugment_instructions_p5.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "size_jugment_instructions_p5" ---
        # if trial has changed, end Routine now
        if isinstance(size_jugment_instructions_loop, data.TrialHandler2) and thisSize_jugment_instructions_loop.thisN != size_jugment_instructions_loop.thisTrial.thisN:
            continueRoutine = False
        size_jugment_instructions_p5.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *turtle_halfcircle_for_size_instructions_3* updates
            
            # if turtle_halfcircle_for_size_instructions_3 is starting this frame...
            if turtle_halfcircle_for_size_instructions_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                turtle_halfcircle_for_size_instructions_3.frameNStart = frameN  # exact frame index
                turtle_halfcircle_for_size_instructions_3.tStart = t  # local t and not account for scr refresh
                turtle_halfcircle_for_size_instructions_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(turtle_halfcircle_for_size_instructions_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'turtle_halfcircle_for_size_instructions_3.started')
                # update status
                turtle_halfcircle_for_size_instructions_3.status = STARTED
                turtle_halfcircle_for_size_instructions_3.setAutoDraw(True)
            
            # if turtle_halfcircle_for_size_instructions_3 is active this frame...
            if turtle_halfcircle_for_size_instructions_3.status == STARTED:
                # update params
                pass
            
            # *turtle_wedge_for_size_instructions_3* updates
            
            # if turtle_wedge_for_size_instructions_3 is starting this frame...
            if turtle_wedge_for_size_instructions_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                turtle_wedge_for_size_instructions_3.frameNStart = frameN  # exact frame index
                turtle_wedge_for_size_instructions_3.tStart = t  # local t and not account for scr refresh
                turtle_wedge_for_size_instructions_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(turtle_wedge_for_size_instructions_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'turtle_wedge_for_size_instructions_3.started')
                # update status
                turtle_wedge_for_size_instructions_3.status = STARTED
                turtle_wedge_for_size_instructions_3.setAutoDraw(True)
            
            # if turtle_wedge_for_size_instructions_3 is active this frame...
            if turtle_wedge_for_size_instructions_3.status == STARTED:
                # update params
                pass
            
            # *turtle_wedge_boundary_for_instructions_3* updates
            
            # if turtle_wedge_boundary_for_instructions_3 is starting this frame...
            if turtle_wedge_boundary_for_instructions_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                turtle_wedge_boundary_for_instructions_3.frameNStart = frameN  # exact frame index
                turtle_wedge_boundary_for_instructions_3.tStart = t  # local t and not account for scr refresh
                turtle_wedge_boundary_for_instructions_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(turtle_wedge_boundary_for_instructions_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'turtle_wedge_boundary_for_instructions_3.started')
                # update status
                turtle_wedge_boundary_for_instructions_3.status = STARTED
                turtle_wedge_boundary_for_instructions_3.setAutoDraw(True)
            
            # if turtle_wedge_boundary_for_instructions_3 is active this frame...
            if turtle_wedge_boundary_for_instructions_3.status == STARTED:
                # update params
                pass
            
            # *avg_turtle_instr_4* updates
            
            # if avg_turtle_instr_4 is starting this frame...
            if avg_turtle_instr_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                avg_turtle_instr_4.frameNStart = frameN  # exact frame index
                avg_turtle_instr_4.tStart = t  # local t and not account for scr refresh
                avg_turtle_instr_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(avg_turtle_instr_4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'avg_turtle_instr_4.started')
                # update status
                avg_turtle_instr_4.status = STARTED
                avg_turtle_instr_4.setAutoDraw(True)
            
            # if avg_turtle_instr_4 is active this frame...
            if avg_turtle_instr_4.status == STARTED:
                # update params
                pass
            
            # *key_resp_5* updates
            waitOnFlip = False
            
            # if key_resp_5 is starting this frame...
            if key_resp_5.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
                # keep track of start time/frame for later
                key_resp_5.frameNStart = frameN  # exact frame index
                key_resp_5.tStart = t  # local t and not account for scr refresh
                key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_5.started')
                # update status
                key_resp_5.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_5.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_5.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_5_allKeys.extend(theseKeys)
                if len(_key_resp_5_allKeys):
                    key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
                    key_resp_5.rt = _key_resp_5_allKeys[-1].rt
                    key_resp_5.duration = _key_resp_5_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                size_jugment_instructions_p5.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in size_jugment_instructions_p5.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "size_jugment_instructions_p5" ---
        for thisComponent in size_jugment_instructions_p5.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for size_jugment_instructions_p5
        size_jugment_instructions_p5.tStop = globalClock.getTime(format='float')
        size_jugment_instructions_p5.tStopRefresh = tThisFlipGlobal
        thisExp.addData('size_jugment_instructions_p5.stopped', size_jugment_instructions_p5.tStop)
        # check responses
        if key_resp_5.keys in ['', [], None]:  # No response was made
            key_resp_5.keys = None
        size_jugment_instructions_loop.addData('key_resp_5.keys',key_resp_5.keys)
        if key_resp_5.keys != None:  # we had a response
            size_jugment_instructions_loop.addData('key_resp_5.rt', key_resp_5.rt)
            size_jugment_instructions_loop.addData('key_resp_5.duration', key_resp_5.duration)
        # the Routine "size_jugment_instructions_p5" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "size_judgment_instructions_p6" ---
        # create an object to store info about Routine size_judgment_instructions_p6
        size_judgment_instructions_p6 = data.Routine(
            name='size_judgment_instructions_p6',
            components=[turtle_halfcircle_for_size_instructions_4, turtle_wedge_for_size_instructions_4, turtle_wedge_boundary_for_instructions_4, avg_turtle_instr_5, key_resp_6],
        )
        size_judgment_instructions_p6.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        turtle_halfcircle_for_size_instructions_4.setVertices(avg_turtle_halfcircle_vertices)
        turtle_wedge_for_size_instructions_4.setVertices(avg_turtle_wedge_vertices)
        # create starting attributes for key_resp_6
        key_resp_6.keys = []
        key_resp_6.rt = []
        _key_resp_6_allKeys = []
        # store start times for size_judgment_instructions_p6
        size_judgment_instructions_p6.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        size_judgment_instructions_p6.tStart = globalClock.getTime(format='float')
        size_judgment_instructions_p6.status = STARTED
        thisExp.addData('size_judgment_instructions_p6.started', size_judgment_instructions_p6.tStart)
        size_judgment_instructions_p6.maxDuration = None
        # keep track of which components have finished
        size_judgment_instructions_p6Components = size_judgment_instructions_p6.components
        for thisComponent in size_judgment_instructions_p6.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "size_judgment_instructions_p6" ---
        # if trial has changed, end Routine now
        if isinstance(size_jugment_instructions_loop, data.TrialHandler2) and thisSize_jugment_instructions_loop.thisN != size_jugment_instructions_loop.thisTrial.thisN:
            continueRoutine = False
        size_judgment_instructions_p6.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *turtle_halfcircle_for_size_instructions_4* updates
            
            # if turtle_halfcircle_for_size_instructions_4 is starting this frame...
            if turtle_halfcircle_for_size_instructions_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                turtle_halfcircle_for_size_instructions_4.frameNStart = frameN  # exact frame index
                turtle_halfcircle_for_size_instructions_4.tStart = t  # local t and not account for scr refresh
                turtle_halfcircle_for_size_instructions_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(turtle_halfcircle_for_size_instructions_4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'turtle_halfcircle_for_size_instructions_4.started')
                # update status
                turtle_halfcircle_for_size_instructions_4.status = STARTED
                turtle_halfcircle_for_size_instructions_4.setAutoDraw(True)
            
            # if turtle_halfcircle_for_size_instructions_4 is active this frame...
            if turtle_halfcircle_for_size_instructions_4.status == STARTED:
                # update params
                pass
            
            # *turtle_wedge_for_size_instructions_4* updates
            
            # if turtle_wedge_for_size_instructions_4 is starting this frame...
            if turtle_wedge_for_size_instructions_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                turtle_wedge_for_size_instructions_4.frameNStart = frameN  # exact frame index
                turtle_wedge_for_size_instructions_4.tStart = t  # local t and not account for scr refresh
                turtle_wedge_for_size_instructions_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(turtle_wedge_for_size_instructions_4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'turtle_wedge_for_size_instructions_4.started')
                # update status
                turtle_wedge_for_size_instructions_4.status = STARTED
                turtle_wedge_for_size_instructions_4.setAutoDraw(True)
            
            # if turtle_wedge_for_size_instructions_4 is active this frame...
            if turtle_wedge_for_size_instructions_4.status == STARTED:
                # update params
                pass
            
            # *turtle_wedge_boundary_for_instructions_4* updates
            
            # if turtle_wedge_boundary_for_instructions_4 is starting this frame...
            if turtle_wedge_boundary_for_instructions_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                turtle_wedge_boundary_for_instructions_4.frameNStart = frameN  # exact frame index
                turtle_wedge_boundary_for_instructions_4.tStart = t  # local t and not account for scr refresh
                turtle_wedge_boundary_for_instructions_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(turtle_wedge_boundary_for_instructions_4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'turtle_wedge_boundary_for_instructions_4.started')
                # update status
                turtle_wedge_boundary_for_instructions_4.status = STARTED
                turtle_wedge_boundary_for_instructions_4.setAutoDraw(True)
            
            # if turtle_wedge_boundary_for_instructions_4 is active this frame...
            if turtle_wedge_boundary_for_instructions_4.status == STARTED:
                # update params
                pass
            
            # *avg_turtle_instr_5* updates
            
            # if avg_turtle_instr_5 is starting this frame...
            if avg_turtle_instr_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                avg_turtle_instr_5.frameNStart = frameN  # exact frame index
                avg_turtle_instr_5.tStart = t  # local t and not account for scr refresh
                avg_turtle_instr_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(avg_turtle_instr_5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'avg_turtle_instr_5.started')
                # update status
                avg_turtle_instr_5.status = STARTED
                avg_turtle_instr_5.setAutoDraw(True)
            
            # if avg_turtle_instr_5 is active this frame...
            if avg_turtle_instr_5.status == STARTED:
                # update params
                pass
            
            # *key_resp_6* updates
            waitOnFlip = False
            
            # if key_resp_6 is starting this frame...
            if key_resp_6.status == NOT_STARTED and tThisFlip >= .5-frameTolerance:
                # keep track of start time/frame for later
                key_resp_6.frameNStart = frameN  # exact frame index
                key_resp_6.tStart = t  # local t and not account for scr refresh
                key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_6.started')
                # update status
                key_resp_6.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_6.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_6.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_6_allKeys.extend(theseKeys)
                if len(_key_resp_6_allKeys):
                    key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
                    key_resp_6.rt = _key_resp_6_allKeys[-1].rt
                    key_resp_6.duration = _key_resp_6_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                size_judgment_instructions_p6.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in size_judgment_instructions_p6.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "size_judgment_instructions_p6" ---
        for thisComponent in size_judgment_instructions_p6.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for size_judgment_instructions_p6
        size_judgment_instructions_p6.tStop = globalClock.getTime(format='float')
        size_judgment_instructions_p6.tStopRefresh = tThisFlipGlobal
        thisExp.addData('size_judgment_instructions_p6.stopped', size_judgment_instructions_p6.tStop)
        # check responses
        if key_resp_6.keys in ['', [], None]:  # No response was made
            key_resp_6.keys = None
        size_jugment_instructions_loop.addData('key_resp_6.keys',key_resp_6.keys)
        if key_resp_6.keys != None:  # we had a response
            size_jugment_instructions_loop.addData('key_resp_6.rt', key_resp_6.rt)
            size_jugment_instructions_loop.addData('key_resp_6.duration', key_resp_6.duration)
        # the Routine "size_judgment_instructions_p6" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    # completed 1.0 repeats of 'size_jugment_instructions_loop'
    
    
    # set up handler to look after randomisation of conditions etc
    size_judgment_trials = data.TrialHandler2(
        name='size_judgment_trials',
        nReps=num_size_blocks, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('stim/stim_train_with_areas.csv'), 
        seed=None, 
    )
    thisExp.addLoop(size_judgment_trials)  # add the loop to the experiment
    thisSize_judgment_trial = size_judgment_trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisSize_judgment_trial.rgb)
    if thisSize_judgment_trial != None:
        for paramName in thisSize_judgment_trial:
            globals()[paramName] = thisSize_judgment_trial[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisSize_judgment_trial in size_judgment_trials:
        currentLoop = size_judgment_trials
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisSize_judgment_trial.rgb)
        if thisSize_judgment_trial != None:
            for paramName in thisSize_judgment_trial:
                globals()[paramName] = thisSize_judgment_trial[paramName]
        
        # --- Prepare to start Routine "fixation_cross" ---
        # create an object to store info about Routine fixation_cross
        fixation_cross = data.Routine(
            name='fixation_cross',
            components=[fixation_cross_1],
        )
        fixation_cross.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for fixation_cross
        fixation_cross.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        fixation_cross.tStart = globalClock.getTime(format='float')
        fixation_cross.status = STARTED
        thisExp.addData('fixation_cross.started', fixation_cross.tStart)
        fixation_cross.maxDuration = None
        # keep track of which components have finished
        fixation_crossComponents = fixation_cross.components
        for thisComponent in fixation_cross.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "fixation_cross" ---
        # if trial has changed, end Routine now
        if isinstance(size_judgment_trials, data.TrialHandler2) and thisSize_judgment_trial.thisN != size_judgment_trials.thisTrial.thisN:
            continueRoutine = False
        fixation_cross.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.4:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixation_cross_1* updates
            
            # if fixation_cross_1 is starting this frame...
            if fixation_cross_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation_cross_1.frameNStart = frameN  # exact frame index
                fixation_cross_1.tStart = t  # local t and not account for scr refresh
                fixation_cross_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation_cross_1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation_cross_1.started')
                # update status
                fixation_cross_1.status = STARTED
                fixation_cross_1.setAutoDraw(True)
            
            # if fixation_cross_1 is active this frame...
            if fixation_cross_1.status == STARTED:
                # update params
                pass
            
            # if fixation_cross_1 is stopping this frame...
            if fixation_cross_1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation_cross_1.tStartRefresh + .4-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation_cross_1.tStop = t  # not accounting for scr refresh
                    fixation_cross_1.tStopRefresh = tThisFlipGlobal  # on global time
                    fixation_cross_1.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixation_cross_1.stopped')
                    # update status
                    fixation_cross_1.status = FINISHED
                    fixation_cross_1.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                fixation_cross.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fixation_cross.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "fixation_cross" ---
        for thisComponent in fixation_cross.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for fixation_cross
        fixation_cross.tStop = globalClock.getTime(format='float')
        fixation_cross.tStopRefresh = tThisFlipGlobal
        thisExp.addData('fixation_cross.stopped', fixation_cross.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if fixation_cross.maxDurationReached:
            routineTimer.addTime(-fixation_cross.maxDuration)
        elif fixation_cross.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.400000)
        
        # --- Prepare to start Routine "blank" ---
        # create an object to store info about Routine blank
        blank = data.Routine(
            name='blank',
            components=[text_2],
        )
        blank.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for blank
        blank.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        blank.tStart = globalClock.getTime(format='float')
        blank.status = STARTED
        thisExp.addData('blank.started', blank.tStart)
        blank.maxDuration = None
        # keep track of which components have finished
        blankComponents = blank.components
        for thisComponent in blank.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "blank" ---
        # if trial has changed, end Routine now
        if isinstance(size_judgment_trials, data.TrialHandler2) and thisSize_judgment_trial.thisN != size_judgment_trials.thisTrial.thisN:
            continueRoutine = False
        blank.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.2:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_2* updates
            
            # if text_2 is starting this frame...
            if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_2.frameNStart = frameN  # exact frame index
                text_2.tStart = t  # local t and not account for scr refresh
                text_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_2.started')
                # update status
                text_2.status = STARTED
                text_2.setAutoDraw(True)
            
            # if text_2 is active this frame...
            if text_2.status == STARTED:
                # update params
                pass
            
            # if text_2 is stopping this frame...
            if text_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_2.tStartRefresh + .2-frameTolerance:
                    # keep track of stop time/frame for later
                    text_2.tStop = t  # not accounting for scr refresh
                    text_2.tStopRefresh = tThisFlipGlobal  # on global time
                    text_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_2.stopped')
                    # update status
                    text_2.status = FINISHED
                    text_2.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                blank.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in blank.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "blank" ---
        for thisComponent in blank.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for blank
        blank.tStop = globalClock.getTime(format='float')
        blank.tStopRefresh = tThisFlipGlobal
        thisExp.addData('blank.stopped', blank.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if blank.maxDurationReached:
            routineTimer.addTime(-blank.maxDuration)
        elif blank.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.200000)
        
        # --- Prepare to start Routine "size_judgment_params" ---
        # create an object to store info about Routine size_judgment_params
        size_judgment_params = data.Routine(
            name='size_judgment_params',
            components=[],
        )
        size_judgment_params.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from get_turtle_params_for_size
        turtle_halfcircle_vertices = get_turtle_halfcircle_vertices(radius)
        turtle_wedge_vertices = get_turtle_wedge_vertices(angle)
        
        if area < avg_turtle_area:
            print("correct response is f")
            corr_resp_size_tmp='f'
        elif area > avg_turtle_area:
            print("correct response is j")
            corr_resp_size_tmp='j'
        # store start times for size_judgment_params
        size_judgment_params.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        size_judgment_params.tStart = globalClock.getTime(format='float')
        size_judgment_params.status = STARTED
        thisExp.addData('size_judgment_params.started', size_judgment_params.tStart)
        size_judgment_params.maxDuration = None
        # keep track of which components have finished
        size_judgment_paramsComponents = size_judgment_params.components
        for thisComponent in size_judgment_params.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "size_judgment_params" ---
        # if trial has changed, end Routine now
        if isinstance(size_judgment_trials, data.TrialHandler2) and thisSize_judgment_trial.thisN != size_judgment_trials.thisTrial.thisN:
            continueRoutine = False
        size_judgment_params.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                size_judgment_params.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in size_judgment_params.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "size_judgment_params" ---
        for thisComponent in size_judgment_params.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for size_judgment_params
        size_judgment_params.tStop = globalClock.getTime(format='float')
        size_judgment_params.tStopRefresh = tThisFlipGlobal
        thisExp.addData('size_judgment_params.stopped', size_judgment_params.tStop)
        # the Routine "size_judgment_params" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "size_judgment_response" ---
        # create an object to store info about Routine size_judgment_response
        size_judgment_response = data.Routine(
            name='size_judgment_response',
            components=[turtle_half_circle_for_size_judgment, turtle_wedge_for_size_judgment, turtle_boundary_for_size_judgment, size_judgment_prompt, key_resp_size_judgment],
        )
        size_judgment_response.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        turtle_half_circle_for_size_judgment.setVertices(turtle_halfcircle_vertices)
        turtle_wedge_for_size_judgment.setVertices(turtle_wedge_vertices)
        # create starting attributes for key_resp_size_judgment
        key_resp_size_judgment.keys = []
        key_resp_size_judgment.rt = []
        _key_resp_size_judgment_allKeys = []
        # store start times for size_judgment_response
        size_judgment_response.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        size_judgment_response.tStart = globalClock.getTime(format='float')
        size_judgment_response.status = STARTED
        thisExp.addData('size_judgment_response.started', size_judgment_response.tStart)
        size_judgment_response.maxDuration = None
        # keep track of which components have finished
        size_judgment_responseComponents = size_judgment_response.components
        for thisComponent in size_judgment_response.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "size_judgment_response" ---
        # if trial has changed, end Routine now
        if isinstance(size_judgment_trials, data.TrialHandler2) and thisSize_judgment_trial.thisN != size_judgment_trials.thisTrial.thisN:
            continueRoutine = False
        size_judgment_response.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *turtle_half_circle_for_size_judgment* updates
            
            # if turtle_half_circle_for_size_judgment is starting this frame...
            if turtle_half_circle_for_size_judgment.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                turtle_half_circle_for_size_judgment.frameNStart = frameN  # exact frame index
                turtle_half_circle_for_size_judgment.tStart = t  # local t and not account for scr refresh
                turtle_half_circle_for_size_judgment.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(turtle_half_circle_for_size_judgment, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'turtle_half_circle_for_size_judgment.started')
                # update status
                turtle_half_circle_for_size_judgment.status = STARTED
                turtle_half_circle_for_size_judgment.setAutoDraw(True)
            
            # if turtle_half_circle_for_size_judgment is active this frame...
            if turtle_half_circle_for_size_judgment.status == STARTED:
                # update params
                pass
            
            # *turtle_wedge_for_size_judgment* updates
            
            # if turtle_wedge_for_size_judgment is starting this frame...
            if turtle_wedge_for_size_judgment.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                turtle_wedge_for_size_judgment.frameNStart = frameN  # exact frame index
                turtle_wedge_for_size_judgment.tStart = t  # local t and not account for scr refresh
                turtle_wedge_for_size_judgment.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(turtle_wedge_for_size_judgment, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'turtle_wedge_for_size_judgment.started')
                # update status
                turtle_wedge_for_size_judgment.status = STARTED
                turtle_wedge_for_size_judgment.setAutoDraw(True)
            
            # if turtle_wedge_for_size_judgment is active this frame...
            if turtle_wedge_for_size_judgment.status == STARTED:
                # update params
                pass
            
            # *turtle_boundary_for_size_judgment* updates
            
            # if turtle_boundary_for_size_judgment is starting this frame...
            if turtle_boundary_for_size_judgment.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                turtle_boundary_for_size_judgment.frameNStart = frameN  # exact frame index
                turtle_boundary_for_size_judgment.tStart = t  # local t and not account for scr refresh
                turtle_boundary_for_size_judgment.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(turtle_boundary_for_size_judgment, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'turtle_boundary_for_size_judgment.started')
                # update status
                turtle_boundary_for_size_judgment.status = STARTED
                turtle_boundary_for_size_judgment.setAutoDraw(True)
            
            # if turtle_boundary_for_size_judgment is active this frame...
            if turtle_boundary_for_size_judgment.status == STARTED:
                # update params
                pass
            
            # *size_judgment_prompt* updates
            
            # if size_judgment_prompt is starting this frame...
            if size_judgment_prompt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                size_judgment_prompt.frameNStart = frameN  # exact frame index
                size_judgment_prompt.tStart = t  # local t and not account for scr refresh
                size_judgment_prompt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(size_judgment_prompt, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'size_judgment_prompt.started')
                # update status
                size_judgment_prompt.status = STARTED
                size_judgment_prompt.setAutoDraw(True)
            
            # if size_judgment_prompt is active this frame...
            if size_judgment_prompt.status == STARTED:
                # update params
                pass
            
            # *key_resp_size_judgment* updates
            waitOnFlip = False
            
            # if key_resp_size_judgment is starting this frame...
            if key_resp_size_judgment.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_size_judgment.frameNStart = frameN  # exact frame index
                key_resp_size_judgment.tStart = t  # local t and not account for scr refresh
                key_resp_size_judgment.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_size_judgment, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_size_judgment.started')
                # update status
                key_resp_size_judgment.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_size_judgment.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_size_judgment.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_size_judgment.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_size_judgment.getKeys(keyList=['f','j'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_size_judgment_allKeys.extend(theseKeys)
                if len(_key_resp_size_judgment_allKeys):
                    key_resp_size_judgment.keys = _key_resp_size_judgment_allKeys[-1].name  # just the last key pressed
                    key_resp_size_judgment.rt = _key_resp_size_judgment_allKeys[-1].rt
                    key_resp_size_judgment.duration = _key_resp_size_judgment_allKeys[-1].duration
                    # was this correct?
                    if (key_resp_size_judgment.keys == str(corr_resp_size_tmp)) or (key_resp_size_judgment.keys == corr_resp_size_tmp):
                        key_resp_size_judgment.corr = 1
                    else:
                        key_resp_size_judgment.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                size_judgment_response.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in size_judgment_response.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "size_judgment_response" ---
        for thisComponent in size_judgment_response.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for size_judgment_response
        size_judgment_response.tStop = globalClock.getTime(format='float')
        size_judgment_response.tStopRefresh = tThisFlipGlobal
        thisExp.addData('size_judgment_response.stopped', size_judgment_response.tStop)
        # check responses
        if key_resp_size_judgment.keys in ['', [], None]:  # No response was made
            key_resp_size_judgment.keys = None
            # was no response the correct answer?!
            if str(corr_resp_size_tmp).lower() == 'none':
               key_resp_size_judgment.corr = 1;  # correct non-response
            else:
               key_resp_size_judgment.corr = 0;  # failed to respond (incorrectly)
        # store data for size_judgment_trials (TrialHandler)
        size_judgment_trials.addData('key_resp_size_judgment.keys',key_resp_size_judgment.keys)
        size_judgment_trials.addData('key_resp_size_judgment.corr', key_resp_size_judgment.corr)
        if key_resp_size_judgment.keys != None:  # we had a response
            size_judgment_trials.addData('key_resp_size_judgment.rt', key_resp_size_judgment.rt)
            size_judgment_trials.addData('key_resp_size_judgment.duration', key_resp_size_judgment.duration)
        # the Routine "size_judgment_response" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "size_jugment_code_check" ---
        # create an object to store info about Routine size_jugment_code_check
        size_jugment_code_check = data.Routine(
            name='size_jugment_code_check',
            components=[],
        )
        size_jugment_code_check.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from size_judgment_code_check
        if key_resp_size_judgment.corr==1:
            size_feedback_dur=1;
            size_feedback_col="#008000"
            if corr_resp_size_tmp=='f':
                size_feedback_text="You were correct! This turtle is smaller than the average turtle."
            elif corr_resp_size_tmp=="j":
                size_feedback_text="You were correct! This turtle is larger than the average turtle."
        elif key_resp_size_judgment.corr==0:
            size_feedback_dur=2;
            size_feedback_col="#FF0000"
            if corr_resp_size_tmp=='f':
                size_feedback_text="You were incorrect. This turtle is smaller than the average turtle."
            elif corr_resp_size_tmp=="j":
                size_feedback_text="You were incorrect. This turtle is larger than the average turtle."
        
        # store start times for size_jugment_code_check
        size_jugment_code_check.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        size_jugment_code_check.tStart = globalClock.getTime(format='float')
        size_jugment_code_check.status = STARTED
        thisExp.addData('size_jugment_code_check.started', size_jugment_code_check.tStart)
        size_jugment_code_check.maxDuration = None
        # keep track of which components have finished
        size_jugment_code_checkComponents = size_jugment_code_check.components
        for thisComponent in size_jugment_code_check.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "size_jugment_code_check" ---
        # if trial has changed, end Routine now
        if isinstance(size_judgment_trials, data.TrialHandler2) and thisSize_judgment_trial.thisN != size_judgment_trials.thisTrial.thisN:
            continueRoutine = False
        size_jugment_code_check.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                size_jugment_code_check.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in size_jugment_code_check.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "size_jugment_code_check" ---
        for thisComponent in size_jugment_code_check.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for size_jugment_code_check
        size_jugment_code_check.tStop = globalClock.getTime(format='float')
        size_jugment_code_check.tStopRefresh = tThisFlipGlobal
        thisExp.addData('size_jugment_code_check.stopped', size_jugment_code_check.tStop)
        # the Routine "size_jugment_code_check" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "size_judgment_feedback" ---
        # create an object to store info about Routine size_judgment_feedback
        size_judgment_feedback = data.Routine(
            name='size_judgment_feedback',
            components=[turtle_half_circle_for_size_judgment_feedback, turtle_wedge_for_size_judgment_feedback, turtle_boundary_for_size_judgment_feedback, size_feedback_text_display],
        )
        size_judgment_feedback.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        turtle_half_circle_for_size_judgment_feedback.setVertices(turtle_halfcircle_vertices)
        turtle_wedge_for_size_judgment_feedback.setVertices(turtle_wedge_vertices)
        size_feedback_text_display.setColor(size_feedback_col, colorSpace='rgb')
        size_feedback_text_display.setText(size_feedback_text)
        # store start times for size_judgment_feedback
        size_judgment_feedback.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        size_judgment_feedback.tStart = globalClock.getTime(format='float')
        size_judgment_feedback.status = STARTED
        thisExp.addData('size_judgment_feedback.started', size_judgment_feedback.tStart)
        size_judgment_feedback.maxDuration = None
        # keep track of which components have finished
        size_judgment_feedbackComponents = size_judgment_feedback.components
        for thisComponent in size_judgment_feedback.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "size_judgment_feedback" ---
        # if trial has changed, end Routine now
        if isinstance(size_judgment_trials, data.TrialHandler2) and thisSize_judgment_trial.thisN != size_judgment_trials.thisTrial.thisN:
            continueRoutine = False
        size_judgment_feedback.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *turtle_half_circle_for_size_judgment_feedback* updates
            
            # if turtle_half_circle_for_size_judgment_feedback is starting this frame...
            if turtle_half_circle_for_size_judgment_feedback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                turtle_half_circle_for_size_judgment_feedback.frameNStart = frameN  # exact frame index
                turtle_half_circle_for_size_judgment_feedback.tStart = t  # local t and not account for scr refresh
                turtle_half_circle_for_size_judgment_feedback.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(turtle_half_circle_for_size_judgment_feedback, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'turtle_half_circle_for_size_judgment_feedback.started')
                # update status
                turtle_half_circle_for_size_judgment_feedback.status = STARTED
                turtle_half_circle_for_size_judgment_feedback.setAutoDraw(True)
            
            # if turtle_half_circle_for_size_judgment_feedback is active this frame...
            if turtle_half_circle_for_size_judgment_feedback.status == STARTED:
                # update params
                pass
            
            # if turtle_half_circle_for_size_judgment_feedback is stopping this frame...
            if turtle_half_circle_for_size_judgment_feedback.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > turtle_half_circle_for_size_judgment_feedback.tStartRefresh + size_feedback_dur-frameTolerance:
                    # keep track of stop time/frame for later
                    turtle_half_circle_for_size_judgment_feedback.tStop = t  # not accounting for scr refresh
                    turtle_half_circle_for_size_judgment_feedback.tStopRefresh = tThisFlipGlobal  # on global time
                    turtle_half_circle_for_size_judgment_feedback.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'turtle_half_circle_for_size_judgment_feedback.stopped')
                    # update status
                    turtle_half_circle_for_size_judgment_feedback.status = FINISHED
                    turtle_half_circle_for_size_judgment_feedback.setAutoDraw(False)
            
            # *turtle_wedge_for_size_judgment_feedback* updates
            
            # if turtle_wedge_for_size_judgment_feedback is starting this frame...
            if turtle_wedge_for_size_judgment_feedback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                turtle_wedge_for_size_judgment_feedback.frameNStart = frameN  # exact frame index
                turtle_wedge_for_size_judgment_feedback.tStart = t  # local t and not account for scr refresh
                turtle_wedge_for_size_judgment_feedback.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(turtle_wedge_for_size_judgment_feedback, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'turtle_wedge_for_size_judgment_feedback.started')
                # update status
                turtle_wedge_for_size_judgment_feedback.status = STARTED
                turtle_wedge_for_size_judgment_feedback.setAutoDraw(True)
            
            # if turtle_wedge_for_size_judgment_feedback is active this frame...
            if turtle_wedge_for_size_judgment_feedback.status == STARTED:
                # update params
                pass
            
            # if turtle_wedge_for_size_judgment_feedback is stopping this frame...
            if turtle_wedge_for_size_judgment_feedback.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > turtle_wedge_for_size_judgment_feedback.tStartRefresh + size_feedback_dur-frameTolerance:
                    # keep track of stop time/frame for later
                    turtle_wedge_for_size_judgment_feedback.tStop = t  # not accounting for scr refresh
                    turtle_wedge_for_size_judgment_feedback.tStopRefresh = tThisFlipGlobal  # on global time
                    turtle_wedge_for_size_judgment_feedback.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'turtle_wedge_for_size_judgment_feedback.stopped')
                    # update status
                    turtle_wedge_for_size_judgment_feedback.status = FINISHED
                    turtle_wedge_for_size_judgment_feedback.setAutoDraw(False)
            
            # *turtle_boundary_for_size_judgment_feedback* updates
            
            # if turtle_boundary_for_size_judgment_feedback is starting this frame...
            if turtle_boundary_for_size_judgment_feedback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                turtle_boundary_for_size_judgment_feedback.frameNStart = frameN  # exact frame index
                turtle_boundary_for_size_judgment_feedback.tStart = t  # local t and not account for scr refresh
                turtle_boundary_for_size_judgment_feedback.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(turtle_boundary_for_size_judgment_feedback, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'turtle_boundary_for_size_judgment_feedback.started')
                # update status
                turtle_boundary_for_size_judgment_feedback.status = STARTED
                turtle_boundary_for_size_judgment_feedback.setAutoDraw(True)
            
            # if turtle_boundary_for_size_judgment_feedback is active this frame...
            if turtle_boundary_for_size_judgment_feedback.status == STARTED:
                # update params
                pass
            
            # if turtle_boundary_for_size_judgment_feedback is stopping this frame...
            if turtle_boundary_for_size_judgment_feedback.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > turtle_boundary_for_size_judgment_feedback.tStartRefresh + size_feedback_dur-frameTolerance:
                    # keep track of stop time/frame for later
                    turtle_boundary_for_size_judgment_feedback.tStop = t  # not accounting for scr refresh
                    turtle_boundary_for_size_judgment_feedback.tStopRefresh = tThisFlipGlobal  # on global time
                    turtle_boundary_for_size_judgment_feedback.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'turtle_boundary_for_size_judgment_feedback.stopped')
                    # update status
                    turtle_boundary_for_size_judgment_feedback.status = FINISHED
                    turtle_boundary_for_size_judgment_feedback.setAutoDraw(False)
            
            # *size_feedback_text_display* updates
            
            # if size_feedback_text_display is starting this frame...
            if size_feedback_text_display.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                size_feedback_text_display.frameNStart = frameN  # exact frame index
                size_feedback_text_display.tStart = t  # local t and not account for scr refresh
                size_feedback_text_display.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(size_feedback_text_display, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'size_feedback_text_display.started')
                # update status
                size_feedback_text_display.status = STARTED
                size_feedback_text_display.setAutoDraw(True)
            
            # if size_feedback_text_display is active this frame...
            if size_feedback_text_display.status == STARTED:
                # update params
                pass
            
            # if size_feedback_text_display is stopping this frame...
            if size_feedback_text_display.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > size_feedback_text_display.tStartRefresh + size_feedback_dur-frameTolerance:
                    # keep track of stop time/frame for later
                    size_feedback_text_display.tStop = t  # not accounting for scr refresh
                    size_feedback_text_display.tStopRefresh = tThisFlipGlobal  # on global time
                    size_feedback_text_display.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'size_feedback_text_display.stopped')
                    # update status
                    size_feedback_text_display.status = FINISHED
                    size_feedback_text_display.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                size_judgment_feedback.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in size_judgment_feedback.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "size_judgment_feedback" ---
        for thisComponent in size_judgment_feedback.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for size_judgment_feedback
        size_judgment_feedback.tStop = globalClock.getTime(format='float')
        size_judgment_feedback.tStopRefresh = tThisFlipGlobal
        thisExp.addData('size_judgment_feedback.stopped', size_judgment_feedback.tStop)
        # the Routine "size_judgment_feedback" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "blank" ---
        # create an object to store info about Routine blank
        blank = data.Routine(
            name='blank',
            components=[text_2],
        )
        blank.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for blank
        blank.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        blank.tStart = globalClock.getTime(format='float')
        blank.status = STARTED
        thisExp.addData('blank.started', blank.tStart)
        blank.maxDuration = None
        # keep track of which components have finished
        blankComponents = blank.components
        for thisComponent in blank.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "blank" ---
        # if trial has changed, end Routine now
        if isinstance(size_judgment_trials, data.TrialHandler2) and thisSize_judgment_trial.thisN != size_judgment_trials.thisTrial.thisN:
            continueRoutine = False
        blank.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 0.2:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_2* updates
            
            # if text_2 is starting this frame...
            if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_2.frameNStart = frameN  # exact frame index
                text_2.tStart = t  # local t and not account for scr refresh
                text_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_2.started')
                # update status
                text_2.status = STARTED
                text_2.setAutoDraw(True)
            
            # if text_2 is active this frame...
            if text_2.status == STARTED:
                # update params
                pass
            
            # if text_2 is stopping this frame...
            if text_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_2.tStartRefresh + .2-frameTolerance:
                    # keep track of stop time/frame for later
                    text_2.tStop = t  # not accounting for scr refresh
                    text_2.tStopRefresh = tThisFlipGlobal  # on global time
                    text_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_2.stopped')
                    # update status
                    text_2.status = FINISHED
                    text_2.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                blank.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in blank.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "blank" ---
        for thisComponent in blank.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for blank
        blank.tStop = globalClock.getTime(format='float')
        blank.tStopRefresh = tThisFlipGlobal
        thisExp.addData('blank.stopped', blank.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if blank.maxDurationReached:
            routineTimer.addTime(-blank.maxDuration)
        elif blank.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-0.200000)
        
        # --- Prepare to start Routine "del_corr_size_resp_tmp" ---
        # create an object to store info about Routine del_corr_size_resp_tmp
        del_corr_size_resp_tmp = data.Routine(
            name='del_corr_size_resp_tmp',
            components=[],
        )
        del_corr_size_resp_tmp.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from del_corr_resp_size_tmp_code
        del corr_resp_size_tmp
        # store start times for del_corr_size_resp_tmp
        del_corr_size_resp_tmp.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        del_corr_size_resp_tmp.tStart = globalClock.getTime(format='float')
        del_corr_size_resp_tmp.status = STARTED
        thisExp.addData('del_corr_size_resp_tmp.started', del_corr_size_resp_tmp.tStart)
        del_corr_size_resp_tmp.maxDuration = None
        # keep track of which components have finished
        del_corr_size_resp_tmpComponents = del_corr_size_resp_tmp.components
        for thisComponent in del_corr_size_resp_tmp.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "del_corr_size_resp_tmp" ---
        # if trial has changed, end Routine now
        if isinstance(size_judgment_trials, data.TrialHandler2) and thisSize_judgment_trial.thisN != size_judgment_trials.thisTrial.thisN:
            continueRoutine = False
        del_corr_size_resp_tmp.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                del_corr_size_resp_tmp.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in del_corr_size_resp_tmp.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "del_corr_size_resp_tmp" ---
        for thisComponent in del_corr_size_resp_tmp.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for del_corr_size_resp_tmp
        del_corr_size_resp_tmp.tStop = globalClock.getTime(format='float')
        del_corr_size_resp_tmp.tStopRefresh = tThisFlipGlobal
        thisExp.addData('del_corr_size_resp_tmp.stopped', del_corr_size_resp_tmp.tStop)
        # the Routine "del_corr_size_resp_tmp" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed num_size_blocks repeats of 'size_judgment_trials'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "index" ---
    # create an object to store info about Routine index
    index = data.Routine(
        name='index',
        components=[],
    )
    index.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from index_setup
    i=0
    # store start times for index
    index.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    index.tStart = globalClock.getTime(format='float')
    index.status = STARTED
    thisExp.addData('index.started', index.tStart)
    index.maxDuration = None
    # keep track of which components have finished
    indexComponents = index.components
    for thisComponent in index.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "index" ---
    index.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            index.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in index.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "index" ---
    for thisComponent in index.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for index
    index.tStop = globalClock.getTime(format='float')
    index.tStopRefresh = tThisFlipGlobal
    thisExp.addData('index.stopped', index.tStop)
    thisExp.nextEntry()
    # the Routine "index" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    transfer_trials = data.TrialHandler2(
        name='transfer_trials',
        nReps=2.0, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=[None], 
        seed=None, 
    )
    thisExp.addLoop(transfer_trials)  # add the loop to the experiment
    thisTransfer_trial = transfer_trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTransfer_trial.rgb)
    if thisTransfer_trial != None:
        for paramName in thisTransfer_trial:
            globals()[paramName] = thisTransfer_trial[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisTransfer_trial in transfer_trials:
        currentLoop = transfer_trials
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisTransfer_trial.rgb)
        if thisTransfer_trial != None:
            for paramName in thisTransfer_trial:
                globals()[paramName] = thisTransfer_trial[paramName]
        
        # --- Prepare to start Routine "transfer_loop_setup" ---
        # create an object to store info about Routine transfer_loop_setup
        transfer_loop_setup = data.Routine(
            name='transfer_loop_setup',
            components=[],
        )
        transfer_loop_setup.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from index_update
        if i==0:
            if condition=="switch/standard":
                num_repeats_1=0
                num_repeats_2=num_transfer_blocks
                do_standard_instructions=0
                do_switch_instructions=1
            elif condition=="standard/switch":
                num_repeats_1=num_transfer_blocks
                num_repeats_2=0
                do_standard_instructions=1
                do_switch_instructions=0
        elif i==1:
            if condition=="switch/standard":
                num_repeats_1=num_transfer_blocks
                num_repeats_2=0
                do_standard_instructions=1
                do_switch_instructions=0
            elif condition=="standard/switch":
                num_repeats_1=0
                num_repeats_2=num_transfer_blocks
                do_standard_instructions=0
                do_switch_instructions=1
        i=i+1
        # store start times for transfer_loop_setup
        transfer_loop_setup.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        transfer_loop_setup.tStart = globalClock.getTime(format='float')
        transfer_loop_setup.status = STARTED
        thisExp.addData('transfer_loop_setup.started', transfer_loop_setup.tStart)
        transfer_loop_setup.maxDuration = None
        # keep track of which components have finished
        transfer_loop_setupComponents = transfer_loop_setup.components
        for thisComponent in transfer_loop_setup.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "transfer_loop_setup" ---
        # if trial has changed, end Routine now
        if isinstance(transfer_trials, data.TrialHandler2) and thisTransfer_trial.thisN != transfer_trials.thisTrial.thisN:
            continueRoutine = False
        transfer_loop_setup.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                transfer_loop_setup.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in transfer_loop_setup.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "transfer_loop_setup" ---
        for thisComponent in transfer_loop_setup.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for transfer_loop_setup
        transfer_loop_setup.tStop = globalClock.getTime(format='float')
        transfer_loop_setup.tStopRefresh = tThisFlipGlobal
        thisExp.addData('transfer_loop_setup.stopped', transfer_loop_setup.tStop)
        # the Routine "transfer_loop_setup" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        transfer_standard_instructions_loop = data.TrialHandler2(
            name='transfer_standard_instructions_loop',
            nReps=do_standard_instructions, 
            method='sequential', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=[None], 
            seed=None, 
        )
        thisExp.addLoop(transfer_standard_instructions_loop)  # add the loop to the experiment
        thisTransfer_standard_instructions_loop = transfer_standard_instructions_loop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTransfer_standard_instructions_loop.rgb)
        if thisTransfer_standard_instructions_loop != None:
            for paramName in thisTransfer_standard_instructions_loop:
                globals()[paramName] = thisTransfer_standard_instructions_loop[paramName]
        
        for thisTransfer_standard_instructions_loop in transfer_standard_instructions_loop:
            currentLoop = transfer_standard_instructions_loop
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            # abbreviate parameter names if possible (e.g. rgb = thisTransfer_standard_instructions_loop.rgb)
            if thisTransfer_standard_instructions_loop != None:
                for paramName in thisTransfer_standard_instructions_loop:
                    globals()[paramName] = thisTransfer_standard_instructions_loop[paramName]
            
            # --- Prepare to start Routine "transfer_standard_instructions_p1" ---
            # create an object to store info about Routine transfer_standard_instructions_p1
            transfer_standard_instructions_p1 = data.Routine(
                name='transfer_standard_instructions_p1',
                components=[transfer_standard_instructions_text_1, space_7, space_8],
            )
            transfer_standard_instructions_p1.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # create starting attributes for space_8
            space_8.keys = []
            space_8.rt = []
            _space_8_allKeys = []
            # store start times for transfer_standard_instructions_p1
            transfer_standard_instructions_p1.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            transfer_standard_instructions_p1.tStart = globalClock.getTime(format='float')
            transfer_standard_instructions_p1.status = STARTED
            thisExp.addData('transfer_standard_instructions_p1.started', transfer_standard_instructions_p1.tStart)
            transfer_standard_instructions_p1.maxDuration = None
            # keep track of which components have finished
            transfer_standard_instructions_p1Components = transfer_standard_instructions_p1.components
            for thisComponent in transfer_standard_instructions_p1.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "transfer_standard_instructions_p1" ---
            # if trial has changed, end Routine now
            if isinstance(transfer_standard_instructions_loop, data.TrialHandler2) and thisTransfer_standard_instructions_loop.thisN != transfer_standard_instructions_loop.thisTrial.thisN:
                continueRoutine = False
            transfer_standard_instructions_p1.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *transfer_standard_instructions_text_1* updates
                
                # if transfer_standard_instructions_text_1 is starting this frame...
                if transfer_standard_instructions_text_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    transfer_standard_instructions_text_1.frameNStart = frameN  # exact frame index
                    transfer_standard_instructions_text_1.tStart = t  # local t and not account for scr refresh
                    transfer_standard_instructions_text_1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(transfer_standard_instructions_text_1, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'transfer_standard_instructions_text_1.started')
                    # update status
                    transfer_standard_instructions_text_1.status = STARTED
                    transfer_standard_instructions_text_1.setAutoDraw(True)
                
                # if transfer_standard_instructions_text_1 is active this frame...
                if transfer_standard_instructions_text_1.status == STARTED:
                    # update params
                    pass
                
                # *space_7* updates
                
                # if space_7 is starting this frame...
                if space_7.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                    # keep track of start time/frame for later
                    space_7.frameNStart = frameN  # exact frame index
                    space_7.tStart = t  # local t and not account for scr refresh
                    space_7.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(space_7, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'space_7.started')
                    # update status
                    space_7.status = STARTED
                    space_7.setAutoDraw(True)
                
                # if space_7 is active this frame...
                if space_7.status == STARTED:
                    # update params
                    pass
                
                # *space_8* updates
                waitOnFlip = False
                
                # if space_8 is starting this frame...
                if space_8.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                    # keep track of start time/frame for later
                    space_8.frameNStart = frameN  # exact frame index
                    space_8.tStart = t  # local t and not account for scr refresh
                    space_8.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(space_8, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'space_8.started')
                    # update status
                    space_8.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(space_8.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(space_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if space_8.status == STARTED and not waitOnFlip:
                    theseKeys = space_8.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                    _space_8_allKeys.extend(theseKeys)
                    if len(_space_8_allKeys):
                        space_8.keys = _space_8_allKeys[-1].name  # just the last key pressed
                        space_8.rt = _space_8_allKeys[-1].rt
                        space_8.duration = _space_8_allKeys[-1].duration
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    transfer_standard_instructions_p1.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in transfer_standard_instructions_p1.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "transfer_standard_instructions_p1" ---
            for thisComponent in transfer_standard_instructions_p1.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for transfer_standard_instructions_p1
            transfer_standard_instructions_p1.tStop = globalClock.getTime(format='float')
            transfer_standard_instructions_p1.tStopRefresh = tThisFlipGlobal
            thisExp.addData('transfer_standard_instructions_p1.stopped', transfer_standard_instructions_p1.tStop)
            # check responses
            if space_8.keys in ['', [], None]:  # No response was made
                space_8.keys = None
            transfer_standard_instructions_loop.addData('space_8.keys',space_8.keys)
            if space_8.keys != None:  # we had a response
                transfer_standard_instructions_loop.addData('space_8.rt', space_8.rt)
                transfer_standard_instructions_loop.addData('space_8.duration', space_8.duration)
            # the Routine "transfer_standard_instructions_p1" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "transfer_standard_instructions_p2" ---
            # create an object to store info about Routine transfer_standard_instructions_p2
            transfer_standard_instructions_p2 = data.Routine(
                name='transfer_standard_instructions_p2',
                components=[transfer_standard_instructions_text, space_9, space_10],
            )
            transfer_standard_instructions_p2.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # create starting attributes for space_10
            space_10.keys = []
            space_10.rt = []
            _space_10_allKeys = []
            # store start times for transfer_standard_instructions_p2
            transfer_standard_instructions_p2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            transfer_standard_instructions_p2.tStart = globalClock.getTime(format='float')
            transfer_standard_instructions_p2.status = STARTED
            thisExp.addData('transfer_standard_instructions_p2.started', transfer_standard_instructions_p2.tStart)
            transfer_standard_instructions_p2.maxDuration = None
            # keep track of which components have finished
            transfer_standard_instructions_p2Components = transfer_standard_instructions_p2.components
            for thisComponent in transfer_standard_instructions_p2.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "transfer_standard_instructions_p2" ---
            # if trial has changed, end Routine now
            if isinstance(transfer_standard_instructions_loop, data.TrialHandler2) and thisTransfer_standard_instructions_loop.thisN != transfer_standard_instructions_loop.thisTrial.thisN:
                continueRoutine = False
            transfer_standard_instructions_p2.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *transfer_standard_instructions_text* updates
                
                # if transfer_standard_instructions_text is starting this frame...
                if transfer_standard_instructions_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    transfer_standard_instructions_text.frameNStart = frameN  # exact frame index
                    transfer_standard_instructions_text.tStart = t  # local t and not account for scr refresh
                    transfer_standard_instructions_text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(transfer_standard_instructions_text, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'transfer_standard_instructions_text.started')
                    # update status
                    transfer_standard_instructions_text.status = STARTED
                    transfer_standard_instructions_text.setAutoDraw(True)
                
                # if transfer_standard_instructions_text is active this frame...
                if transfer_standard_instructions_text.status == STARTED:
                    # update params
                    pass
                
                # *space_9* updates
                
                # if space_9 is starting this frame...
                if space_9.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                    # keep track of start time/frame for later
                    space_9.frameNStart = frameN  # exact frame index
                    space_9.tStart = t  # local t and not account for scr refresh
                    space_9.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(space_9, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'space_9.started')
                    # update status
                    space_9.status = STARTED
                    space_9.setAutoDraw(True)
                
                # if space_9 is active this frame...
                if space_9.status == STARTED:
                    # update params
                    pass
                
                # *space_10* updates
                waitOnFlip = False
                
                # if space_10 is starting this frame...
                if space_10.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                    # keep track of start time/frame for later
                    space_10.frameNStart = frameN  # exact frame index
                    space_10.tStart = t  # local t and not account for scr refresh
                    space_10.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(space_10, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'space_10.started')
                    # update status
                    space_10.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(space_10.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(space_10.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if space_10.status == STARTED and not waitOnFlip:
                    theseKeys = space_10.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                    _space_10_allKeys.extend(theseKeys)
                    if len(_space_10_allKeys):
                        space_10.keys = _space_10_allKeys[-1].name  # just the last key pressed
                        space_10.rt = _space_10_allKeys[-1].rt
                        space_10.duration = _space_10_allKeys[-1].duration
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    transfer_standard_instructions_p2.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in transfer_standard_instructions_p2.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "transfer_standard_instructions_p2" ---
            for thisComponent in transfer_standard_instructions_p2.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for transfer_standard_instructions_p2
            transfer_standard_instructions_p2.tStop = globalClock.getTime(format='float')
            transfer_standard_instructions_p2.tStopRefresh = tThisFlipGlobal
            thisExp.addData('transfer_standard_instructions_p2.stopped', transfer_standard_instructions_p2.tStop)
            # check responses
            if space_10.keys in ['', [], None]:  # No response was made
                space_10.keys = None
            transfer_standard_instructions_loop.addData('space_10.keys',space_10.keys)
            if space_10.keys != None:  # we had a response
                transfer_standard_instructions_loop.addData('space_10.rt', space_10.rt)
                transfer_standard_instructions_loop.addData('space_10.duration', space_10.duration)
            # the Routine "transfer_standard_instructions_p2" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "transfer_standard_instructions_p3" ---
            # create an object to store info about Routine transfer_standard_instructions_p3
            transfer_standard_instructions_p3 = data.Routine(
                name='transfer_standard_instructions_p3',
                components=[transfer_standard_instructions_text_2, space_11, space_12],
            )
            transfer_standard_instructions_p3.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # create starting attributes for space_12
            space_12.keys = []
            space_12.rt = []
            _space_12_allKeys = []
            # store start times for transfer_standard_instructions_p3
            transfer_standard_instructions_p3.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            transfer_standard_instructions_p3.tStart = globalClock.getTime(format='float')
            transfer_standard_instructions_p3.status = STARTED
            thisExp.addData('transfer_standard_instructions_p3.started', transfer_standard_instructions_p3.tStart)
            transfer_standard_instructions_p3.maxDuration = None
            # keep track of which components have finished
            transfer_standard_instructions_p3Components = transfer_standard_instructions_p3.components
            for thisComponent in transfer_standard_instructions_p3.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "transfer_standard_instructions_p3" ---
            # if trial has changed, end Routine now
            if isinstance(transfer_standard_instructions_loop, data.TrialHandler2) and thisTransfer_standard_instructions_loop.thisN != transfer_standard_instructions_loop.thisTrial.thisN:
                continueRoutine = False
            transfer_standard_instructions_p3.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *transfer_standard_instructions_text_2* updates
                
                # if transfer_standard_instructions_text_2 is starting this frame...
                if transfer_standard_instructions_text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    transfer_standard_instructions_text_2.frameNStart = frameN  # exact frame index
                    transfer_standard_instructions_text_2.tStart = t  # local t and not account for scr refresh
                    transfer_standard_instructions_text_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(transfer_standard_instructions_text_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'transfer_standard_instructions_text_2.started')
                    # update status
                    transfer_standard_instructions_text_2.status = STARTED
                    transfer_standard_instructions_text_2.setAutoDraw(True)
                
                # if transfer_standard_instructions_text_2 is active this frame...
                if transfer_standard_instructions_text_2.status == STARTED:
                    # update params
                    pass
                
                # *space_11* updates
                
                # if space_11 is starting this frame...
                if space_11.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                    # keep track of start time/frame for later
                    space_11.frameNStart = frameN  # exact frame index
                    space_11.tStart = t  # local t and not account for scr refresh
                    space_11.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(space_11, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'space_11.started')
                    # update status
                    space_11.status = STARTED
                    space_11.setAutoDraw(True)
                
                # if space_11 is active this frame...
                if space_11.status == STARTED:
                    # update params
                    pass
                
                # *space_12* updates
                waitOnFlip = False
                
                # if space_12 is starting this frame...
                if space_12.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                    # keep track of start time/frame for later
                    space_12.frameNStart = frameN  # exact frame index
                    space_12.tStart = t  # local t and not account for scr refresh
                    space_12.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(space_12, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'space_12.started')
                    # update status
                    space_12.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(space_12.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(space_12.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if space_12.status == STARTED and not waitOnFlip:
                    theseKeys = space_12.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                    _space_12_allKeys.extend(theseKeys)
                    if len(_space_12_allKeys):
                        space_12.keys = _space_12_allKeys[-1].name  # just the last key pressed
                        space_12.rt = _space_12_allKeys[-1].rt
                        space_12.duration = _space_12_allKeys[-1].duration
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    transfer_standard_instructions_p3.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in transfer_standard_instructions_p3.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "transfer_standard_instructions_p3" ---
            for thisComponent in transfer_standard_instructions_p3.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for transfer_standard_instructions_p3
            transfer_standard_instructions_p3.tStop = globalClock.getTime(format='float')
            transfer_standard_instructions_p3.tStopRefresh = tThisFlipGlobal
            thisExp.addData('transfer_standard_instructions_p3.stopped', transfer_standard_instructions_p3.tStop)
            # check responses
            if space_12.keys in ['', [], None]:  # No response was made
                space_12.keys = None
            transfer_standard_instructions_loop.addData('space_12.keys',space_12.keys)
            if space_12.keys != None:  # we had a response
                transfer_standard_instructions_loop.addData('space_12.rt', space_12.rt)
                transfer_standard_instructions_loop.addData('space_12.duration', space_12.duration)
            # the Routine "transfer_standard_instructions_p3" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
        # completed do_standard_instructions repeats of 'transfer_standard_instructions_loop'
        
        
        # set up handler to look after randomisation of conditions etc
        transfer_standard = data.TrialHandler2(
            name='transfer_standard',
            nReps=num_repeats_1, 
            method='random', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=data.importConditions('stim/stim_transfer_standard.csv'), 
            seed=None, 
        )
        thisExp.addLoop(transfer_standard)  # add the loop to the experiment
        thisTransfer_standard = transfer_standard.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTransfer_standard.rgb)
        if thisTransfer_standard != None:
            for paramName in thisTransfer_standard:
                globals()[paramName] = thisTransfer_standard[paramName]
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        for thisTransfer_standard in transfer_standard:
            currentLoop = transfer_standard
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            # abbreviate parameter names if possible (e.g. rgb = thisTransfer_standard.rgb)
            if thisTransfer_standard != None:
                for paramName in thisTransfer_standard:
                    globals()[paramName] = thisTransfer_standard[paramName]
            
            # --- Prepare to start Routine "fixation_cross" ---
            # create an object to store info about Routine fixation_cross
            fixation_cross = data.Routine(
                name='fixation_cross',
                components=[fixation_cross_1],
            )
            fixation_cross.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # store start times for fixation_cross
            fixation_cross.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            fixation_cross.tStart = globalClock.getTime(format='float')
            fixation_cross.status = STARTED
            thisExp.addData('fixation_cross.started', fixation_cross.tStart)
            fixation_cross.maxDuration = None
            # keep track of which components have finished
            fixation_crossComponents = fixation_cross.components
            for thisComponent in fixation_cross.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "fixation_cross" ---
            # if trial has changed, end Routine now
            if isinstance(transfer_standard, data.TrialHandler2) and thisTransfer_standard.thisN != transfer_standard.thisTrial.thisN:
                continueRoutine = False
            fixation_cross.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 0.4:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *fixation_cross_1* updates
                
                # if fixation_cross_1 is starting this frame...
                if fixation_cross_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    fixation_cross_1.frameNStart = frameN  # exact frame index
                    fixation_cross_1.tStart = t  # local t and not account for scr refresh
                    fixation_cross_1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(fixation_cross_1, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixation_cross_1.started')
                    # update status
                    fixation_cross_1.status = STARTED
                    fixation_cross_1.setAutoDraw(True)
                
                # if fixation_cross_1 is active this frame...
                if fixation_cross_1.status == STARTED:
                    # update params
                    pass
                
                # if fixation_cross_1 is stopping this frame...
                if fixation_cross_1.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > fixation_cross_1.tStartRefresh + .4-frameTolerance:
                        # keep track of stop time/frame for later
                        fixation_cross_1.tStop = t  # not accounting for scr refresh
                        fixation_cross_1.tStopRefresh = tThisFlipGlobal  # on global time
                        fixation_cross_1.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'fixation_cross_1.stopped')
                        # update status
                        fixation_cross_1.status = FINISHED
                        fixation_cross_1.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    fixation_cross.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in fixation_cross.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "fixation_cross" ---
            for thisComponent in fixation_cross.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for fixation_cross
            fixation_cross.tStop = globalClock.getTime(format='float')
            fixation_cross.tStopRefresh = tThisFlipGlobal
            thisExp.addData('fixation_cross.stopped', fixation_cross.tStop)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if fixation_cross.maxDurationReached:
                routineTimer.addTime(-fixation_cross.maxDuration)
            elif fixation_cross.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-0.400000)
            
            # --- Prepare to start Routine "blank" ---
            # create an object to store info about Routine blank
            blank = data.Routine(
                name='blank',
                components=[text_2],
            )
            blank.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # store start times for blank
            blank.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            blank.tStart = globalClock.getTime(format='float')
            blank.status = STARTED
            thisExp.addData('blank.started', blank.tStart)
            blank.maxDuration = None
            # keep track of which components have finished
            blankComponents = blank.components
            for thisComponent in blank.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "blank" ---
            # if trial has changed, end Routine now
            if isinstance(transfer_standard, data.TrialHandler2) and thisTransfer_standard.thisN != transfer_standard.thisTrial.thisN:
                continueRoutine = False
            blank.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 0.2:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *text_2* updates
                
                # if text_2 is starting this frame...
                if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_2.frameNStart = frameN  # exact frame index
                    text_2.tStart = t  # local t and not account for scr refresh
                    text_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_2.started')
                    # update status
                    text_2.status = STARTED
                    text_2.setAutoDraw(True)
                
                # if text_2 is active this frame...
                if text_2.status == STARTED:
                    # update params
                    pass
                
                # if text_2 is stopping this frame...
                if text_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text_2.tStartRefresh + .2-frameTolerance:
                        # keep track of stop time/frame for later
                        text_2.tStop = t  # not accounting for scr refresh
                        text_2.tStopRefresh = tThisFlipGlobal  # on global time
                        text_2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text_2.stopped')
                        # update status
                        text_2.status = FINISHED
                        text_2.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    blank.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in blank.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "blank" ---
            for thisComponent in blank.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for blank
            blank.tStop = globalClock.getTime(format='float')
            blank.tStopRefresh = tThisFlipGlobal
            thisExp.addData('blank.stopped', blank.tStop)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if blank.maxDurationReached:
                routineTimer.addTime(-blank.maxDuration)
            elif blank.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-0.200000)
            
            # --- Prepare to start Routine "transfer_response_standard" ---
            # create an object to store info about Routine transfer_response_standard
            transfer_response_standard = data.Routine(
                name='transfer_response_standard',
                components=[transfer_prompt_standard_trials, key_resp_transfer_standard, turtle_halfcircle_standard, turtle_wedge_standard, turtle_wedge_boundary_standard],
            )
            transfer_response_standard.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from get_turtle_params_transfer_standard
            turtle_halfcircle_vertices = get_turtle_halfcircle_vertices(radius)
            turtle_wedge_vertices = get_turtle_wedge_vertices(angle)
            
            transfer_prompt_standard_trials.setText('Is this turtle in Species F or Species J? \n\nF - Species F, J - Species J')
            # create starting attributes for key_resp_transfer_standard
            key_resp_transfer_standard.keys = []
            key_resp_transfer_standard.rt = []
            _key_resp_transfer_standard_allKeys = []
            turtle_halfcircle_standard.setVertices(turtle_halfcircle_vertices)
            turtle_wedge_standard.setVertices(turtle_wedge_vertices)
            # store start times for transfer_response_standard
            transfer_response_standard.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            transfer_response_standard.tStart = globalClock.getTime(format='float')
            transfer_response_standard.status = STARTED
            thisExp.addData('transfer_response_standard.started', transfer_response_standard.tStart)
            transfer_response_standard.maxDuration = None
            # keep track of which components have finished
            transfer_response_standardComponents = transfer_response_standard.components
            for thisComponent in transfer_response_standard.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "transfer_response_standard" ---
            # if trial has changed, end Routine now
            if isinstance(transfer_standard, data.TrialHandler2) and thisTransfer_standard.thisN != transfer_standard.thisTrial.thisN:
                continueRoutine = False
            transfer_response_standard.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *transfer_prompt_standard_trials* updates
                
                # if transfer_prompt_standard_trials is starting this frame...
                if transfer_prompt_standard_trials.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    transfer_prompt_standard_trials.frameNStart = frameN  # exact frame index
                    transfer_prompt_standard_trials.tStart = t  # local t and not account for scr refresh
                    transfer_prompt_standard_trials.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(transfer_prompt_standard_trials, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'transfer_prompt_standard_trials.started')
                    # update status
                    transfer_prompt_standard_trials.status = STARTED
                    transfer_prompt_standard_trials.setAutoDraw(True)
                
                # if transfer_prompt_standard_trials is active this frame...
                if transfer_prompt_standard_trials.status == STARTED:
                    # update params
                    pass
                
                # *key_resp_transfer_standard* updates
                waitOnFlip = False
                
                # if key_resp_transfer_standard is starting this frame...
                if key_resp_transfer_standard.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_transfer_standard.frameNStart = frameN  # exact frame index
                    key_resp_transfer_standard.tStart = t  # local t and not account for scr refresh
                    key_resp_transfer_standard.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_transfer_standard, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp_transfer_standard.started')
                    # update status
                    key_resp_transfer_standard.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_transfer_standard.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp_transfer_standard.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp_transfer_standard.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_transfer_standard.getKeys(keyList=['f','j'], ignoreKeys=["escape"], waitRelease=False)
                    _key_resp_transfer_standard_allKeys.extend(theseKeys)
                    if len(_key_resp_transfer_standard_allKeys):
                        key_resp_transfer_standard.keys = _key_resp_transfer_standard_allKeys[-1].name  # just the last key pressed
                        key_resp_transfer_standard.rt = _key_resp_transfer_standard_allKeys[-1].rt
                        key_resp_transfer_standard.duration = _key_resp_transfer_standard_allKeys[-1].duration
                        # a response ends the routine
                        continueRoutine = False
                
                # *turtle_halfcircle_standard* updates
                
                # if turtle_halfcircle_standard is starting this frame...
                if turtle_halfcircle_standard.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    turtle_halfcircle_standard.frameNStart = frameN  # exact frame index
                    turtle_halfcircle_standard.tStart = t  # local t and not account for scr refresh
                    turtle_halfcircle_standard.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(turtle_halfcircle_standard, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'turtle_halfcircle_standard.started')
                    # update status
                    turtle_halfcircle_standard.status = STARTED
                    turtle_halfcircle_standard.setAutoDraw(True)
                
                # if turtle_halfcircle_standard is active this frame...
                if turtle_halfcircle_standard.status == STARTED:
                    # update params
                    pass
                
                # *turtle_wedge_standard* updates
                
                # if turtle_wedge_standard is starting this frame...
                if turtle_wedge_standard.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    turtle_wedge_standard.frameNStart = frameN  # exact frame index
                    turtle_wedge_standard.tStart = t  # local t and not account for scr refresh
                    turtle_wedge_standard.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(turtle_wedge_standard, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'turtle_wedge_standard.started')
                    # update status
                    turtle_wedge_standard.status = STARTED
                    turtle_wedge_standard.setAutoDraw(True)
                
                # if turtle_wedge_standard is active this frame...
                if turtle_wedge_standard.status == STARTED:
                    # update params
                    pass
                
                # *turtle_wedge_boundary_standard* updates
                
                # if turtle_wedge_boundary_standard is starting this frame...
                if turtle_wedge_boundary_standard.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    turtle_wedge_boundary_standard.frameNStart = frameN  # exact frame index
                    turtle_wedge_boundary_standard.tStart = t  # local t and not account for scr refresh
                    turtle_wedge_boundary_standard.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(turtle_wedge_boundary_standard, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'turtle_wedge_boundary_standard.started')
                    # update status
                    turtle_wedge_boundary_standard.status = STARTED
                    turtle_wedge_boundary_standard.setAutoDraw(True)
                
                # if turtle_wedge_boundary_standard is active this frame...
                if turtle_wedge_boundary_standard.status == STARTED:
                    # update params
                    pass
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    transfer_response_standard.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in transfer_response_standard.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "transfer_response_standard" ---
            for thisComponent in transfer_response_standard.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for transfer_response_standard
            transfer_response_standard.tStop = globalClock.getTime(format='float')
            transfer_response_standard.tStopRefresh = tThisFlipGlobal
            thisExp.addData('transfer_response_standard.stopped', transfer_response_standard.tStop)
            # check responses
            if key_resp_transfer_standard.keys in ['', [], None]:  # No response was made
                key_resp_transfer_standard.keys = None
            transfer_standard.addData('key_resp_transfer_standard.keys',key_resp_transfer_standard.keys)
            if key_resp_transfer_standard.keys != None:  # we had a response
                transfer_standard.addData('key_resp_transfer_standard.rt', key_resp_transfer_standard.rt)
                transfer_standard.addData('key_resp_transfer_standard.duration', key_resp_transfer_standard.duration)
            # the Routine "transfer_response_standard" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "blank" ---
            # create an object to store info about Routine blank
            blank = data.Routine(
                name='blank',
                components=[text_2],
            )
            blank.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # store start times for blank
            blank.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            blank.tStart = globalClock.getTime(format='float')
            blank.status = STARTED
            thisExp.addData('blank.started', blank.tStart)
            blank.maxDuration = None
            # keep track of which components have finished
            blankComponents = blank.components
            for thisComponent in blank.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "blank" ---
            # if trial has changed, end Routine now
            if isinstance(transfer_standard, data.TrialHandler2) and thisTransfer_standard.thisN != transfer_standard.thisTrial.thisN:
                continueRoutine = False
            blank.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 0.2:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *text_2* updates
                
                # if text_2 is starting this frame...
                if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_2.frameNStart = frameN  # exact frame index
                    text_2.tStart = t  # local t and not account for scr refresh
                    text_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_2.started')
                    # update status
                    text_2.status = STARTED
                    text_2.setAutoDraw(True)
                
                # if text_2 is active this frame...
                if text_2.status == STARTED:
                    # update params
                    pass
                
                # if text_2 is stopping this frame...
                if text_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text_2.tStartRefresh + .2-frameTolerance:
                        # keep track of stop time/frame for later
                        text_2.tStop = t  # not accounting for scr refresh
                        text_2.tStopRefresh = tThisFlipGlobal  # on global time
                        text_2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text_2.stopped')
                        # update status
                        text_2.status = FINISHED
                        text_2.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    blank.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in blank.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "blank" ---
            for thisComponent in blank.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for blank
            blank.tStop = globalClock.getTime(format='float')
            blank.tStopRefresh = tThisFlipGlobal
            thisExp.addData('blank.stopped', blank.tStop)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if blank.maxDurationReached:
                routineTimer.addTime(-blank.maxDuration)
            elif blank.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-0.200000)
            thisExp.nextEntry()
            
        # completed num_repeats_1 repeats of 'transfer_standard'
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        # set up handler to look after randomisation of conditions etc
        transfer_switch_instructions_loop = data.TrialHandler2(
            name='transfer_switch_instructions_loop',
            nReps=do_switch_instructions, 
            method='sequential', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=[None], 
            seed=None, 
        )
        thisExp.addLoop(transfer_switch_instructions_loop)  # add the loop to the experiment
        thisTransfer_switch_instructions_loop = transfer_switch_instructions_loop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTransfer_switch_instructions_loop.rgb)
        if thisTransfer_switch_instructions_loop != None:
            for paramName in thisTransfer_switch_instructions_loop:
                globals()[paramName] = thisTransfer_switch_instructions_loop[paramName]
        
        for thisTransfer_switch_instructions_loop in transfer_switch_instructions_loop:
            currentLoop = transfer_switch_instructions_loop
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            # abbreviate parameter names if possible (e.g. rgb = thisTransfer_switch_instructions_loop.rgb)
            if thisTransfer_switch_instructions_loop != None:
                for paramName in thisTransfer_switch_instructions_loop:
                    globals()[paramName] = thisTransfer_switch_instructions_loop[paramName]
            
            # --- Prepare to start Routine "transfer_switch_instructions_p1" ---
            # create an object to store info about Routine transfer_switch_instructions_p1
            transfer_switch_instructions_p1 = data.Routine(
                name='transfer_switch_instructions_p1',
                components=[transfer_switch_instructions_text_1, space_13, space_14],
            )
            transfer_switch_instructions_p1.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # create starting attributes for space_14
            space_14.keys = []
            space_14.rt = []
            _space_14_allKeys = []
            # store start times for transfer_switch_instructions_p1
            transfer_switch_instructions_p1.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            transfer_switch_instructions_p1.tStart = globalClock.getTime(format='float')
            transfer_switch_instructions_p1.status = STARTED
            thisExp.addData('transfer_switch_instructions_p1.started', transfer_switch_instructions_p1.tStart)
            transfer_switch_instructions_p1.maxDuration = None
            # keep track of which components have finished
            transfer_switch_instructions_p1Components = transfer_switch_instructions_p1.components
            for thisComponent in transfer_switch_instructions_p1.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "transfer_switch_instructions_p1" ---
            # if trial has changed, end Routine now
            if isinstance(transfer_switch_instructions_loop, data.TrialHandler2) and thisTransfer_switch_instructions_loop.thisN != transfer_switch_instructions_loop.thisTrial.thisN:
                continueRoutine = False
            transfer_switch_instructions_p1.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *transfer_switch_instructions_text_1* updates
                
                # if transfer_switch_instructions_text_1 is starting this frame...
                if transfer_switch_instructions_text_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    transfer_switch_instructions_text_1.frameNStart = frameN  # exact frame index
                    transfer_switch_instructions_text_1.tStart = t  # local t and not account for scr refresh
                    transfer_switch_instructions_text_1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(transfer_switch_instructions_text_1, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'transfer_switch_instructions_text_1.started')
                    # update status
                    transfer_switch_instructions_text_1.status = STARTED
                    transfer_switch_instructions_text_1.setAutoDraw(True)
                
                # if transfer_switch_instructions_text_1 is active this frame...
                if transfer_switch_instructions_text_1.status == STARTED:
                    # update params
                    pass
                
                # *space_13* updates
                
                # if space_13 is starting this frame...
                if space_13.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                    # keep track of start time/frame for later
                    space_13.frameNStart = frameN  # exact frame index
                    space_13.tStart = t  # local t and not account for scr refresh
                    space_13.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(space_13, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'space_13.started')
                    # update status
                    space_13.status = STARTED
                    space_13.setAutoDraw(True)
                
                # if space_13 is active this frame...
                if space_13.status == STARTED:
                    # update params
                    pass
                
                # *space_14* updates
                waitOnFlip = False
                
                # if space_14 is starting this frame...
                if space_14.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                    # keep track of start time/frame for later
                    space_14.frameNStart = frameN  # exact frame index
                    space_14.tStart = t  # local t and not account for scr refresh
                    space_14.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(space_14, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'space_14.started')
                    # update status
                    space_14.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(space_14.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(space_14.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if space_14.status == STARTED and not waitOnFlip:
                    theseKeys = space_14.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                    _space_14_allKeys.extend(theseKeys)
                    if len(_space_14_allKeys):
                        space_14.keys = _space_14_allKeys[-1].name  # just the last key pressed
                        space_14.rt = _space_14_allKeys[-1].rt
                        space_14.duration = _space_14_allKeys[-1].duration
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    transfer_switch_instructions_p1.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in transfer_switch_instructions_p1.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "transfer_switch_instructions_p1" ---
            for thisComponent in transfer_switch_instructions_p1.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for transfer_switch_instructions_p1
            transfer_switch_instructions_p1.tStop = globalClock.getTime(format='float')
            transfer_switch_instructions_p1.tStopRefresh = tThisFlipGlobal
            thisExp.addData('transfer_switch_instructions_p1.stopped', transfer_switch_instructions_p1.tStop)
            # check responses
            if space_14.keys in ['', [], None]:  # No response was made
                space_14.keys = None
            transfer_switch_instructions_loop.addData('space_14.keys',space_14.keys)
            if space_14.keys != None:  # we had a response
                transfer_switch_instructions_loop.addData('space_14.rt', space_14.rt)
                transfer_switch_instructions_loop.addData('space_14.duration', space_14.duration)
            # the Routine "transfer_switch_instructions_p1" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "transfer_switch_instructions_p2" ---
            # create an object to store info about Routine transfer_switch_instructions_p2
            transfer_switch_instructions_p2 = data.Routine(
                name='transfer_switch_instructions_p2',
                components=[transfer_switch_instructions_text_2, space_15, space_16],
            )
            transfer_switch_instructions_p2.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # create starting attributes for space_16
            space_16.keys = []
            space_16.rt = []
            _space_16_allKeys = []
            # store start times for transfer_switch_instructions_p2
            transfer_switch_instructions_p2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            transfer_switch_instructions_p2.tStart = globalClock.getTime(format='float')
            transfer_switch_instructions_p2.status = STARTED
            thisExp.addData('transfer_switch_instructions_p2.started', transfer_switch_instructions_p2.tStart)
            transfer_switch_instructions_p2.maxDuration = None
            # keep track of which components have finished
            transfer_switch_instructions_p2Components = transfer_switch_instructions_p2.components
            for thisComponent in transfer_switch_instructions_p2.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "transfer_switch_instructions_p2" ---
            # if trial has changed, end Routine now
            if isinstance(transfer_switch_instructions_loop, data.TrialHandler2) and thisTransfer_switch_instructions_loop.thisN != transfer_switch_instructions_loop.thisTrial.thisN:
                continueRoutine = False
            transfer_switch_instructions_p2.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *transfer_switch_instructions_text_2* updates
                
                # if transfer_switch_instructions_text_2 is starting this frame...
                if transfer_switch_instructions_text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    transfer_switch_instructions_text_2.frameNStart = frameN  # exact frame index
                    transfer_switch_instructions_text_2.tStart = t  # local t and not account for scr refresh
                    transfer_switch_instructions_text_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(transfer_switch_instructions_text_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'transfer_switch_instructions_text_2.started')
                    # update status
                    transfer_switch_instructions_text_2.status = STARTED
                    transfer_switch_instructions_text_2.setAutoDraw(True)
                
                # if transfer_switch_instructions_text_2 is active this frame...
                if transfer_switch_instructions_text_2.status == STARTED:
                    # update params
                    pass
                
                # *space_15* updates
                
                # if space_15 is starting this frame...
                if space_15.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                    # keep track of start time/frame for later
                    space_15.frameNStart = frameN  # exact frame index
                    space_15.tStart = t  # local t and not account for scr refresh
                    space_15.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(space_15, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'space_15.started')
                    # update status
                    space_15.status = STARTED
                    space_15.setAutoDraw(True)
                
                # if space_15 is active this frame...
                if space_15.status == STARTED:
                    # update params
                    pass
                
                # *space_16* updates
                waitOnFlip = False
                
                # if space_16 is starting this frame...
                if space_16.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                    # keep track of start time/frame for later
                    space_16.frameNStart = frameN  # exact frame index
                    space_16.tStart = t  # local t and not account for scr refresh
                    space_16.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(space_16, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'space_16.started')
                    # update status
                    space_16.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(space_16.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(space_16.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if space_16.status == STARTED and not waitOnFlip:
                    theseKeys = space_16.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                    _space_16_allKeys.extend(theseKeys)
                    if len(_space_16_allKeys):
                        space_16.keys = _space_16_allKeys[-1].name  # just the last key pressed
                        space_16.rt = _space_16_allKeys[-1].rt
                        space_16.duration = _space_16_allKeys[-1].duration
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    transfer_switch_instructions_p2.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in transfer_switch_instructions_p2.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "transfer_switch_instructions_p2" ---
            for thisComponent in transfer_switch_instructions_p2.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for transfer_switch_instructions_p2
            transfer_switch_instructions_p2.tStop = globalClock.getTime(format='float')
            transfer_switch_instructions_p2.tStopRefresh = tThisFlipGlobal
            thisExp.addData('transfer_switch_instructions_p2.stopped', transfer_switch_instructions_p2.tStop)
            # check responses
            if space_16.keys in ['', [], None]:  # No response was made
                space_16.keys = None
            transfer_switch_instructions_loop.addData('space_16.keys',space_16.keys)
            if space_16.keys != None:  # we had a response
                transfer_switch_instructions_loop.addData('space_16.rt', space_16.rt)
                transfer_switch_instructions_loop.addData('space_16.duration', space_16.duration)
            # the Routine "transfer_switch_instructions_p2" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "transfer_switch_instructions_p3" ---
            # create an object to store info about Routine transfer_switch_instructions_p3
            transfer_switch_instructions_p3 = data.Routine(
                name='transfer_switch_instructions_p3',
                components=[transfer_switch_instructions_text, space_17, space_18],
            )
            transfer_switch_instructions_p3.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # create starting attributes for space_18
            space_18.keys = []
            space_18.rt = []
            _space_18_allKeys = []
            # store start times for transfer_switch_instructions_p3
            transfer_switch_instructions_p3.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            transfer_switch_instructions_p3.tStart = globalClock.getTime(format='float')
            transfer_switch_instructions_p3.status = STARTED
            thisExp.addData('transfer_switch_instructions_p3.started', transfer_switch_instructions_p3.tStart)
            transfer_switch_instructions_p3.maxDuration = None
            # keep track of which components have finished
            transfer_switch_instructions_p3Components = transfer_switch_instructions_p3.components
            for thisComponent in transfer_switch_instructions_p3.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "transfer_switch_instructions_p3" ---
            # if trial has changed, end Routine now
            if isinstance(transfer_switch_instructions_loop, data.TrialHandler2) and thisTransfer_switch_instructions_loop.thisN != transfer_switch_instructions_loop.thisTrial.thisN:
                continueRoutine = False
            transfer_switch_instructions_p3.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *transfer_switch_instructions_text* updates
                
                # if transfer_switch_instructions_text is starting this frame...
                if transfer_switch_instructions_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    transfer_switch_instructions_text.frameNStart = frameN  # exact frame index
                    transfer_switch_instructions_text.tStart = t  # local t and not account for scr refresh
                    transfer_switch_instructions_text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(transfer_switch_instructions_text, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'transfer_switch_instructions_text.started')
                    # update status
                    transfer_switch_instructions_text.status = STARTED
                    transfer_switch_instructions_text.setAutoDraw(True)
                
                # if transfer_switch_instructions_text is active this frame...
                if transfer_switch_instructions_text.status == STARTED:
                    # update params
                    pass
                
                # *space_17* updates
                
                # if space_17 is starting this frame...
                if space_17.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                    # keep track of start time/frame for later
                    space_17.frameNStart = frameN  # exact frame index
                    space_17.tStart = t  # local t and not account for scr refresh
                    space_17.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(space_17, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'space_17.started')
                    # update status
                    space_17.status = STARTED
                    space_17.setAutoDraw(True)
                
                # if space_17 is active this frame...
                if space_17.status == STARTED:
                    # update params
                    pass
                
                # *space_18* updates
                waitOnFlip = False
                
                # if space_18 is starting this frame...
                if space_18.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                    # keep track of start time/frame for later
                    space_18.frameNStart = frameN  # exact frame index
                    space_18.tStart = t  # local t and not account for scr refresh
                    space_18.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(space_18, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'space_18.started')
                    # update status
                    space_18.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(space_18.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(space_18.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if space_18.status == STARTED and not waitOnFlip:
                    theseKeys = space_18.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                    _space_18_allKeys.extend(theseKeys)
                    if len(_space_18_allKeys):
                        space_18.keys = _space_18_allKeys[-1].name  # just the last key pressed
                        space_18.rt = _space_18_allKeys[-1].rt
                        space_18.duration = _space_18_allKeys[-1].duration
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    transfer_switch_instructions_p3.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in transfer_switch_instructions_p3.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "transfer_switch_instructions_p3" ---
            for thisComponent in transfer_switch_instructions_p3.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for transfer_switch_instructions_p3
            transfer_switch_instructions_p3.tStop = globalClock.getTime(format='float')
            transfer_switch_instructions_p3.tStopRefresh = tThisFlipGlobal
            thisExp.addData('transfer_switch_instructions_p3.stopped', transfer_switch_instructions_p3.tStop)
            # check responses
            if space_18.keys in ['', [], None]:  # No response was made
                space_18.keys = None
            transfer_switch_instructions_loop.addData('space_18.keys',space_18.keys)
            if space_18.keys != None:  # we had a response
                transfer_switch_instructions_loop.addData('space_18.rt', space_18.rt)
                transfer_switch_instructions_loop.addData('space_18.duration', space_18.duration)
            # the Routine "transfer_switch_instructions_p3" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "transfer_switch_instructions_p4" ---
            # create an object to store info about Routine transfer_switch_instructions_p4
            transfer_switch_instructions_p4 = data.Routine(
                name='transfer_switch_instructions_p4',
                components=[transfer_switch_instructions_text_3, space_to_begin_switch],
            )
            transfer_switch_instructions_p4.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # create starting attributes for space_to_begin_switch
            space_to_begin_switch.keys = []
            space_to_begin_switch.rt = []
            _space_to_begin_switch_allKeys = []
            # store start times for transfer_switch_instructions_p4
            transfer_switch_instructions_p4.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            transfer_switch_instructions_p4.tStart = globalClock.getTime(format='float')
            transfer_switch_instructions_p4.status = STARTED
            thisExp.addData('transfer_switch_instructions_p4.started', transfer_switch_instructions_p4.tStart)
            transfer_switch_instructions_p4.maxDuration = None
            # keep track of which components have finished
            transfer_switch_instructions_p4Components = transfer_switch_instructions_p4.components
            for thisComponent in transfer_switch_instructions_p4.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "transfer_switch_instructions_p4" ---
            # if trial has changed, end Routine now
            if isinstance(transfer_switch_instructions_loop, data.TrialHandler2) and thisTransfer_switch_instructions_loop.thisN != transfer_switch_instructions_loop.thisTrial.thisN:
                continueRoutine = False
            transfer_switch_instructions_p4.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *transfer_switch_instructions_text_3* updates
                
                # if transfer_switch_instructions_text_3 is starting this frame...
                if transfer_switch_instructions_text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    transfer_switch_instructions_text_3.frameNStart = frameN  # exact frame index
                    transfer_switch_instructions_text_3.tStart = t  # local t and not account for scr refresh
                    transfer_switch_instructions_text_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(transfer_switch_instructions_text_3, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'transfer_switch_instructions_text_3.started')
                    # update status
                    transfer_switch_instructions_text_3.status = STARTED
                    transfer_switch_instructions_text_3.setAutoDraw(True)
                
                # if transfer_switch_instructions_text_3 is active this frame...
                if transfer_switch_instructions_text_3.status == STARTED:
                    # update params
                    pass
                
                # *space_to_begin_switch* updates
                waitOnFlip = False
                
                # if space_to_begin_switch is starting this frame...
                if space_to_begin_switch.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    space_to_begin_switch.frameNStart = frameN  # exact frame index
                    space_to_begin_switch.tStart = t  # local t and not account for scr refresh
                    space_to_begin_switch.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(space_to_begin_switch, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'space_to_begin_switch.started')
                    # update status
                    space_to_begin_switch.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(space_to_begin_switch.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(space_to_begin_switch.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if space_to_begin_switch.status == STARTED and not waitOnFlip:
                    theseKeys = space_to_begin_switch.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
                    _space_to_begin_switch_allKeys.extend(theseKeys)
                    if len(_space_to_begin_switch_allKeys):
                        space_to_begin_switch.keys = _space_to_begin_switch_allKeys[-1].name  # just the last key pressed
                        space_to_begin_switch.rt = _space_to_begin_switch_allKeys[-1].rt
                        space_to_begin_switch.duration = _space_to_begin_switch_allKeys[-1].duration
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    transfer_switch_instructions_p4.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in transfer_switch_instructions_p4.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "transfer_switch_instructions_p4" ---
            for thisComponent in transfer_switch_instructions_p4.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for transfer_switch_instructions_p4
            transfer_switch_instructions_p4.tStop = globalClock.getTime(format='float')
            transfer_switch_instructions_p4.tStopRefresh = tThisFlipGlobal
            thisExp.addData('transfer_switch_instructions_p4.stopped', transfer_switch_instructions_p4.tStop)
            # check responses
            if space_to_begin_switch.keys in ['', [], None]:  # No response was made
                space_to_begin_switch.keys = None
            transfer_switch_instructions_loop.addData('space_to_begin_switch.keys',space_to_begin_switch.keys)
            if space_to_begin_switch.keys != None:  # we had a response
                transfer_switch_instructions_loop.addData('space_to_begin_switch.rt', space_to_begin_switch.rt)
                transfer_switch_instructions_loop.addData('space_to_begin_switch.duration', space_to_begin_switch.duration)
            # the Routine "transfer_switch_instructions_p4" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "blank" ---
            # create an object to store info about Routine blank
            blank = data.Routine(
                name='blank',
                components=[text_2],
            )
            blank.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # store start times for blank
            blank.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            blank.tStart = globalClock.getTime(format='float')
            blank.status = STARTED
            thisExp.addData('blank.started', blank.tStart)
            blank.maxDuration = None
            # keep track of which components have finished
            blankComponents = blank.components
            for thisComponent in blank.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "blank" ---
            # if trial has changed, end Routine now
            if isinstance(transfer_switch_instructions_loop, data.TrialHandler2) and thisTransfer_switch_instructions_loop.thisN != transfer_switch_instructions_loop.thisTrial.thisN:
                continueRoutine = False
            blank.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 0.2:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *text_2* updates
                
                # if text_2 is starting this frame...
                if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_2.frameNStart = frameN  # exact frame index
                    text_2.tStart = t  # local t and not account for scr refresh
                    text_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_2.started')
                    # update status
                    text_2.status = STARTED
                    text_2.setAutoDraw(True)
                
                # if text_2 is active this frame...
                if text_2.status == STARTED:
                    # update params
                    pass
                
                # if text_2 is stopping this frame...
                if text_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text_2.tStartRefresh + .2-frameTolerance:
                        # keep track of stop time/frame for later
                        text_2.tStop = t  # not accounting for scr refresh
                        text_2.tStopRefresh = tThisFlipGlobal  # on global time
                        text_2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text_2.stopped')
                        # update status
                        text_2.status = FINISHED
                        text_2.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    blank.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in blank.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "blank" ---
            for thisComponent in blank.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for blank
            blank.tStop = globalClock.getTime(format='float')
            blank.tStopRefresh = tThisFlipGlobal
            thisExp.addData('blank.stopped', blank.tStop)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if blank.maxDurationReached:
                routineTimer.addTime(-blank.maxDuration)
            elif blank.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-0.200000)
        # completed do_switch_instructions repeats of 'transfer_switch_instructions_loop'
        
        
        # set up handler to look after randomisation of conditions etc
        transfer_switch_loop = data.TrialHandler2(
            name='transfer_switch_loop',
            nReps=num_repeats_2, 
            method='sequential', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=[None], 
            seed=None, 
        )
        thisExp.addLoop(transfer_switch_loop)  # add the loop to the experiment
        thisTransfer_switch_loop = transfer_switch_loop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTransfer_switch_loop.rgb)
        if thisTransfer_switch_loop != None:
            for paramName in thisTransfer_switch_loop:
                globals()[paramName] = thisTransfer_switch_loop[paramName]
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        for thisTransfer_switch_loop in transfer_switch_loop:
            currentLoop = transfer_switch_loop
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            # abbreviate parameter names if possible (e.g. rgb = thisTransfer_switch_loop.rgb)
            if thisTransfer_switch_loop != None:
                for paramName in thisTransfer_switch_loop:
                    globals()[paramName] = thisTransfer_switch_loop[paramName]
            
            # --- Prepare to start Routine "randomize_switch_trials" ---
            # create an object to store info about Routine randomize_switch_trials
            randomize_switch_trials = data.Routine(
                name='randomize_switch_trials',
                components=[],
            )
            randomize_switch_trials.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from randomize
            import pandas as pd
            s=pd.read_csv("stim/stim_transfer_switch.csv")
            do_sample=True
            while do_sample:
                s=s.sample(frac=1).reset_index(drop=True)
                X=0
                if s.iloc[0]["trial_type"]=="switch":
                    X=X+1
                for j in range(2,s.shape[0]-1):
                    if (s.iloc[j]["trial_type"]=='switch'):
                        if (s.iloc[j-1]["trial_type"]=='switch'):
                            X=X+1
                if(X==0):
                    do_sample=False
            s.to_csv("stim/stim_transfer_switch_random_tmp.csv",index=False)
            # store start times for randomize_switch_trials
            randomize_switch_trials.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            randomize_switch_trials.tStart = globalClock.getTime(format='float')
            randomize_switch_trials.status = STARTED
            thisExp.addData('randomize_switch_trials.started', randomize_switch_trials.tStart)
            randomize_switch_trials.maxDuration = None
            # keep track of which components have finished
            randomize_switch_trialsComponents = randomize_switch_trials.components
            for thisComponent in randomize_switch_trials.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "randomize_switch_trials" ---
            # if trial has changed, end Routine now
            if isinstance(transfer_switch_loop, data.TrialHandler2) and thisTransfer_switch_loop.thisN != transfer_switch_loop.thisTrial.thisN:
                continueRoutine = False
            randomize_switch_trials.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    randomize_switch_trials.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in randomize_switch_trials.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "randomize_switch_trials" ---
            for thisComponent in randomize_switch_trials.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for randomize_switch_trials
            randomize_switch_trials.tStop = globalClock.getTime(format='float')
            randomize_switch_trials.tStopRefresh = tThisFlipGlobal
            thisExp.addData('randomize_switch_trials.stopped', randomize_switch_trials.tStop)
            # the Routine "randomize_switch_trials" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # set up handler to look after randomisation of conditions etc
            transfer_switch = data.TrialHandler2(
                name='transfer_switch',
                nReps=1.0, 
                method='sequential', 
                extraInfo=expInfo, 
                originPath=-1, 
                trialList=data.importConditions('stim/stim_transfer_switch_random_tmp.csv'), 
                seed=None, 
            )
            thisExp.addLoop(transfer_switch)  # add the loop to the experiment
            thisTransfer_switch = transfer_switch.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisTransfer_switch.rgb)
            if thisTransfer_switch != None:
                for paramName in thisTransfer_switch:
                    globals()[paramName] = thisTransfer_switch[paramName]
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            
            for thisTransfer_switch in transfer_switch:
                currentLoop = transfer_switch
                thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
                if thisSession is not None:
                    # if running in a Session with a Liaison client, send data up to now
                    thisSession.sendExperimentData()
                # abbreviate parameter names if possible (e.g. rgb = thisTransfer_switch.rgb)
                if thisTransfer_switch != None:
                    for paramName in thisTransfer_switch:
                        globals()[paramName] = thisTransfer_switch[paramName]
                
                # --- Prepare to start Routine "fixation_cross" ---
                # create an object to store info about Routine fixation_cross
                fixation_cross = data.Routine(
                    name='fixation_cross',
                    components=[fixation_cross_1],
                )
                fixation_cross.status = NOT_STARTED
                continueRoutine = True
                # update component parameters for each repeat
                # store start times for fixation_cross
                fixation_cross.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
                fixation_cross.tStart = globalClock.getTime(format='float')
                fixation_cross.status = STARTED
                thisExp.addData('fixation_cross.started', fixation_cross.tStart)
                fixation_cross.maxDuration = None
                # keep track of which components have finished
                fixation_crossComponents = fixation_cross.components
                for thisComponent in fixation_cross.components:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "fixation_cross" ---
                # if trial has changed, end Routine now
                if isinstance(transfer_switch, data.TrialHandler2) and thisTransfer_switch.thisN != transfer_switch.thisTrial.thisN:
                    continueRoutine = False
                fixation_cross.forceEnded = routineForceEnded = not continueRoutine
                while continueRoutine and routineTimer.getTime() < 0.4:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *fixation_cross_1* updates
                    
                    # if fixation_cross_1 is starting this frame...
                    if fixation_cross_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        fixation_cross_1.frameNStart = frameN  # exact frame index
                        fixation_cross_1.tStart = t  # local t and not account for scr refresh
                        fixation_cross_1.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(fixation_cross_1, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'fixation_cross_1.started')
                        # update status
                        fixation_cross_1.status = STARTED
                        fixation_cross_1.setAutoDraw(True)
                    
                    # if fixation_cross_1 is active this frame...
                    if fixation_cross_1.status == STARTED:
                        # update params
                        pass
                    
                    # if fixation_cross_1 is stopping this frame...
                    if fixation_cross_1.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > fixation_cross_1.tStartRefresh + .4-frameTolerance:
                            # keep track of stop time/frame for later
                            fixation_cross_1.tStop = t  # not accounting for scr refresh
                            fixation_cross_1.tStopRefresh = tThisFlipGlobal  # on global time
                            fixation_cross_1.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'fixation_cross_1.stopped')
                            # update status
                            fixation_cross_1.status = FINISHED
                            fixation_cross_1.setAutoDraw(False)
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, win=win)
                        return
                    # pause experiment here if requested
                    if thisExp.status == PAUSED:
                        pauseExperiment(
                            thisExp=thisExp, 
                            win=win, 
                            timers=[routineTimer], 
                            playbackComponents=[]
                        )
                        # skip the frame we paused on
                        continue
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        fixation_cross.forceEnded = routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in fixation_cross.components:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "fixation_cross" ---
                for thisComponent in fixation_cross.components:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # store stop times for fixation_cross
                fixation_cross.tStop = globalClock.getTime(format='float')
                fixation_cross.tStopRefresh = tThisFlipGlobal
                thisExp.addData('fixation_cross.stopped', fixation_cross.tStop)
                # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
                if fixation_cross.maxDurationReached:
                    routineTimer.addTime(-fixation_cross.maxDuration)
                elif fixation_cross.forceEnded:
                    routineTimer.reset()
                else:
                    routineTimer.addTime(-0.400000)
                
                # --- Prepare to start Routine "blank" ---
                # create an object to store info about Routine blank
                blank = data.Routine(
                    name='blank',
                    components=[text_2],
                )
                blank.status = NOT_STARTED
                continueRoutine = True
                # update component parameters for each repeat
                # store start times for blank
                blank.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
                blank.tStart = globalClock.getTime(format='float')
                blank.status = STARTED
                thisExp.addData('blank.started', blank.tStart)
                blank.maxDuration = None
                # keep track of which components have finished
                blankComponents = blank.components
                for thisComponent in blank.components:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "blank" ---
                # if trial has changed, end Routine now
                if isinstance(transfer_switch, data.TrialHandler2) and thisTransfer_switch.thisN != transfer_switch.thisTrial.thisN:
                    continueRoutine = False
                blank.forceEnded = routineForceEnded = not continueRoutine
                while continueRoutine and routineTimer.getTime() < 0.2:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *text_2* updates
                    
                    # if text_2 is starting this frame...
                    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        text_2.frameNStart = frameN  # exact frame index
                        text_2.tStart = t  # local t and not account for scr refresh
                        text_2.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text_2.started')
                        # update status
                        text_2.status = STARTED
                        text_2.setAutoDraw(True)
                    
                    # if text_2 is active this frame...
                    if text_2.status == STARTED:
                        # update params
                        pass
                    
                    # if text_2 is stopping this frame...
                    if text_2.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > text_2.tStartRefresh + .2-frameTolerance:
                            # keep track of stop time/frame for later
                            text_2.tStop = t  # not accounting for scr refresh
                            text_2.tStopRefresh = tThisFlipGlobal  # on global time
                            text_2.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'text_2.stopped')
                            # update status
                            text_2.status = FINISHED
                            text_2.setAutoDraw(False)
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, win=win)
                        return
                    # pause experiment here if requested
                    if thisExp.status == PAUSED:
                        pauseExperiment(
                            thisExp=thisExp, 
                            win=win, 
                            timers=[routineTimer], 
                            playbackComponents=[]
                        )
                        # skip the frame we paused on
                        continue
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        blank.forceEnded = routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in blank.components:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "blank" ---
                for thisComponent in blank.components:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # store stop times for blank
                blank.tStop = globalClock.getTime(format='float')
                blank.tStopRefresh = tThisFlipGlobal
                thisExp.addData('blank.stopped', blank.tStop)
                # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
                if blank.maxDurationReached:
                    routineTimer.addTime(-blank.maxDuration)
                elif blank.forceEnded:
                    routineTimer.reset()
                else:
                    routineTimer.addTime(-0.200000)
                
                # --- Prepare to start Routine "transfer_response_switch" ---
                # create an object to store info about Routine transfer_response_switch
                transfer_response_switch = data.Routine(
                    name='transfer_response_switch',
                    components=[turtle_halfcircle_switch, turtle_wedge_switch, turtle_wedge_boundary_switch, transfer_prompt_switch_trials, key_resp_transfer_switch],
                )
                transfer_response_switch.status = NOT_STARTED
                continueRoutine = True
                # update component parameters for each repeat
                # Run 'Begin Routine' code from get_turtle_params_transfer
                turtle_halfcircle_vertices = get_turtle_halfcircle_vertices(radius)
                turtle_wedge_vertices = get_turtle_wedge_vertices(angle)
                
                if trial_type=="standard":
                    transfer_prompt_col="#000000"
                    transfer_prompt="Is this turtle in Species F or Species J?\n\n F-Species F, J-Species J"
                elif trial_type=="switch":
                    transfer_prompt_col="#FF0000"
                    transfer_prompt="Is this turtle smaller or larger than the average turtle?\n\n F-smaller, J-larger"
                turtle_halfcircle_switch.setVertices(turtle_halfcircle_vertices)
                turtle_wedge_switch.setVertices(turtle_wedge_vertices)
                transfer_prompt_switch_trials.setColor(transfer_prompt_col, colorSpace='rgb')
                transfer_prompt_switch_trials.setText(transfer_prompt)
                # create starting attributes for key_resp_transfer_switch
                key_resp_transfer_switch.keys = []
                key_resp_transfer_switch.rt = []
                _key_resp_transfer_switch_allKeys = []
                # store start times for transfer_response_switch
                transfer_response_switch.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
                transfer_response_switch.tStart = globalClock.getTime(format='float')
                transfer_response_switch.status = STARTED
                thisExp.addData('transfer_response_switch.started', transfer_response_switch.tStart)
                transfer_response_switch.maxDuration = None
                # keep track of which components have finished
                transfer_response_switchComponents = transfer_response_switch.components
                for thisComponent in transfer_response_switch.components:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "transfer_response_switch" ---
                # if trial has changed, end Routine now
                if isinstance(transfer_switch, data.TrialHandler2) and thisTransfer_switch.thisN != transfer_switch.thisTrial.thisN:
                    continueRoutine = False
                transfer_response_switch.forceEnded = routineForceEnded = not continueRoutine
                while continueRoutine:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *turtle_halfcircle_switch* updates
                    
                    # if turtle_halfcircle_switch is starting this frame...
                    if turtle_halfcircle_switch.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        turtle_halfcircle_switch.frameNStart = frameN  # exact frame index
                        turtle_halfcircle_switch.tStart = t  # local t and not account for scr refresh
                        turtle_halfcircle_switch.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(turtle_halfcircle_switch, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'turtle_halfcircle_switch.started')
                        # update status
                        turtle_halfcircle_switch.status = STARTED
                        turtle_halfcircle_switch.setAutoDraw(True)
                    
                    # if turtle_halfcircle_switch is active this frame...
                    if turtle_halfcircle_switch.status == STARTED:
                        # update params
                        pass
                    
                    # *turtle_wedge_switch* updates
                    
                    # if turtle_wedge_switch is starting this frame...
                    if turtle_wedge_switch.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        turtle_wedge_switch.frameNStart = frameN  # exact frame index
                        turtle_wedge_switch.tStart = t  # local t and not account for scr refresh
                        turtle_wedge_switch.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(turtle_wedge_switch, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'turtle_wedge_switch.started')
                        # update status
                        turtle_wedge_switch.status = STARTED
                        turtle_wedge_switch.setAutoDraw(True)
                    
                    # if turtle_wedge_switch is active this frame...
                    if turtle_wedge_switch.status == STARTED:
                        # update params
                        pass
                    
                    # *turtle_wedge_boundary_switch* updates
                    
                    # if turtle_wedge_boundary_switch is starting this frame...
                    if turtle_wedge_boundary_switch.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        turtle_wedge_boundary_switch.frameNStart = frameN  # exact frame index
                        turtle_wedge_boundary_switch.tStart = t  # local t and not account for scr refresh
                        turtle_wedge_boundary_switch.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(turtle_wedge_boundary_switch, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'turtle_wedge_boundary_switch.started')
                        # update status
                        turtle_wedge_boundary_switch.status = STARTED
                        turtle_wedge_boundary_switch.setAutoDraw(True)
                    
                    # if turtle_wedge_boundary_switch is active this frame...
                    if turtle_wedge_boundary_switch.status == STARTED:
                        # update params
                        pass
                    
                    # *transfer_prompt_switch_trials* updates
                    
                    # if transfer_prompt_switch_trials is starting this frame...
                    if transfer_prompt_switch_trials.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        transfer_prompt_switch_trials.frameNStart = frameN  # exact frame index
                        transfer_prompt_switch_trials.tStart = t  # local t and not account for scr refresh
                        transfer_prompt_switch_trials.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(transfer_prompt_switch_trials, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'transfer_prompt_switch_trials.started')
                        # update status
                        transfer_prompt_switch_trials.status = STARTED
                        transfer_prompt_switch_trials.setAutoDraw(True)
                    
                    # if transfer_prompt_switch_trials is active this frame...
                    if transfer_prompt_switch_trials.status == STARTED:
                        # update params
                        pass
                    
                    # *key_resp_transfer_switch* updates
                    waitOnFlip = False
                    
                    # if key_resp_transfer_switch is starting this frame...
                    if key_resp_transfer_switch.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        key_resp_transfer_switch.frameNStart = frameN  # exact frame index
                        key_resp_transfer_switch.tStart = t  # local t and not account for scr refresh
                        key_resp_transfer_switch.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(key_resp_transfer_switch, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'key_resp_transfer_switch.started')
                        # update status
                        key_resp_transfer_switch.status = STARTED
                        # keyboard checking is just starting
                        waitOnFlip = True
                        win.callOnFlip(key_resp_transfer_switch.clock.reset)  # t=0 on next screen flip
                        win.callOnFlip(key_resp_transfer_switch.clearEvents, eventType='keyboard')  # clear events on next screen flip
                    if key_resp_transfer_switch.status == STARTED and not waitOnFlip:
                        theseKeys = key_resp_transfer_switch.getKeys(keyList=['f','j'], ignoreKeys=["escape"], waitRelease=False)
                        _key_resp_transfer_switch_allKeys.extend(theseKeys)
                        if len(_key_resp_transfer_switch_allKeys):
                            key_resp_transfer_switch.keys = _key_resp_transfer_switch_allKeys[-1].name  # just the last key pressed
                            key_resp_transfer_switch.rt = _key_resp_transfer_switch_allKeys[-1].rt
                            key_resp_transfer_switch.duration = _key_resp_transfer_switch_allKeys[-1].duration
                            # a response ends the routine
                            continueRoutine = False
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, win=win)
                        return
                    # pause experiment here if requested
                    if thisExp.status == PAUSED:
                        pauseExperiment(
                            thisExp=thisExp, 
                            win=win, 
                            timers=[routineTimer], 
                            playbackComponents=[]
                        )
                        # skip the frame we paused on
                        continue
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        transfer_response_switch.forceEnded = routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in transfer_response_switch.components:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "transfer_response_switch" ---
                for thisComponent in transfer_response_switch.components:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # store stop times for transfer_response_switch
                transfer_response_switch.tStop = globalClock.getTime(format='float')
                transfer_response_switch.tStopRefresh = tThisFlipGlobal
                thisExp.addData('transfer_response_switch.stopped', transfer_response_switch.tStop)
                # check responses
                if key_resp_transfer_switch.keys in ['', [], None]:  # No response was made
                    key_resp_transfer_switch.keys = None
                transfer_switch.addData('key_resp_transfer_switch.keys',key_resp_transfer_switch.keys)
                if key_resp_transfer_switch.keys != None:  # we had a response
                    transfer_switch.addData('key_resp_transfer_switch.rt', key_resp_transfer_switch.rt)
                    transfer_switch.addData('key_resp_transfer_switch.duration', key_resp_transfer_switch.duration)
                # the Routine "transfer_response_switch" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                
                # --- Prepare to start Routine "blank" ---
                # create an object to store info about Routine blank
                blank = data.Routine(
                    name='blank',
                    components=[text_2],
                )
                blank.status = NOT_STARTED
                continueRoutine = True
                # update component parameters for each repeat
                # store start times for blank
                blank.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
                blank.tStart = globalClock.getTime(format='float')
                blank.status = STARTED
                thisExp.addData('blank.started', blank.tStart)
                blank.maxDuration = None
                # keep track of which components have finished
                blankComponents = blank.components
                for thisComponent in blank.components:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "blank" ---
                # if trial has changed, end Routine now
                if isinstance(transfer_switch, data.TrialHandler2) and thisTransfer_switch.thisN != transfer_switch.thisTrial.thisN:
                    continueRoutine = False
                blank.forceEnded = routineForceEnded = not continueRoutine
                while continueRoutine and routineTimer.getTime() < 0.2:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *text_2* updates
                    
                    # if text_2 is starting this frame...
                    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        text_2.frameNStart = frameN  # exact frame index
                        text_2.tStart = t  # local t and not account for scr refresh
                        text_2.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text_2.started')
                        # update status
                        text_2.status = STARTED
                        text_2.setAutoDraw(True)
                    
                    # if text_2 is active this frame...
                    if text_2.status == STARTED:
                        # update params
                        pass
                    
                    # if text_2 is stopping this frame...
                    if text_2.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > text_2.tStartRefresh + .2-frameTolerance:
                            # keep track of stop time/frame for later
                            text_2.tStop = t  # not accounting for scr refresh
                            text_2.tStopRefresh = tThisFlipGlobal  # on global time
                            text_2.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'text_2.stopped')
                            # update status
                            text_2.status = FINISHED
                            text_2.setAutoDraw(False)
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, win=win)
                        return
                    # pause experiment here if requested
                    if thisExp.status == PAUSED:
                        pauseExperiment(
                            thisExp=thisExp, 
                            win=win, 
                            timers=[routineTimer], 
                            playbackComponents=[]
                        )
                        # skip the frame we paused on
                        continue
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        blank.forceEnded = routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in blank.components:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "blank" ---
                for thisComponent in blank.components:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # store stop times for blank
                blank.tStop = globalClock.getTime(format='float')
                blank.tStopRefresh = tThisFlipGlobal
                thisExp.addData('blank.stopped', blank.tStop)
                # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
                if blank.maxDurationReached:
                    routineTimer.addTime(-blank.maxDuration)
                elif blank.forceEnded:
                    routineTimer.reset()
                else:
                    routineTimer.addTime(-0.200000)
                thisExp.nextEntry()
                
            # completed 1.0 repeats of 'transfer_switch'
            
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            
            # --- Prepare to start Routine "delete_switch_order" ---
            # create an object to store info about Routine delete_switch_order
            delete_switch_order = data.Routine(
                name='delete_switch_order',
                components=[],
            )
            delete_switch_order.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from delete_switch_order_code
            os.remove("stim/stim_transfer_switch_random_tmp.csv")
            # store start times for delete_switch_order
            delete_switch_order.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            delete_switch_order.tStart = globalClock.getTime(format='float')
            delete_switch_order.status = STARTED
            thisExp.addData('delete_switch_order.started', delete_switch_order.tStart)
            delete_switch_order.maxDuration = None
            # keep track of which components have finished
            delete_switch_orderComponents = delete_switch_order.components
            for thisComponent in delete_switch_order.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "delete_switch_order" ---
            # if trial has changed, end Routine now
            if isinstance(transfer_switch_loop, data.TrialHandler2) and thisTransfer_switch_loop.thisN != transfer_switch_loop.thisTrial.thisN:
                continueRoutine = False
            delete_switch_order.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    delete_switch_order.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in delete_switch_order.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "delete_switch_order" ---
            for thisComponent in delete_switch_order.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for delete_switch_order
            delete_switch_order.tStop = globalClock.getTime(format='float')
            delete_switch_order.tStopRefresh = tThisFlipGlobal
            thisExp.addData('delete_switch_order.stopped', delete_switch_order.tStop)
            # the Routine "delete_switch_order" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed num_repeats_2 repeats of 'transfer_switch_loop'
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        thisExp.nextEntry()
        
    # completed 2.0 repeats of 'transfer_trials'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "begin_debrief" ---
    # create an object to store info about Routine begin_debrief
    begin_debrief = data.Routine(
        name='begin_debrief',
        components=[begin_debrief_text, space_20, space_to_begin_debrief],
    )
    begin_debrief.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for space_to_begin_debrief
    space_to_begin_debrief.keys = []
    space_to_begin_debrief.rt = []
    _space_to_begin_debrief_allKeys = []
    # store start times for begin_debrief
    begin_debrief.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    begin_debrief.tStart = globalClock.getTime(format='float')
    begin_debrief.status = STARTED
    thisExp.addData('begin_debrief.started', begin_debrief.tStart)
    begin_debrief.maxDuration = None
    # keep track of which components have finished
    begin_debriefComponents = begin_debrief.components
    for thisComponent in begin_debrief.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "begin_debrief" ---
    begin_debrief.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *begin_debrief_text* updates
        
        # if begin_debrief_text is starting this frame...
        if begin_debrief_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            begin_debrief_text.frameNStart = frameN  # exact frame index
            begin_debrief_text.tStart = t  # local t and not account for scr refresh
            begin_debrief_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(begin_debrief_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'begin_debrief_text.started')
            # update status
            begin_debrief_text.status = STARTED
            begin_debrief_text.setAutoDraw(True)
        
        # if begin_debrief_text is active this frame...
        if begin_debrief_text.status == STARTED:
            # update params
            pass
        
        # *space_20* updates
        
        # if space_20 is starting this frame...
        if space_20.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            space_20.frameNStart = frameN  # exact frame index
            space_20.tStart = t  # local t and not account for scr refresh
            space_20.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(space_20, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'space_20.started')
            # update status
            space_20.status = STARTED
            space_20.setAutoDraw(True)
        
        # if space_20 is active this frame...
        if space_20.status == STARTED:
            # update params
            pass
        
        # *space_to_begin_debrief* updates
        waitOnFlip = False
        
        # if space_to_begin_debrief is starting this frame...
        if space_to_begin_debrief.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            space_to_begin_debrief.frameNStart = frameN  # exact frame index
            space_to_begin_debrief.tStart = t  # local t and not account for scr refresh
            space_to_begin_debrief.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(space_to_begin_debrief, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'space_to_begin_debrief.started')
            # update status
            space_to_begin_debrief.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(space_to_begin_debrief.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(space_to_begin_debrief.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if space_to_begin_debrief.status == STARTED and not waitOnFlip:
            theseKeys = space_to_begin_debrief.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _space_to_begin_debrief_allKeys.extend(theseKeys)
            if len(_space_to_begin_debrief_allKeys):
                space_to_begin_debrief.keys = _space_to_begin_debrief_allKeys[-1].name  # just the last key pressed
                space_to_begin_debrief.rt = _space_to_begin_debrief_allKeys[-1].rt
                space_to_begin_debrief.duration = _space_to_begin_debrief_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            begin_debrief.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in begin_debrief.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "begin_debrief" ---
    for thisComponent in begin_debrief.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for begin_debrief
    begin_debrief.tStop = globalClock.getTime(format='float')
    begin_debrief.tStopRefresh = tThisFlipGlobal
    thisExp.addData('begin_debrief.stopped', begin_debrief.tStop)
    # check responses
    if space_to_begin_debrief.keys in ['', [], None]:  # No response was made
        space_to_begin_debrief.keys = None
    thisExp.addData('space_to_begin_debrief.keys',space_to_begin_debrief.keys)
    if space_to_begin_debrief.keys != None:  # we had a response
        thisExp.addData('space_to_begin_debrief.rt', space_to_begin_debrief.rt)
        thisExp.addData('space_to_begin_debrief.duration', space_to_begin_debrief.duration)
    thisExp.nextEntry()
    # the Routine "begin_debrief" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "debrief" ---
    # create an object to store info about Routine debrief
    debrief = data.Routine(
        name='debrief',
        components=[debrief_img, space_to_end],
    )
    debrief.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for space_to_end
    space_to_end.keys = []
    space_to_end.rt = []
    _space_to_end_allKeys = []
    # store start times for debrief
    debrief.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    debrief.tStart = globalClock.getTime(format='float')
    debrief.status = STARTED
    thisExp.addData('debrief.started', debrief.tStart)
    debrief.maxDuration = None
    # keep track of which components have finished
    debriefComponents = debrief.components
    for thisComponent in debrief.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "debrief" ---
    debrief.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *debrief_img* updates
        
        # if debrief_img is starting this frame...
        if debrief_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            debrief_img.frameNStart = frameN  # exact frame index
            debrief_img.tStart = t  # local t and not account for scr refresh
            debrief_img.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(debrief_img, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'debrief_img.started')
            # update status
            debrief_img.status = STARTED
            debrief_img.setAutoDraw(True)
        
        # if debrief_img is active this frame...
        if debrief_img.status == STARTED:
            # update params
            pass
        
        # *space_to_end* updates
        waitOnFlip = False
        
        # if space_to_end is starting this frame...
        if space_to_end.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
            # keep track of start time/frame for later
            space_to_end.frameNStart = frameN  # exact frame index
            space_to_end.tStart = t  # local t and not account for scr refresh
            space_to_end.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(space_to_end, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'space_to_end.started')
            # update status
            space_to_end.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(space_to_end.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(space_to_end.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if space_to_end.status == STARTED and not waitOnFlip:
            theseKeys = space_to_end.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _space_to_end_allKeys.extend(theseKeys)
            if len(_space_to_end_allKeys):
                space_to_end.keys = _space_to_end_allKeys[-1].name  # just the last key pressed
                space_to_end.rt = _space_to_end_allKeys[-1].rt
                space_to_end.duration = _space_to_end_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            debrief.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in debrief.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "debrief" ---
    for thisComponent in debrief.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for debrief
    debrief.tStop = globalClock.getTime(format='float')
    debrief.tStopRefresh = tThisFlipGlobal
    thisExp.addData('debrief.stopped', debrief.tStop)
    # check responses
    if space_to_end.keys in ['', [], None]:  # No response was made
        space_to_end.keys = None
    thisExp.addData('space_to_end.keys',space_to_end.keys)
    if space_to_end.keys != None:  # we had a response
        thisExp.addData('space_to_end.rt', space_to_end.rt)
        thisExp.addData('space_to_end.duration', space_to_end.duration)
    thisExp.nextEntry()
    # the Routine "debrief" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # return console logger level to WARNING
    logging.console.setLevel(logging.WARNING)
    # mark experiment handler as finished
    thisExp.status = FINISHED
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
