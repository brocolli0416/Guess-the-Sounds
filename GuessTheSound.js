/********************** 
 * Guessthesound Test *
 **********************/

import { PsychoJS } from './lib/core-2020.2.js';
import * as core from './lib/core-2020.2.js';
import { TrialHandler } from './lib/data-2020.2.js';
import { Scheduler } from './lib/util-2020.2.js';
import * as visual from './lib/visual-2020.2.js';
import * as sound from './lib/sound-2020.2.js';
import * as util from './lib/util-2020.2.js';
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;

// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0, 0, 0]),
  units: 'height',
  waitBlanking: true
});

// store info about the experiment session:
let expName = 'GuessTheSound';  // from the Builder filename that created this script
let expInfo = {'participant': '', 'session': '001'};

// Start code blocks for 'Before Experiment'
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(WelcomeRoutineBegin());
flowScheduler.add(WelcomeRoutineEachFrame());
flowScheduler.add(WelcomeRoutineEnd());
flowScheduler.add(StartAdjustmentRoutineBegin());
flowScheduler.add(StartAdjustmentRoutineEachFrame());
flowScheduler.add(StartAdjustmentRoutineEnd());
flowScheduler.add(VolumeAdjustmentRoutineBegin());
flowScheduler.add(VolumeAdjustmentRoutineEachFrame());
flowScheduler.add(VolumeAdjustmentRoutineEnd());
flowScheduler.add(Welcome1RoutineBegin());
flowScheduler.add(Welcome1RoutineEachFrame());
flowScheduler.add(Welcome1RoutineEnd());
flowScheduler.add(PracticeBeginRoutineBegin());
flowScheduler.add(PracticeBeginRoutineEachFrame());
flowScheduler.add(PracticeBeginRoutineEnd());
const PracticeTrialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(PracticeTrialsLoopBegin, PracticeTrialsLoopScheduler);
flowScheduler.add(PracticeTrialsLoopScheduler);
flowScheduler.add(PracticeTrialsLoopEnd);
flowScheduler.add(StartRoutineBegin());
flowScheduler.add(StartRoutineEachFrame());
flowScheduler.add(StartRoutineEnd());
const trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsLoopBegin, trialsLoopScheduler);
flowScheduler.add(trialsLoopScheduler);
flowScheduler.add(trialsLoopEnd);
flowScheduler.add(EndRoutineBegin());
flowScheduler.add(EndRoutineEachFrame());
flowScheduler.add(EndRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    {'name': 'Initial/Doubled/Cat_A.wav', 'path': 'Initial/Doubled/Cat_A.wav'},
    {'name': 'Cough_C.wav', 'path': 'Cough_C.wav'},
    {'name': 'Initial/NoRepeat/Baby_B.wav', 'path': 'Initial/NoRepeat/Baby_B.wav'},
    {'name': 'Initial/NoRepeat/Snore_B.wav', 'path': 'Initial/NoRepeat/Snore_B.wav'},
    {'name': 'Initial/Doubled/Writing_A.wav', 'path': 'Initial/Doubled/Writing_A.wav'},
    {'name': 'Test/Foils/Bullfrog.wav', 'path': 'Test/Foils/Bullfrog.wav'},
    {'name': 'Initial/Repeat/Pour.wav', 'path': 'Initial/Repeat/Pour.wav'},
    {'name': 'Initial/Repeat/Whistle_A.wav', 'path': 'Initial/Repeat/Whistle_A.wav'},
    {'name': 'Goat_C.wav', 'path': 'Goat_C.wav'},
    {'name': 'Siren_C.wav', 'path': 'Siren_C.wav'},
    {'name': 'Laugh_C.wav', 'path': 'Laugh_C.wav'},
    {'name': 'Initial/NoRepeat/Thunder_A.wav', 'path': 'Initial/NoRepeat/Thunder_A.wav'},
    {'name': 'Initial/NoRepeat/Fireworks.wav', 'path': 'Initial/NoRepeat/Fireworks.wav'},
    {'name': 'CarStart_B.wav', 'path': 'CarStart_B.wav'},
    {'name': 'Initial/NoRepeat/Footsteps_B.wav', 'path': 'Initial/NoRepeat/Footsteps_B.wav'},
    {'name': 'Initial/Doubled/Growl_A.wav', 'path': 'Initial/Doubled/Growl_A.wav'},
    {'name': 'Pour_D.wav', 'path': 'Pour_D.wav'},
    {'name': 'Initial/Doubled/Piano_A.wav', 'path': 'Initial/Doubled/Piano_A.wav'},
    {'name': 'CarStart_D.wav', 'path': 'CarStart_D.wav'},
    {'name': 'Initial/NoRepeat/Helicopter_A.wav', 'path': 'Initial/NoRepeat/Helicopter_A.wav'},
    {'name': 'Initial/Doubled/Cuckoo_A.wav', 'path': 'Initial/Doubled/Cuckoo_A.wav'},
    {'name': 'Initial/Doubled/Laugh_A.wav', 'path': 'Initial/Doubled/Laugh_A.wav'},
    {'name': 'Initial/NoRepeat/Elephant_A.wav', 'path': 'Initial/NoRepeat/Elephant_A.wav'},
    {'name': 'Piano_D.wav', 'path': 'Piano_D.wav'},
    {'name': 'Growl_B.wav', 'path': 'Growl_B.wav'},
    {'name': 'Bird_D.wav', 'path': 'Bird_D.wav'},
    {'name': 'Goat_A.wav', 'path': 'Goat_A.wav'},
    {'name': 'Initial/NoRepeat/Sleighbells_B.wav', 'path': 'Initial/NoRepeat/Sleighbells_B.wav'},
    {'name': 'Initial/NoRepeat/Toilet_B.wav', 'path': 'Initial/NoRepeat/Toilet_B.wav'},
    {'name': 'Initial/Doubled/Guitar_A.wav', 'path': 'Initial/Doubled/Guitar_A.wav'},
    {'name': 'Whistle_C.wav', 'path': 'Whistle_C.wav'},
    {'name': 'Baby_A.wav', 'path': 'Baby_A.wav'},
    {'name': 'Initial/Doubled/Cough_A.wav', 'path': 'Initial/Doubled/Cough_A.wav'},
    {'name': 'Initial/NoRepeat/Puff_A.wav', 'path': 'Initial/NoRepeat/Puff_A.wav'},
    {'name': 'Whistle_B.wav', 'path': 'Whistle_B.wav'},
    {'name': 'Initial/Repeat/Phone_A.wav', 'path': 'Initial/Repeat/Phone_A.wav'},
    {'name': 'Initial/Doubled/Chicken_A.wav', 'path': 'Initial/Doubled/Chicken_A.wav'},
    {'name': 'Initial/Doubled/Chomp_A.wav', 'path': 'Initial/Doubled/Chomp_A.wav'},
    {'name': 'Test/Foils/Typing.wav', 'path': 'Test/Foils/Typing.wav'},
    {'name': 'GuessSounds_conditions.xlsx', 'path': 'GuessSounds_conditions.xlsx'},
    {'name': 'Coin_B.wav', 'path': 'Coin_B.wav'},
    {'name': 'Initial/Doubled/Bubbles_A.wav', 'path': 'Initial/Doubled/Bubbles_A.wav'},
    {'name': 'Growl_C.wav', 'path': 'Growl_C.wav'},
    {'name': 'Dog_D.wav', 'path': 'Dog_D.wav'},
    {'name': 'Siren_B.wav', 'path': 'Siren_B.wav'},
    {'name': 'Coin_C.wav', 'path': 'Coin_C.wav'},
    {'name': 'Cough_D.wav', 'path': 'Cough_D.wav'},
    {'name': 'Initial/Repeat/IceDrop.wav', 'path': 'Initial/Repeat/IceDrop.wav'},
    {'name': 'Initial/Doubled/HairDryer_A.wav', 'path': 'Initial/Doubled/HairDryer_A.wav'},
    {'name': 'Chomp_C.wav', 'path': 'Chomp_C.wav'},
    {'name': 'Initial/Repeat/Howl.wav', 'path': 'Initial/Repeat/Howl.wav'},
    {'name': 'Bird_C.wav', 'path': 'Bird_C.wav'},
    {'name': 'Test/Foils/Wind_B.wav', 'path': 'Test/Foils/Wind_B.wav'},
    {'name': 'Practice/Gargle_A.wav', 'path': 'Practice/Gargle_A.wav'},
    {'name': 'Test/Foils/PaperRip.wav', 'path': 'Test/Foils/PaperRip.wav'},
    {'name': 'Dog_C.wav', 'path': 'Dog_C.wav'},
    {'name': 'Laugh_D.wav', 'path': 'Laugh_D.wav'},
    {'name': 'Initial/NoRepeat/Goat_B.wav', 'path': 'Initial/NoRepeat/Goat_B.wav'},
    {'name': 'Initial/Repeat/Airplane_B.wav', 'path': 'Initial/Repeat/Airplane_B.wav'},
    {'name': 'Initial/Doubled/Clap_A.wav', 'path': 'Initial/Doubled/Clap_A.wav'},
    {'name': 'Initial/Doubled/Coin_A.wav', 'path': 'Initial/Doubled/Coin_A.wav'},
    {'name': 'volumeadjust.wav', 'path': 'volumeadjust.wav'},
    {'name': 'Pour_C.wav', 'path': 'Pour_C.wav'},
    {'name': 'Initial/NoRepeat/Droplet_B.wav', 'path': 'Initial/NoRepeat/Droplet_B.wav'},
    {'name': 'Baby_C.wav', 'path': 'Baby_C.wav'},
    {'name': 'Initial/Repeat/ManWhistle.wav', 'path': 'Initial/Repeat/ManWhistle.wav'},
    {'name': 'Phone_C.wav', 'path': 'Phone_C.wav'},
    {'name': 'Test/Foils/DialTone.wav', 'path': 'Test/Foils/DialTone.wav'},
    {'name': 'Practice/Skid_B.wav', 'path': 'Practice/Skid_B.wav'},
    {'name': 'Practice/Gargle_B.wav', 'path': 'Practice/Gargle_B.wav'},
    {'name': 'Initial/Doubled/Dog_A.wav', 'path': 'Initial/Doubled/Dog_A.wav'},
    {'name': 'Test/Foils/Bird.wav', 'path': 'Test/Foils/Bird.wav'},
    {'name': 'Initial/NoRepeat/Cow.wav', 'path': 'Initial/NoRepeat/Cow.wav'},
    {'name': 'Initial/Doubled/Siren_A.wav', 'path': 'Initial/Doubled/Siren_A.wav'},
    {'name': 'Test/Foils/Donkey.wav', 'path': 'Test/Foils/Donkey.wav'},
    {'name': 'Initial/Doubled/Chime_A.wav', 'path': 'Initial/Doubled/Chime_A.wav'},
    {'name': 'Initial/NoRepeat/Faucet_A.wav', 'path': 'Initial/NoRepeat/Faucet_A.wav'},
    {'name': 'Test/Foils/Camera.wav', 'path': 'Test/Foils/Camera.wav'},
    {'name': 'Phone_D.wav', 'path': 'Phone_D.wav'},
    {'name': 'Piano_C.wav', 'path': 'Piano_C.wav'},
    {'name': 'Practice/Seagull_A.wav', 'path': 'Practice/Seagull_A.wav'},
    {'name': 'Initial/Doubled/CarStart_A.wav', 'path': 'Initial/Doubled/CarStart_A.wav'},
    {'name': 'Initial/Repeat/Sneeze_B.wav', 'path': 'Initial/Repeat/Sneeze_B.wav'},
    {'name': 'Chomp_B.wav', 'path': 'Chomp_B.wav'},
    {'name': 'Test/Foils/Buzz.wav', 'path': 'Test/Foils/Buzz.wav'}
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var frameDur;
function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2020.2.10';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}


var WelcomeClock;
var InstructionTxt;
var WelcomeContinueKey;
var count;
var WelcomContinue;
var StartAdjustmentClock;
var VolumeBeginTxt;
var VolumeContinue;
var VolumeContinueKey;
var VolumeAdjustmentClock;
var text;
var Music;
var EndAdjustment;
var AdjustContinue;
var Welcome1Clock;
var WelcomeTxt1;
var ContinueKey1;
var ContinueResp;
var PracticeBeginClock;
var InstructionTxt2;
var WelcomeContinue2;
var WelcomeContinueKey2;
var Tcount;
var TrialCount;
var Practice1Clock;
var TrialNumber;
var PracticeSound;
var PracticeCross;
var PracticeFeedbackClock;
var Practice_resp;
var PracticeMssg;
var FeedbackCross;
var Continue;
var Options;
var StartClock;
var StartTxt;
var StartTast;
var ContinueStart;
var Count1Clock;
var no1;
var no_2;
var no_3;
var MSTSoundClock;
var TargetSound;
var Cross;
var ItemNumber;
var MSTClock;
var MSTQuestion;
var MSTResp;
var EndClock;
var ThankyouMssg;
var CompletionCode;
var ExitTxt;
var ExitKey;
var CodeTxt;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "Welcome"
  WelcomeClock = new util.Clock();
  InstructionTxt = new visual.TextStim({
    win: psychoJS.window,
    name: 'InstructionTxt',
    text: "Welcome to 'Sound Memory Test'!\n\n\nIn this experiment, we will test your memory for different sound items. \n\n\n",
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  WelcomeContinueKey = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  count = 0;
  
  WelcomContinue = new visual.TextStim({
    win: psychoJS.window,
    name: 'WelcomContinue',
    text: 'Press SPACE to continue',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  // Initialize components for Routine "StartAdjustment"
  StartAdjustmentClock = new util.Clock();
  VolumeBeginTxt = new visual.TextStim({
    win: psychoJS.window,
    name: 'VolumeBeginTxt',
    text: 'We will first play some music to make sure your volume is at a comfortable level.\n\n',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  VolumeContinue = new visual.TextStim({
    win: psychoJS.window,
    name: 'VolumeContinue',
    text: 'Press SPACE when you are ready for the sound check',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  VolumeContinueKey = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "VolumeAdjustment"
  VolumeAdjustmentClock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: 'Please adjust your volume to a comfortable level.\n',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  Music = new sound.Sound({
    win: psychoJS.window,
    value: 'volumeadjust.wav',
    secs: (- 1),
    });
  Music.setVolume(0.3);
  EndAdjustment = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  AdjustContinue = new visual.TextStim({
    win: psychoJS.window,
    name: 'AdjustContinue',
    text: 'Press SPACE when you are ready to begin the task',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  // Initialize components for Routine "Welcome1"
  Welcome1Clock = new util.Clock();
  WelcomeTxt1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'WelcomeTxt1',
    text: "In this task, you will be presented with different enviornmental sounds one by one. For each sound you hear, please indicate whether it is a NEW sound that has never been presented before, a REPEAT of a previously presented sound, or a sound that is SIMILAR but different from a previously presented sound. \n\nPress '1' on your keyboard for REPEAT, '2' for SIMILAR, and '3' for NEW.",
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  ContinueKey1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'ContinueKey1',
    text: 'Press SPACE to continue',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  ContinueResp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "PracticeBegin"
  PracticeBeginClock = new util.Clock();
  InstructionTxt2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'InstructionTxt2',
    text: "Let's begin with a few practice trials. \n\n\n",
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  WelcomeContinue2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'WelcomeContinue2',
    text: 'Press SPACE to begin practice\n',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  WelcomeContinueKey2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  Tcount = 1;
  TrialCount = ("Trial " + Tcount.toString());
  
  // Initialize components for Routine "Practice1"
  Practice1Clock = new util.Clock();
  TrialNumber = new visual.TextStim({
    win: psychoJS.window,
    name: 'TrialNumber',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.3], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  PracticeSound = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: (- 1),
    });
  PracticeSound.setVolume(1);
  PracticeCross = new visual.TextStim({
    win: psychoJS.window,
    name: 'PracticeCross',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "PracticeFeedback"
  PracticeFeedbackClock = new util.Clock();
  Practice_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  PracticeMssg = new visual.TextStim({
    win: psychoJS.window,
    name: 'PracticeMssg',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.2], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  FeedbackCross = new visual.TextStim({
    win: psychoJS.window,
    name: 'FeedbackCross',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  Continue = new visual.TextStim({
    win: psychoJS.window,
    name: 'Continue',
    text: 'Press the correct number on your keyboard',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  Options = new visual.TextStim({
    win: psychoJS.window,
    name: 'Options',
    text: '1 = REPEAT\n2 = SIMILAR\n3 = NEW',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.2)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -5.0 
  });
  
  // Initialize components for Routine "Start"
  StartClock = new util.Clock();
  StartTxt = new visual.TextStim({
    win: psychoJS.window,
    name: 'StartTxt',
    text: 'This is the end of practice.\n\n\nWe will now begin the actual task.\nThere are 80 items in total. Listen to each sound carefully as they will play once.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  StartTast = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  ContinueStart = new visual.TextStim({
    win: psychoJS.window,
    name: 'ContinueStart',
    text: 'Press SPACE to begin the task',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "Count1"
  Count1Clock = new util.Clock();
  no1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'no1',
    text: '1',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  no_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'no_2',
    text: '2',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  no_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'no_3',
    text: '3',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  // Initialize components for Routine "MSTSound"
  MSTSoundClock = new util.Clock();
  TargetSound = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: (- 1),
    });
  TargetSound.setVolume(1);
  Cross = new visual.TextStim({
    win: psychoJS.window,
    name: 'Cross',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  ItemNumber = new visual.TextStim({
    win: psychoJS.window,
    name: 'ItemNumber',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.3], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "MST"
  MSTClock = new util.Clock();
  MSTQuestion = new visual.TextStim({
    win: psychoJS.window,
    name: 'MSTQuestion',
    text: '1 = REPEAT\n\n2 = SIMILAR\n\n3 = NEW\n',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  MSTResp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "End"
  EndClock = new util.Clock();
  ThankyouMssg = new visual.TextStim({
    win: psychoJS.window,
    name: 'ThankyouMssg',
    text: 'This is the end of the experiment.\n\nThank you for your participation!\n\n\n\nYour Completion Code is',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.2], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  CompletionCode = new visual.TextBox({
    win: psychoJS.window,
    name: 'CompletionCode',
    text: '51DF249E',
    font: 'Arial',
    pos: [0, 0], letterHeight: 0.04,
    size: [0.25, 0.07],  units: undefined, 
    color: 'Black', colorSpace: 'rgb',
    fillColor: 'White', borderColor: 'Black',
    bold: true, italic: false,
    opacity: 1,
    padding: undefined,
    editable: false,
    anchor: 'center',
    depth: -1.0 
  });
  
  ExitTxt = new visual.TextStim({
    win: psychoJS.window,
    name: 'ExitTxt',
    text: 'Press SPACE to exit the study',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  ExitKey = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  CodeTxt = new visual.TextStim({
    win: psychoJS.window,
    name: 'CodeTxt',
    text: 'Please write the code down so you can enter it when you return to Prolific. You may then exit the study by pressing SPACE.',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.22)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var _WelcomeContinueKey_allKeys;
var WelcomeComponents;
function WelcomeRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'Welcome'-------
    t = 0;
    WelcomeClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    WelcomeContinueKey.keys = undefined;
    WelcomeContinueKey.rt = undefined;
    _WelcomeContinueKey_allKeys = [];
    // keep track of which components have finished
    WelcomeComponents = [];
    WelcomeComponents.push(InstructionTxt);
    WelcomeComponents.push(WelcomeContinueKey);
    WelcomeComponents.push(WelcomContinue);
    
    for (const thisComponent of WelcomeComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function WelcomeRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'Welcome'-------
    // get current time
    t = WelcomeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *InstructionTxt* updates
    if (t >= 0.0 && InstructionTxt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      InstructionTxt.tStart = t;  // (not accounting for frame time here)
      InstructionTxt.frameNStart = frameN;  // exact frame index
      
      InstructionTxt.setAutoDraw(true);
    }

    
    // *WelcomeContinueKey* updates
    if (t >= 0.0 && WelcomeContinueKey.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      WelcomeContinueKey.tStart = t;  // (not accounting for frame time here)
      WelcomeContinueKey.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { WelcomeContinueKey.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { WelcomeContinueKey.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { WelcomeContinueKey.clearEvents(); });
    }

    if (WelcomeContinueKey.status === PsychoJS.Status.STARTED) {
      let theseKeys = WelcomeContinueKey.getKeys({keyList: ['space'], waitRelease: false});
      _WelcomeContinueKey_allKeys = _WelcomeContinueKey_allKeys.concat(theseKeys);
      if (_WelcomeContinueKey_allKeys.length > 0) {
        WelcomeContinueKey.keys = _WelcomeContinueKey_allKeys[_WelcomeContinueKey_allKeys.length - 1].name;  // just the last key pressed
        WelcomeContinueKey.rt = _WelcomeContinueKey_allKeys[_WelcomeContinueKey_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *WelcomContinue* updates
    if (t >= 0.0 && WelcomContinue.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      WelcomContinue.tStart = t;  // (not accounting for frame time here)
      WelcomContinue.frameNStart = frameN;  // exact frame index
      
      WelcomContinue.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of WelcomeComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function WelcomeRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'Welcome'-------
    for (const thisComponent of WelcomeComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "Welcome" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _VolumeContinueKey_allKeys;
var StartAdjustmentComponents;
function StartAdjustmentRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'StartAdjustment'-------
    t = 0;
    StartAdjustmentClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    VolumeContinueKey.keys = undefined;
    VolumeContinueKey.rt = undefined;
    _VolumeContinueKey_allKeys = [];
    // keep track of which components have finished
    StartAdjustmentComponents = [];
    StartAdjustmentComponents.push(VolumeBeginTxt);
    StartAdjustmentComponents.push(VolumeContinue);
    StartAdjustmentComponents.push(VolumeContinueKey);
    
    for (const thisComponent of StartAdjustmentComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function StartAdjustmentRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'StartAdjustment'-------
    // get current time
    t = StartAdjustmentClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *VolumeBeginTxt* updates
    if (t >= 0.0 && VolumeBeginTxt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      VolumeBeginTxt.tStart = t;  // (not accounting for frame time here)
      VolumeBeginTxt.frameNStart = frameN;  // exact frame index
      
      VolumeBeginTxt.setAutoDraw(true);
    }

    
    // *VolumeContinue* updates
    if (t >= 0.0 && VolumeContinue.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      VolumeContinue.tStart = t;  // (not accounting for frame time here)
      VolumeContinue.frameNStart = frameN;  // exact frame index
      
      VolumeContinue.setAutoDraw(true);
    }

    
    // *VolumeContinueKey* updates
    if (t >= 0.0 && VolumeContinueKey.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      VolumeContinueKey.tStart = t;  // (not accounting for frame time here)
      VolumeContinueKey.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { VolumeContinueKey.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { VolumeContinueKey.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { VolumeContinueKey.clearEvents(); });
    }

    if (VolumeContinueKey.status === PsychoJS.Status.STARTED) {
      let theseKeys = VolumeContinueKey.getKeys({keyList: ['space'], waitRelease: false});
      _VolumeContinueKey_allKeys = _VolumeContinueKey_allKeys.concat(theseKeys);
      if (_VolumeContinueKey_allKeys.length > 0) {
        VolumeContinueKey.keys = _VolumeContinueKey_allKeys[_VolumeContinueKey_allKeys.length - 1].name;  // just the last key pressed
        VolumeContinueKey.rt = _VolumeContinueKey_allKeys[_VolumeContinueKey_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of StartAdjustmentComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function StartAdjustmentRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'StartAdjustment'-------
    for (const thisComponent of StartAdjustmentComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('VolumeContinueKey.keys', VolumeContinueKey.keys);
    if (typeof VolumeContinueKey.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('VolumeContinueKey.rt', VolumeContinueKey.rt);
        routineTimer.reset();
        }
    
    VolumeContinueKey.stop();
    // the Routine "StartAdjustment" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _EndAdjustment_allKeys;
var VolumeAdjustmentComponents;
function VolumeAdjustmentRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'VolumeAdjustment'-------
    t = 0;
    VolumeAdjustmentClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    Music.setVolume(0.3);
    EndAdjustment.keys = undefined;
    EndAdjustment.rt = undefined;
    _EndAdjustment_allKeys = [];
    // keep track of which components have finished
    VolumeAdjustmentComponents = [];
    VolumeAdjustmentComponents.push(text);
    VolumeAdjustmentComponents.push(Music);
    VolumeAdjustmentComponents.push(EndAdjustment);
    VolumeAdjustmentComponents.push(AdjustContinue);
    
    for (const thisComponent of VolumeAdjustmentComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function VolumeAdjustmentRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'VolumeAdjustment'-------
    // get current time
    t = VolumeAdjustmentClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text* updates
    if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text.tStart = t;  // (not accounting for frame time here)
      text.frameNStart = frameN;  // exact frame index
      
      text.setAutoDraw(true);
    }

    // start/stop Music
    if (t >= 0.0 && Music.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Music.tStart = t;  // (not accounting for frame time here)
      Music.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ Music.play(); });  // screen flip
      Music.status = PsychoJS.Status.STARTED;
    }
    if (t >= (Music.getDuration() + Music.tStart)     && Music.status === PsychoJS.Status.STARTED) {
      Music.stop();  // stop the sound (if longer than duration)
      Music.status = PsychoJS.Status.FINISHED;
    }
    
    // *EndAdjustment* updates
    if (t >= 0.0 && EndAdjustment.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      EndAdjustment.tStart = t;  // (not accounting for frame time here)
      EndAdjustment.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { EndAdjustment.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { EndAdjustment.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { EndAdjustment.clearEvents(); });
    }

    if (EndAdjustment.status === PsychoJS.Status.STARTED) {
      let theseKeys = EndAdjustment.getKeys({keyList: ['space'], waitRelease: false});
      _EndAdjustment_allKeys = _EndAdjustment_allKeys.concat(theseKeys);
      if (_EndAdjustment_allKeys.length > 0) {
        EndAdjustment.keys = _EndAdjustment_allKeys[_EndAdjustment_allKeys.length - 1].name;  // just the last key pressed
        EndAdjustment.rt = _EndAdjustment_allKeys[_EndAdjustment_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *AdjustContinue* updates
    if (t >= 0.0 && AdjustContinue.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      AdjustContinue.tStart = t;  // (not accounting for frame time here)
      AdjustContinue.frameNStart = frameN;  // exact frame index
      
      AdjustContinue.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of VolumeAdjustmentComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function VolumeAdjustmentRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'VolumeAdjustment'-------
    for (const thisComponent of VolumeAdjustmentComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    Music.stop();  // ensure sound has stopped at end of routine
    // the Routine "VolumeAdjustment" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _ContinueResp_allKeys;
var Welcome1Components;
function Welcome1RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'Welcome1'-------
    t = 0;
    Welcome1Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    ContinueResp.keys = undefined;
    ContinueResp.rt = undefined;
    _ContinueResp_allKeys = [];
    // keep track of which components have finished
    Welcome1Components = [];
    Welcome1Components.push(WelcomeTxt1);
    Welcome1Components.push(ContinueKey1);
    Welcome1Components.push(ContinueResp);
    
    for (const thisComponent of Welcome1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function Welcome1RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'Welcome1'-------
    // get current time
    t = Welcome1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *WelcomeTxt1* updates
    if (t >= 0.0 && WelcomeTxt1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      WelcomeTxt1.tStart = t;  // (not accounting for frame time here)
      WelcomeTxt1.frameNStart = frameN;  // exact frame index
      
      WelcomeTxt1.setAutoDraw(true);
    }

    
    // *ContinueKey1* updates
    if (t >= 0.0 && ContinueKey1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ContinueKey1.tStart = t;  // (not accounting for frame time here)
      ContinueKey1.frameNStart = frameN;  // exact frame index
      
      ContinueKey1.setAutoDraw(true);
    }

    
    // *ContinueResp* updates
    if (t >= 0.0 && ContinueResp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ContinueResp.tStart = t;  // (not accounting for frame time here)
      ContinueResp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { ContinueResp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { ContinueResp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { ContinueResp.clearEvents(); });
    }

    if (ContinueResp.status === PsychoJS.Status.STARTED) {
      let theseKeys = ContinueResp.getKeys({keyList: ['space'], waitRelease: false});
      _ContinueResp_allKeys = _ContinueResp_allKeys.concat(theseKeys);
      if (_ContinueResp_allKeys.length > 0) {
        ContinueResp.keys = _ContinueResp_allKeys[_ContinueResp_allKeys.length - 1].name;  // just the last key pressed
        ContinueResp.rt = _ContinueResp_allKeys[_ContinueResp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Welcome1Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Welcome1RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'Welcome1'-------
    for (const thisComponent of Welcome1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('ContinueResp.keys', ContinueResp.keys);
    if (typeof ContinueResp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('ContinueResp.rt', ContinueResp.rt);
        routineTimer.reset();
        }
    
    ContinueResp.stop();
    // the Routine "Welcome1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _WelcomeContinueKey2_allKeys;
var PracticeBeginComponents;
function PracticeBeginRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'PracticeBegin'-------
    t = 0;
    PracticeBeginClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    WelcomeContinueKey2.keys = undefined;
    WelcomeContinueKey2.rt = undefined;
    _WelcomeContinueKey2_allKeys = [];
    // keep track of which components have finished
    PracticeBeginComponents = [];
    PracticeBeginComponents.push(InstructionTxt2);
    PracticeBeginComponents.push(WelcomeContinue2);
    PracticeBeginComponents.push(WelcomeContinueKey2);
    
    for (const thisComponent of PracticeBeginComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function PracticeBeginRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'PracticeBegin'-------
    // get current time
    t = PracticeBeginClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *InstructionTxt2* updates
    if (t >= 0.0 && InstructionTxt2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      InstructionTxt2.tStart = t;  // (not accounting for frame time here)
      InstructionTxt2.frameNStart = frameN;  // exact frame index
      
      InstructionTxt2.setAutoDraw(true);
    }

    
    // *WelcomeContinue2* updates
    if (t >= 0.0 && WelcomeContinue2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      WelcomeContinue2.tStart = t;  // (not accounting for frame time here)
      WelcomeContinue2.frameNStart = frameN;  // exact frame index
      
      WelcomeContinue2.setAutoDraw(true);
    }

    
    // *WelcomeContinueKey2* updates
    if (t >= 0.0 && WelcomeContinueKey2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      WelcomeContinueKey2.tStart = t;  // (not accounting for frame time here)
      WelcomeContinueKey2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { WelcomeContinueKey2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { WelcomeContinueKey2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { WelcomeContinueKey2.clearEvents(); });
    }

    if (WelcomeContinueKey2.status === PsychoJS.Status.STARTED) {
      let theseKeys = WelcomeContinueKey2.getKeys({keyList: ['space'], waitRelease: false});
      _WelcomeContinueKey2_allKeys = _WelcomeContinueKey2_allKeys.concat(theseKeys);
      if (_WelcomeContinueKey2_allKeys.length > 0) {
        WelcomeContinueKey2.keys = _WelcomeContinueKey2_allKeys[_WelcomeContinueKey2_allKeys.length - 1].name;  // just the last key pressed
        WelcomeContinueKey2.rt = _WelcomeContinueKey2_allKeys[_WelcomeContinueKey2_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of PracticeBeginComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function PracticeBeginRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'PracticeBegin'-------
    for (const thisComponent of PracticeBeginComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('WelcomeContinueKey2.keys', WelcomeContinueKey2.keys);
    if (typeof WelcomeContinueKey2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('WelcomeContinueKey2.rt', WelcomeContinueKey2.rt);
        routineTimer.reset();
        }
    
    WelcomeContinueKey2.stop();
    // the Routine "PracticeBegin" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var PracticeTrials;
var currentLoop;
function PracticeTrialsLoopBegin(PracticeTrialsLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  PracticeTrials = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, 'GuessSounds_conditions.xlsx', '0:5'),
    seed: undefined, name: 'PracticeTrials'
  });
  psychoJS.experiment.addLoop(PracticeTrials); // add the loop to the experiment
  currentLoop = PracticeTrials;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisPracticeTrial of PracticeTrials) {
    const snapshot = PracticeTrials.getSnapshot();
    PracticeTrialsLoopScheduler.add(importConditions(snapshot));
    PracticeTrialsLoopScheduler.add(Practice1RoutineBegin(snapshot));
    PracticeTrialsLoopScheduler.add(Practice1RoutineEachFrame(snapshot));
    PracticeTrialsLoopScheduler.add(Practice1RoutineEnd(snapshot));
    PracticeTrialsLoopScheduler.add(PracticeFeedbackRoutineBegin(snapshot));
    PracticeTrialsLoopScheduler.add(PracticeFeedbackRoutineEachFrame(snapshot));
    PracticeTrialsLoopScheduler.add(PracticeFeedbackRoutineEnd(snapshot));
    PracticeTrialsLoopScheduler.add(endLoopIteration(PracticeTrialsLoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function PracticeTrialsLoopEnd() {
  psychoJS.experiment.removeLoop(PracticeTrials);

  return Scheduler.Event.NEXT;
}


var trials;
function trialsLoopBegin(trialsLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, 'GuessSounds_conditions.xlsx', '5:115'),
    seed: undefined, name: 'trials'
  });
  psychoJS.experiment.addLoop(trials); // add the loop to the experiment
  currentLoop = trials;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisTrial of trials) {
    const snapshot = trials.getSnapshot();
    trialsLoopScheduler.add(importConditions(snapshot));
    trialsLoopScheduler.add(Count1RoutineBegin(snapshot));
    trialsLoopScheduler.add(Count1RoutineEachFrame(snapshot));
    trialsLoopScheduler.add(Count1RoutineEnd(snapshot));
    trialsLoopScheduler.add(MSTSoundRoutineBegin(snapshot));
    trialsLoopScheduler.add(MSTSoundRoutineEachFrame(snapshot));
    trialsLoopScheduler.add(MSTSoundRoutineEnd(snapshot));
    trialsLoopScheduler.add(MSTRoutineBegin(snapshot));
    trialsLoopScheduler.add(MSTRoutineEachFrame(snapshot));
    trialsLoopScheduler.add(MSTRoutineEnd(snapshot));
    trialsLoopScheduler.add(endLoopIteration(trialsLoopScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function trialsLoopEnd() {
  psychoJS.experiment.removeLoop(trials);

  return Scheduler.Event.NEXT;
}


var Practice1Components;
function Practice1RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'Practice1'-------
    t = 0;
    Practice1Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    TrialNumber.setText(TrialCount);
    PracticeSound = new sound.Sound({
    win: psychoJS.window,
    value: SoundFiles3,
    secs: -1,
    });
    PracticeSound.setVolume(1);
    // keep track of which components have finished
    Practice1Components = [];
    Practice1Components.push(TrialNumber);
    Practice1Components.push(PracticeSound);
    Practice1Components.push(PracticeCross);
    
    for (const thisComponent of Practice1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function Practice1RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'Practice1'-------
    // get current time
    t = Practice1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *TrialNumber* updates
    if (t >= 0.0 && TrialNumber.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      TrialNumber.tStart = t;  // (not accounting for frame time here)
      TrialNumber.frameNStart = frameN;  // exact frame index
      
      TrialNumber.setAutoDraw(true);
    }

    frameRemains = 0.0 + PracticeSound.getDuration() - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((TrialNumber.status === PsychoJS.Status.STARTED || TrialNumber.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      TrialNumber.setAutoDraw(false);
    }
    // start/stop PracticeSound
    if (t >= 0.0 && PracticeSound.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      PracticeSound.tStart = t;  // (not accounting for frame time here)
      PracticeSound.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ PracticeSound.play(); });  // screen flip
      PracticeSound.status = PsychoJS.Status.STARTED;
    }
    if (t >= (PracticeSound.getDuration() + PracticeSound.tStart)     && PracticeSound.status === PsychoJS.Status.STARTED) {
      PracticeSound.stop();  // stop the sound (if longer than duration)
      PracticeSound.status = PsychoJS.Status.FINISHED;
    }
    
    // *PracticeCross* updates
    if (t >= 0.0 && PracticeCross.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      PracticeCross.tStart = t;  // (not accounting for frame time here)
      PracticeCross.frameNStart = frameN;  // exact frame index
      
      PracticeCross.setAutoDraw(true);
    }

    frameRemains = 0.0 + PracticeSound.getDuration() - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((PracticeCross.status === PsychoJS.Status.STARTED || PracticeCross.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      PracticeCross.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Practice1Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Practice1RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'Practice1'-------
    for (const thisComponent of Practice1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    PracticeSound.stop();  // ensure sound has stopped at end of routine
    Tcount += 1;
    TrialCount = ("Trial " + Tcount.toString());
    
    // the Routine "Practice1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var message;
var _Practice_resp_allKeys;
var PracticeFeedbackComponents;
function PracticeFeedbackRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'PracticeFeedback'-------
    t = 0;
    PracticeFeedbackClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    if ((Correct === 3)) {
        message = "This is a NEW sound. \nThis sound has never been played before.";
    } else {
        if ((Correct === 2)) {
            message = "This is a SIMILAR sound. \nThis sound is similar but not identical to a previously played sound.";
        } else {
            if ((Correct === 1)) {
                message = "This is a REPEAT sound. \nThe exact same sound has been played previously.";
            }
        }
    }
    
    Practice_resp.keys = undefined;
    Practice_resp.rt = undefined;
    _Practice_resp_allKeys = [];
    PracticeMssg.setText(message);
    // keep track of which components have finished
    PracticeFeedbackComponents = [];
    PracticeFeedbackComponents.push(Practice_resp);
    PracticeFeedbackComponents.push(PracticeMssg);
    PracticeFeedbackComponents.push(FeedbackCross);
    PracticeFeedbackComponents.push(Continue);
    PracticeFeedbackComponents.push(Options);
    
    for (const thisComponent of PracticeFeedbackComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function PracticeFeedbackRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'PracticeFeedback'-------
    // get current time
    t = PracticeFeedbackClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Practice_resp* updates
    if (t >= 0.0 && Practice_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Practice_resp.tStart = t;  // (not accounting for frame time here)
      Practice_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { Practice_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { Practice_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { Practice_resp.clearEvents(); });
    }

    if (Practice_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = Practice_resp.getKeys({keyList: ['1', '2', '3'], waitRelease: false});
      _Practice_resp_allKeys = _Practice_resp_allKeys.concat(theseKeys);
      if (_Practice_resp_allKeys.length > 0) {
        Practice_resp.keys = _Practice_resp_allKeys[_Practice_resp_allKeys.length - 1].name;  // just the last key pressed
        Practice_resp.rt = _Practice_resp_allKeys[_Practice_resp_allKeys.length - 1].rt;
        // was this correct?
        if (Practice_resp.keys == Correct) {
            Practice_resp.corr = 1;
        } else {
            Practice_resp.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *PracticeMssg* updates
    if (t >= 0.0 && PracticeMssg.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      PracticeMssg.tStart = t;  // (not accounting for frame time here)
      PracticeMssg.frameNStart = frameN;  // exact frame index
      
      PracticeMssg.setAutoDraw(true);
    }

    
    // *FeedbackCross* updates
    if (t >= 0.0 && FeedbackCross.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      FeedbackCross.tStart = t;  // (not accounting for frame time here)
      FeedbackCross.frameNStart = frameN;  // exact frame index
      
      FeedbackCross.setAutoDraw(true);
    }

    
    // *Continue* updates
    if (t >= 0.0 && Continue.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Continue.tStart = t;  // (not accounting for frame time here)
      Continue.frameNStart = frameN;  // exact frame index
      
      Continue.setAutoDraw(true);
    }

    
    // *Options* updates
    if (t >= 0.0 && Options.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Options.tStart = t;  // (not accounting for frame time here)
      Options.frameNStart = frameN;  // exact frame index
      
      Options.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of PracticeFeedbackComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function PracticeFeedbackRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'PracticeFeedback'-------
    for (const thisComponent of PracticeFeedbackComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // was no response the correct answer?!
    if (Practice_resp.keys === undefined) {
      if (['None','none',undefined].includes(Correct)) {
         Practice_resp.corr = 1;  // correct non-response
      } else {
         Practice_resp.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for thisExp (ExperimentHandler)
    psychoJS.experiment.addData('Practice_resp.keys', Practice_resp.keys);
    psychoJS.experiment.addData('Practice_resp.corr', Practice_resp.corr);
    if (typeof Practice_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('Practice_resp.rt', Practice_resp.rt);
        routineTimer.reset();
        }
    
    Practice_resp.stop();
    // the Routine "PracticeFeedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _StartTast_allKeys;
var StartComponents;
function StartRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'Start'-------
    t = 0;
    StartClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    StartTast.keys = undefined;
    StartTast.rt = undefined;
    _StartTast_allKeys = [];
    // keep track of which components have finished
    StartComponents = [];
    StartComponents.push(StartTxt);
    StartComponents.push(StartTast);
    StartComponents.push(ContinueStart);
    
    for (const thisComponent of StartComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function StartRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'Start'-------
    // get current time
    t = StartClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *StartTxt* updates
    if (t >= 0.0 && StartTxt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      StartTxt.tStart = t;  // (not accounting for frame time here)
      StartTxt.frameNStart = frameN;  // exact frame index
      
      StartTxt.setAutoDraw(true);
    }

    
    // *StartTast* updates
    if (t >= 0.0 && StartTast.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      StartTast.tStart = t;  // (not accounting for frame time here)
      StartTast.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { StartTast.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { StartTast.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { StartTast.clearEvents(); });
    }

    if (StartTast.status === PsychoJS.Status.STARTED) {
      let theseKeys = StartTast.getKeys({keyList: ['space'], waitRelease: false});
      _StartTast_allKeys = _StartTast_allKeys.concat(theseKeys);
      if (_StartTast_allKeys.length > 0) {
        StartTast.keys = _StartTast_allKeys[_StartTast_allKeys.length - 1].name;  // just the last key pressed
        StartTast.rt = _StartTast_allKeys[_StartTast_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *ContinueStart* updates
    if (t >= 0.0 && ContinueStart.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ContinueStart.tStart = t;  // (not accounting for frame time here)
      ContinueStart.frameNStart = frameN;  // exact frame index
      
      ContinueStart.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of StartComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function StartRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'Start'-------
    for (const thisComponent of StartComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('StartTast.keys', StartTast.keys);
    if (typeof StartTast.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('StartTast.rt', StartTast.rt);
        routineTimer.reset();
        }
    
    StartTast.stop();
    // the Routine "Start" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var number;
var Count1Components;
function Count1RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'Count1'-------
    t = 0;
    Count1Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(3.000000);
    // update component parameters for each repeat
    count += 1;
    number = (count.toString() + "/110");
    
    // keep track of which components have finished
    Count1Components = [];
    Count1Components.push(no1);
    Count1Components.push(no_2);
    Count1Components.push(no_3);
    
    for (const thisComponent of Count1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function Count1RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'Count1'-------
    // get current time
    t = Count1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *no1* updates
    if (t >= 2 && no1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      no1.tStart = t;  // (not accounting for frame time here)
      no1.frameNStart = frameN;  // exact frame index
      
      no1.setAutoDraw(true);
    }

    frameRemains = 2 + 1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((no1.status === PsychoJS.Status.STARTED || no1.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      no1.setAutoDraw(false);
    }
    
    // *no_2* updates
    if (t >= 1 && no_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      no_2.tStart = t;  // (not accounting for frame time here)
      no_2.frameNStart = frameN;  // exact frame index
      
      no_2.setAutoDraw(true);
    }

    frameRemains = 1 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((no_2.status === PsychoJS.Status.STARTED || no_2.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      no_2.setAutoDraw(false);
    }
    
    // *no_3* updates
    if (t >= 0.0 && no_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      no_3.tStart = t;  // (not accounting for frame time here)
      no_3.frameNStart = frameN;  // exact frame index
      
      no_3.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((no_3.status === PsychoJS.Status.STARTED || no_3.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      no_3.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Count1Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Count1RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'Count1'-------
    for (const thisComponent of Count1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}


var MSTSoundComponents;
function MSTSoundRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'MSTSound'-------
    t = 0;
    MSTSoundClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    TargetSound = new sound.Sound({
    win: psychoJS.window,
    value: SoundFiles3,
    secs: -1,
    });
    TargetSound.setVolume(1);
    ItemNumber.setText(number);
    // keep track of which components have finished
    MSTSoundComponents = [];
    MSTSoundComponents.push(TargetSound);
    MSTSoundComponents.push(Cross);
    MSTSoundComponents.push(ItemNumber);
    
    for (const thisComponent of MSTSoundComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function MSTSoundRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'MSTSound'-------
    // get current time
    t = MSTSoundClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // start/stop TargetSound
    if (t >= 0.0 && TargetSound.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      TargetSound.tStart = t;  // (not accounting for frame time here)
      TargetSound.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ TargetSound.play(); });  // screen flip
      TargetSound.status = PsychoJS.Status.STARTED;
    }
    if (t >= (TargetSound.getDuration() + TargetSound.tStart)     && TargetSound.status === PsychoJS.Status.STARTED) {
      TargetSound.stop();  // stop the sound (if longer than duration)
      TargetSound.status = PsychoJS.Status.FINISHED;
    }
    
    // *Cross* updates
    if (t >= 0.0 && Cross.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Cross.tStart = t;  // (not accounting for frame time here)
      Cross.frameNStart = frameN;  // exact frame index
      
      Cross.setAutoDraw(true);
    }

    frameRemains = 0.0 + TargetSound.getDuration() - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((Cross.status === PsychoJS.Status.STARTED || Cross.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      Cross.setAutoDraw(false);
    }
    
    // *ItemNumber* updates
    if (t >= 0.0 && ItemNumber.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ItemNumber.tStart = t;  // (not accounting for frame time here)
      ItemNumber.frameNStart = frameN;  // exact frame index
      
      ItemNumber.setAutoDraw(true);
    }

    frameRemains = 0.0 + TargetSound.getDuration() - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((ItemNumber.status === PsychoJS.Status.STARTED || ItemNumber.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      ItemNumber.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of MSTSoundComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function MSTSoundRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'MSTSound'-------
    for (const thisComponent of MSTSoundComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    TargetSound.stop();  // ensure sound has stopped at end of routine
    // the Routine "MSTSound" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _MSTResp_allKeys;
var MSTComponents;
function MSTRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'MST'-------
    t = 0;
    MSTClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    MSTResp.keys = undefined;
    MSTResp.rt = undefined;
    _MSTResp_allKeys = [];
    // keep track of which components have finished
    MSTComponents = [];
    MSTComponents.push(MSTQuestion);
    MSTComponents.push(MSTResp);
    
    for (const thisComponent of MSTComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function MSTRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'MST'-------
    // get current time
    t = MSTClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *MSTQuestion* updates
    if (t >= 0.0 && MSTQuestion.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      MSTQuestion.tStart = t;  // (not accounting for frame time here)
      MSTQuestion.frameNStart = frameN;  // exact frame index
      
      MSTQuestion.setAutoDraw(true);
    }

    
    // *MSTResp* updates
    if (t >= 0.0 && MSTResp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      MSTResp.tStart = t;  // (not accounting for frame time here)
      MSTResp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { MSTResp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { MSTResp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { MSTResp.clearEvents(); });
    }

    if (MSTResp.status === PsychoJS.Status.STARTED) {
      let theseKeys = MSTResp.getKeys({keyList: ['1', '2', '3'], waitRelease: false});
      _MSTResp_allKeys = _MSTResp_allKeys.concat(theseKeys);
      if (_MSTResp_allKeys.length > 0) {
        MSTResp.keys = _MSTResp_allKeys[_MSTResp_allKeys.length - 1].name;  // just the last key pressed
        MSTResp.rt = _MSTResp_allKeys[_MSTResp_allKeys.length - 1].rt;
        // was this correct?
        if (MSTResp.keys == Correct) {
            MSTResp.corr = 1;
        } else {
            MSTResp.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of MSTComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function MSTRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'MST'-------
    for (const thisComponent of MSTComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // was no response the correct answer?!
    if (MSTResp.keys === undefined) {
      if (['None','none',undefined].includes(Correct)) {
         MSTResp.corr = 1;  // correct non-response
      } else {
         MSTResp.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for thisExp (ExperimentHandler)
    psychoJS.experiment.addData('MSTResp.keys', MSTResp.keys);
    psychoJS.experiment.addData('MSTResp.corr', MSTResp.corr);
    if (typeof MSTResp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('MSTResp.rt', MSTResp.rt);
        routineTimer.reset();
        }
    
    MSTResp.stop();
    // the Routine "MST" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _ExitKey_allKeys;
var EndComponents;
function EndRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'End'-------
    t = 0;
    EndClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    ExitKey.keys = undefined;
    ExitKey.rt = undefined;
    _ExitKey_allKeys = [];
    // keep track of which components have finished
    EndComponents = [];
    EndComponents.push(ThankyouMssg);
    EndComponents.push(CompletionCode);
    EndComponents.push(ExitTxt);
    EndComponents.push(ExitKey);
    EndComponents.push(CodeTxt);
    
    for (const thisComponent of EndComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function EndRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'End'-------
    // get current time
    t = EndClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *ThankyouMssg* updates
    if (t >= 0.0 && ThankyouMssg.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ThankyouMssg.tStart = t;  // (not accounting for frame time here)
      ThankyouMssg.frameNStart = frameN;  // exact frame index
      
      ThankyouMssg.setAutoDraw(true);
    }

    
    // *CompletionCode* updates
    if (t >= 0.0 && CompletionCode.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      CompletionCode.tStart = t;  // (not accounting for frame time here)
      CompletionCode.frameNStart = frameN;  // exact frame index
      
      CompletionCode.setAutoDraw(true);
    }

    
    // *ExitTxt* updates
    if (t >= 0.0 && ExitTxt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ExitTxt.tStart = t;  // (not accounting for frame time here)
      ExitTxt.frameNStart = frameN;  // exact frame index
      
      ExitTxt.setAutoDraw(true);
    }

    
    // *ExitKey* updates
    if (t >= 0.0 && ExitKey.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ExitKey.tStart = t;  // (not accounting for frame time here)
      ExitKey.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { ExitKey.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { ExitKey.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { ExitKey.clearEvents(); });
    }

    if (ExitKey.status === PsychoJS.Status.STARTED) {
      let theseKeys = ExitKey.getKeys({keyList: ['space'], waitRelease: false});
      _ExitKey_allKeys = _ExitKey_allKeys.concat(theseKeys);
      if (_ExitKey_allKeys.length > 0) {
        ExitKey.keys = _ExitKey_allKeys[_ExitKey_allKeys.length - 1].name;  // just the last key pressed
        ExitKey.rt = _ExitKey_allKeys[_ExitKey_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *CodeTxt* updates
    if (t >= 0.0 && CodeTxt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      CodeTxt.tStart = t;  // (not accounting for frame time here)
      CodeTxt.frameNStart = frameN;  // exact frame index
      
      CodeTxt.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of EndComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function EndRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'End'-------
    for (const thisComponent of EndComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('ExitKey.keys', ExitKey.keys);
    if (typeof ExitKey.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('ExitKey.rt', ExitKey.rt);
        routineTimer.reset();
        }
    
    ExitKey.stop();
    // the Routine "End" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


function endLoopIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        const thisTrial = snapshot.getCurrentTrial();
        if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
          psychoJS.experiment.nextEntry(snapshot);
        }
      }
    return Scheduler.Event.NEXT;
    }
  };
}


function importConditions(currentLoop) {
  return function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  
  
  
  
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
