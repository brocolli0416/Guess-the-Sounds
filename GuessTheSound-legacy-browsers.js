﻿/********************** 
 * Guessthesound Test *
 **********************/

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
flowScheduler.add(EndRoutineBegin());
flowScheduler.add(EndRoutineEachFrame());
flowScheduler.add(EndRoutineEnd());
flowScheduler.add(WelcomeRoutineBegin());
flowScheduler.add(WelcomeRoutineEachFrame());
flowScheduler.add(WelcomeRoutineEnd());
flowScheduler.add(Welcome2RoutineBegin());
flowScheduler.add(Welcome2RoutineEachFrame());
flowScheduler.add(Welcome2RoutineEnd());
flowScheduler.add(StartAdjustmentRoutineBegin());
flowScheduler.add(StartAdjustmentRoutineEachFrame());
flowScheduler.add(StartAdjustmentRoutineEnd());
flowScheduler.add(VolumeAdjustmentRoutineBegin());
flowScheduler.add(VolumeAdjustmentRoutineEachFrame());
flowScheduler.add(VolumeAdjustmentRoutineEnd());
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
    {'name': 'Test/Foils/Gallop.wav', 'path': 'Test/Foils/Gallop.wav'},
    {'name': 'Initial/Repeat/Phone_A.wav', 'path': 'Initial/Repeat/Phone_A.wav'},
    {'name': 'Initial/Doubled/Chomp_A.wav', 'path': 'Initial/Doubled/Chomp_A.wav'},
    {'name': 'Test/Foils/Harmonica.wav', 'path': 'Test/Foils/Harmonica.wav'},
    {'name': 'Initial/NoRepeat/Helicopter_A.wav', 'path': 'Initial/NoRepeat/Helicopter_A.wav'},
    {'name': 'Initial/Repeat/Cymbal_A.wav', 'path': 'Initial/Repeat/Cymbal_A.wav'},
    {'name': 'Initial/Doubled/Harp_A.wav', 'path': 'Initial/Doubled/Harp_A.wav'},
    {'name': 'volumeadjust.wav', 'path': 'volumeadjust.wav'},
    {'name': 'Initial/Doubled/Siren_A.wav', 'path': 'Initial/Doubled/Siren_A.wav'},
    {'name': 'Initial/NoRepeat/Footsteps_B.wav', 'path': 'Initial/NoRepeat/Footsteps_B.wav'},
    {'name': 'Test/Foils/Gulp.wav', 'path': 'Test/Foils/Gulp.wav'},
    {'name': 'Initial/NoRepeat/Goat_B.wav', 'path': 'Initial/NoRepeat/Goat_B.wav'},
    {'name': 'Initial/Doubled/Surf_A.wav', 'path': 'Initial/Doubled/Surf_A.wav'},
    {'name': 'Test/Foils/Slurp.wav', 'path': 'Test/Foils/Slurp.wav'},
    {'name': 'Initial/NoRepeat/Mosquito_B.wav', 'path': 'Initial/NoRepeat/Mosquito_B.wav'},
    {'name': 'Initial/Doubled/Cat_A.wav', 'path': 'Initial/Doubled/Cat_A.wav'},
    {'name': 'Initial/Repeat/Sneeze_B.wav', 'path': 'Initial/Repeat/Sneeze_B.wav'},
    {'name': 'Test/Foils/DialTone.wav', 'path': 'Test/Foils/DialTone.wav'},
    {'name': 'Initial/Doubled/Turkey_A.wav', 'path': 'Initial/Doubled/Turkey_A.wav'},
    {'name': 'Initial/Doubled/Coin_A.wav', 'path': 'Initial/Doubled/Coin_A.wav'},
    {'name': 'Initial/Doubled/Gargle_A.wav', 'path': 'Initial/Doubled/Gargle_A.wav'},
    {'name': 'Initial/Repeat/Stir.wav', 'path': 'Initial/Repeat/Stir.wav'},
    {'name': 'Initial/Doubled/Cricket_A.wav', 'path': 'Initial/Doubled/Cricket_A.wav'},
    {'name': 'Initial/NoRepeat/Hammer_A.wav', 'path': 'Initial/NoRepeat/Hammer_A.wav'},
    {'name': 'Test/Foils/Heartbeat.wav', 'path': 'Test/Foils/Heartbeat.wav'},
    {'name': 'Initial/NoRepeat/Baby_B.wav', 'path': 'Initial/NoRepeat/Baby_B.wav'},
    {'name': 'Test/Foils/Curtain.wav', 'path': 'Test/Foils/Curtain.wav'},
    {'name': 'Initial/Doubled/Windchime_A.wav', 'path': 'Initial/Doubled/Windchime_A.wav'},
    {'name': 'Initial/Doubled/Laugh_A.wav', 'path': 'Initial/Doubled/Laugh_A.wav'},
    {'name': 'Initial/Repeat/Cicade.wav', 'path': 'Initial/Repeat/Cicade.wav'},
    {'name': 'Test/Foils/Bird.wav', 'path': 'Test/Foils/Bird.wav'},
    {'name': 'Initial/NoRepeat/Eagle_B.wav', 'path': 'Initial/NoRepeat/Eagle_B.wav'},
    {'name': 'Initial/NoRepeat/Rooster_B.wav', 'path': 'Initial/NoRepeat/Rooster_B.wav'},
    {'name': 'Initial/Repeat/Drum_B.wav', 'path': 'Initial/Repeat/Drum_B.wav'},
    {'name': 'Initial/Doubled/Clap_A.wav', 'path': 'Initial/Doubled/Clap_A.wav'},
    {'name': 'Initial/Repeat/Whistle_A.wav', 'path': 'Initial/Repeat/Whistle_A.wav'},
    {'name': 'Initial/Doubled/CarStart_A.wav', 'path': 'Initial/Doubled/CarStart_A.wav'},
    {'name': 'Initial/Repeat/Pour.wav', 'path': 'Initial/Repeat/Pour.wav'},
    {'name': 'Initial/NoRepeat/Snore_B.wav', 'path': 'Initial/NoRepeat/Snore_B.wav'},
    {'name': 'Initial/NoRepeat/Toilet_B.wav', 'path': 'Initial/NoRepeat/Toilet_B.wav'},
    {'name': 'Initial/Repeat/Howl.wav', 'path': 'Initial/Repeat/Howl.wav'},
    {'name': 'Initial/NoRepeat/Sleighbells_B.wav', 'path': 'Initial/NoRepeat/Sleighbells_B.wav'},
    {'name': 'Initial/Doubled/Dog_A.wav', 'path': 'Initial/Doubled/Dog_A.wav'},
    {'name': 'Test/Foils/Steam.wav', 'path': 'Test/Foils/Steam.wav'},
    {'name': 'Initial/Repeat/Crow_B.wav', 'path': 'Initial/Repeat/Crow_B.wav'},
    {'name': 'GuessSounds_conditions.xlsx', 'path': 'GuessSounds_conditions.xlsx'},
    {'name': 'Test/Foils/Typing.wav', 'path': 'Test/Foils/Typing.wav'},
    {'name': 'Initial/Doubled/HairDryer_A.wav', 'path': 'Initial/Doubled/HairDryer_A.wav'},
    {'name': 'Initial/Doubled/Cuckoo_A.wav', 'path': 'Initial/Doubled/Cuckoo_A.wav'},
    {'name': 'Initial/NoRepeat/Chainsaw_A.wav', 'path': 'Initial/NoRepeat/Chainsaw_A.wav'},
    {'name': 'Test/Foils/Buzz.wav', 'path': 'Test/Foils/Buzz.wav'},
    {'name': 'Initial/NoRepeat/Elephant_A.wav', 'path': 'Initial/NoRepeat/Elephant_A.wav'},
    {'name': 'Initial/Doubled/Piano_A.wav', 'path': 'Initial/Doubled/Piano_A.wav'},
    {'name': 'Initial/Doubled/Chicken_A.wav', 'path': 'Initial/Doubled/Chicken_A.wav'},
    {'name': 'Initial/Repeat/IceDrop.wav', 'path': 'Initial/Repeat/IceDrop.wav'},
    {'name': 'Initial/Repeat/Trumpet_B.wav', 'path': 'Initial/Repeat/Trumpet_B.wav'},
    {'name': 'Test/Foils/Axe.wav', 'path': 'Test/Foils/Axe.wav'},
    {'name': 'Initial/Repeat/Cello.wav', 'path': 'Initial/Repeat/Cello.wav'},
    {'name': 'Initial/NoRepeat/Faucet_A.wav', 'path': 'Initial/NoRepeat/Faucet_A.wav'},
    {'name': 'Initial/Doubled/Cough_A.wav', 'path': 'Initial/Doubled/Cough_A.wav'},
    {'name': 'Initial/NoRepeat/Droplet_B.wav', 'path': 'Initial/NoRepeat/Droplet_B.wav'},
    {'name': 'Initial/Doubled/Writing_A.wav', 'path': 'Initial/Doubled/Writing_A.wav'},
    {'name': 'Initial/Doubled/Bubbles_A.wav', 'path': 'Initial/Doubled/Bubbles_A.wav'},
    {'name': 'Initial/Doubled/Chime_A.wav', 'path': 'Initial/Doubled/Chime_A.wav'},
    {'name': 'Initial/Doubled/Train_A.wav', 'path': 'Initial/Doubled/Train_A.wav'},
    {'name': 'Initial/NoRepeat/Saw_A.wav', 'path': 'Initial/NoRepeat/Saw_A.wav'},
    {'name': 'Test/Foils/Camera.wav', 'path': 'Test/Foils/Camera.wav'},
    {'name': 'Initial/NoRepeat/Thunder_A.wav', 'path': 'Initial/NoRepeat/Thunder_A.wav'},
    {'name': 'Test/Foils/Wind_B.wav', 'path': 'Test/Foils/Wind_B.wav'},
    {'name': 'Initial/Doubled/Clock_A.wav', 'path': 'Initial/Doubled/Clock_A.wav'},
    {'name': 'Test/Foils/Donkey.wav', 'path': 'Test/Foils/Donkey.wav'},
    {'name': 'Test/Foils/PartyHorn.wav', 'path': 'Test/Foils/PartyHorn.wav'},
    {'name': 'Initial/Repeat/Cup.wav', 'path': 'Initial/Repeat/Cup.wav'},
    {'name': 'Initial/Repeat/Sealion.wav', 'path': 'Initial/Repeat/Sealion.wav'},
    {'name': 'Initial/Doubled/Doorchime_A.wav', 'path': 'Initial/Doubled/Doorchime_A.wav'},
    {'name': 'Test/Foils/Bullfrog.wav', 'path': 'Test/Foils/Bullfrog.wav'},
    {'name': 'Initial/NoRepeat/Cow.wav', 'path': 'Initial/NoRepeat/Cow.wav'},
    {'name': 'Initial/Doubled/Owl_A.wav', 'path': 'Initial/Doubled/Owl_A.wav'},
    {'name': 'Initial/Doubled/Geese_A.wav', 'path': 'Initial/Doubled/Geese_A.wav'},
    {'name': 'Initial/NoRepeat/MusicBox_A.wav', 'path': 'Initial/NoRepeat/MusicBox_A.wav'},
    {'name': 'Initial/NoRepeat/Fireworks.wav', 'path': 'Initial/NoRepeat/Fireworks.wav'},
    {'name': 'Initial/NoRepeat/Puff_A.wav', 'path': 'Initial/NoRepeat/Puff_A.wav'},
    {'name': 'Initial/Repeat/Printer.wav', 'path': 'Initial/Repeat/Printer.wav'},
    {'name': 'Initial/Repeat/Bagpipe.wav', 'path': 'Initial/Repeat/Bagpipe.wav'},
    {'name': 'Test/Foils/Cards.wav', 'path': 'Test/Foils/Cards.wav'},
    {'name': 'Test/Foils/Airhorn.wav', 'path': 'Test/Foils/Airhorn.wav'},
    {'name': 'Test/Foils/Brushing.wav', 'path': 'Test/Foils/Brushing.wav'},
    {'name': 'Test/Foils/Robot.wav', 'path': 'Test/Foils/Robot.wav'},
    {'name': 'Initial/Repeat/ManWhistle.wav', 'path': 'Initial/Repeat/ManWhistle.wav'},
    {'name': 'Initial/Repeat/MetalBang.wav', 'path': 'Initial/Repeat/MetalBang.wav'},
    {'name': 'Initial/NoRepeat/Sax_A.wav', 'path': 'Initial/NoRepeat/Sax_A.wav'},
    {'name': 'Test/Foils/Bowlingpins.wav', 'path': 'Test/Foils/Bowlingpins.wav'},
    {'name': 'Initial/NoRepeat/Duck_A.wav', 'path': 'Initial/NoRepeat/Duck_A.wav'},
    {'name': 'Initial/Doubled/Guitar_A.wav', 'path': 'Initial/Doubled/Guitar_A.wav'},
    {'name': 'Initial/Repeat/Airplane_B.wav', 'path': 'Initial/Repeat/Airplane_B.wav'},
    {'name': 'Test/Foils/PaperRip.wav', 'path': 'Test/Foils/PaperRip.wav'},
    {'name': 'Initial/Repeat/Bat.wav', 'path': 'Initial/Repeat/Bat.wav'},
    {'name': 'Initial/Repeat/Pingpong.wav', 'path': 'Initial/Repeat/Pingpong.wav'},
    {'name': 'Initial/Doubled/Creak.wav', 'path': 'Initial/Doubled/Creak.wav'},
    {'name': 'Initial/Doubled/Growl_A.wav', 'path': 'Initial/Doubled/Growl_A.wav'},
    {'name': 'Test/Foils/Horse.wav', 'path': 'Test/Foils/Horse.wav'},
    {'name': 'Test/Foils/Kettle.wav', 'path': 'Test/Foils/Kettle.wav'}
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


