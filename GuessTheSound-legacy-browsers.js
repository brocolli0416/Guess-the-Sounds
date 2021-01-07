/********************** 
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
flowScheduler.add(WelcomeRoutineBegin());
flowScheduler.add(WelcomeRoutineEachFrame());
flowScheduler.add(WelcomeRoutineEnd());
flowScheduler.add(Welcome1RoutineBegin());
flowScheduler.add(Welcome1RoutineEachFrame());
flowScheduler.add(Welcome1RoutineEnd());
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
    {'name': 'Laugh_C.wav', 'path': 'Laugh_C.wav'},
    {'name': 'Test/Foils/Slurp.wav', 'path': 'Test/Foils/Slurp.wav'},
    {'name': 'Initial/Doubled/Cough_A.wav', 'path': 'Initial/Doubled/Cough_A.wav'},
    {'name': 'GuessSounds_conditions.xlsx', 'path': 'GuessSounds_conditions.xlsx'},
    {'name': 'Initial/Repeat/ManWhistle.wav', 'path': 'Initial/Repeat/ManWhistle.wav'},
    {'name': 'Initial/Doubled/Siren_A.wav', 'path': 'Initial/Doubled/Siren_A.wav'},
    {'name': 'Piano_D.wav', 'path': 'Piano_D.wav'},
    {'name': 'Test/Foils/Donkey.wav', 'path': 'Test/Foils/Donkey.wav'},
    {'name': 'Initial/Doubled/CarStart_A.wav', 'path': 'Initial/Doubled/CarStart_A.wav'},
    {'name': 'Initial/NoRepeat/Helicopter_A.wav', 'path': 'Initial/NoRepeat/Helicopter_A.wav'},
    {'name': 'Initial/Repeat/Whistle_A.wav', 'path': 'Initial/Repeat/Whistle_A.wav'},
    {'name': 'Initial/NoRepeat/Footsteps_B.wav', 'path': 'Initial/NoRepeat/Footsteps_B.wav'},
    {'name': 'Test/Foils/Airhorn.wav', 'path': 'Test/Foils/Airhorn.wav'},
    {'name': 'Initial/Doubled/Clap_A.wav', 'path': 'Initial/Doubled/Clap_A.wav'},
    {'name': 'Initial/Doubled/Dog_A.wav', 'path': 'Initial/Doubled/Dog_A.wav'},
    {'name': 'Initial/Repeat/Airplane_B.wav', 'path': 'Initial/Repeat/Airplane_B.wav'},
    {'name': 'Piano_C.wav', 'path': 'Piano_C.wav'},
    {'name': 'Initial/Doubled/Chomp_A.wav', 'path': 'Initial/Doubled/Chomp_A.wav'},
    {'name': 'Test/Foils/Wind_B.wav', 'path': 'Test/Foils/Wind_B.wav'},
    {'name': 'Laugh_D.wav', 'path': 'Laugh_D.wav'},
    {'name': 'Carstart_B.wav', 'path': 'Carstart_B.wav'},
    {'name': 'Initial/Doubled/Cat_A.wav', 'path': 'Initial/Doubled/Cat_A.wav'},
    {'name': 'Dog_D.wav', 'path': 'Dog_D.wav'},
    {'name': 'Initial/Doubled/Writing_A.wav', 'path': 'Initial/Doubled/Writing_A.wav'},
    {'name': 'Test/Foils/PaperRip.wav', 'path': 'Test/Foils/PaperRip.wav'},
    {'name': 'CarStart_D.wav', 'path': 'CarStart_D.wav'},
    {'name': 'Cough_D.wav', 'path': 'Cough_D.wav'},
    {'name': 'Initial/Doubled/Piano_A.wav', 'path': 'Initial/Doubled/Piano_A.wav'},
    {'name': 'Initial/NoRepeat/Duck_A.wav', 'path': 'Initial/NoRepeat/Duck_A.wav'},
    {'name': 'Initial/NoRepeat/Snore_B.wav', 'path': 'Initial/NoRepeat/Snore_B.wav'},
    {'name': 'Bird_D.wav', 'path': 'Bird_D.wav'},
    {'name': 'Siren_B.wav', 'path': 'Siren_B.wav'},
    {'name': 'Initial/Doubled/Guitar_A.wav', 'path': 'Initial/Doubled/Guitar_A.wav'},
    {'name': 'Baby_A.wav', 'path': 'Baby_A.wav'},
    {'name': 'Initial/NoRepeat/Baby_B.wav', 'path': 'Initial/NoRepeat/Baby_B.wav'},
    {'name': 'Siren_C.wav', 'path': 'Siren_C.wav'},
    {'name': 'Test/Foils/Bird.wav', 'path': 'Test/Foils/Bird.wav'},
    {'name': 'Initial/Doubled/Laugh_A.wav', 'path': 'Initial/Doubled/Laugh_A.wav'},
    {'name': 'Chomp_B.wav', 'path': 'Chomp_B.wav'},
    {'name': 'Cough_C.wav', 'path': 'Cough_C.wav'},
    {'name': 'Pour_D.wav', 'path': 'Pour_D.wav'},
    {'name': 'Test/Foils/Buzz.wav', 'path': 'Test/Foils/Buzz.wav'},
    {'name': 'Initial/Doubled/Growl_A.wav', 'path': 'Initial/Doubled/Growl_A.wav'},
    {'name': 'Initial/Doubled/HairDryer_A.wav', 'path': 'Initial/Doubled/HairDryer_A.wav'},
    {'name': 'Initial/Doubled/Chime_A.wav', 'path': 'Initial/Doubled/Chime_A.wav'},
    {'name': 'Initial/NoRepeat/Toilet_B.wav', 'path': 'Initial/NoRepeat/Toilet_B.wav'},
    {'name': 'volumeadjust.wav', 'path': 'volumeadjust.wav'},
    {'name': 'Test/Foils/Camera.wav', 'path': 'Test/Foils/Camera.wav'},
    {'name': 'Chomp_C.wav', 'path': 'Chomp_C.wav'},
    {'name': 'Initial/NoRepeat/Droplet_B.wav', 'path': 'Initial/NoRepeat/Droplet_B.wav'},
    {'name': 'Initial/Repeat/IceDrop.wav', 'path': 'Initial/Repeat/IceDrop.wav'},
    {'name': 'Baby_C.wav', 'path': 'Baby_C.wav'},
    {'name': 'Initial/Doubled/Chicken_A.wav', 'path': 'Initial/Doubled/Chicken_A.wav'},
    {'name': 'Initial/NoRepeat/Fireworks.wav', 'path': 'Initial/NoRepeat/Fireworks.wav'},
    {'name': 'Bird_C.wav', 'path': 'Bird_C.wav'},
    {'name': 'Initial/NoRepeat/Mosquito_B.wav', 'path': 'Initial/NoRepeat/Mosquito_B.wav'},
    {'name': 'Initial/Repeat/Pour.wav', 'path': 'Initial/Repeat/Pour.wav'},
    {'name': 'Dog_C.wav', 'path': 'Dog_C.wav'},
    {'name': 'Pour_C.wav', 'path': 'Pour_C.wav'},
    {'name': 'Test/Foils/Typing.wav', 'path': 'Test/Foils/Typing.wav'},
    {'name': 'Test/Foils/Heartbeat.wav', 'path': 'Test/Foils/Heartbeat.wav'},
    {'name': 'Test/Foils/Bullfrog.wav', 'path': 'Test/Foils/Bullfrog.wav'}
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
var Welcome1Clock;
var WelcomeTxt1;
var ContinueKey1;
var ContinueResp;
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
  
  // Initialize components for Routine "Welcome1"
  Welcome1Clock = new util.Clock();
  WelcomeTxt1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'WelcomeTxt1',
    text: 'Occasionally, you will hear the same sound file being played for the second time. You will also hear sounds that are similar but different from a previously played sound. In each trial, please also indicate whether the sound is a new sound, a repeat, or similar to a previously played sound.',
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
  
  // Initialize components for Routine "MST"
  MSTClock = new util.Clock();
  MSTQuestion = new visual.TextStim({
    win: psychoJS.window,
    name: 'MSTQuestion',
    text: 'Has this sound been played before?\n(press the corresponding number on your keyboard)\n\n\n1 = YES, I have heard this exact same sound \n\n2 = NO, but I have heard a similar sound\n\n3 = NO, this is my first time hearing this sound\n',
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
    
    Welcome1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
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
    Welcome1Components.forEach( function(thisComponent) {
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


function Welcome1RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'Welcome1'-------
    Welcome1Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
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
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
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
    trialsLoopScheduler.add(MSTRoutineBegin(snapshot));
    trialsLoopScheduler.add(MSTRoutineEachFrame(snapshot));
    trialsLoopScheduler.add(MSTRoutineEnd(snapshot));
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
    number = (count.toString() + "/80");
    
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
    value: SoundFiles3,
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
    /* Syntax Error: Fix Python code */
    // the Routine "Study" was not non-slip safe, so reset the non-slip timer
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
    
    MSTComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
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
    MSTComponents.forEach( function(thisComponent) {
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


function MSTRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'MST'-------
    MSTComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
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