var EndClock;
var ThankyouMssg;
var CompletionCode;
var ExitTxt;
var ExitKey;
var CodeTxt;
var WelcomeClock;
var InstructionTxt;
var WelcomeContinueKey;
var count;
var WelcomContinue;
var Welcome2Clock;
var InstructionTxt2;
var WelcomeContinue2;
var WelcomeContinueKey2;
var StartAdjustmentClock;
var VolumeBeginTxt;
var VolumeContinue;
var VolumeContinueKey;
var VolumeAdjustmentClock;
var text;
var Music;
var EndAdjustment;
var AdjustContinue;
var StartClock;
var StartTxt;
var Count3Clock;
var no3;
var Count2Clock;
var no2;
var Count1Clock;
var no1;
var StudyClock;
var Question;
var ResponseBox;
var SubmitClick;
var ClickTheButton;
var SoundItem;
var ItemNo;
var Submit;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "End"
  EndClock = new util.Clock();
  ThankyouMssg = new visual.TextStim({
    win: psychoJS.window,
    name: 'ThankyouMssg',
    text: 'This is the end of the experiment.\n\nThank you for your participation!\n\n\n\nYour Completion Code is',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.1], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  CompletionCode = new visual.TextBox({
    win: psychoJS.window,
    name: 'CompletionCode',
    text: '51DF249E',
    font: 'Arial',
    pos: [0, (- 0.1)], letterHeight: 0.04,
    size: [0.22, 0.07],  units: undefined, 
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
  
  // Initialize components for Routine "Welcome"
  WelcomeClock = new util.Clock();
  InstructionTxt = new visual.TextStim({
    win: psychoJS.window,
    name: 'InstructionTxt',
    text: "Welcome to 'Guess the Sound!'\n\n\nIn this task, you will be presented with different environmental sounds one by one. Listen to each sound and try to give it a short label so that another person, seeing only your labels, can guess what the sound was.\n\n\n",
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
  
  // Initialize components for Routine "Welcome2"
  Welcome2Clock = new util.Clock();
  InstructionTxt2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'InstructionTxt2',
    text: 'Each sound will be only played once so please listen carefully and make sure you are in a quiet environment.\n\nYou can leave your answer blank, but please try to label as many items as possible.\n\n\n',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  WelcomeContinue2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'WelcomeContinue2',
    text: 'Press SPACE to continue',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  WelcomeContinueKey2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
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
  
  // Initialize components for Routine "Start"
  StartClock = new util.Clock();
  StartTxt = new visual.TextStim({
    win: psychoJS.window,
    name: 'StartTxt',
    text: 'We will now begin the task',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "Count3"
  Count3Clock = new util.Clock();
  no3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'no3',
    text: '3',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "Count2"
  Count2Clock = new util.Clock();
  no2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'no2',
    text: '2',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
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
  
  // Initialize components for Routine "Study"
  StudyClock = new util.Clock();
  Question = new visual.TextStim({
    win: psychoJS.window,
    name: 'Question',
    text: 'What is this sound?\n',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  ResponseBox = new visual.TextBox({
    win: psychoJS.window,
    name: 'ResponseBox',
    text: 'default text',
    font: 'Arial',
    pos: [0, (- 0.2)], letterHeight: 0.03,
    size: undefined,  units: undefined, 
    color: 'black', colorSpace: 'rgb',
    fillColor: 'white', borderColor: 'black',
    bold: false, italic: false,
    opacity: 1,
    padding: undefined,
    editable: true,
    anchor: 'center',
    depth: -1.0 
  });
  
  SubmitClick = new core.Mouse({
    win: psychoJS.window,
  });
  SubmitClick.mouseClock = new util.Clock();
  ClickTheButton = new visual.TextStim({
    win: psychoJS.window,
    name: 'ClickTheButton',
    text: "Click 'Submit' to continue.",
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.03)], height: 0.025,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  SoundItem = new sound.Sound({
    win: psychoJS.window,
    value: 'A',
    secs: (- 1),
    });
  SoundItem.setVolume(1.1);
  ItemNo = new visual.TextStim({
    win: psychoJS.window,
    name: 'ItemNo',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.45], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -5.0 
  });
  
  Submit = new visual.TextBox({
    win: psychoJS.window,
    name: 'Submit',
    text: 'Submit',
    font: 'Arial',
    pos: [0, (- 0.4)], letterHeight: 0.03,
    size: [0.15, 0.1],  units: undefined, 
    color: 'black', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    bold: false, italic: false,
    opacity: 1,
    padding: undefined,
    editable: false,
    anchor: 'center',
    depth: -7.0 
  });
  
  // Initialize components for Routine "End"
  EndClock = new util.Clock();
  ThankyouMssg = new visual.TextStim({
    win: psychoJS.window,
    name: 'ThankyouMssg',
    text: 'This is the end of the experiment.\n\nThank you for your participation!\n\n\n\nYour Completion Code is',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.1], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  CompletionCode = new visual.TextBox({
    win: psychoJS.window,
    name: 'CompletionCode',
    text: '51DF249E',
    font: 'Arial',
    pos: [0, (- 0.1)], letterHeight: 0.04,
    size: [0.22, 0.07],  units: undefined, 
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
    
    EndComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
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
    EndComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
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
    EndComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
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
    
    WelcomeComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
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
    WelcomeComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
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
    WelcomeComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "Welcome" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _WelcomeContinueKey2_allKeys;
var Welcome2Components;
function Welcome2RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'Welcome2'-------
    t = 0;
    Welcome2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    WelcomeContinueKey2.keys = undefined;
    WelcomeContinueKey2.rt = undefined;
    _WelcomeContinueKey2_allKeys = [];
    // keep track of which components have finished
    Welcome2Components = [];
    Welcome2Components.push(InstructionTxt2);
    Welcome2Components.push(WelcomeContinue2);
    Welcome2Components.push(WelcomeContinueKey2);
    
    Welcome2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function Welcome2RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'Welcome2'-------
    // get current time
    t = Welcome2Clock.getTime();
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
    Welcome2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Welcome2RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'Welcome2'-------
    Welcome2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('WelcomeContinueKey2.keys', WelcomeContinueKey2.keys);
    if (typeof WelcomeContinueKey2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('WelcomeContinueKey2.rt', WelcomeContinueKey2.rt);
        routineTimer.reset();
        }
    
    WelcomeContinueKey2.stop();
    // the Routine "Welcome2" was not non-slip safe, so reset the non-slip timer
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
    
    StartAdjustmentComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
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
    StartAdjustmentComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
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
    StartAdjustmentComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
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
    
    VolumeAdjustmentComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
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
    VolumeAdjustmentComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
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
    VolumeAdjustmentComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    Music.stop();  // ensure sound has stopped at end of routine
    // the Routine "VolumeAdjustment" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var StartComponents;
function StartRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'Start'-------
    t = 0;
    StartClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(2.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    StartComponents = [];
    StartComponents.push(StartTxt);
    
    StartComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
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

    frameRemains = 0.0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((StartTxt.status === PsychoJS.Status.STARTED || StartTxt.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      StartTxt.setAutoDraw(false);
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
    StartComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function StartRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'Start'-------
    StartComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


var trials;
var currentLoop;
function trialsLoopBegin(trialsLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'GuessSounds_conditions.xlsx',
    seed: undefined, name: 'trials'
  });
  psychoJS.experiment.addLoop(trials); // add the loop to the experiment
  currentLoop = trials;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trials.forEach(function() {
    const snapshot = trials.getSnapshot();

    trialsLoopScheduler.add(importConditions(snapshot));
    trialsLoopScheduler.add(Count3RoutineBegin(snapshot));
    trialsLoopScheduler.add(Count3RoutineEachFrame(snapshot));
    trialsLoopScheduler.add(Count3RoutineEnd(snapshot));
    trialsLoopScheduler.add(Count2RoutineBegin(snapshot));
    trialsLoopScheduler.add(Count2RoutineEachFrame(snapshot));
    trialsLoopScheduler.add(Count2RoutineEnd(snapshot));
    trialsLoopScheduler.add(Count1RoutineBegin(snapshot));
    trialsLoopScheduler.add(Count1RoutineEachFrame(snapshot));
    trialsLoopScheduler.add(Count1RoutineEnd(snapshot));
    trialsLoopScheduler.add(StudyRoutineBegin(snapshot));
    trialsLoopScheduler.add(StudyRoutineEachFrame(snapshot));
    trialsLoopScheduler.add(StudyRoutineEnd(snapshot));
    trialsLoopScheduler.add(endLoopIteration(trialsLoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function trialsLoopEnd() {
  psychoJS.experiment.removeLoop(trials);

  return Scheduler.Event.NEXT;
}


var Count3Components;
function Count3RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'Count3'-------
    t = 0;
    Count3Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    Count3Components = [];
    Count3Components.push(no3);
    
    Count3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function Count3RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'Count3'-------
    // get current time
    t = Count3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *no3* updates
    if (t >= 0 && no3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      no3.tStart = t;  // (not accounting for frame time here)
      no3.frameNStart = frameN;  // exact frame index
      
      no3.setAutoDraw(true);
    }

    frameRemains = 0 + 1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((no3.status === PsychoJS.Status.STARTED || no3.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      no3.setAutoDraw(false);
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
    Count3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Count3RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'Count3'-------
    Count3Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


var Count2Components;
function Count2RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'Count2'-------
    t = 0;
    Count2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    Count2Components = [];
    Count2Components.push(no2);
    
    Count2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function Count2RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'Count2'-------
    // get current time
    t = Count2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *no2* updates
    if (t >= 0.0 && no2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      no2.tStart = t;  // (not accounting for frame time here)
      no2.frameNStart = frameN;  // exact frame index
      
      no2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((no2.status === PsychoJS.Status.STARTED || no2.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      no2.setAutoDraw(false);
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
    Count2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Count2RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'Count2'-------
    Count2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
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
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    count += 1;
    number = (count.toString() + "/60");
    
    // keep track of which components have finished
    Count1Components = [];
    Count1Components.push(no1);
    
    Count1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
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
    if (t >= 0.0 && no1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      no1.tStart = t;  // (not accounting for frame time here)
      no1.frameNStart = frameN;  // exact frame index
      
      no1.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if ((no1.status === PsychoJS.Status.STARTED || no1.status === PsychoJS.Status.FINISHED) && t >= frameRemains) {
      no1.setAutoDraw(false);
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
    Count1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
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
    Count1Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


var gotValidClick;
var StudyComponents;
function StudyRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'Study'-------
    t = 0;
    StudyClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    ResponseBox.setText('\n\n');
    // setup some python lists for storing info about the SubmitClick
    SubmitClick.clicked_name = [];
    gotValidClick = false; // until a click is received
    SoundItem = new sound.Sound({
    win: psychoJS.window,
    value: SoundFiles,
    secs: -1,
    });
    SoundItem.setVolume(1.1);
    ItemNo.setText(number);
    // keep track of which components have finished
    StudyComponents = [];
    StudyComponents.push(Question);
    StudyComponents.push(ResponseBox);
    StudyComponents.push(SubmitClick);
    StudyComponents.push(ClickTheButton);
    StudyComponents.push(SoundItem);
    StudyComponents.push(ItemNo);
    StudyComponents.push(Submit);
    
    StudyComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var prevButtonState;
var _mouseButtons;
function StudyRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'Study'-------
    // get current time
    t = StudyClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Question* updates
    if (t >= 0.0 && Question.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Question.tStart = t;  // (not accounting for frame time here)
      Question.frameNStart = frameN;  // exact frame index
      
      Question.setAutoDraw(true);
    }

    
    // *ResponseBox* updates
    if (t >= 0.0 && ResponseBox.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ResponseBox.tStart = t;  // (not accounting for frame time here)
      ResponseBox.frameNStart = frameN;  // exact frame index
      
      ResponseBox.setAutoDraw(true);
    }

    // *SubmitClick* updates
    if (t >= 0.0 && SubmitClick.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      SubmitClick.tStart = t;  // (not accounting for frame time here)
      SubmitClick.frameNStart = frameN;  // exact frame index
      
      SubmitClick.status = PsychoJS.Status.STARTED;
      SubmitClick.mouseClock.reset();
      prevButtonState = [0, 0, 0];  // if now button is down we will treat as 'new' click
      }
    if (SubmitClick.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = SubmitClick.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [Submit]) {
            if (obj.contains(SubmitClick)) {
              gotValidClick = true;
              SubmitClick.clicked_name.push(obj.name)
            }
          }
          if (gotValidClick === true) { // abort routine on response
            continueRoutine = false;
          }
        }
      }
    }
    
    // *ClickTheButton* updates
    if (t >= 0.0 && ClickTheButton.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ClickTheButton.tStart = t;  // (not accounting for frame time here)
      ClickTheButton.frameNStart = frameN;  // exact frame index
      
      ClickTheButton.setAutoDraw(true);
    }

    // start/stop SoundItem
    if (t >= 0.0 && SoundItem.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      SoundItem.tStart = t;  // (not accounting for frame time here)
      SoundItem.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ SoundItem.play(); });  // screen flip
      SoundItem.status = PsychoJS.Status.STARTED;
    }
    if (t >= (SoundItem.getDuration() + SoundItem.tStart)     && SoundItem.status === PsychoJS.Status.STARTED) {
      SoundItem.stop();  // stop the sound (if longer than duration)
      SoundItem.status = PsychoJS.Status.FINISHED;
    }
    
    // *ItemNo* updates
    if (t >= 0.0 && ItemNo.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ItemNo.tStart = t;  // (not accounting for frame time here)
      ItemNo.frameNStart = frameN;  // exact frame index
      
      ItemNo.setAutoDraw(true);
    }

    
    // *Submit* updates
    if (t >= 0.0 && Submit.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Submit.tStart = t;  // (not accounting for frame time here)
      Submit.frameNStart = frameN;  // exact frame index
      
      Submit.setAutoDraw(true);
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
    StudyComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function StudyRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'Study'-------
    StudyComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('ResponseBox.text', ResponseBox.text);
    // store data for thisExp (ExperimentHandler)
    SoundItem.stop();  // ensure sound has stopped at end of routine
    if ((count === 60)) {
        trials.finished = true;
    }
    
    // the Routine "Study" was not non-slip safe, so reset the non-slip timer
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
