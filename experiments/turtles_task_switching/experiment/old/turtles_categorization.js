/******************************* 
 * Turtles_Categorization *
 *******************************/

import { core, data, sound, util, visual, hardware } from './lib/psychojs-2024.2.1post4.js';
const { PsychoJS } = core;
const { TrialHandler, MultiStairHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = 'turtles_categorization';  // from the Builder filename that created this script
let expInfo = {
    'participant': '',
    'computer_number': '',
};

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0.6549, 0.6549, 0.6549]),
  units: 'pix',
  waitBlanking: true,
  backgroundImage: '',
  backgroundFit: 'none',
});
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
flowScheduler.add(exp_setupRoutineBegin());
flowScheduler.add(exp_setupRoutineEachFrame());
flowScheduler.add(exp_setupRoutineEnd());
flowScheduler.add(turtle_param_functionsRoutineBegin());
flowScheduler.add(turtle_param_functionsRoutineEachFrame());
flowScheduler.add(turtle_param_functionsRoutineEnd());
const categorization_instructionsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(categorization_instructionsLoopBegin(categorization_instructionsLoopScheduler));
flowScheduler.add(categorization_instructionsLoopScheduler);
flowScheduler.add(categorization_instructionsLoopEnd);









const trainingLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trainingLoopBegin(trainingLoopScheduler));
flowScheduler.add(trainingLoopScheduler);
flowScheduler.add(trainingLoopEnd);









const size_jugment_instructions_loopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(size_jugment_instructions_loopLoopBegin(size_jugment_instructions_loopLoopScheduler));
flowScheduler.add(size_jugment_instructions_loopLoopScheduler);
flowScheduler.add(size_jugment_instructions_loopLoopEnd);








const size_judgment_trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(size_judgment_trialsLoopBegin(size_judgment_trialsLoopScheduler));
flowScheduler.add(size_judgment_trialsLoopScheduler);
flowScheduler.add(size_judgment_trialsLoopEnd);









flowScheduler.add(indexRoutineBegin());
flowScheduler.add(indexRoutineEachFrame());
flowScheduler.add(indexRoutineEnd());
const transfer_trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(transfer_trialsLoopBegin(transfer_trialsLoopScheduler));
flowScheduler.add(transfer_trialsLoopScheduler);
flowScheduler.add(transfer_trialsLoopEnd);






























flowScheduler.add(begin_debriefRoutineBegin());
flowScheduler.add(begin_debriefRoutineEachFrame());
flowScheduler.add(begin_debriefRoutineEnd());
flowScheduler.add(debriefRoutineBegin());
flowScheduler.add(debriefRoutineEachFrame());
flowScheduler.add(debriefRoutineEnd());
flowScheduler.add(quitPsychoJS, 'Thank you for your patience.', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, 'Thank you for your patience.', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
    {'name': 'stim/stim_train.csv', 'path': 'stim/stim_train.csv'},
    {'name': 'stim/stim_train_with_areas.csv', 'path': 'stim/stim_train_with_areas.csv'},
    {'name': 'stim/stim_transfer_standard.csv', 'path': 'stim/stim_transfer_standard.csv'},
    {'name': 'stim/stim_transfer_switch_random_tmp.csv', 'path': 'stim/stim_transfer_switch_random_tmp.csv'},
    {'name': 'debrief.png', 'path': 'debrief.png'},
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.INFO);

async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2024.2.1post4';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  

  
  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);
  psychoJS.experiment.field_separator = '\t';


  return Scheduler.Event.NEXT;
}

async function experimentInit() {
  // Initialize components for Routine "exp_setup"
  exp_setupClock = new util.Clock();
  // Run 'Begin Experiment' code from setup
  import * as np from 'numpy';
  participant_number = Number.parseInt(expInfo["participant"]);
  num_transfer_blocks = 4;
  num_train_blocks = 4;
  num_size_blocks = 2;
  max_transfer_rt = 5;
  if (((participant_number % 2) === 0)) {
      condition = "switch/standard";
  } else {
      if (((participant_number % 2) !== 0)) {
          condition = "standard/switch";
      }
  }
  category_labels = np.array(["f", "j"]);
  np.random.shuffle(category_labels);
  category_A_label = category_labels[0];
  category_B_label = category_labels[1];
  psychoJS.experiment.addData("condition", condition);
  psychoJS.experiment.addData("category_A_label", category_A_label);
  psychoJS.experiment.addData("category_B_label", category_B_label);
  
  // Initialize components for Routine "turtle_param_functions"
  turtle_param_functionsClock = new util.Clock();
  // Run 'Begin Experiment' code from turtle_functions
  import * as np from 'numpy';
  function get_turtle_halfcircle_vertices(radius) {
      var angles, arc_x, arc_y, n_points, verts;
      n_points = 300;
      angles = np.linspace(0, np.pi, n_points);
      arc_x = (radius * np.cos(angles));
      arc_y = (radius * np.sin(angles));
      verts = np.column_stack([arc_x, arc_y]);
      verts = np.vstack([[(- radius), 0], verts, [radius, 0]]);
      return verts;
  }
  function get_turtle_wedge_vertices(angle) {
      var angle_rad, angles, arc_x, arc_y, n_points, radius, verts;
      radius = 150;
      n_points = 300;
      angle_rad = np.deg2rad(angle);
      angles = np.linspace(0, angle_rad, n_points);
      arc_x = (radius * np.cos(angles));
      arc_y = (radius * np.sin(angles));
      verts = np.column_stack([arc_x, arc_y]);
      verts = np.vstack([[0, 0], verts, [0, 0]]);
      return verts;
  }
  
  // Initialize components for Routine "categorization_instructions_p1"
  categorization_instructions_p1Clock = new util.Clock();
  categorization_instructions_text_1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'categorization_instructions_text_1',
    text: 'Welcome to the experiment!\n\nPress space to continue.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 20.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color((-1.0000, -1.0000, -1.0000)),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_7 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "categorization_instructions_p2"
  categorization_instructions_p2Clock = new util.Clock();
  categorization_instructions_text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'categorization_instructions_text_2',
    text: 'The stimuli:\n\nIn this experiment you will be making judgments about turtles!\n\nHere is an example:\n',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 20.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color((-1.0000, -1.0000, -1.0000)),  opacity: undefined,
    depth: -1.0 
  });
  
  turtle_halfcircle_for_categorization_instructions = new visual.ShapeStim({
    win: psychoJS.window, name: 'turtle_halfcircle_for_categorization_instructions', 
    vertices: [[(- 0.5), (- 0.5)], [(- 0.5), 0.5], [0.5, 0.5], [0.5, (- 0.5)]], size: [1, 1],
    ori: 0.0, 
    pos: [0, (- 200)], 
    draggable: false, 
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color([(- 1.0), 0.0039, (- 1.0)]),
    fillColor: new util.Color([(- 1.0), 0.0039, (- 1.0)]),
    fillColor: [(- 1.0), 0.0039, (- 1.0)],
    opacity: undefined, depth: -2, interpolate: true,
  });
  
  turtle_wedge_for_categorization_instructions = new visual.ShapeStim({
    win: psychoJS.window, name: 'turtle_wedge_for_categorization_instructions', 
    vertices: [[(- 0.5), (- 0.5)], [(- 0.5), 0.5], [0.5, 0.5], [0.5, (- 0.5)]], size: [1, 1],
    ori: 0.0, 
    pos: [0, (- 201)], 
    draggable: false, 
    anchor: 'center',
    lineWidth: 0.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color([1.0, 0.5059, (- 1.0)]),
    fillColor: new util.Color([1.0, 0.5059, (- 1.0)]),
    fillColor: [1.0, 0.5059, (- 1.0)],
    opacity: undefined, depth: -3, interpolate: true,
  });
  
  turtle_wedge_boundary_for_categorization_instructions = new visual.ShapeStim ({
    win: psychoJS.window, name: 'turtle_wedge_boundary_for_categorization_instructions', 
    vertices: [[-[150, 1][0]/2.0, 0], [+[150, 1][0]/2.0, 0]],
    ori: 0.0, 
    pos: [0, (- 200)], 
    draggable: false, 
    anchor: 'bottom-left',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color([1.0, 0.5059, (- 1.0)]),
    fillColor: new util.Color([1.0, 0.5059, (- 1.0)]),
    fillColor: [1.0, 0.5059, (- 1.0)],
    opacity: undefined, depth: -4, interpolate: true,
  });
  
  space = new visual.TextStim({
    win: psychoJS.window,
    name: 'space',
    text: 'Press space to continue',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 400)], draggable: false, height: 20.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -5.0 
  });
  
  key_resp_8 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "categorization_instructions_p3"
  categorization_instructions_p3Clock = new util.Clock();
  categorization_instructions_text_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'categorization_instructions_text_3',
    text: 'Here is another example:\n',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 20.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color((-1.0000, -1.0000, -1.0000)),  opacity: undefined,
    depth: -1.0 
  });
  
  turtle_halfcircle_for_categorization_instructions_2 = new visual.ShapeStim({
    win: psychoJS.window, name: 'turtle_halfcircle_for_categorization_instructions_2', 
    vertices: [[(- 0.5), (- 0.5)], [(- 0.5), 0.5], [0.5, 0.5], [0.5, (- 0.5)]], size: [1, 1],
    ori: 0.0, 
    pos: [0, (- 200)], 
    draggable: false, 
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color([(- 1.0), 0.0039, (- 1.0)]),
    fillColor: new util.Color([(- 1.0), 0.0039, (- 1.0)]),
    fillColor: [(- 1.0), 0.0039, (- 1.0)],
    opacity: undefined, depth: -2, interpolate: true,
  });
  
  space_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'space_2',
    text: 'Press space to continue',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 400)], draggable: false, height: 20.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -3.0 
  });
  
  key_resp_9 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  turtle_wedge_for_categorization_instructions_2 = new visual.ShapeStim({
    win: psychoJS.window, name: 'turtle_wedge_for_categorization_instructions_2', 
    vertices: [[(- 0.5), (- 0.5)], [(- 0.5), 0.5], [0.5, 0.5], [0.5, (- 0.5)]], size: [1, 1],
    ori: 0.0, 
    pos: [0, (- 201)], 
    draggable: false, 
    anchor: 'center',
    lineWidth: 0.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color([1.0, 0.5059, (- 1.0)]),
    fillColor: new util.Color([1.0, 0.5059, (- 1.0)]),
    fillColor: [1.0, 0.5059, (- 1.0)],
    opacity: undefined, depth: -5, interpolate: true,
  });
  
  turtle_wedge_boundary_for_categorization_instructions_2 = new visual.ShapeStim ({
    win: psychoJS.window, name: 'turtle_wedge_boundary_for_categorization_instructions_2', 
    vertices: [[-[150, 1][0]/2.0, 0], [+[150, 1][0]/2.0, 0]],
    ori: 0.0, 
    pos: [0, (- 200)], 
    draggable: false, 
    anchor: 'bottom-left',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color([1.0, 0.5059, (- 1.0)]),
    fillColor: new util.Color([1.0, 0.5059, (- 1.0)]),
    fillColor: [1.0, 0.5059, (- 1.0)],
    opacity: undefined, depth: -6, interpolate: true,
  });
  
  // Initialize components for Routine "categorization_instructions_p4"
  categorization_instructions_p4Clock = new util.Clock();
  categorization_instructions_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'categorization_instructions_text',
    text: 'First, you are tasked with determining which turtle belongs to Species F or Species J. \n\nThere are TWO components related to the turtles’ species classification. You should consider both \n-   the height of the green shell AND\n\n-   the angle of the yellow head\n',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 20.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color((-1.0000, -1.0000, -1.0000)),  opacity: undefined,
    depth: 0.0 
  });
  
  turtle_halfcircle_for_categorization_instructions_3 = new visual.ShapeStim({
    win: psychoJS.window, name: 'turtle_halfcircle_for_categorization_instructions_3', 
    vertices: [[(- 0.5), (- 0.5)], [(- 0.5), 0.5], [0.5, 0.5], [0.5, (- 0.5)]], size: [1, 1],
    ori: 0.0, 
    pos: [0, (- 200)], 
    draggable: false, 
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color([(- 1.0), 0.0039, (- 1.0)]),
    fillColor: new util.Color([(- 1.0), 0.0039, (- 1.0)]),
    fillColor: [(- 1.0), 0.0039, (- 1.0)],
    opacity: undefined, depth: -1, interpolate: true,
  });
  
  turtle_wedge_for_categorization_instructions_3 = new visual.ShapeStim({
    win: psychoJS.window, name: 'turtle_wedge_for_categorization_instructions_3', 
    vertices: [[(- 0.5), (- 0.5)], [(- 0.5), 0.5], [0.5, 0.5], [0.5, (- 0.5)]], size: [1, 1],
    ori: 0.0, 
    pos: [0, (- 201)], 
    draggable: false, 
    anchor: 'center',
    lineWidth: 0.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color([1.0, 0.5059, (- 1.0)]),
    fillColor: new util.Color([1.0, 0.5059, (- 1.0)]),
    fillColor: [1.0, 0.5059, (- 1.0)],
    opacity: undefined, depth: -2, interpolate: true,
  });
  
  space_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'space_3',
    text: 'Press space to continue',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 400)], draggable: false, height: 20.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -3.0 
  });
  
  turtle_wedge_boundary_for_categorization_instructions_3 = new visual.ShapeStim ({
    win: psychoJS.window, name: 'turtle_wedge_boundary_for_categorization_instructions_3', 
    vertices: [[-[150, 1][0]/2.0, 0], [+[150, 1][0]/2.0, 0]],
    ori: 0.0, 
    pos: [0, (- 200)], 
    draggable: false, 
    anchor: 'bottom-left',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color([1.0, 0.5059, (- 1.0)]),
    fillColor: new util.Color([1.0, 0.5059, (- 1.0)]),
    fillColor: [1.0, 0.5059, (- 1.0)],
    opacity: undefined, depth: -4, interpolate: true,
  });
  
  key_resp_10 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "categorization_instructions_p5"
  categorization_instructions_p5Clock = new util.Clock();
  categorization_instructions_text_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'categorization_instructions_text_4',
    text: 'For now, you will learn to classify a single turtle on each trial.\n\n\nBefore each trial, you will see a plus sign. This will let you know that you are about to see a new turtle.\n\n\nWhen the trial begins, you will be shown a turtle.\n\n',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 20.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color((-1.0000, -1.0000, -1.0000)),  opacity: undefined,
    depth: 0.0 
  });
  
  turtle_halfcircle_for_categorization_instructions_4 = new visual.ShapeStim({
    win: psychoJS.window, name: 'turtle_halfcircle_for_categorization_instructions_4', 
    vertices: [[(- 0.5), (- 0.5)], [(- 0.5), 0.5], [0.5, 0.5], [0.5, (- 0.5)]], size: [1, 1],
    ori: 0.0, 
    pos: [0, (- 200)], 
    draggable: false, 
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color([(- 1.0), 0.0039, (- 1.0)]),
    fillColor: new util.Color([(- 1.0), 0.0039, (- 1.0)]),
    fillColor: [(- 1.0), 0.0039, (- 1.0)],
    opacity: undefined, depth: -1, interpolate: true,
  });
  
  turtle_wedge_for_categorization_instructions_4 = new visual.ShapeStim({
    win: psychoJS.window, name: 'turtle_wedge_for_categorization_instructions_4', 
    vertices: [[(- 0.5), (- 0.5)], [(- 0.5), 0.5], [0.5, 0.5], [0.5, (- 0.5)]], size: [1, 1],
    ori: 0.0, 
    pos: [0, (- 201)], 
    draggable: false, 
    anchor: 'center',
    lineWidth: 0.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color([1.0, 0.5059, (- 1.0)]),
    fillColor: new util.Color([1.0, 0.5059, (- 1.0)]),
    fillColor: [1.0, 0.5059, (- 1.0)],
    opacity: undefined, depth: -2, interpolate: true,
  });
  
  space_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'space_4',
    text: 'Press space to continue',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 400)], draggable: false, height: 20.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -3.0 
  });
  
  turtle_wedge_boundary_for_categorization_instructions_4 = new visual.ShapeStim ({
    win: psychoJS.window, name: 'turtle_wedge_boundary_for_categorization_instructions_4', 
    vertices: [[-[150, 1][0]/2.0, 0], [+[150, 1][0]/2.0, 0]],
    ori: 0.0, 
    pos: [0, (- 200)], 
    draggable: false, 
    anchor: 'bottom-left',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color([1.0, 0.5059, (- 1.0)]),
    fillColor: new util.Color([1.0, 0.5059, (- 1.0)]),
    fillColor: [1.0, 0.5059, (- 1.0)],
    opacity: undefined, depth: -4, interpolate: true,
  });
  
  key_resp_11 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "categorization_instructions_p6"
  categorization_instructions_p6Clock = new util.Clock();
  categorization_instructions_text_5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'categorization_instructions_text_5',
    text: 'Press “f” on the keyboard if the turtle belongs to Species F, and “j” if it belongs to Species J.\n\n\nAfter each response you will be told whether or not your answer was correct.\n\n\nAt first you will be guessing, however, the feedback will help you get better at classifying these turtles.\n\n',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 20.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color((-1.0000, -1.0000, -1.0000)),  opacity: undefined,
    depth: 0.0 
  });
  
  turtle_halfcircle_for_categorization_instructions_5 = new visual.ShapeStim({
    win: psychoJS.window, name: 'turtle_halfcircle_for_categorization_instructions_5', 
    vertices: [[(- 0.5), (- 0.5)], [(- 0.5), 0.5], [0.5, 0.5], [0.5, (- 0.5)]], size: [1, 1],
    ori: 0.0, 
    pos: [0, (- 200)], 
    draggable: false, 
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color([(- 1.0), 0.0039, (- 1.0)]),
    fillColor: new util.Color([(- 1.0), 0.0039, (- 1.0)]),
    fillColor: [(- 1.0), 0.0039, (- 1.0)],
    opacity: undefined, depth: -1, interpolate: true,
  });
  
  turtle_wedge_for_categorization_instructions_5 = new visual.ShapeStim({
    win: psychoJS.window, name: 'turtle_wedge_for_categorization_instructions_5', 
    vertices: [[(- 0.5), (- 0.5)], [(- 0.5), 0.5], [0.5, 0.5], [0.5, (- 0.5)]], size: [1, 1],
    ori: 0.0, 
    pos: [0, (- 201)], 
    draggable: false, 
    anchor: 'center',
    lineWidth: 0.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color([1.0, 0.5059, (- 1.0)]),
    fillColor: new util.Color([1.0, 0.5059, (- 1.0)]),
    fillColor: [1.0, 0.5059, (- 1.0)],
    opacity: undefined, depth: -2, interpolate: true,
  });
  
  turtle_wedge_boundary_for_categorization_instructions_5 = new visual.ShapeStim ({
    win: psychoJS.window, name: 'turtle_wedge_boundary_for_categorization_instructions_5', 
    vertices: [[-[150, 1][0]/2.0, 0], [+[150, 1][0]/2.0, 0]],
    ori: 0.0, 
    pos: [0, (- 200)], 
    draggable: false, 
    anchor: 'bottom-left',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color([1.0, 0.5059, (- 1.0)]),
    fillColor: new util.Color([1.0, 0.5059, (- 1.0)]),
    fillColor: [1.0, 0.5059, (- 1.0)],
    opacity: undefined, depth: -3, interpolate: true,
  });
  
  space_5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'space_5',
    text: 'Press space to continue',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 400)], draggable: false, height: 20.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -4.0 
  });
  
  key_resp_12 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "categorization_instructions_p7"
  categorization_instructions_p7Clock = new util.Clock();
  categorization_instructions_text_6 = new visual.TextStim({
    win: psychoJS.window,
    name: 'categorization_instructions_text_6',
    text: 'There will be other parts to this experiment, but instructions for those will come later.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 20.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color((-1.0000, -1.0000, -1.0000)),  opacity: undefined,
    depth: 0.0 
  });
  
  turtle_halfcircle_for_categorization_instructions_6 = new visual.ShapeStim({
    win: psychoJS.window, name: 'turtle_halfcircle_for_categorization_instructions_6', 
    vertices: [[(- 0.5), (- 0.5)], [(- 0.5), 0.5], [0.5, 0.5], [0.5, (- 0.5)]], size: [1, 1],
    ori: 0.0, 
    pos: [0, (- 200)], 
    draggable: false, 
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color([(- 1.0), 0.0039, (- 1.0)]),
    fillColor: new util.Color([(- 1.0), 0.0039, (- 1.0)]),
    fillColor: [(- 1.0), 0.0039, (- 1.0)],
    opacity: undefined, depth: -1, interpolate: true,
  });
  
  turtle_wedge_for_categorization_instructions_6 = new visual.ShapeStim({
    win: psychoJS.window, name: 'turtle_wedge_for_categorization_instructions_6', 
    vertices: [[(- 0.5), (- 0.5)], [(- 0.5), 0.5], [0.5, 0.5], [0.5, (- 0.5)]], size: [1, 1],
    ori: 0.0, 
    pos: [0, (- 201)], 
    draggable: false, 
    anchor: 'center',
    lineWidth: 0.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color([1.0, 0.5059, (- 1.0)]),
    fillColor: new util.Color([1.0, 0.5059, (- 1.0)]),
    fillColor: [1.0, 0.5059, (- 1.0)],
    opacity: undefined, depth: -2, interpolate: true,
  });
  
  turtle_wedge_boundary_for_categorization_instructions_6 = new visual.ShapeStim ({
    win: psychoJS.window, name: 'turtle_wedge_boundary_for_categorization_instructions_6', 
    vertices: [[-[150, 1][0]/2.0, 0], [+[150, 1][0]/2.0, 0]],
    ori: 0.0, 
    pos: [0, (- 200)], 
    draggable: false, 
    anchor: 'bottom-left',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color([1.0, 0.5059, (- 1.0)]),
    fillColor: new util.Color([1.0, 0.5059, (- 1.0)]),
    fillColor: [1.0, 0.5059, (- 1.0)],
    opacity: undefined, depth: -3, interpolate: true,
  });
  
  space_6 = new visual.TextStim({
    win: psychoJS.window,
    name: 'space_6',
    text: 'Press space to continue',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 400)], draggable: false, height: 20.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -4.0 
  });
  
  key_resp_13 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "categorization_instructions_p8"
  categorization_instructions_p8Clock = new util.Clock();
  space_to_begin_exp = new visual.TextStim({
    win: psychoJS.window,
    name: 'space_to_begin_exp',
    text: 'Press space to begin classifying turtles.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 20.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color((-1.0000, -1.0000, -1.0000)),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_14 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "fixation_cross"
  fixation_crossClock = new util.Clock();
  fixation_cross_1 = new visual.ShapeStim ({
    win: psychoJS.window, name: 'fixation_cross_1', 
    vertices: 'cross', size:[30, 30],
    ori: 0.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
    fillColor: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
    fillColor: [(- 1.0), (- 1.0), (- 1.0)],
    opacity: undefined, depth: 0, interpolate: true,
  });
  
  // Initialize components for Routine "blank"
  blankClock = new util.Clock();
  text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_2',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "get_turtle_params_training"
  get_turtle_params_trainingClock = new util.Clock();
  // Initialize components for Routine "training_response"
  training_responseClock = new util.Clock();
  key_resp_training = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  turtle_halfcircle = new visual.ShapeStim({
    win: psychoJS.window, name: 'turtle_halfcircle', 
    vertices: [[(- 0.5), (- 0.5)], [(- 0.5), 0.5], [0.5, 0.5], [0.5, (- 0.5)]], size: [1, 1],
    ori: 0.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color([(- 1.0), 0.0039, (- 1.0)]),
    fillColor: new util.Color([(- 1.0), 0.0039, (- 1.0)]),
    fillColor: [(- 1.0), 0.0039, (- 1.0)],
    opacity: undefined, depth: -1, interpolate: true,
  });
  
  turtle_wedge = new visual.ShapeStim({
    win: psychoJS.window, name: 'turtle_wedge', 
    vertices: [[(- 0.5), (- 0.5)], [(- 0.5), 0.5], [0.5, 0.5], [0.5, (- 0.5)]], size: [1, 1],
    ori: 0.0, 
    pos: [0, (- 1)], 
    draggable: false, 
    anchor: 'center',
    lineWidth: 0.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color([1.0, 0.5059, (- 1.0)]),
    fillColor: new util.Color([1.0, 0.5059, (- 1.0)]),
    fillColor: [1.0, 0.5059, (- 1.0)],
    opacity: undefined, depth: -2, interpolate: true,
  });
  
  turtle_wedge_boundary = new visual.Rect ({
    win: psychoJS.window, name: 'turtle_wedge_boundary', 
    width: [150, 1][0], height: [150, 1][1],
    ori: 0.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'bottom-left',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color([1.0, 0.5059, (- 1.0)]),
    fillColor: new util.Color([1.0, 0.5059, (- 1.0)]),
    fillColor: [1.0, 0.5059, (- 1.0)],
    opacity: undefined, depth: -3, interpolate: true,
  });
  
  training_prompt = new visual.TextStim({
    win: psychoJS.window,
    name: 'training_prompt',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 100)], draggable: false, height: 20.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: 1.0,
    depth: -4.0 
  });
  
  // Initialize components for Routine "train_feedback_code_checks"
  train_feedback_code_checksClock = new util.Clock();
  // Initialize components for Routine "training_feedback"
  training_feedbackClock = new util.Clock();
  train_feedback_text_display = new visual.TextStim({
    win: psychoJS.window,
    name: 'train_feedback_text_display',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 100)], draggable: false, height: 20.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  turtle_halfcircle_for_feedback = new visual.ShapeStim({
    win: psychoJS.window, name: 'turtle_halfcircle_for_feedback', 
    vertices: [[(- 0.5), (- 0.5)], [(- 0.5), 0.5], [0.5, 0.5], [0.5, (- 0.5)]], size: [1, 1],
    ori: 0.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color([(- 1.0), 0.0039, (- 1.0)]),
    fillColor: new util.Color([(- 1.0), 0.0039, (- 1.0)]),
    fillColor: [(- 1.0), 0.0039, (- 1.0)],
    opacity: undefined, depth: -1, interpolate: true,
  });
  
  turtle_wedge_for_feedback = new visual.ShapeStim({
    win: psychoJS.window, name: 'turtle_wedge_for_feedback', 
    vertices: [[(- 0.5), (- 0.5)], [(- 0.5), 0.5], [0.5, 0.5], [0.5, (- 0.5)]], size: [1, 1],
    ori: 0.0, 
    pos: [0, (- 1)], 
    draggable: false, 
    anchor: 'center',
    lineWidth: 0.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color([1.0, 0.5059, (- 1.0)]),
    fillColor: new util.Color([1.0, 0.5059, (- 1.0)]),
    fillColor: [1.0, 0.5059, (- 1.0)],
    opacity: undefined, depth: -2, interpolate: true,
  });
  
  turtle_wedge_boundary_for_feedback = new visual.ShapeStim ({
    win: psychoJS.window, name: 'turtle_wedge_boundary_for_feedback', 
    vertices: [[-[150, 1][0]/2.0, 0], [+[150, 1][0]/2.0, 0]],
    ori: 0.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'bottom-left',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color([1.0, 0.5059, (- 1.0)]),
    fillColor: new util.Color([1.0, 0.5059, (- 1.0)]),
    fillColor: [1.0, 0.5059, (- 1.0)],
    opacity: undefined, depth: -3, interpolate: true,
  });
  
  // Initialize components for Routine "del_corr_resp"
  del_corr_respClock = new util.Clock();
  // Initialize components for Routine "avg_turtle_setup"
  avg_turtle_setupClock = new util.Clock();
  // Run 'Begin Experiment' code from get_avg_turtle
  import * as pd from 'pandas';
  avg_turtle = pd.read_csv("stim/stim_avg_turtle.csv");
  avg_turtle_radius = avg_turtle["radius"][0];
  avg_turtle_angle = avg_turtle["angle"][0];
  avg_turtle_halfcircle_vertices = get_turtle_halfcircle_vertices(avg_turtle_radius);
  avg_turtle_wedge_vertices = get_turtle_wedge_vertices(avg_turtle_angle);
  avg_turtle_area = avg_turtle["area"][0];
  
  // Initialize components for Routine "size_judgment_instructions_p1"
  size_judgment_instructions_p1Clock = new util.Clock();
  avg_turtle_instr_1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'avg_turtle_instr_1',
    text: 'You have completed the first phase of the experiment.\n\nPress space to continue.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 20.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "size_judgment_instructions_p2"
  size_judgment_instructions_p2Clock = new util.Clock();
  avg_turtle_instr_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'avg_turtle_instr_2',
    text: 'In the next phase, we are going to ask you to learn something else about the turtles. \n\nHowever, make sure not to forget the turtle species names you just learned.\n\nPress space to continue.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 20.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "size_judgment_instructions_p3"
  size_judgment_instructions_p3Clock = new util.Clock();
  turtle_halfcircle_for_size_instructions = new visual.ShapeStim({
    win: psychoJS.window, name: 'turtle_halfcircle_for_size_instructions', 
    vertices: [[(- 0.5), (- 0.5)], [(- 0.5), 0.5], [0.5, 0.5], [0.5, (- 0.5)]], size: [1, 1],
    ori: 0.0, 
    pos: [0, (- 200)], 
    draggable: false, 
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color([(- 1.0), 0.0039, (- 1.0)]),
    fillColor: new util.Color([(- 1.0), 0.0039, (- 1.0)]),
    fillColor: [(- 1.0), 0.0039, (- 1.0)],
    opacity: undefined, depth: 0, interpolate: true,
  });
  
  turtle_wedge_for_size_instructions = new visual.ShapeStim({
    win: psychoJS.window, name: 'turtle_wedge_for_size_instructions', 
    vertices: [[(- 0.5), (- 0.5)], [(- 0.5), 0.5], [0.5, 0.5], [0.5, (- 0.5)]], size: [1, 1],
    ori: 0.0, 
    pos: [0, (- 201)], 
    draggable: false, 
    anchor: 'center',
    lineWidth: 0.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color([1.0, 0.5059, (- 1.0)]),
    fillColor: new util.Color([1.0, 0.5059, (- 1.0)]),
    fillColor: [1.0, 0.5059, (- 1.0)],
    opacity: undefined, depth: -1, interpolate: true,
  });
  
  turtle_wedge_boundary_for_instructions = new visual.ShapeStim ({
    win: psychoJS.window, name: 'turtle_wedge_boundary_for_instructions', 
    vertices: [[-[150, 1][0]/2.0, 0], [+[150, 1][0]/2.0, 0]],
    ori: 0.0, 
    pos: [0, (- 200)], 
    draggable: false, 
    anchor: 'bottom-left',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color([1.0, 0.5059, (- 1.0)]),
    fillColor: new util.Color([1.0, 0.5059, (- 1.0)]),
    fillColor: [1.0, 0.5059, (- 1.0)],
    opacity: undefined, depth: -2, interpolate: true,
  });
  
  avg_turtle_instr_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'avg_turtle_instr_3',
    text: 'Here is an average turtle. This turtle’s size - the total area taken up by its shell and head - is very average compared to the other turtles you have seen so far.\n\npress space to continue',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 20.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: -3.0 
  });
  
  key_resp_3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "size_judgment_instructions_p4"
  size_judgment_instructions_p4Clock = new util.Clock();
  turtle_halfcircle_for_size_instructions_2 = new visual.ShapeStim({
    win: psychoJS.window, name: 'turtle_halfcircle_for_size_instructions_2', 
    vertices: [[(- 0.5), (- 0.5)], [(- 0.5), 0.5], [0.5, 0.5], [0.5, (- 0.5)]], size: [1, 1],
    ori: 0.0, 
    pos: [0, (- 200)], 
    draggable: false, 
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color([(- 1.0), 0.0039, (- 1.0)]),
    fillColor: new util.Color([(- 1.0), 0.0039, (- 1.0)]),
    fillColor: [(- 1.0), 0.0039, (- 1.0)],
    opacity: undefined, depth: 0, interpolate: true,
  });
  
  turtle_wedge_for_size_instructions_2 = new visual.ShapeStim({
    win: psychoJS.window, name: 'turtle_wedge_for_size_instructions_2', 
    vertices: [[(- 0.5), (- 0.5)], [(- 0.5), 0.5], [0.5, 0.5], [0.5, (- 0.5)]], size: [1, 1],
    ori: 0.0, 
    pos: [0, (- 201)], 
    draggable: false, 
    anchor: 'center',
    lineWidth: 0.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color([1.0, 0.5059, (- 1.0)]),
    fillColor: new util.Color([1.0, 0.5059, (- 1.0)]),
    fillColor: [1.0, 0.5059, (- 1.0)],
    opacity: undefined, depth: -1, interpolate: true,
  });
  
  turtle_wedge_boundary_for_instructions_2 = new visual.ShapeStim ({
    win: psychoJS.window, name: 'turtle_wedge_boundary_for_instructions_2', 
    vertices: [[-[150, 1][0]/2.0, 0], [+[150, 1][0]/2.0, 0]],
    ori: 0.0, 
    pos: [0, (- 200)], 
    draggable: false, 
    anchor: 'bottom-left',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color([1.0, 0.5059, (- 1.0)]),
    fillColor: new util.Color([1.0, 0.5059, (- 1.0)]),
    fillColor: [1.0, 0.5059, (- 1.0)],
    opacity: undefined, depth: -2, interpolate: true,
  });
  
  avg_turtle_instr = new visual.TextStim({
    win: psychoJS.window,
    name: 'avg_turtle_instr',
    text: 'Your task, in the next part of the experiment, is to determine whether each turtle you see is smaller or larger than this average turtle.\n\nYou will still use the f and j keys - f for smaller, j for larger.\n\nPress space to continue.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 20.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: -3.0 
  });
  
  key_resp_4 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "size_jugment_instructions_p5"
  size_jugment_instructions_p5Clock = new util.Clock();
  turtle_halfcircle_for_size_instructions_3 = new visual.ShapeStim({
    win: psychoJS.window, name: 'turtle_halfcircle_for_size_instructions_3', 
    vertices: [[(- 0.5), (- 0.5)], [(- 0.5), 0.5], [0.5, 0.5], [0.5, (- 0.5)]], size: [1, 1],
    ori: 0.0, 
    pos: [0, (- 200)], 
    draggable: false, 
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color([(- 1.0), 0.0039, (- 1.0)]),
    fillColor: new util.Color([(- 1.0), 0.0039, (- 1.0)]),
    fillColor: [(- 1.0), 0.0039, (- 1.0)],
    opacity: undefined, depth: 0, interpolate: true,
  });
  
  turtle_wedge_for_size_instructions_3 = new visual.ShapeStim({
    win: psychoJS.window, name: 'turtle_wedge_for_size_instructions_3', 
    vertices: [[(- 0.5), (- 0.5)], [(- 0.5), 0.5], [0.5, 0.5], [0.5, (- 0.5)]], size: [1, 1],
    ori: 0.0, 
    pos: [0, (- 201)], 
    draggable: false, 
    anchor: 'center',
    lineWidth: 0.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color([1.0, 0.5059, (- 1.0)]),
    fillColor: new util.Color([1.0, 0.5059, (- 1.0)]),
    fillColor: [1.0, 0.5059, (- 1.0)],
    opacity: undefined, depth: -1, interpolate: true,
  });
  
  turtle_wedge_boundary_for_instructions_3 = new visual.ShapeStim ({
    win: psychoJS.window, name: 'turtle_wedge_boundary_for_instructions_3', 
    vertices: [[-[150, 1][0]/2.0, 0], [+[150, 1][0]/2.0, 0]],
    ori: 0.0, 
    pos: [0, (- 200)], 
    draggable: false, 
    anchor: 'bottom-left',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color([1.0, 0.5059, (- 1.0)]),
    fillColor: new util.Color([1.0, 0.5059, (- 1.0)]),
    fillColor: [1.0, 0.5059, (- 1.0)],
    opacity: undefined, depth: -2, interpolate: true,
  });
  
  avg_turtle_instr_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'avg_turtle_instr_4',
    text: 'We will still give you feedback on your answer.\n\nSome trials will be harder than others; we simply ask you to please try your best.\n\nPress space to continue.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 20.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: -3.0 
  });
  
  key_resp_5 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "size_judgment_instructions_p6"
  size_judgment_instructions_p6Clock = new util.Clock();
  turtle_halfcircle_for_size_instructions_4 = new visual.ShapeStim({
    win: psychoJS.window, name: 'turtle_halfcircle_for_size_instructions_4', 
    vertices: [[(- 0.5), (- 0.5)], [(- 0.5), 0.5], [0.5, 0.5], [0.5, (- 0.5)]], size: [1, 1],
    ori: 0.0, 
    pos: [0, (- 200)], 
    draggable: false, 
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color([(- 1.0), 0.0039, (- 1.0)]),
    fillColor: new util.Color([(- 1.0), 0.0039, (- 1.0)]),
    fillColor: [(- 1.0), 0.0039, (- 1.0)],
    opacity: undefined, depth: 0, interpolate: true,
  });
  
  turtle_wedge_for_size_instructions_4 = new visual.ShapeStim({
    win: psychoJS.window, name: 'turtle_wedge_for_size_instructions_4', 
    vertices: [[(- 0.5), (- 0.5)], [(- 0.5), 0.5], [0.5, 0.5], [0.5, (- 0.5)]], size: [1, 1],
    ori: 0.0, 
    pos: [0, (- 201)], 
    draggable: false, 
    anchor: 'center',
    lineWidth: 0.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color([1.0, 0.5059, (- 1.0)]),
    fillColor: new util.Color([1.0, 0.5059, (- 1.0)]),
    fillColor: [1.0, 0.5059, (- 1.0)],
    opacity: undefined, depth: -1, interpolate: true,
  });
  
  turtle_wedge_boundary_for_instructions_4 = new visual.ShapeStim ({
    win: psychoJS.window, name: 'turtle_wedge_boundary_for_instructions_4', 
    vertices: [[-[150, 1][0]/2.0, 0], [+[150, 1][0]/2.0, 0]],
    ori: 0.0, 
    pos: [0, (- 200)], 
    draggable: false, 
    anchor: 'bottom-left',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color([1.0, 0.5059, (- 1.0)]),
    fillColor: new util.Color([1.0, 0.5059, (- 1.0)]),
    fillColor: [1.0, 0.5059, (- 1.0)],
    opacity: undefined, depth: -2, interpolate: true,
  });
  
  avg_turtle_instr_5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'avg_turtle_instr_5',
    text: 'The next part of the experiment will now begin.\n\nPress space to continue.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 20.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: -3.0 
  });
  
  key_resp_6 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "size_judgment_params"
  size_judgment_paramsClock = new util.Clock();
  // Initialize components for Routine "size_judgment_response"
  size_judgment_responseClock = new util.Clock();
  turtle_half_circle_for_size_judgment = new visual.ShapeStim({
    win: psychoJS.window, name: 'turtle_half_circle_for_size_judgment', 
    vertices: [[(- 0.5), (- 0.5)], [(- 0.5), 0.5], [0.5, 0.5], [0.5, (- 0.5)]], size: [1, 1],
    ori: 0.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color([(- 1.0), 0.0039, (- 1.0)]),
    fillColor: new util.Color([(- 1.0), 0.0039, (- 1.0)]),
    fillColor: [(- 1.0), 0.0039, (- 1.0)],
    opacity: undefined, depth: 0, interpolate: true,
  });
  
  turtle_wedge_for_size_judgment = new visual.ShapeStim({
    win: psychoJS.window, name: 'turtle_wedge_for_size_judgment', 
    vertices: [[(- 0.5), (- 0.5)], [(- 0.5), 0.5], [0.5, 0.5], [0.5, (- 0.5)]], size: [1, 1],
    ori: 0.0, 
    pos: [0, (- 1)], 
    draggable: false, 
    anchor: 'center',
    lineWidth: 0.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color([1.0, 0.5059, (- 1.0)]),
    fillColor: new util.Color([1.0, 0.5059, (- 1.0)]),
    fillColor: [1.0, 0.5059, (- 1.0)],
    opacity: undefined, depth: -1, interpolate: true,
  });
  
  turtle_boundary_for_size_judgment = new visual.ShapeStim ({
    win: psychoJS.window, name: 'turtle_boundary_for_size_judgment', 
    vertices: [[-[150, 1][0]/2.0, 0], [+[150, 1][0]/2.0, 0]],
    ori: 0.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'bottom-left',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color([1.0, 0.5059, (- 1.0)]),
    fillColor: new util.Color([1.0, 0.5059, (- 1.0)]),
    fillColor: [1.0, 0.5059, (- 1.0)],
    opacity: undefined, depth: -2, interpolate: true,
  });
  
  size_judgment_prompt = new visual.TextStim({
    win: psychoJS.window,
    name: 'size_judgment_prompt',
    text: 'Is this turtle smaller or larger than the average turtle?\n\nF - smaller, J - larger',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 100)], draggable: false, height: 20.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: 1.0,
    depth: -3.0 
  });
  
  key_resp_size_judgment = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "size_jugment_code_check"
  size_jugment_code_checkClock = new util.Clock();
  // Initialize components for Routine "size_judgment_feedback"
  size_judgment_feedbackClock = new util.Clock();
  turtle_half_circle_for_size_judgment_feedback = new visual.ShapeStim({
    win: psychoJS.window, name: 'turtle_half_circle_for_size_judgment_feedback', 
    vertices: [[(- 0.5), (- 0.5)], [(- 0.5), 0.5], [0.5, 0.5], [0.5, (- 0.5)]], size: [1, 1],
    ori: 0.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color([(- 1.0), 0.0039, (- 1.0)]),
    fillColor: new util.Color([(- 1.0), 0.0039, (- 1.0)]),
    fillColor: [(- 1.0), 0.0039, (- 1.0)],
    opacity: undefined, depth: 0, interpolate: true,
  });
  
  turtle_wedge_for_size_judgment_feedback = new visual.ShapeStim({
    win: psychoJS.window, name: 'turtle_wedge_for_size_judgment_feedback', 
    vertices: [[(- 0.5), (- 0.5)], [(- 0.5), 0.5], [0.5, 0.5], [0.5, (- 0.5)]], size: [1, 1],
    ori: 0.0, 
    pos: [0, (- 1)], 
    draggable: false, 
    anchor: 'center',
    lineWidth: 0.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color([1.0, 0.5059, (- 1.0)]),
    fillColor: new util.Color([1.0, 0.5059, (- 1.0)]),
    fillColor: [1.0, 0.5059, (- 1.0)],
    opacity: undefined, depth: -1, interpolate: true,
  });
  
  turtle_boundary_for_size_judgment_feedback = new visual.ShapeStim ({
    win: psychoJS.window, name: 'turtle_boundary_for_size_judgment_feedback', 
    vertices: [[-[150, 1][0]/2.0, 0], [+[150, 1][0]/2.0, 0]],
    ori: 0.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'bottom-left',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color([1.0, 0.5059, (- 1.0)]),
    fillColor: new util.Color([1.0, 0.5059, (- 1.0)]),
    fillColor: [1.0, 0.5059, (- 1.0)],
    opacity: undefined, depth: -2, interpolate: true,
  });
  
  size_feedback_text_display = new visual.TextStim({
    win: psychoJS.window,
    name: 'size_feedback_text_display',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 100)], draggable: false, height: 20.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0 
  });
  
  // Initialize components for Routine "del_corr_size_resp_tmp"
  del_corr_size_resp_tmpClock = new util.Clock();
  // Initialize components for Routine "index"
  indexClock = new util.Clock();
  // Initialize components for Routine "transfer_loop_setup"
  transfer_loop_setupClock = new util.Clock();
  // Initialize components for Routine "transfer_standard_instructions_p1"
  transfer_standard_instructions_p1Clock = new util.Clock();
  transfer_standard_instructions_text_1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'transfer_standard_instructions_text_1',
    text: 'Now you will be asked to categorize some turtles again, using your knowledge of what makes a turtle belong to Species F or Species J. \n\nWe will not be asking you about size right now.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 20.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color((-1.0000, -1.0000, -1.0000)),  opacity: undefined,
    depth: 0.0 
  });
  
  space_7 = new visual.TextStim({
    win: psychoJS.window,
    name: 'space_7',
    text: 'Press space to continue',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 400)], draggable: false, height: 20.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  space_8 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "transfer_standard_instructions_p2"
  transfer_standard_instructions_p2Clock = new util.Clock();
  transfer_standard_instructions_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'transfer_standard_instructions_text',
    text: 'You will not receive feedback after your responses.\n\nHowever, please make sure to respond carefully.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 20.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color((-1.0000, -1.0000, -1.0000)),  opacity: undefined,
    depth: 0.0 
  });
  
  space_9 = new visual.TextStim({
    win: psychoJS.window,
    name: 'space_9',
    text: 'Press space to continue',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 400)], draggable: false, height: 20.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  space_10 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "transfer_standard_instructions_p3"
  transfer_standard_instructions_p3Clock = new util.Clock();
  transfer_standard_instructions_text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'transfer_standard_instructions_text_2',
    text: 'Press space to start the next phase of the experiment.\n',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 20.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color((-1.0000, -1.0000, -1.0000)),  opacity: undefined,
    depth: 0.0 
  });
  
  space_11 = new visual.TextStim({
    win: psychoJS.window,
    name: 'space_11',
    text: 'Press space to continue',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 400)], draggable: false, height: 20.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  space_12 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "transfer_response_standard"
  transfer_response_standardClock = new util.Clock();
  transfer_prompt_standard_trials = new visual.TextStim({
    win: psychoJS.window,
    name: 'transfer_prompt_standard_trials',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 100)], draggable: false, height: 20.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: -1.0 
  });
  
  key_resp_transfer_standard = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  turtle_halfcircle_standard = new visual.ShapeStim({
    win: psychoJS.window, name: 'turtle_halfcircle_standard', 
    vertices: [[(- 0.5), (- 0.5)], [(- 0.5), 0.5], [0.5, 0.5], [0.5, (- 0.5)]], size: [1, 1],
    ori: 0.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color([(- 1.0), 0.0039, (- 1.0)]),
    fillColor: new util.Color([(- 1.0), 0.0039, (- 1.0)]),
    fillColor: [(- 1.0), 0.0039, (- 1.0)],
    opacity: undefined, depth: -3, interpolate: true,
  });
  
  turtle_wedge_standard = new visual.ShapeStim({
    win: psychoJS.window, name: 'turtle_wedge_standard', 
    vertices: [[(- 0.5), (- 0.5)], [(- 0.5), 0.5], [0.5, 0.5], [0.5, (- 0.5)]], size: [1, 1],
    ori: 0.0, 
    pos: [0, (- 1)], 
    draggable: false, 
    anchor: 'center',
    lineWidth: 0.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color([1.0, 0.5059, (- 1.0)]),
    fillColor: new util.Color([1.0, 0.5059, (- 1.0)]),
    fillColor: [1.0, 0.5059, (- 1.0)],
    opacity: undefined, depth: -4, interpolate: true,
  });
  
  turtle_wedge_boundary_standard = new visual.ShapeStim ({
    win: psychoJS.window, name: 'turtle_wedge_boundary_standard', 
    vertices: [[-[150, 1][0]/2.0, 0], [+[150, 1][0]/2.0, 0]],
    ori: 0.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'bottom-left',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color([1.0, 0.5059, (- 1.0)]),
    fillColor: new util.Color([1.0, 0.5059, (- 1.0)]),
    fillColor: [1.0, 0.5059, (- 1.0)],
    opacity: undefined, depth: -5, interpolate: true,
  });
  
  // Initialize components for Routine "transfer_switch_instructions_p1"
  transfer_switch_instructions_p1Clock = new util.Clock();
  transfer_switch_instructions_text_1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'transfer_switch_instructions_text_1',
    text: 'In this next phase, you will be asked to both categorize turtles into species, and to make judgments about their size.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 20.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color((-1.0000, -1.0000, -1.0000)),  opacity: undefined,
    depth: 0.0 
  });
  
  space_13 = new visual.TextStim({
    win: psychoJS.window,
    name: 'space_13',
    text: 'Press space to continue',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 400)], draggable: false, height: 20.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  space_14 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "transfer_switch_instructions_p2"
  transfer_switch_instructions_p2Clock = new util.Clock();
  transfer_switch_instructions_text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'transfer_switch_instructions_text_2',
    text: 'We will usually ask you about the species, but sometimes we will ask you about size.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 20.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color((-1.0000, -1.0000, -1.0000)),  opacity: undefined,
    depth: 0.0 
  });
  
  space_15 = new visual.TextStim({
    win: psychoJS.window,
    name: 'space_15',
    text: 'Press space to continue',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 400)], draggable: false, height: 20.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  space_16 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "transfer_switch_instructions_p3"
  transfer_switch_instructions_p3Clock = new util.Clock();
  transfer_switch_instructions_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'transfer_switch_instructions_text',
    text: 'You will not receive feedback after your responses.\n\nHowever, please make sure to respond carefully.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 20.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color((-1.0000, -1.0000, -1.0000)),  opacity: undefined,
    depth: 0.0 
  });
  
  space_17 = new visual.TextStim({
    win: psychoJS.window,
    name: 'space_17',
    text: 'Press space to continue',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 400)], draggable: false, height: 20.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  space_18 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "transfer_switch_instructions_p4"
  transfer_switch_instructions_p4Clock = new util.Clock();
  transfer_switch_instructions_text_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'transfer_switch_instructions_text_3',
    text: 'Press space to begin the next phase of the experiment.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 20.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color((-1.0000, -1.0000, -1.0000)),  opacity: undefined,
    depth: 0.0 
  });
  
  space_to_begin_switch = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "randomize_switch_trials"
  randomize_switch_trialsClock = new util.Clock();
  // Initialize components for Routine "transfer_response_switch"
  transfer_response_switchClock = new util.Clock();
  turtle_halfcircle_switch = new visual.ShapeStim({
    win: psychoJS.window, name: 'turtle_halfcircle_switch', 
    vertices: [[(- 0.5), (- 0.5)], [(- 0.5), 0.5], [0.5, 0.5], [0.5, (- 0.5)]], size: [1, 1],
    ori: 0.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color([(- 1.0), 0.0039, (- 1.0)]),
    fillColor: new util.Color([(- 1.0), 0.0039, (- 1.0)]),
    fillColor: [(- 1.0), 0.0039, (- 1.0)],
    opacity: undefined, depth: -1, interpolate: true,
  });
  
  turtle_wedge_switch = new visual.ShapeStim({
    win: psychoJS.window, name: 'turtle_wedge_switch', 
    vertices: [[(- 0.5), (- 0.5)], [(- 0.5), 0.5], [0.5, 0.5], [0.5, (- 0.5)]], size: [1, 1],
    ori: 0.0, 
    pos: [0, (- 1)], 
    draggable: false, 
    anchor: 'center',
    lineWidth: 0.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color([1.0, 0.5059, (- 1.0)]),
    fillColor: new util.Color([1.0, 0.5059, (- 1.0)]),
    fillColor: [1.0, 0.5059, (- 1.0)],
    opacity: undefined, depth: -2, interpolate: true,
  });
  
  turtle_wedge_boundary_switch = new visual.ShapeStim ({
    win: psychoJS.window, name: 'turtle_wedge_boundary_switch', 
    vertices: [[-[150, 1][0]/2.0, 0], [+[150, 1][0]/2.0, 0]],
    ori: 0.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'bottom-left',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color([1.0, 0.5059, (- 1.0)]),
    fillColor: new util.Color([1.0, 0.5059, (- 1.0)]),
    fillColor: [1.0, 0.5059, (- 1.0)],
    opacity: undefined, depth: -3, interpolate: true,
  });
  
  transfer_prompt_switch_trials = new visual.TextStim({
    win: psychoJS.window,
    name: 'transfer_prompt_switch_trials',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 100)], draggable: false, height: 20.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -4.0 
  });
  
  key_resp_transfer_switch = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "delete_switch_order"
  delete_switch_orderClock = new util.Clock();
  // Initialize components for Routine "begin_debrief"
  begin_debriefClock = new util.Clock();
  begin_debrief_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'begin_debrief_text',
    text: 'The experiment has now finished. On the next page, you will see a debriefing form explaining the purpose of our study and providing you with more information. After you finish reading this form, press space and the experiment will end. \n\nYou can then tell the researcher, and you are free to go.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 20.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color((-1.0000, -1.0000, -1.0000)),  opacity: undefined,
    depth: 0.0 
  });
  
  space_20 = new visual.TextStim({
    win: psychoJS.window,
    name: 'space_20',
    text: 'Press space to continue',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 400)], draggable: false, height: 20.0,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  space_to_begin_debrief = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "debrief"
  debriefClock = new util.Clock();
  debrief_img = new visual.ImageStim({
    win : psychoJS.window,
    name : 'debrief_img', units : undefined, 
    image : 'debrief.png', mask : undefined,
    anchor : 'bottom-center',
    ori : 0.0, 
    pos : [0, (- 500)], 
    draggable: false,
    size : [800, 1000],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  space_to_end = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}

function exp_setupRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'exp_setup' ---
    t = 0;
    exp_setupClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    exp_setupMaxDurationReached = false;
    // update component parameters for each repeat
    psychoJS.experiment.addData('exp_setup.started', globalClock.getTime());
    exp_setupMaxDuration = null
    // keep track of which components have finished
    exp_setupComponents = [];
    
    for (const thisComponent of exp_setupComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function exp_setupRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'exp_setup' ---
    // get current time
    t = exp_setupClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of exp_setupComponents)
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

function exp_setupRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'exp_setup' ---
    for (const thisComponent of exp_setupComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('exp_setup.stopped', globalClock.getTime());
    // the Routine "exp_setup" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function turtle_param_functionsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'turtle_param_functions' ---
    t = 0;
    turtle_param_functionsClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    turtle_param_functionsMaxDurationReached = false;
    // update component parameters for each repeat
    psychoJS.experiment.addData('turtle_param_functions.started', globalClock.getTime());
    turtle_param_functionsMaxDuration = null
    // keep track of which components have finished
    turtle_param_functionsComponents = [];
    
    for (const thisComponent of turtle_param_functionsComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function turtle_param_functionsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'turtle_param_functions' ---
    // get current time
    t = turtle_param_functionsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of turtle_param_functionsComponents)
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

function turtle_param_functionsRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'turtle_param_functions' ---
    for (const thisComponent of turtle_param_functionsComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('turtle_param_functions.stopped', globalClock.getTime());
    // the Routine "turtle_param_functions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function categorization_instructionsLoopBegin(categorization_instructionsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    categorization_instructions = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 0, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'categorization_instructions'
    });
    psychoJS.experiment.addLoop(categorization_instructions); // add the loop to the experiment
    currentLoop = categorization_instructions;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisCategorization_instruction of categorization_instructions) {
      snapshot = categorization_instructions.getSnapshot();
      categorization_instructionsLoopScheduler.add(importConditions(snapshot));
      categorization_instructionsLoopScheduler.add(categorization_instructions_p1RoutineBegin(snapshot));
      categorization_instructionsLoopScheduler.add(categorization_instructions_p1RoutineEachFrame());
      categorization_instructionsLoopScheduler.add(categorization_instructions_p1RoutineEnd(snapshot));
      categorization_instructionsLoopScheduler.add(categorization_instructions_p2RoutineBegin(snapshot));
      categorization_instructionsLoopScheduler.add(categorization_instructions_p2RoutineEachFrame());
      categorization_instructionsLoopScheduler.add(categorization_instructions_p2RoutineEnd(snapshot));
      categorization_instructionsLoopScheduler.add(categorization_instructions_p3RoutineBegin(snapshot));
      categorization_instructionsLoopScheduler.add(categorization_instructions_p3RoutineEachFrame());
      categorization_instructionsLoopScheduler.add(categorization_instructions_p3RoutineEnd(snapshot));
      categorization_instructionsLoopScheduler.add(categorization_instructions_p4RoutineBegin(snapshot));
      categorization_instructionsLoopScheduler.add(categorization_instructions_p4RoutineEachFrame());
      categorization_instructionsLoopScheduler.add(categorization_instructions_p4RoutineEnd(snapshot));
      categorization_instructionsLoopScheduler.add(categorization_instructions_p5RoutineBegin(snapshot));
      categorization_instructionsLoopScheduler.add(categorization_instructions_p5RoutineEachFrame());
      categorization_instructionsLoopScheduler.add(categorization_instructions_p5RoutineEnd(snapshot));
      categorization_instructionsLoopScheduler.add(categorization_instructions_p6RoutineBegin(snapshot));
      categorization_instructionsLoopScheduler.add(categorization_instructions_p6RoutineEachFrame());
      categorization_instructionsLoopScheduler.add(categorization_instructions_p6RoutineEnd(snapshot));
      categorization_instructionsLoopScheduler.add(categorization_instructions_p7RoutineBegin(snapshot));
      categorization_instructionsLoopScheduler.add(categorization_instructions_p7RoutineEachFrame());
      categorization_instructionsLoopScheduler.add(categorization_instructions_p7RoutineEnd(snapshot));
      categorization_instructionsLoopScheduler.add(categorization_instructions_p8RoutineBegin(snapshot));
      categorization_instructionsLoopScheduler.add(categorization_instructions_p8RoutineEachFrame());
      categorization_instructionsLoopScheduler.add(categorization_instructions_p8RoutineEnd(snapshot));
      categorization_instructionsLoopScheduler.add(categorization_instructionsLoopEndIteration(categorization_instructionsLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}

async function categorization_instructionsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(categorization_instructions);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function categorization_instructionsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      }
    return Scheduler.Event.NEXT;
    }
  };
}

function trainingLoopBegin(trainingLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    training = new TrialHandler({
      psychoJS: psychoJS,
      nReps: num_train_blocks, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'stim/stim_train.csv',
      seed: undefined, name: 'training'
    });
    psychoJS.experiment.addLoop(training); // add the loop to the experiment
    currentLoop = training;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTraining of training) {
      snapshot = training.getSnapshot();
      trainingLoopScheduler.add(importConditions(snapshot));
      trainingLoopScheduler.add(fixation_crossRoutineBegin(snapshot));
      trainingLoopScheduler.add(fixation_crossRoutineEachFrame());
      trainingLoopScheduler.add(fixation_crossRoutineEnd(snapshot));
      trainingLoopScheduler.add(blankRoutineBegin(snapshot));
      trainingLoopScheduler.add(blankRoutineEachFrame());
      trainingLoopScheduler.add(blankRoutineEnd(snapshot));
      trainingLoopScheduler.add(get_turtle_params_trainingRoutineBegin(snapshot));
      trainingLoopScheduler.add(get_turtle_params_trainingRoutineEachFrame());
      trainingLoopScheduler.add(get_turtle_params_trainingRoutineEnd(snapshot));
      trainingLoopScheduler.add(training_responseRoutineBegin(snapshot));
      trainingLoopScheduler.add(training_responseRoutineEachFrame());
      trainingLoopScheduler.add(training_responseRoutineEnd(snapshot));
      trainingLoopScheduler.add(train_feedback_code_checksRoutineBegin(snapshot));
      trainingLoopScheduler.add(train_feedback_code_checksRoutineEachFrame());
      trainingLoopScheduler.add(train_feedback_code_checksRoutineEnd(snapshot));
      trainingLoopScheduler.add(training_feedbackRoutineBegin(snapshot));
      trainingLoopScheduler.add(training_feedbackRoutineEachFrame());
      trainingLoopScheduler.add(training_feedbackRoutineEnd(snapshot));
      trainingLoopScheduler.add(blankRoutineBegin(snapshot));
      trainingLoopScheduler.add(blankRoutineEachFrame());
      trainingLoopScheduler.add(blankRoutineEnd(snapshot));
      trainingLoopScheduler.add(del_corr_respRoutineBegin(snapshot));
      trainingLoopScheduler.add(del_corr_respRoutineEachFrame());
      trainingLoopScheduler.add(del_corr_respRoutineEnd(snapshot));
      trainingLoopScheduler.add(trainingLoopEndIteration(trainingLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}

async function trainingLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(training);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function trainingLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}

function size_jugment_instructions_loopLoopBegin(size_jugment_instructions_loopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    size_jugment_instructions_loop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'size_jugment_instructions_loop'
    });
    psychoJS.experiment.addLoop(size_jugment_instructions_loop); // add the loop to the experiment
    currentLoop = size_jugment_instructions_loop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisSize_jugment_instructions_loop of size_jugment_instructions_loop) {
      snapshot = size_jugment_instructions_loop.getSnapshot();
      size_jugment_instructions_loopLoopScheduler.add(importConditions(snapshot));
      size_jugment_instructions_loopLoopScheduler.add(avg_turtle_setupRoutineBegin(snapshot));
      size_jugment_instructions_loopLoopScheduler.add(avg_turtle_setupRoutineEachFrame());
      size_jugment_instructions_loopLoopScheduler.add(avg_turtle_setupRoutineEnd(snapshot));
      size_jugment_instructions_loopLoopScheduler.add(size_judgment_instructions_p1RoutineBegin(snapshot));
      size_jugment_instructions_loopLoopScheduler.add(size_judgment_instructions_p1RoutineEachFrame());
      size_jugment_instructions_loopLoopScheduler.add(size_judgment_instructions_p1RoutineEnd(snapshot));
      size_jugment_instructions_loopLoopScheduler.add(size_judgment_instructions_p2RoutineBegin(snapshot));
      size_jugment_instructions_loopLoopScheduler.add(size_judgment_instructions_p2RoutineEachFrame());
      size_jugment_instructions_loopLoopScheduler.add(size_judgment_instructions_p2RoutineEnd(snapshot));
      size_jugment_instructions_loopLoopScheduler.add(size_judgment_instructions_p3RoutineBegin(snapshot));
      size_jugment_instructions_loopLoopScheduler.add(size_judgment_instructions_p3RoutineEachFrame());
      size_jugment_instructions_loopLoopScheduler.add(size_judgment_instructions_p3RoutineEnd(snapshot));
      size_jugment_instructions_loopLoopScheduler.add(size_judgment_instructions_p4RoutineBegin(snapshot));
      size_jugment_instructions_loopLoopScheduler.add(size_judgment_instructions_p4RoutineEachFrame());
      size_jugment_instructions_loopLoopScheduler.add(size_judgment_instructions_p4RoutineEnd(snapshot));
      size_jugment_instructions_loopLoopScheduler.add(size_jugment_instructions_p5RoutineBegin(snapshot));
      size_jugment_instructions_loopLoopScheduler.add(size_jugment_instructions_p5RoutineEachFrame());
      size_jugment_instructions_loopLoopScheduler.add(size_jugment_instructions_p5RoutineEnd(snapshot));
      size_jugment_instructions_loopLoopScheduler.add(size_judgment_instructions_p6RoutineBegin(snapshot));
      size_jugment_instructions_loopLoopScheduler.add(size_judgment_instructions_p6RoutineEachFrame());
      size_jugment_instructions_loopLoopScheduler.add(size_judgment_instructions_p6RoutineEnd(snapshot));
      size_jugment_instructions_loopLoopScheduler.add(size_jugment_instructions_loopLoopEndIteration(size_jugment_instructions_loopLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}

async function size_jugment_instructions_loopLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(size_jugment_instructions_loop);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function size_jugment_instructions_loopLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      }
    return Scheduler.Event.NEXT;
    }
  };
}

function size_judgment_trialsLoopBegin(size_judgment_trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    size_judgment_trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: num_size_blocks, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'stim/stim_train_with_areas.csv',
      seed: undefined, name: 'size_judgment_trials'
    });
    psychoJS.experiment.addLoop(size_judgment_trials); // add the loop to the experiment
    currentLoop = size_judgment_trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisSize_judgment_trial of size_judgment_trials) {
      snapshot = size_judgment_trials.getSnapshot();
      size_judgment_trialsLoopScheduler.add(importConditions(snapshot));
      size_judgment_trialsLoopScheduler.add(fixation_crossRoutineBegin(snapshot));
      size_judgment_trialsLoopScheduler.add(fixation_crossRoutineEachFrame());
      size_judgment_trialsLoopScheduler.add(fixation_crossRoutineEnd(snapshot));
      size_judgment_trialsLoopScheduler.add(blankRoutineBegin(snapshot));
      size_judgment_trialsLoopScheduler.add(blankRoutineEachFrame());
      size_judgment_trialsLoopScheduler.add(blankRoutineEnd(snapshot));
      size_judgment_trialsLoopScheduler.add(size_judgment_paramsRoutineBegin(snapshot));
      size_judgment_trialsLoopScheduler.add(size_judgment_paramsRoutineEachFrame());
      size_judgment_trialsLoopScheduler.add(size_judgment_paramsRoutineEnd(snapshot));
      size_judgment_trialsLoopScheduler.add(size_judgment_responseRoutineBegin(snapshot));
      size_judgment_trialsLoopScheduler.add(size_judgment_responseRoutineEachFrame());
      size_judgment_trialsLoopScheduler.add(size_judgment_responseRoutineEnd(snapshot));
      size_judgment_trialsLoopScheduler.add(size_jugment_code_checkRoutineBegin(snapshot));
      size_judgment_trialsLoopScheduler.add(size_jugment_code_checkRoutineEachFrame());
      size_judgment_trialsLoopScheduler.add(size_jugment_code_checkRoutineEnd(snapshot));
      size_judgment_trialsLoopScheduler.add(size_judgment_feedbackRoutineBegin(snapshot));
      size_judgment_trialsLoopScheduler.add(size_judgment_feedbackRoutineEachFrame());
      size_judgment_trialsLoopScheduler.add(size_judgment_feedbackRoutineEnd(snapshot));
      size_judgment_trialsLoopScheduler.add(blankRoutineBegin(snapshot));
      size_judgment_trialsLoopScheduler.add(blankRoutineEachFrame());
      size_judgment_trialsLoopScheduler.add(blankRoutineEnd(snapshot));
      size_judgment_trialsLoopScheduler.add(del_corr_size_resp_tmpRoutineBegin(snapshot));
      size_judgment_trialsLoopScheduler.add(del_corr_size_resp_tmpRoutineEachFrame());
      size_judgment_trialsLoopScheduler.add(del_corr_size_resp_tmpRoutineEnd(snapshot));
      size_judgment_trialsLoopScheduler.add(size_judgment_trialsLoopEndIteration(size_judgment_trialsLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}

async function size_judgment_trialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(size_judgment_trials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function size_judgment_trialsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}

function transfer_trialsLoopBegin(transfer_trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    transfer_trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 2, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'transfer_trials'
    });
    psychoJS.experiment.addLoop(transfer_trials); // add the loop to the experiment
    currentLoop = transfer_trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTransfer_trial of transfer_trials) {
      snapshot = transfer_trials.getSnapshot();
      transfer_trialsLoopScheduler.add(importConditions(snapshot));
      transfer_trialsLoopScheduler.add(transfer_loop_setupRoutineBegin(snapshot));
      transfer_trialsLoopScheduler.add(transfer_loop_setupRoutineEachFrame());
      transfer_trialsLoopScheduler.add(transfer_loop_setupRoutineEnd(snapshot));
      const transfer_standard_instructions_loopLoopScheduler = new Scheduler(psychoJS);
      transfer_trialsLoopScheduler.add(transfer_standard_instructions_loopLoopBegin(transfer_standard_instructions_loopLoopScheduler, snapshot));
      transfer_trialsLoopScheduler.add(transfer_standard_instructions_loopLoopScheduler);
      transfer_trialsLoopScheduler.add(transfer_standard_instructions_loopLoopEnd);
      const transfer_standardLoopScheduler = new Scheduler(psychoJS);
      transfer_trialsLoopScheduler.add(transfer_standardLoopBegin(transfer_standardLoopScheduler, snapshot));
      transfer_trialsLoopScheduler.add(transfer_standardLoopScheduler);
      transfer_trialsLoopScheduler.add(transfer_standardLoopEnd);
      const transfer_switch_instructions_loopLoopScheduler = new Scheduler(psychoJS);
      transfer_trialsLoopScheduler.add(transfer_switch_instructions_loopLoopBegin(transfer_switch_instructions_loopLoopScheduler, snapshot));
      transfer_trialsLoopScheduler.add(transfer_switch_instructions_loopLoopScheduler);
      transfer_trialsLoopScheduler.add(transfer_switch_instructions_loopLoopEnd);
      const transfer_switch_loopLoopScheduler = new Scheduler(psychoJS);
      transfer_trialsLoopScheduler.add(transfer_switch_loopLoopBegin(transfer_switch_loopLoopScheduler, snapshot));
      transfer_trialsLoopScheduler.add(transfer_switch_loopLoopScheduler);
      transfer_trialsLoopScheduler.add(transfer_switch_loopLoopEnd);
      transfer_trialsLoopScheduler.add(transfer_trialsLoopEndIteration(transfer_trialsLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}

function transfer_standard_instructions_loopLoopBegin(transfer_standard_instructions_loopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    transfer_standard_instructions_loop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: do_standard_instructions, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'transfer_standard_instructions_loop'
    });
    psychoJS.experiment.addLoop(transfer_standard_instructions_loop); // add the loop to the experiment
    currentLoop = transfer_standard_instructions_loop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTransfer_standard_instructions_loop of transfer_standard_instructions_loop) {
      snapshot = transfer_standard_instructions_loop.getSnapshot();
      transfer_standard_instructions_loopLoopScheduler.add(importConditions(snapshot));
      transfer_standard_instructions_loopLoopScheduler.add(transfer_standard_instructions_p1RoutineBegin(snapshot));
      transfer_standard_instructions_loopLoopScheduler.add(transfer_standard_instructions_p1RoutineEachFrame());
      transfer_standard_instructions_loopLoopScheduler.add(transfer_standard_instructions_p1RoutineEnd(snapshot));
      transfer_standard_instructions_loopLoopScheduler.add(transfer_standard_instructions_p2RoutineBegin(snapshot));
      transfer_standard_instructions_loopLoopScheduler.add(transfer_standard_instructions_p2RoutineEachFrame());
      transfer_standard_instructions_loopLoopScheduler.add(transfer_standard_instructions_p2RoutineEnd(snapshot));
      transfer_standard_instructions_loopLoopScheduler.add(transfer_standard_instructions_p3RoutineBegin(snapshot));
      transfer_standard_instructions_loopLoopScheduler.add(transfer_standard_instructions_p3RoutineEachFrame());
      transfer_standard_instructions_loopLoopScheduler.add(transfer_standard_instructions_p3RoutineEnd(snapshot));
      transfer_standard_instructions_loopLoopScheduler.add(transfer_standard_instructions_loopLoopEndIteration(transfer_standard_instructions_loopLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}

async function transfer_standard_instructions_loopLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(transfer_standard_instructions_loop);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function transfer_standard_instructions_loopLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      }
    return Scheduler.Event.NEXT;
    }
  };
}

function transfer_standardLoopBegin(transfer_standardLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    transfer_standard = new TrialHandler({
      psychoJS: psychoJS,
      nReps: num_repeats_1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'stim/stim_transfer_standard.csv',
      seed: undefined, name: 'transfer_standard'
    });
    psychoJS.experiment.addLoop(transfer_standard); // add the loop to the experiment
    currentLoop = transfer_standard;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTransfer_standard of transfer_standard) {
      snapshot = transfer_standard.getSnapshot();
      transfer_standardLoopScheduler.add(importConditions(snapshot));
      transfer_standardLoopScheduler.add(fixation_crossRoutineBegin(snapshot));
      transfer_standardLoopScheduler.add(fixation_crossRoutineEachFrame());
      transfer_standardLoopScheduler.add(fixation_crossRoutineEnd(snapshot));
      transfer_standardLoopScheduler.add(blankRoutineBegin(snapshot));
      transfer_standardLoopScheduler.add(blankRoutineEachFrame());
      transfer_standardLoopScheduler.add(blankRoutineEnd(snapshot));
      transfer_standardLoopScheduler.add(transfer_response_standardRoutineBegin(snapshot));
      transfer_standardLoopScheduler.add(transfer_response_standardRoutineEachFrame());
      transfer_standardLoopScheduler.add(transfer_response_standardRoutineEnd(snapshot));
      transfer_standardLoopScheduler.add(blankRoutineBegin(snapshot));
      transfer_standardLoopScheduler.add(blankRoutineEachFrame());
      transfer_standardLoopScheduler.add(blankRoutineEnd(snapshot));
      transfer_standardLoopScheduler.add(transfer_standardLoopEndIteration(transfer_standardLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}

async function transfer_standardLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(transfer_standard);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function transfer_standardLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}

function transfer_switch_instructions_loopLoopBegin(transfer_switch_instructions_loopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    transfer_switch_instructions_loop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: do_switch_instructions, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'transfer_switch_instructions_loop'
    });
    psychoJS.experiment.addLoop(transfer_switch_instructions_loop); // add the loop to the experiment
    currentLoop = transfer_switch_instructions_loop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTransfer_switch_instructions_loop of transfer_switch_instructions_loop) {
      snapshot = transfer_switch_instructions_loop.getSnapshot();
      transfer_switch_instructions_loopLoopScheduler.add(importConditions(snapshot));
      transfer_switch_instructions_loopLoopScheduler.add(transfer_switch_instructions_p1RoutineBegin(snapshot));
      transfer_switch_instructions_loopLoopScheduler.add(transfer_switch_instructions_p1RoutineEachFrame());
      transfer_switch_instructions_loopLoopScheduler.add(transfer_switch_instructions_p1RoutineEnd(snapshot));
      transfer_switch_instructions_loopLoopScheduler.add(transfer_switch_instructions_p2RoutineBegin(snapshot));
      transfer_switch_instructions_loopLoopScheduler.add(transfer_switch_instructions_p2RoutineEachFrame());
      transfer_switch_instructions_loopLoopScheduler.add(transfer_switch_instructions_p2RoutineEnd(snapshot));
      transfer_switch_instructions_loopLoopScheduler.add(transfer_switch_instructions_p3RoutineBegin(snapshot));
      transfer_switch_instructions_loopLoopScheduler.add(transfer_switch_instructions_p3RoutineEachFrame());
      transfer_switch_instructions_loopLoopScheduler.add(transfer_switch_instructions_p3RoutineEnd(snapshot));
      transfer_switch_instructions_loopLoopScheduler.add(transfer_switch_instructions_p4RoutineBegin(snapshot));
      transfer_switch_instructions_loopLoopScheduler.add(transfer_switch_instructions_p4RoutineEachFrame());
      transfer_switch_instructions_loopLoopScheduler.add(transfer_switch_instructions_p4RoutineEnd(snapshot));
      transfer_switch_instructions_loopLoopScheduler.add(blankRoutineBegin(snapshot));
      transfer_switch_instructions_loopLoopScheduler.add(blankRoutineEachFrame());
      transfer_switch_instructions_loopLoopScheduler.add(blankRoutineEnd(snapshot));
      transfer_switch_instructions_loopLoopScheduler.add(transfer_switch_instructions_loopLoopEndIteration(transfer_switch_instructions_loopLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}

async function transfer_switch_instructions_loopLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(transfer_switch_instructions_loop);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function transfer_switch_instructions_loopLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      }
    return Scheduler.Event.NEXT;
    }
  };
}

function transfer_switch_loopLoopBegin(transfer_switch_loopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    transfer_switch_loop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: num_repeats_2, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'transfer_switch_loop'
    });
    psychoJS.experiment.addLoop(transfer_switch_loop); // add the loop to the experiment
    currentLoop = transfer_switch_loop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTransfer_switch_loop of transfer_switch_loop) {
      snapshot = transfer_switch_loop.getSnapshot();
      transfer_switch_loopLoopScheduler.add(importConditions(snapshot));
      transfer_switch_loopLoopScheduler.add(randomize_switch_trialsRoutineBegin(snapshot));
      transfer_switch_loopLoopScheduler.add(randomize_switch_trialsRoutineEachFrame());
      transfer_switch_loopLoopScheduler.add(randomize_switch_trialsRoutineEnd(snapshot));
      const transfer_switchLoopScheduler = new Scheduler(psychoJS);
      transfer_switch_loopLoopScheduler.add(transfer_switchLoopBegin(transfer_switchLoopScheduler, snapshot));
      transfer_switch_loopLoopScheduler.add(transfer_switchLoopScheduler);
      transfer_switch_loopLoopScheduler.add(transfer_switchLoopEnd);
      transfer_switch_loopLoopScheduler.add(delete_switch_orderRoutineBegin(snapshot));
      transfer_switch_loopLoopScheduler.add(delete_switch_orderRoutineEachFrame());
      transfer_switch_loopLoopScheduler.add(delete_switch_orderRoutineEnd(snapshot));
      transfer_switch_loopLoopScheduler.add(transfer_switch_loopLoopEndIteration(transfer_switch_loopLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}

function transfer_switchLoopBegin(transfer_switchLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    transfer_switch = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'stim/stim_transfer_switch_random_tmp.csv',
      seed: undefined, name: 'transfer_switch'
    });
    psychoJS.experiment.addLoop(transfer_switch); // add the loop to the experiment
    currentLoop = transfer_switch;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTransfer_switch of transfer_switch) {
      snapshot = transfer_switch.getSnapshot();
      transfer_switchLoopScheduler.add(importConditions(snapshot));
      transfer_switchLoopScheduler.add(fixation_crossRoutineBegin(snapshot));
      transfer_switchLoopScheduler.add(fixation_crossRoutineEachFrame());
      transfer_switchLoopScheduler.add(fixation_crossRoutineEnd(snapshot));
      transfer_switchLoopScheduler.add(blankRoutineBegin(snapshot));
      transfer_switchLoopScheduler.add(blankRoutineEachFrame());
      transfer_switchLoopScheduler.add(blankRoutineEnd(snapshot));
      transfer_switchLoopScheduler.add(transfer_response_switchRoutineBegin(snapshot));
      transfer_switchLoopScheduler.add(transfer_response_switchRoutineEachFrame());
      transfer_switchLoopScheduler.add(transfer_response_switchRoutineEnd(snapshot));
      transfer_switchLoopScheduler.add(blankRoutineBegin(snapshot));
      transfer_switchLoopScheduler.add(blankRoutineEachFrame());
      transfer_switchLoopScheduler.add(blankRoutineEnd(snapshot));
      transfer_switchLoopScheduler.add(transfer_switchLoopEndIteration(transfer_switchLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}

async function transfer_switchLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(transfer_switch);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function transfer_switchLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}

async function transfer_switch_loopLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(transfer_switch_loop);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function transfer_switch_loopLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}

async function transfer_trialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(transfer_trials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function transfer_trialsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}

function categorization_instructions_p1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'categorization_instructions_p1' ---
    t = 0;
    categorization_instructions_p1Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    categorization_instructions_p1MaxDurationReached = false;
    // update component parameters for each repeat
    key_resp_7.keys = undefined;
    key_resp_7.rt = undefined;
    _key_resp_7_allKeys = [];
    psychoJS.experiment.addData('categorization_instructions_p1.started', globalClock.getTime());
    categorization_instructions_p1MaxDuration = null
    // keep track of which components have finished
    categorization_instructions_p1Components = [];
    categorization_instructions_p1Components.push(categorization_instructions_text_1);
    categorization_instructions_p1Components.push(key_resp_7);
    
    for (const thisComponent of categorization_instructions_p1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function categorization_instructions_p1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'categorization_instructions_p1' ---
    // get current time
    t = categorization_instructions_p1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *categorization_instructions_text_1* updates
    if (t >= 0.0 && categorization_instructions_text_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      categorization_instructions_text_1.tStart = t;  // (not accounting for frame time here)
      categorization_instructions_text_1.frameNStart = frameN;  // exact frame index
      
      categorization_instructions_text_1.setAutoDraw(true);
    }
    
    
    // *key_resp_7* updates
    if (t >= 0.5 && key_resp_7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_7.tStart = t;  // (not accounting for frame time here)
      key_resp_7.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_7.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_7.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_7.clearEvents(); });
    }
    
    if (key_resp_7.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_7.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_7_allKeys = _key_resp_7_allKeys.concat(theseKeys);
      if (_key_resp_7_allKeys.length > 0) {
        key_resp_7.keys = _key_resp_7_allKeys[_key_resp_7_allKeys.length - 1].name;  // just the last key pressed
        key_resp_7.rt = _key_resp_7_allKeys[_key_resp_7_allKeys.length - 1].rt;
        key_resp_7.duration = _key_resp_7_allKeys[_key_resp_7_allKeys.length - 1].duration;
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
    for (const thisComponent of categorization_instructions_p1Components)
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

function categorization_instructions_p1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'categorization_instructions_p1' ---
    for (const thisComponent of categorization_instructions_p1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('categorization_instructions_p1.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_7.corr, level);
    }
    psychoJS.experiment.addData('key_resp_7.keys', key_resp_7.keys);
    if (typeof key_resp_7.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_7.rt', key_resp_7.rt);
        psychoJS.experiment.addData('key_resp_7.duration', key_resp_7.duration);
        routineTimer.reset();
        }
    
    key_resp_7.stop();
    // the Routine "categorization_instructions_p1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function categorization_instructions_p2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'categorization_instructions_p2' ---
    t = 0;
    categorization_instructions_p2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    categorization_instructions_p2MaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from turtle_setup_for_categorization_instructions
    example_turtle_radius = 113;
    example_turtle_angle = 25;
    example_turtle_halfcircle_vertices = get_turtle_halfcircle_vertices(example_turtle_radius);
    example_turtle_wedge_vertices = get_turtle_wedge_vertices(example_turtle_angle);
    
    turtle_halfcircle_for_categorization_instructions.setVertices(example_turtle_halfcircle_vertices);
    turtle_wedge_for_categorization_instructions.setVertices(example_turtle_wedge_vertices);
    key_resp_8.keys = undefined;
    key_resp_8.rt = undefined;
    _key_resp_8_allKeys = [];
    psychoJS.experiment.addData('categorization_instructions_p2.started', globalClock.getTime());
    categorization_instructions_p2MaxDuration = null
    // keep track of which components have finished
    categorization_instructions_p2Components = [];
    categorization_instructions_p2Components.push(categorization_instructions_text_2);
    categorization_instructions_p2Components.push(turtle_halfcircle_for_categorization_instructions);
    categorization_instructions_p2Components.push(turtle_wedge_for_categorization_instructions);
    categorization_instructions_p2Components.push(turtle_wedge_boundary_for_categorization_instructions);
    categorization_instructions_p2Components.push(space);
    categorization_instructions_p2Components.push(key_resp_8);
    
    for (const thisComponent of categorization_instructions_p2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function categorization_instructions_p2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'categorization_instructions_p2' ---
    // get current time
    t = categorization_instructions_p2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *categorization_instructions_text_2* updates
    if (t >= 0.0 && categorization_instructions_text_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      categorization_instructions_text_2.tStart = t;  // (not accounting for frame time here)
      categorization_instructions_text_2.frameNStart = frameN;  // exact frame index
      
      categorization_instructions_text_2.setAutoDraw(true);
    }
    
    
    // *turtle_halfcircle_for_categorization_instructions* updates
    if (t >= 0.0 && turtle_halfcircle_for_categorization_instructions.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      turtle_halfcircle_for_categorization_instructions.tStart = t;  // (not accounting for frame time here)
      turtle_halfcircle_for_categorization_instructions.frameNStart = frameN;  // exact frame index
      
      turtle_halfcircle_for_categorization_instructions.setAutoDraw(true);
    }
    
    
    // *turtle_wedge_for_categorization_instructions* updates
    if (t >= 0.0 && turtle_wedge_for_categorization_instructions.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      turtle_wedge_for_categorization_instructions.tStart = t;  // (not accounting for frame time here)
      turtle_wedge_for_categorization_instructions.frameNStart = frameN;  // exact frame index
      
      turtle_wedge_for_categorization_instructions.setAutoDraw(true);
    }
    
    
    // *turtle_wedge_boundary_for_categorization_instructions* updates
    if (t >= 0.0 && turtle_wedge_boundary_for_categorization_instructions.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      turtle_wedge_boundary_for_categorization_instructions.tStart = t;  // (not accounting for frame time here)
      turtle_wedge_boundary_for_categorization_instructions.frameNStart = frameN;  // exact frame index
      
      turtle_wedge_boundary_for_categorization_instructions.setAutoDraw(true);
    }
    
    
    // *space* updates
    if (t >= 2 && space.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      space.tStart = t;  // (not accounting for frame time here)
      space.frameNStart = frameN;  // exact frame index
      
      space.setAutoDraw(true);
    }
    
    
    // *key_resp_8* updates
    if (t >= 2 && key_resp_8.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_8.tStart = t;  // (not accounting for frame time here)
      key_resp_8.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_8.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_8.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_8.clearEvents(); });
    }
    
    if (key_resp_8.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_8.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_8_allKeys = _key_resp_8_allKeys.concat(theseKeys);
      if (_key_resp_8_allKeys.length > 0) {
        key_resp_8.keys = _key_resp_8_allKeys[_key_resp_8_allKeys.length - 1].name;  // just the last key pressed
        key_resp_8.rt = _key_resp_8_allKeys[_key_resp_8_allKeys.length - 1].rt;
        key_resp_8.duration = _key_resp_8_allKeys[_key_resp_8_allKeys.length - 1].duration;
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
    for (const thisComponent of categorization_instructions_p2Components)
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

function categorization_instructions_p2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'categorization_instructions_p2' ---
    for (const thisComponent of categorization_instructions_p2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('categorization_instructions_p2.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_8.corr, level);
    }
    psychoJS.experiment.addData('key_resp_8.keys', key_resp_8.keys);
    if (typeof key_resp_8.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_8.rt', key_resp_8.rt);
        psychoJS.experiment.addData('key_resp_8.duration', key_resp_8.duration);
        routineTimer.reset();
        }
    
    key_resp_8.stop();
    // the Routine "categorization_instructions_p2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function categorization_instructions_p3RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'categorization_instructions_p3' ---
    t = 0;
    categorization_instructions_p3Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    categorization_instructions_p3MaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from turtle_setup_for_categorization_instructions_2
    example_turtle_radius = 40;
    example_turtle_angle = 30;
    example_turtle_halfcircle_vertices = get_turtle_halfcircle_vertices(example_turtle_radius);
    example_turtle_wedge_vertices = get_turtle_wedge_vertices(example_turtle_angle);
    
    turtle_halfcircle_for_categorization_instructions_2.setVertices(example_turtle_halfcircle_vertices);
    key_resp_9.keys = undefined;
    key_resp_9.rt = undefined;
    _key_resp_9_allKeys = [];
    turtle_wedge_for_categorization_instructions_2.setVertices(example_turtle_wedge_vertices);
    psychoJS.experiment.addData('categorization_instructions_p3.started', globalClock.getTime());
    categorization_instructions_p3MaxDuration = null
    // keep track of which components have finished
    categorization_instructions_p3Components = [];
    categorization_instructions_p3Components.push(categorization_instructions_text_3);
    categorization_instructions_p3Components.push(turtle_halfcircle_for_categorization_instructions_2);
    categorization_instructions_p3Components.push(space_2);
    categorization_instructions_p3Components.push(key_resp_9);
    categorization_instructions_p3Components.push(turtle_wedge_for_categorization_instructions_2);
    categorization_instructions_p3Components.push(turtle_wedge_boundary_for_categorization_instructions_2);
    
    for (const thisComponent of categorization_instructions_p3Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function categorization_instructions_p3RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'categorization_instructions_p3' ---
    // get current time
    t = categorization_instructions_p3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *categorization_instructions_text_3* updates
    if (t >= 0.0 && categorization_instructions_text_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      categorization_instructions_text_3.tStart = t;  // (not accounting for frame time here)
      categorization_instructions_text_3.frameNStart = frameN;  // exact frame index
      
      categorization_instructions_text_3.setAutoDraw(true);
    }
    
    
    // *turtle_halfcircle_for_categorization_instructions_2* updates
    if (t >= 0.0 && turtle_halfcircle_for_categorization_instructions_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      turtle_halfcircle_for_categorization_instructions_2.tStart = t;  // (not accounting for frame time here)
      turtle_halfcircle_for_categorization_instructions_2.frameNStart = frameN;  // exact frame index
      
      turtle_halfcircle_for_categorization_instructions_2.setAutoDraw(true);
    }
    
    
    // *space_2* updates
    if (t >= 2 && space_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      space_2.tStart = t;  // (not accounting for frame time here)
      space_2.frameNStart = frameN;  // exact frame index
      
      space_2.setAutoDraw(true);
    }
    
    
    // *key_resp_9* updates
    if (t >= 2 && key_resp_9.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_9.tStart = t;  // (not accounting for frame time here)
      key_resp_9.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_9.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_9.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_9.clearEvents(); });
    }
    
    if (key_resp_9.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_9.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_9_allKeys = _key_resp_9_allKeys.concat(theseKeys);
      if (_key_resp_9_allKeys.length > 0) {
        key_resp_9.keys = _key_resp_9_allKeys[_key_resp_9_allKeys.length - 1].name;  // just the last key pressed
        key_resp_9.rt = _key_resp_9_allKeys[_key_resp_9_allKeys.length - 1].rt;
        key_resp_9.duration = _key_resp_9_allKeys[_key_resp_9_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *turtle_wedge_for_categorization_instructions_2* updates
    if (t >= 0.0 && turtle_wedge_for_categorization_instructions_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      turtle_wedge_for_categorization_instructions_2.tStart = t;  // (not accounting for frame time here)
      turtle_wedge_for_categorization_instructions_2.frameNStart = frameN;  // exact frame index
      
      turtle_wedge_for_categorization_instructions_2.setAutoDraw(true);
    }
    
    
    // *turtle_wedge_boundary_for_categorization_instructions_2* updates
    if (t >= 0.0 && turtle_wedge_boundary_for_categorization_instructions_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      turtle_wedge_boundary_for_categorization_instructions_2.tStart = t;  // (not accounting for frame time here)
      turtle_wedge_boundary_for_categorization_instructions_2.frameNStart = frameN;  // exact frame index
      
      turtle_wedge_boundary_for_categorization_instructions_2.setAutoDraw(true);
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
    for (const thisComponent of categorization_instructions_p3Components)
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

function categorization_instructions_p3RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'categorization_instructions_p3' ---
    for (const thisComponent of categorization_instructions_p3Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('categorization_instructions_p3.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_9.corr, level);
    }
    psychoJS.experiment.addData('key_resp_9.keys', key_resp_9.keys);
    if (typeof key_resp_9.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_9.rt', key_resp_9.rt);
        psychoJS.experiment.addData('key_resp_9.duration', key_resp_9.duration);
        routineTimer.reset();
        }
    
    key_resp_9.stop();
    // the Routine "categorization_instructions_p3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function categorization_instructions_p4RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'categorization_instructions_p4' ---
    t = 0;
    categorization_instructions_p4Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    categorization_instructions_p4MaxDurationReached = false;
    // update component parameters for each repeat
    turtle_halfcircle_for_categorization_instructions_3.setVertices(example_turtle_halfcircle_vertices);
    turtle_wedge_for_categorization_instructions_3.setVertices(example_turtle_wedge_vertices);
    key_resp_10.keys = undefined;
    key_resp_10.rt = undefined;
    _key_resp_10_allKeys = [];
    psychoJS.experiment.addData('categorization_instructions_p4.started', globalClock.getTime());
    categorization_instructions_p4MaxDuration = null
    // keep track of which components have finished
    categorization_instructions_p4Components = [];
    categorization_instructions_p4Components.push(categorization_instructions_text);
    categorization_instructions_p4Components.push(turtle_halfcircle_for_categorization_instructions_3);
    categorization_instructions_p4Components.push(turtle_wedge_for_categorization_instructions_3);
    categorization_instructions_p4Components.push(space_3);
    categorization_instructions_p4Components.push(turtle_wedge_boundary_for_categorization_instructions_3);
    categorization_instructions_p4Components.push(key_resp_10);
    
    for (const thisComponent of categorization_instructions_p4Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function categorization_instructions_p4RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'categorization_instructions_p4' ---
    // get current time
    t = categorization_instructions_p4Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *categorization_instructions_text* updates
    if (t >= 0.0 && categorization_instructions_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      categorization_instructions_text.tStart = t;  // (not accounting for frame time here)
      categorization_instructions_text.frameNStart = frameN;  // exact frame index
      
      categorization_instructions_text.setAutoDraw(true);
    }
    
    
    // *turtle_halfcircle_for_categorization_instructions_3* updates
    if (t >= 0.0 && turtle_halfcircle_for_categorization_instructions_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      turtle_halfcircle_for_categorization_instructions_3.tStart = t;  // (not accounting for frame time here)
      turtle_halfcircle_for_categorization_instructions_3.frameNStart = frameN;  // exact frame index
      
      turtle_halfcircle_for_categorization_instructions_3.setAutoDraw(true);
    }
    
    
    // *turtle_wedge_for_categorization_instructions_3* updates
    if (t >= 0.0 && turtle_wedge_for_categorization_instructions_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      turtle_wedge_for_categorization_instructions_3.tStart = t;  // (not accounting for frame time here)
      turtle_wedge_for_categorization_instructions_3.frameNStart = frameN;  // exact frame index
      
      turtle_wedge_for_categorization_instructions_3.setAutoDraw(true);
    }
    
    
    // *space_3* updates
    if (t >= 2 && space_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      space_3.tStart = t;  // (not accounting for frame time here)
      space_3.frameNStart = frameN;  // exact frame index
      
      space_3.setAutoDraw(true);
    }
    
    
    // *turtle_wedge_boundary_for_categorization_instructions_3* updates
    if (t >= 0.0 && turtle_wedge_boundary_for_categorization_instructions_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      turtle_wedge_boundary_for_categorization_instructions_3.tStart = t;  // (not accounting for frame time here)
      turtle_wedge_boundary_for_categorization_instructions_3.frameNStart = frameN;  // exact frame index
      
      turtle_wedge_boundary_for_categorization_instructions_3.setAutoDraw(true);
    }
    
    
    // *key_resp_10* updates
    if (t >= 2 && key_resp_10.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_10.tStart = t;  // (not accounting for frame time here)
      key_resp_10.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_10.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_10.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_10.clearEvents(); });
    }
    
    if (key_resp_10.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_10.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_10_allKeys = _key_resp_10_allKeys.concat(theseKeys);
      if (_key_resp_10_allKeys.length > 0) {
        key_resp_10.keys = _key_resp_10_allKeys[_key_resp_10_allKeys.length - 1].name;  // just the last key pressed
        key_resp_10.rt = _key_resp_10_allKeys[_key_resp_10_allKeys.length - 1].rt;
        key_resp_10.duration = _key_resp_10_allKeys[_key_resp_10_allKeys.length - 1].duration;
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
    for (const thisComponent of categorization_instructions_p4Components)
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

function categorization_instructions_p4RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'categorization_instructions_p4' ---
    for (const thisComponent of categorization_instructions_p4Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('categorization_instructions_p4.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_10.corr, level);
    }
    psychoJS.experiment.addData('key_resp_10.keys', key_resp_10.keys);
    if (typeof key_resp_10.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_10.rt', key_resp_10.rt);
        psychoJS.experiment.addData('key_resp_10.duration', key_resp_10.duration);
        routineTimer.reset();
        }
    
    key_resp_10.stop();
    // the Routine "categorization_instructions_p4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function categorization_instructions_p5RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'categorization_instructions_p5' ---
    t = 0;
    categorization_instructions_p5Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    categorization_instructions_p5MaxDurationReached = false;
    // update component parameters for each repeat
    turtle_halfcircle_for_categorization_instructions_4.setVertices(example_turtle_halfcircle_vertices);
    turtle_wedge_for_categorization_instructions_4.setVertices(example_turtle_wedge_vertices);
    key_resp_11.keys = undefined;
    key_resp_11.rt = undefined;
    _key_resp_11_allKeys = [];
    psychoJS.experiment.addData('categorization_instructions_p5.started', globalClock.getTime());
    categorization_instructions_p5MaxDuration = null
    // keep track of which components have finished
    categorization_instructions_p5Components = [];
    categorization_instructions_p5Components.push(categorization_instructions_text_4);
    categorization_instructions_p5Components.push(turtle_halfcircle_for_categorization_instructions_4);
    categorization_instructions_p5Components.push(turtle_wedge_for_categorization_instructions_4);
    categorization_instructions_p5Components.push(space_4);
    categorization_instructions_p5Components.push(turtle_wedge_boundary_for_categorization_instructions_4);
    categorization_instructions_p5Components.push(key_resp_11);
    
    for (const thisComponent of categorization_instructions_p5Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function categorization_instructions_p5RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'categorization_instructions_p5' ---
    // get current time
    t = categorization_instructions_p5Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *categorization_instructions_text_4* updates
    if (t >= 0.0 && categorization_instructions_text_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      categorization_instructions_text_4.tStart = t;  // (not accounting for frame time here)
      categorization_instructions_text_4.frameNStart = frameN;  // exact frame index
      
      categorization_instructions_text_4.setAutoDraw(true);
    }
    
    
    // *turtle_halfcircle_for_categorization_instructions_4* updates
    if (t >= 0.0 && turtle_halfcircle_for_categorization_instructions_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      turtle_halfcircle_for_categorization_instructions_4.tStart = t;  // (not accounting for frame time here)
      turtle_halfcircle_for_categorization_instructions_4.frameNStart = frameN;  // exact frame index
      
      turtle_halfcircle_for_categorization_instructions_4.setAutoDraw(true);
    }
    
    
    // *turtle_wedge_for_categorization_instructions_4* updates
    if (t >= 0.0 && turtle_wedge_for_categorization_instructions_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      turtle_wedge_for_categorization_instructions_4.tStart = t;  // (not accounting for frame time here)
      turtle_wedge_for_categorization_instructions_4.frameNStart = frameN;  // exact frame index
      
      turtle_wedge_for_categorization_instructions_4.setAutoDraw(true);
    }
    
    
    // *space_4* updates
    if (t >= 2 && space_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      space_4.tStart = t;  // (not accounting for frame time here)
      space_4.frameNStart = frameN;  // exact frame index
      
      space_4.setAutoDraw(true);
    }
    
    
    // *turtle_wedge_boundary_for_categorization_instructions_4* updates
    if (t >= 0.0 && turtle_wedge_boundary_for_categorization_instructions_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      turtle_wedge_boundary_for_categorization_instructions_4.tStart = t;  // (not accounting for frame time here)
      turtle_wedge_boundary_for_categorization_instructions_4.frameNStart = frameN;  // exact frame index
      
      turtle_wedge_boundary_for_categorization_instructions_4.setAutoDraw(true);
    }
    
    
    // *key_resp_11* updates
    if (t >= 2 && key_resp_11.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_11.tStart = t;  // (not accounting for frame time here)
      key_resp_11.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_11.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_11.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_11.clearEvents(); });
    }
    
    if (key_resp_11.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_11.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_11_allKeys = _key_resp_11_allKeys.concat(theseKeys);
      if (_key_resp_11_allKeys.length > 0) {
        key_resp_11.keys = _key_resp_11_allKeys[_key_resp_11_allKeys.length - 1].name;  // just the last key pressed
        key_resp_11.rt = _key_resp_11_allKeys[_key_resp_11_allKeys.length - 1].rt;
        key_resp_11.duration = _key_resp_11_allKeys[_key_resp_11_allKeys.length - 1].duration;
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
    for (const thisComponent of categorization_instructions_p5Components)
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

function categorization_instructions_p5RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'categorization_instructions_p5' ---
    for (const thisComponent of categorization_instructions_p5Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('categorization_instructions_p5.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_11.corr, level);
    }
    psychoJS.experiment.addData('key_resp_11.keys', key_resp_11.keys);
    if (typeof key_resp_11.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_11.rt', key_resp_11.rt);
        psychoJS.experiment.addData('key_resp_11.duration', key_resp_11.duration);
        routineTimer.reset();
        }
    
    key_resp_11.stop();
    // the Routine "categorization_instructions_p5" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function categorization_instructions_p6RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'categorization_instructions_p6' ---
    t = 0;
    categorization_instructions_p6Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    categorization_instructions_p6MaxDurationReached = false;
    // update component parameters for each repeat
    turtle_halfcircle_for_categorization_instructions_5.setVertices(example_turtle_halfcircle_vertices);
    turtle_wedge_for_categorization_instructions_5.setVertices(example_turtle_wedge_vertices);
    key_resp_12.keys = undefined;
    key_resp_12.rt = undefined;
    _key_resp_12_allKeys = [];
    psychoJS.experiment.addData('categorization_instructions_p6.started', globalClock.getTime());
    categorization_instructions_p6MaxDuration = null
    // keep track of which components have finished
    categorization_instructions_p6Components = [];
    categorization_instructions_p6Components.push(categorization_instructions_text_5);
    categorization_instructions_p6Components.push(turtle_halfcircle_for_categorization_instructions_5);
    categorization_instructions_p6Components.push(turtle_wedge_for_categorization_instructions_5);
    categorization_instructions_p6Components.push(turtle_wedge_boundary_for_categorization_instructions_5);
    categorization_instructions_p6Components.push(space_5);
    categorization_instructions_p6Components.push(key_resp_12);
    
    for (const thisComponent of categorization_instructions_p6Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function categorization_instructions_p6RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'categorization_instructions_p6' ---
    // get current time
    t = categorization_instructions_p6Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *categorization_instructions_text_5* updates
    if (t >= 0.0 && categorization_instructions_text_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      categorization_instructions_text_5.tStart = t;  // (not accounting for frame time here)
      categorization_instructions_text_5.frameNStart = frameN;  // exact frame index
      
      categorization_instructions_text_5.setAutoDraw(true);
    }
    
    
    // *turtle_halfcircle_for_categorization_instructions_5* updates
    if (t >= 0.0 && turtle_halfcircle_for_categorization_instructions_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      turtle_halfcircle_for_categorization_instructions_5.tStart = t;  // (not accounting for frame time here)
      turtle_halfcircle_for_categorization_instructions_5.frameNStart = frameN;  // exact frame index
      
      turtle_halfcircle_for_categorization_instructions_5.setAutoDraw(true);
    }
    
    
    // *turtle_wedge_for_categorization_instructions_5* updates
    if (t >= 0.0 && turtle_wedge_for_categorization_instructions_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      turtle_wedge_for_categorization_instructions_5.tStart = t;  // (not accounting for frame time here)
      turtle_wedge_for_categorization_instructions_5.frameNStart = frameN;  // exact frame index
      
      turtle_wedge_for_categorization_instructions_5.setAutoDraw(true);
    }
    
    
    // *turtle_wedge_boundary_for_categorization_instructions_5* updates
    if (t >= 0.0 && turtle_wedge_boundary_for_categorization_instructions_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      turtle_wedge_boundary_for_categorization_instructions_5.tStart = t;  // (not accounting for frame time here)
      turtle_wedge_boundary_for_categorization_instructions_5.frameNStart = frameN;  // exact frame index
      
      turtle_wedge_boundary_for_categorization_instructions_5.setAutoDraw(true);
    }
    
    
    // *space_5* updates
    if (t >= 2 && space_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      space_5.tStart = t;  // (not accounting for frame time here)
      space_5.frameNStart = frameN;  // exact frame index
      
      space_5.setAutoDraw(true);
    }
    
    
    // *key_resp_12* updates
    if (t >= 2 && key_resp_12.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_12.tStart = t;  // (not accounting for frame time here)
      key_resp_12.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_12.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_12.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_12.clearEvents(); });
    }
    
    if (key_resp_12.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_12.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_12_allKeys = _key_resp_12_allKeys.concat(theseKeys);
      if (_key_resp_12_allKeys.length > 0) {
        key_resp_12.keys = _key_resp_12_allKeys[_key_resp_12_allKeys.length - 1].name;  // just the last key pressed
        key_resp_12.rt = _key_resp_12_allKeys[_key_resp_12_allKeys.length - 1].rt;
        key_resp_12.duration = _key_resp_12_allKeys[_key_resp_12_allKeys.length - 1].duration;
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
    for (const thisComponent of categorization_instructions_p6Components)
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

function categorization_instructions_p6RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'categorization_instructions_p6' ---
    for (const thisComponent of categorization_instructions_p6Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('categorization_instructions_p6.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_12.corr, level);
    }
    psychoJS.experiment.addData('key_resp_12.keys', key_resp_12.keys);
    if (typeof key_resp_12.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_12.rt', key_resp_12.rt);
        psychoJS.experiment.addData('key_resp_12.duration', key_resp_12.duration);
        routineTimer.reset();
        }
    
    key_resp_12.stop();
    // the Routine "categorization_instructions_p6" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function categorization_instructions_p7RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'categorization_instructions_p7' ---
    t = 0;
    categorization_instructions_p7Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    categorization_instructions_p7MaxDurationReached = false;
    // update component parameters for each repeat
    turtle_halfcircle_for_categorization_instructions_6.setVertices(example_turtle_halfcircle_vertices);
    turtle_wedge_for_categorization_instructions_6.setVertices(example_turtle_wedge_vertices);
    key_resp_13.keys = undefined;
    key_resp_13.rt = undefined;
    _key_resp_13_allKeys = [];
    psychoJS.experiment.addData('categorization_instructions_p7.started', globalClock.getTime());
    categorization_instructions_p7MaxDuration = null
    // keep track of which components have finished
    categorization_instructions_p7Components = [];
    categorization_instructions_p7Components.push(categorization_instructions_text_6);
    categorization_instructions_p7Components.push(turtle_halfcircle_for_categorization_instructions_6);
    categorization_instructions_p7Components.push(turtle_wedge_for_categorization_instructions_6);
    categorization_instructions_p7Components.push(turtle_wedge_boundary_for_categorization_instructions_6);
    categorization_instructions_p7Components.push(space_6);
    categorization_instructions_p7Components.push(key_resp_13);
    
    for (const thisComponent of categorization_instructions_p7Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function categorization_instructions_p7RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'categorization_instructions_p7' ---
    // get current time
    t = categorization_instructions_p7Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *categorization_instructions_text_6* updates
    if (t >= 0.0 && categorization_instructions_text_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      categorization_instructions_text_6.tStart = t;  // (not accounting for frame time here)
      categorization_instructions_text_6.frameNStart = frameN;  // exact frame index
      
      categorization_instructions_text_6.setAutoDraw(true);
    }
    
    
    // *turtle_halfcircle_for_categorization_instructions_6* updates
    if (t >= 0.0 && turtle_halfcircle_for_categorization_instructions_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      turtle_halfcircle_for_categorization_instructions_6.tStart = t;  // (not accounting for frame time here)
      turtle_halfcircle_for_categorization_instructions_6.frameNStart = frameN;  // exact frame index
      
      turtle_halfcircle_for_categorization_instructions_6.setAutoDraw(true);
    }
    
    
    // *turtle_wedge_for_categorization_instructions_6* updates
    if (t >= 0.0 && turtle_wedge_for_categorization_instructions_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      turtle_wedge_for_categorization_instructions_6.tStart = t;  // (not accounting for frame time here)
      turtle_wedge_for_categorization_instructions_6.frameNStart = frameN;  // exact frame index
      
      turtle_wedge_for_categorization_instructions_6.setAutoDraw(true);
    }
    
    
    // *turtle_wedge_boundary_for_categorization_instructions_6* updates
    if (t >= 0.0 && turtle_wedge_boundary_for_categorization_instructions_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      turtle_wedge_boundary_for_categorization_instructions_6.tStart = t;  // (not accounting for frame time here)
      turtle_wedge_boundary_for_categorization_instructions_6.frameNStart = frameN;  // exact frame index
      
      turtle_wedge_boundary_for_categorization_instructions_6.setAutoDraw(true);
    }
    
    
    // *space_6* updates
    if (t >= 2 && space_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      space_6.tStart = t;  // (not accounting for frame time here)
      space_6.frameNStart = frameN;  // exact frame index
      
      space_6.setAutoDraw(true);
    }
    
    
    // *key_resp_13* updates
    if (t >= 2 && key_resp_13.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_13.tStart = t;  // (not accounting for frame time here)
      key_resp_13.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_13.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_13.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_13.clearEvents(); });
    }
    
    if (key_resp_13.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_13.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_13_allKeys = _key_resp_13_allKeys.concat(theseKeys);
      if (_key_resp_13_allKeys.length > 0) {
        key_resp_13.keys = _key_resp_13_allKeys[_key_resp_13_allKeys.length - 1].name;  // just the last key pressed
        key_resp_13.rt = _key_resp_13_allKeys[_key_resp_13_allKeys.length - 1].rt;
        key_resp_13.duration = _key_resp_13_allKeys[_key_resp_13_allKeys.length - 1].duration;
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
    for (const thisComponent of categorization_instructions_p7Components)
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

function categorization_instructions_p7RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'categorization_instructions_p7' ---
    for (const thisComponent of categorization_instructions_p7Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('categorization_instructions_p7.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_13.corr, level);
    }
    psychoJS.experiment.addData('key_resp_13.keys', key_resp_13.keys);
    if (typeof key_resp_13.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_13.rt', key_resp_13.rt);
        psychoJS.experiment.addData('key_resp_13.duration', key_resp_13.duration);
        routineTimer.reset();
        }
    
    key_resp_13.stop();
    // the Routine "categorization_instructions_p7" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function categorization_instructions_p8RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'categorization_instructions_p8' ---
    t = 0;
    categorization_instructions_p8Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    categorization_instructions_p8MaxDurationReached = false;
    // update component parameters for each repeat
    key_resp_14.keys = undefined;
    key_resp_14.rt = undefined;
    _key_resp_14_allKeys = [];
    psychoJS.experiment.addData('categorization_instructions_p8.started', globalClock.getTime());
    categorization_instructions_p8MaxDuration = null
    // keep track of which components have finished
    categorization_instructions_p8Components = [];
    categorization_instructions_p8Components.push(space_to_begin_exp);
    categorization_instructions_p8Components.push(key_resp_14);
    
    for (const thisComponent of categorization_instructions_p8Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function categorization_instructions_p8RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'categorization_instructions_p8' ---
    // get current time
    t = categorization_instructions_p8Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *space_to_begin_exp* updates
    if (t >= 0.0 && space_to_begin_exp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      space_to_begin_exp.tStart = t;  // (not accounting for frame time here)
      space_to_begin_exp.frameNStart = frameN;  // exact frame index
      
      space_to_begin_exp.setAutoDraw(true);
    }
    
    
    // *key_resp_14* updates
    if (t >= 0.0 && key_resp_14.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_14.tStart = t;  // (not accounting for frame time here)
      key_resp_14.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_14.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_14.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_14.clearEvents(); });
    }
    
    if (key_resp_14.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_14.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_14_allKeys = _key_resp_14_allKeys.concat(theseKeys);
      if (_key_resp_14_allKeys.length > 0) {
        key_resp_14.keys = _key_resp_14_allKeys[_key_resp_14_allKeys.length - 1].name;  // just the last key pressed
        key_resp_14.rt = _key_resp_14_allKeys[_key_resp_14_allKeys.length - 1].rt;
        key_resp_14.duration = _key_resp_14_allKeys[_key_resp_14_allKeys.length - 1].duration;
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
    for (const thisComponent of categorization_instructions_p8Components)
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

function categorization_instructions_p8RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'categorization_instructions_p8' ---
    for (const thisComponent of categorization_instructions_p8Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('categorization_instructions_p8.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_14.corr, level);
    }
    psychoJS.experiment.addData('key_resp_14.keys', key_resp_14.keys);
    if (typeof key_resp_14.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_14.rt', key_resp_14.rt);
        psychoJS.experiment.addData('key_resp_14.duration', key_resp_14.duration);
        routineTimer.reset();
        }
    
    key_resp_14.stop();
    // the Routine "categorization_instructions_p8" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function fixation_crossRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'fixation_cross' ---
    t = 0;
    fixation_crossClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(0.400000);
    fixation_crossMaxDurationReached = false;
    // update component parameters for each repeat
    psychoJS.experiment.addData('fixation_cross.started', globalClock.getTime());
    fixation_crossMaxDuration = null
    // keep track of which components have finished
    fixation_crossComponents = [];
    fixation_crossComponents.push(fixation_cross_1);
    
    for (const thisComponent of fixation_crossComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function fixation_crossRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'fixation_cross' ---
    // get current time
    t = fixation_crossClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fixation_cross_1* updates
    if (t >= 0.0 && fixation_cross_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fixation_cross_1.tStart = t;  // (not accounting for frame time here)
      fixation_cross_1.frameNStart = frameN;  // exact frame index
      
      fixation_cross_1.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 0.4 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (fixation_cross_1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fixation_cross_1.setAutoDraw(false);
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
    for (const thisComponent of fixation_crossComponents)
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

function fixation_crossRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'fixation_cross' ---
    for (const thisComponent of fixation_crossComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('fixation_cross.stopped', globalClock.getTime());
    if (fixation_crossMaxDurationReached) {
        routineTimer.add(fixation_crossMaxDuration);
    } else {
        routineTimer.add(-0.400000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function blankRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'blank' ---
    t = 0;
    blankClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(0.200000);
    blankMaxDurationReached = false;
    // update component parameters for each repeat
    psychoJS.experiment.addData('blank.started', globalClock.getTime());
    blankMaxDuration = null
    // keep track of which components have finished
    blankComponents = [];
    blankComponents.push(text_2);
    
    for (const thisComponent of blankComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function blankRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'blank' ---
    // get current time
    t = blankClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_2* updates
    if (t >= 0.0 && text_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_2.tStart = t;  // (not accounting for frame time here)
      text_2.frameNStart = frameN;  // exact frame index
      
      text_2.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 0.2 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (text_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_2.setAutoDraw(false);
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
    for (const thisComponent of blankComponents)
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

function blankRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'blank' ---
    for (const thisComponent of blankComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('blank.stopped', globalClock.getTime());
    if (blankMaxDurationReached) {
        routineTimer.add(blankMaxDuration);
    } else {
        routineTimer.add(-0.200000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function get_turtle_params_trainingRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'get_turtle_params_training' ---
    t = 0;
    get_turtle_params_trainingClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    get_turtle_params_trainingMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from get_turtle_params
    turtle_halfcircle_vertices = get_turtle_halfcircle_vertices(radius);
    turtle_wedge_vertices = get_turtle_wedge_vertices(angle);
    if ((category === "A")) {
        corr_resp_tmp = category_A_label;
    } else {
        if ((category === "B")) {
            corr_resp_tmp = category_B_label;
        }
    }
    
    psychoJS.experiment.addData('get_turtle_params_training.started', globalClock.getTime());
    get_turtle_params_trainingMaxDuration = null
    // keep track of which components have finished
    get_turtle_params_trainingComponents = [];
    
    for (const thisComponent of get_turtle_params_trainingComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function get_turtle_params_trainingRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'get_turtle_params_training' ---
    // get current time
    t = get_turtle_params_trainingClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of get_turtle_params_trainingComponents)
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

function get_turtle_params_trainingRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'get_turtle_params_training' ---
    for (const thisComponent of get_turtle_params_trainingComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('get_turtle_params_training.stopped', globalClock.getTime());
    // the Routine "get_turtle_params_training" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function training_responseRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'training_response' ---
    t = 0;
    training_responseClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    training_responseMaxDurationReached = false;
    // update component parameters for each repeat
    key_resp_training.keys = undefined;
    key_resp_training.rt = undefined;
    _key_resp_training_allKeys = [];
    turtle_halfcircle.setVertices(turtle_halfcircle_vertices);
    turtle_wedge.setVertices(turtle_wedge_vertices);
    training_prompt.setText('Is this turtle in Species F or Species J? \n\nF - Species F, J - Species J');
    psychoJS.experiment.addData('training_response.started', globalClock.getTime());
    training_responseMaxDuration = null
    // keep track of which components have finished
    training_responseComponents = [];
    training_responseComponents.push(key_resp_training);
    training_responseComponents.push(turtle_halfcircle);
    training_responseComponents.push(turtle_wedge);
    training_responseComponents.push(turtle_wedge_boundary);
    training_responseComponents.push(training_prompt);
    
    for (const thisComponent of training_responseComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function training_responseRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'training_response' ---
    // get current time
    t = training_responseClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *key_resp_training* updates
    if (t >= 0.0 && key_resp_training.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_training.tStart = t;  // (not accounting for frame time here)
      key_resp_training.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_training.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_training.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_training.clearEvents(); });
    }
    
    if (key_resp_training.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_training.getKeys({keyList: ['f', 'j'], waitRelease: false});
      _key_resp_training_allKeys = _key_resp_training_allKeys.concat(theseKeys);
      if (_key_resp_training_allKeys.length > 0) {
        key_resp_training.keys = _key_resp_training_allKeys[_key_resp_training_allKeys.length - 1].name;  // just the last key pressed
        key_resp_training.rt = _key_resp_training_allKeys[_key_resp_training_allKeys.length - 1].rt;
        key_resp_training.duration = _key_resp_training_allKeys[_key_resp_training_allKeys.length - 1].duration;
        // was this correct?
        if (key_resp_training.keys == corr_resp_tmp) {
            key_resp_training.corr = 1;
        } else {
            key_resp_training.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *turtle_halfcircle* updates
    if (t >= 0.0 && turtle_halfcircle.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      turtle_halfcircle.tStart = t;  // (not accounting for frame time here)
      turtle_halfcircle.frameNStart = frameN;  // exact frame index
      
      turtle_halfcircle.setAutoDraw(true);
    }
    
    
    // *turtle_wedge* updates
    if (t >= 0.0 && turtle_wedge.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      turtle_wedge.tStart = t;  // (not accounting for frame time here)
      turtle_wedge.frameNStart = frameN;  // exact frame index
      
      turtle_wedge.setAutoDraw(true);
    }
    
    
    // *turtle_wedge_boundary* updates
    if (t >= 0.0 && turtle_wedge_boundary.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      turtle_wedge_boundary.tStart = t;  // (not accounting for frame time here)
      turtle_wedge_boundary.frameNStart = frameN;  // exact frame index
      
      turtle_wedge_boundary.setAutoDraw(true);
    }
    
    
    // *training_prompt* updates
    if (t >= 0.0 && training_prompt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      training_prompt.tStart = t;  // (not accounting for frame time here)
      training_prompt.frameNStart = frameN;  // exact frame index
      
      training_prompt.setAutoDraw(true);
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
    for (const thisComponent of training_responseComponents)
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

function training_responseRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'training_response' ---
    for (const thisComponent of training_responseComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('training_response.stopped', globalClock.getTime());
    // was no response the correct answer?!
    if (key_resp_training.keys === undefined) {
      if (['None','none',undefined].includes(corr_resp_tmp)) {
         key_resp_training.corr = 1;  // correct non-response
      } else {
         key_resp_training.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_training.corr, level);
    }
    psychoJS.experiment.addData('key_resp_training.keys', key_resp_training.keys);
    psychoJS.experiment.addData('key_resp_training.corr', key_resp_training.corr);
    if (typeof key_resp_training.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_training.rt', key_resp_training.rt);
        psychoJS.experiment.addData('key_resp_training.duration', key_resp_training.duration);
        routineTimer.reset();
        }
    
    key_resp_training.stop();
    // the Routine "training_response" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function train_feedback_code_checksRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'train_feedback_code_checks' ---
    t = 0;
    train_feedback_code_checksClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    train_feedback_code_checksMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from train_feedback_text_code_2
    if ((key_resp_training.corr === 1)) {
        train_feedback_dur = 1;
        train_feedback_col = "#008000";
        if ((category === "A")) {
            train_feedback_text = (("You were correct! This turtle belongs to species " + category_A_label.toUpperCase()) + ".");
        } else {
            if ((category === "B")) {
                train_feedback_text = (("You were correct! This turtle belongs to species " + category_B_label.toUpperCase()) + ".");
            }
        }
    } else {
        if ((key_resp_training.corr === 0)) {
            train_feedback_dur = 2;
            train_feedback_col = "#FF0000";
            if ((category === "A")) {
                train_feedback_text = (("You were incorrect. This turtle belongs to species " + category_A_label.toUpperCase()) + ".");
            } else {
                if ((category === "B")) {
                    train_feedback_text = (("You were incorrect. This turtle belongs to species " + category_B_label.toUpperCase()) + ".");
                }
            }
        }
    }
    
    psychoJS.experiment.addData('train_feedback_code_checks.started', globalClock.getTime());
    train_feedback_code_checksMaxDuration = null
    // keep track of which components have finished
    train_feedback_code_checksComponents = [];
    
    for (const thisComponent of train_feedback_code_checksComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function train_feedback_code_checksRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'train_feedback_code_checks' ---
    // get current time
    t = train_feedback_code_checksClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of train_feedback_code_checksComponents)
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

function train_feedback_code_checksRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'train_feedback_code_checks' ---
    for (const thisComponent of train_feedback_code_checksComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('train_feedback_code_checks.stopped', globalClock.getTime());
    // the Routine "train_feedback_code_checks" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function training_feedbackRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'training_feedback' ---
    t = 0;
    training_feedbackClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    training_feedbackMaxDurationReached = false;
    // update component parameters for each repeat
    train_feedback_text_display.setColor(new util.Color(train_feedback_col));
    train_feedback_text_display.setText(train_feedback_text);
    turtle_halfcircle_for_feedback.setVertices(turtle_halfcircle_vertices);
    turtle_wedge_for_feedback.setVertices(turtle_wedge_vertices);
    psychoJS.experiment.addData('training_feedback.started', globalClock.getTime());
    training_feedbackMaxDuration = null
    // keep track of which components have finished
    training_feedbackComponents = [];
    training_feedbackComponents.push(train_feedback_text_display);
    training_feedbackComponents.push(turtle_halfcircle_for_feedback);
    training_feedbackComponents.push(turtle_wedge_for_feedback);
    training_feedbackComponents.push(turtle_wedge_boundary_for_feedback);
    
    for (const thisComponent of training_feedbackComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function training_feedbackRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'training_feedback' ---
    // get current time
    t = training_feedbackClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *train_feedback_text_display* updates
    if (t >= 0.0 && train_feedback_text_display.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      train_feedback_text_display.tStart = t;  // (not accounting for frame time here)
      train_feedback_text_display.frameNStart = frameN;  // exact frame index
      
      train_feedback_text_display.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + train_feedback_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (train_feedback_text_display.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      train_feedback_text_display.setAutoDraw(false);
    }
    
    
    // *turtle_halfcircle_for_feedback* updates
    if (t >= 0.0 && turtle_halfcircle_for_feedback.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      turtle_halfcircle_for_feedback.tStart = t;  // (not accounting for frame time here)
      turtle_halfcircle_for_feedback.frameNStart = frameN;  // exact frame index
      
      turtle_halfcircle_for_feedback.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + train_feedback_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (turtle_halfcircle_for_feedback.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      turtle_halfcircle_for_feedback.setAutoDraw(false);
    }
    
    
    // *turtle_wedge_for_feedback* updates
    if (t >= 0.0 && turtle_wedge_for_feedback.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      turtle_wedge_for_feedback.tStart = t;  // (not accounting for frame time here)
      turtle_wedge_for_feedback.frameNStart = frameN;  // exact frame index
      
      turtle_wedge_for_feedback.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + train_feedback_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (turtle_wedge_for_feedback.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      turtle_wedge_for_feedback.setAutoDraw(false);
    }
    
    
    // *turtle_wedge_boundary_for_feedback* updates
    if (t >= 0.0 && turtle_wedge_boundary_for_feedback.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      turtle_wedge_boundary_for_feedback.tStart = t;  // (not accounting for frame time here)
      turtle_wedge_boundary_for_feedback.frameNStart = frameN;  // exact frame index
      
      turtle_wedge_boundary_for_feedback.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + train_feedback_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (turtle_wedge_boundary_for_feedback.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      turtle_wedge_boundary_for_feedback.setAutoDraw(false);
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
    for (const thisComponent of training_feedbackComponents)
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

function training_feedbackRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'training_feedback' ---
    for (const thisComponent of training_feedbackComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('training_feedback.stopped', globalClock.getTime());
    // the Routine "training_feedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function del_corr_respRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'del_corr_resp' ---
    t = 0;
    del_corr_respClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    del_corr_respMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from delete_corr_resp_tmp_code
    delete corr_resp_tmp;
    
    psychoJS.experiment.addData('del_corr_resp.started', globalClock.getTime());
    del_corr_respMaxDuration = null
    // keep track of which components have finished
    del_corr_respComponents = [];
    
    for (const thisComponent of del_corr_respComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function del_corr_respRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'del_corr_resp' ---
    // get current time
    t = del_corr_respClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of del_corr_respComponents)
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

function del_corr_respRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'del_corr_resp' ---
    for (const thisComponent of del_corr_respComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('del_corr_resp.stopped', globalClock.getTime());
    // the Routine "del_corr_resp" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function avg_turtle_setupRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'avg_turtle_setup' ---
    t = 0;
    avg_turtle_setupClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    avg_turtle_setupMaxDurationReached = false;
    // update component parameters for each repeat
    psychoJS.experiment.addData('avg_turtle_setup.started', globalClock.getTime());
    avg_turtle_setupMaxDuration = null
    // keep track of which components have finished
    avg_turtle_setupComponents = [];
    
    for (const thisComponent of avg_turtle_setupComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function avg_turtle_setupRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'avg_turtle_setup' ---
    // get current time
    t = avg_turtle_setupClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of avg_turtle_setupComponents)
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

function avg_turtle_setupRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'avg_turtle_setup' ---
    for (const thisComponent of avg_turtle_setupComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('avg_turtle_setup.stopped', globalClock.getTime());
    // the Routine "avg_turtle_setup" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function size_judgment_instructions_p1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'size_judgment_instructions_p1' ---
    t = 0;
    size_judgment_instructions_p1Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    size_judgment_instructions_p1MaxDurationReached = false;
    // update component parameters for each repeat
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    psychoJS.experiment.addData('size_judgment_instructions_p1.started', globalClock.getTime());
    size_judgment_instructions_p1MaxDuration = null
    // keep track of which components have finished
    size_judgment_instructions_p1Components = [];
    size_judgment_instructions_p1Components.push(avg_turtle_instr_1);
    size_judgment_instructions_p1Components.push(key_resp);
    
    for (const thisComponent of size_judgment_instructions_p1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function size_judgment_instructions_p1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'size_judgment_instructions_p1' ---
    // get current time
    t = size_judgment_instructions_p1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *avg_turtle_instr_1* updates
    if (t >= 0.0 && avg_turtle_instr_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      avg_turtle_instr_1.tStart = t;  // (not accounting for frame time here)
      avg_turtle_instr_1.frameNStart = frameN;  // exact frame index
      
      avg_turtle_instr_1.setAutoDraw(true);
    }
    
    
    // *key_resp* updates
    if (t >= 1 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp.tStart = t;  // (not accounting for frame time here)
      key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
    }
    
    if (key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys[_key_resp_allKeys.length - 1].name;  // just the last key pressed
        key_resp.rt = _key_resp_allKeys[_key_resp_allKeys.length - 1].rt;
        key_resp.duration = _key_resp_allKeys[_key_resp_allKeys.length - 1].duration;
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
    for (const thisComponent of size_judgment_instructions_p1Components)
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

function size_judgment_instructions_p1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'size_judgment_instructions_p1' ---
    for (const thisComponent of size_judgment_instructions_p1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('size_judgment_instructions_p1.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp.corr, level);
    }
    psychoJS.experiment.addData('key_resp.keys', key_resp.keys);
    if (typeof key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp.rt', key_resp.rt);
        psychoJS.experiment.addData('key_resp.duration', key_resp.duration);
        routineTimer.reset();
        }
    
    key_resp.stop();
    // the Routine "size_judgment_instructions_p1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function size_judgment_instructions_p2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'size_judgment_instructions_p2' ---
    t = 0;
    size_judgment_instructions_p2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    size_judgment_instructions_p2MaxDurationReached = false;
    // update component parameters for each repeat
    key_resp_2.keys = undefined;
    key_resp_2.rt = undefined;
    _key_resp_2_allKeys = [];
    psychoJS.experiment.addData('size_judgment_instructions_p2.started', globalClock.getTime());
    size_judgment_instructions_p2MaxDuration = null
    // keep track of which components have finished
    size_judgment_instructions_p2Components = [];
    size_judgment_instructions_p2Components.push(avg_turtle_instr_2);
    size_judgment_instructions_p2Components.push(key_resp_2);
    
    for (const thisComponent of size_judgment_instructions_p2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function size_judgment_instructions_p2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'size_judgment_instructions_p2' ---
    // get current time
    t = size_judgment_instructions_p2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *avg_turtle_instr_2* updates
    if (t >= 0.0 && avg_turtle_instr_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      avg_turtle_instr_2.tStart = t;  // (not accounting for frame time here)
      avg_turtle_instr_2.frameNStart = frameN;  // exact frame index
      
      avg_turtle_instr_2.setAutoDraw(true);
    }
    
    
    // *key_resp_2* updates
    if (t >= 2 && key_resp_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_2.tStart = t;  // (not accounting for frame time here)
      key_resp_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.clearEvents(); });
    }
    
    if (key_resp_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_2.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_2_allKeys = _key_resp_2_allKeys.concat(theseKeys);
      if (_key_resp_2_allKeys.length > 0) {
        key_resp_2.keys = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].name;  // just the last key pressed
        key_resp_2.rt = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].rt;
        key_resp_2.duration = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].duration;
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
    for (const thisComponent of size_judgment_instructions_p2Components)
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

function size_judgment_instructions_p2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'size_judgment_instructions_p2' ---
    for (const thisComponent of size_judgment_instructions_p2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('size_judgment_instructions_p2.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_2.corr, level);
    }
    psychoJS.experiment.addData('key_resp_2.keys', key_resp_2.keys);
    if (typeof key_resp_2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_2.rt', key_resp_2.rt);
        psychoJS.experiment.addData('key_resp_2.duration', key_resp_2.duration);
        routineTimer.reset();
        }
    
    key_resp_2.stop();
    // the Routine "size_judgment_instructions_p2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function size_judgment_instructions_p3RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'size_judgment_instructions_p3' ---
    t = 0;
    size_judgment_instructions_p3Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    size_judgment_instructions_p3MaxDurationReached = false;
    // update component parameters for each repeat
    turtle_halfcircle_for_size_instructions.setVertices(avg_turtle_halfcircle_vertices);
    turtle_wedge_for_size_instructions.setVertices(avg_turtle_wedge_vertices);
    key_resp_3.keys = undefined;
    key_resp_3.rt = undefined;
    _key_resp_3_allKeys = [];
    psychoJS.experiment.addData('size_judgment_instructions_p3.started', globalClock.getTime());
    size_judgment_instructions_p3MaxDuration = null
    // keep track of which components have finished
    size_judgment_instructions_p3Components = [];
    size_judgment_instructions_p3Components.push(turtle_halfcircle_for_size_instructions);
    size_judgment_instructions_p3Components.push(turtle_wedge_for_size_instructions);
    size_judgment_instructions_p3Components.push(turtle_wedge_boundary_for_instructions);
    size_judgment_instructions_p3Components.push(avg_turtle_instr_3);
    size_judgment_instructions_p3Components.push(key_resp_3);
    
    for (const thisComponent of size_judgment_instructions_p3Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function size_judgment_instructions_p3RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'size_judgment_instructions_p3' ---
    // get current time
    t = size_judgment_instructions_p3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *turtle_halfcircle_for_size_instructions* updates
    if (t >= 0.0 && turtle_halfcircle_for_size_instructions.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      turtle_halfcircle_for_size_instructions.tStart = t;  // (not accounting for frame time here)
      turtle_halfcircle_for_size_instructions.frameNStart = frameN;  // exact frame index
      
      turtle_halfcircle_for_size_instructions.setAutoDraw(true);
    }
    
    
    // *turtle_wedge_for_size_instructions* updates
    if (t >= 0.0 && turtle_wedge_for_size_instructions.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      turtle_wedge_for_size_instructions.tStart = t;  // (not accounting for frame time here)
      turtle_wedge_for_size_instructions.frameNStart = frameN;  // exact frame index
      
      turtle_wedge_for_size_instructions.setAutoDraw(true);
    }
    
    
    // *turtle_wedge_boundary_for_instructions* updates
    if (t >= 0.0 && turtle_wedge_boundary_for_instructions.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      turtle_wedge_boundary_for_instructions.tStart = t;  // (not accounting for frame time here)
      turtle_wedge_boundary_for_instructions.frameNStart = frameN;  // exact frame index
      
      turtle_wedge_boundary_for_instructions.setAutoDraw(true);
    }
    
    
    // *avg_turtle_instr_3* updates
    if (t >= 0.0 && avg_turtle_instr_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      avg_turtle_instr_3.tStart = t;  // (not accounting for frame time here)
      avg_turtle_instr_3.frameNStart = frameN;  // exact frame index
      
      avg_turtle_instr_3.setAutoDraw(true);
    }
    
    
    // *key_resp_3* updates
    if (t >= 3 && key_resp_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_3.tStart = t;  // (not accounting for frame time here)
      key_resp_3.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_3.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_3.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_3.clearEvents(); });
    }
    
    if (key_resp_3.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_3.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_3_allKeys = _key_resp_3_allKeys.concat(theseKeys);
      if (_key_resp_3_allKeys.length > 0) {
        key_resp_3.keys = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].name;  // just the last key pressed
        key_resp_3.rt = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].rt;
        key_resp_3.duration = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].duration;
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
    for (const thisComponent of size_judgment_instructions_p3Components)
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

function size_judgment_instructions_p3RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'size_judgment_instructions_p3' ---
    for (const thisComponent of size_judgment_instructions_p3Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('size_judgment_instructions_p3.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_3.corr, level);
    }
    psychoJS.experiment.addData('key_resp_3.keys', key_resp_3.keys);
    if (typeof key_resp_3.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_3.rt', key_resp_3.rt);
        psychoJS.experiment.addData('key_resp_3.duration', key_resp_3.duration);
        routineTimer.reset();
        }
    
    key_resp_3.stop();
    // the Routine "size_judgment_instructions_p3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function size_judgment_instructions_p4RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'size_judgment_instructions_p4' ---
    t = 0;
    size_judgment_instructions_p4Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    size_judgment_instructions_p4MaxDurationReached = false;
    // update component parameters for each repeat
    turtle_halfcircle_for_size_instructions_2.setVertices(avg_turtle_halfcircle_vertices);
    turtle_wedge_for_size_instructions_2.setVertices(avg_turtle_wedge_vertices);
    key_resp_4.keys = undefined;
    key_resp_4.rt = undefined;
    _key_resp_4_allKeys = [];
    psychoJS.experiment.addData('size_judgment_instructions_p4.started', globalClock.getTime());
    size_judgment_instructions_p4MaxDuration = null
    // keep track of which components have finished
    size_judgment_instructions_p4Components = [];
    size_judgment_instructions_p4Components.push(turtle_halfcircle_for_size_instructions_2);
    size_judgment_instructions_p4Components.push(turtle_wedge_for_size_instructions_2);
    size_judgment_instructions_p4Components.push(turtle_wedge_boundary_for_instructions_2);
    size_judgment_instructions_p4Components.push(avg_turtle_instr);
    size_judgment_instructions_p4Components.push(key_resp_4);
    
    for (const thisComponent of size_judgment_instructions_p4Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function size_judgment_instructions_p4RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'size_judgment_instructions_p4' ---
    // get current time
    t = size_judgment_instructions_p4Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *turtle_halfcircle_for_size_instructions_2* updates
    if (t >= 0.0 && turtle_halfcircle_for_size_instructions_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      turtle_halfcircle_for_size_instructions_2.tStart = t;  // (not accounting for frame time here)
      turtle_halfcircle_for_size_instructions_2.frameNStart = frameN;  // exact frame index
      
      turtle_halfcircle_for_size_instructions_2.setAutoDraw(true);
    }
    
    
    // *turtle_wedge_for_size_instructions_2* updates
    if (t >= 0.0 && turtle_wedge_for_size_instructions_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      turtle_wedge_for_size_instructions_2.tStart = t;  // (not accounting for frame time here)
      turtle_wedge_for_size_instructions_2.frameNStart = frameN;  // exact frame index
      
      turtle_wedge_for_size_instructions_2.setAutoDraw(true);
    }
    
    
    // *turtle_wedge_boundary_for_instructions_2* updates
    if (t >= 0.0 && turtle_wedge_boundary_for_instructions_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      turtle_wedge_boundary_for_instructions_2.tStart = t;  // (not accounting for frame time here)
      turtle_wedge_boundary_for_instructions_2.frameNStart = frameN;  // exact frame index
      
      turtle_wedge_boundary_for_instructions_2.setAutoDraw(true);
    }
    
    
    // *avg_turtle_instr* updates
    if (t >= 0.0 && avg_turtle_instr.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      avg_turtle_instr.tStart = t;  // (not accounting for frame time here)
      avg_turtle_instr.frameNStart = frameN;  // exact frame index
      
      avg_turtle_instr.setAutoDraw(true);
    }
    
    
    // *key_resp_4* updates
    if (t >= 3 && key_resp_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_4.tStart = t;  // (not accounting for frame time here)
      key_resp_4.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_4.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_4.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_4.clearEvents(); });
    }
    
    if (key_resp_4.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_4.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_4_allKeys = _key_resp_4_allKeys.concat(theseKeys);
      if (_key_resp_4_allKeys.length > 0) {
        key_resp_4.keys = _key_resp_4_allKeys[_key_resp_4_allKeys.length - 1].name;  // just the last key pressed
        key_resp_4.rt = _key_resp_4_allKeys[_key_resp_4_allKeys.length - 1].rt;
        key_resp_4.duration = _key_resp_4_allKeys[_key_resp_4_allKeys.length - 1].duration;
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
    for (const thisComponent of size_judgment_instructions_p4Components)
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

function size_judgment_instructions_p4RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'size_judgment_instructions_p4' ---
    for (const thisComponent of size_judgment_instructions_p4Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('size_judgment_instructions_p4.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_4.corr, level);
    }
    psychoJS.experiment.addData('key_resp_4.keys', key_resp_4.keys);
    if (typeof key_resp_4.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_4.rt', key_resp_4.rt);
        psychoJS.experiment.addData('key_resp_4.duration', key_resp_4.duration);
        routineTimer.reset();
        }
    
    key_resp_4.stop();
    // the Routine "size_judgment_instructions_p4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function size_jugment_instructions_p5RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'size_jugment_instructions_p5' ---
    t = 0;
    size_jugment_instructions_p5Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    size_jugment_instructions_p5MaxDurationReached = false;
    // update component parameters for each repeat
    turtle_halfcircle_for_size_instructions_3.setVertices(avg_turtle_halfcircle_vertices);
    turtle_wedge_for_size_instructions_3.setVertices(avg_turtle_wedge_vertices);
    key_resp_5.keys = undefined;
    key_resp_5.rt = undefined;
    _key_resp_5_allKeys = [];
    psychoJS.experiment.addData('size_jugment_instructions_p5.started', globalClock.getTime());
    size_jugment_instructions_p5MaxDuration = null
    // keep track of which components have finished
    size_jugment_instructions_p5Components = [];
    size_jugment_instructions_p5Components.push(turtle_halfcircle_for_size_instructions_3);
    size_jugment_instructions_p5Components.push(turtle_wedge_for_size_instructions_3);
    size_jugment_instructions_p5Components.push(turtle_wedge_boundary_for_instructions_3);
    size_jugment_instructions_p5Components.push(avg_turtle_instr_4);
    size_jugment_instructions_p5Components.push(key_resp_5);
    
    for (const thisComponent of size_jugment_instructions_p5Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function size_jugment_instructions_p5RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'size_jugment_instructions_p5' ---
    // get current time
    t = size_jugment_instructions_p5Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *turtle_halfcircle_for_size_instructions_3* updates
    if (t >= 0.0 && turtle_halfcircle_for_size_instructions_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      turtle_halfcircle_for_size_instructions_3.tStart = t;  // (not accounting for frame time here)
      turtle_halfcircle_for_size_instructions_3.frameNStart = frameN;  // exact frame index
      
      turtle_halfcircle_for_size_instructions_3.setAutoDraw(true);
    }
    
    
    // *turtle_wedge_for_size_instructions_3* updates
    if (t >= 0.0 && turtle_wedge_for_size_instructions_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      turtle_wedge_for_size_instructions_3.tStart = t;  // (not accounting for frame time here)
      turtle_wedge_for_size_instructions_3.frameNStart = frameN;  // exact frame index
      
      turtle_wedge_for_size_instructions_3.setAutoDraw(true);
    }
    
    
    // *turtle_wedge_boundary_for_instructions_3* updates
    if (t >= 0.0 && turtle_wedge_boundary_for_instructions_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      turtle_wedge_boundary_for_instructions_3.tStart = t;  // (not accounting for frame time here)
      turtle_wedge_boundary_for_instructions_3.frameNStart = frameN;  // exact frame index
      
      turtle_wedge_boundary_for_instructions_3.setAutoDraw(true);
    }
    
    
    // *avg_turtle_instr_4* updates
    if (t >= 0.0 && avg_turtle_instr_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      avg_turtle_instr_4.tStart = t;  // (not accounting for frame time here)
      avg_turtle_instr_4.frameNStart = frameN;  // exact frame index
      
      avg_turtle_instr_4.setAutoDraw(true);
    }
    
    
    // *key_resp_5* updates
    if (t >= 3 && key_resp_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_5.tStart = t;  // (not accounting for frame time here)
      key_resp_5.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_5.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_5.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_5.clearEvents(); });
    }
    
    if (key_resp_5.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_5.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_5_allKeys = _key_resp_5_allKeys.concat(theseKeys);
      if (_key_resp_5_allKeys.length > 0) {
        key_resp_5.keys = _key_resp_5_allKeys[_key_resp_5_allKeys.length - 1].name;  // just the last key pressed
        key_resp_5.rt = _key_resp_5_allKeys[_key_resp_5_allKeys.length - 1].rt;
        key_resp_5.duration = _key_resp_5_allKeys[_key_resp_5_allKeys.length - 1].duration;
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
    for (const thisComponent of size_jugment_instructions_p5Components)
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

function size_jugment_instructions_p5RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'size_jugment_instructions_p5' ---
    for (const thisComponent of size_jugment_instructions_p5Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('size_jugment_instructions_p5.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_5.corr, level);
    }
    psychoJS.experiment.addData('key_resp_5.keys', key_resp_5.keys);
    if (typeof key_resp_5.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_5.rt', key_resp_5.rt);
        psychoJS.experiment.addData('key_resp_5.duration', key_resp_5.duration);
        routineTimer.reset();
        }
    
    key_resp_5.stop();
    // the Routine "size_jugment_instructions_p5" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function size_judgment_instructions_p6RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'size_judgment_instructions_p6' ---
    t = 0;
    size_judgment_instructions_p6Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    size_judgment_instructions_p6MaxDurationReached = false;
    // update component parameters for each repeat
    turtle_halfcircle_for_size_instructions_4.setVertices(avg_turtle_halfcircle_vertices);
    turtle_wedge_for_size_instructions_4.setVertices(avg_turtle_wedge_vertices);
    key_resp_6.keys = undefined;
    key_resp_6.rt = undefined;
    _key_resp_6_allKeys = [];
    psychoJS.experiment.addData('size_judgment_instructions_p6.started', globalClock.getTime());
    size_judgment_instructions_p6MaxDuration = null
    // keep track of which components have finished
    size_judgment_instructions_p6Components = [];
    size_judgment_instructions_p6Components.push(turtle_halfcircle_for_size_instructions_4);
    size_judgment_instructions_p6Components.push(turtle_wedge_for_size_instructions_4);
    size_judgment_instructions_p6Components.push(turtle_wedge_boundary_for_instructions_4);
    size_judgment_instructions_p6Components.push(avg_turtle_instr_5);
    size_judgment_instructions_p6Components.push(key_resp_6);
    
    for (const thisComponent of size_judgment_instructions_p6Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function size_judgment_instructions_p6RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'size_judgment_instructions_p6' ---
    // get current time
    t = size_judgment_instructions_p6Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *turtle_halfcircle_for_size_instructions_4* updates
    if (t >= 0.0 && turtle_halfcircle_for_size_instructions_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      turtle_halfcircle_for_size_instructions_4.tStart = t;  // (not accounting for frame time here)
      turtle_halfcircle_for_size_instructions_4.frameNStart = frameN;  // exact frame index
      
      turtle_halfcircle_for_size_instructions_4.setAutoDraw(true);
    }
    
    
    // *turtle_wedge_for_size_instructions_4* updates
    if (t >= 0.0 && turtle_wedge_for_size_instructions_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      turtle_wedge_for_size_instructions_4.tStart = t;  // (not accounting for frame time here)
      turtle_wedge_for_size_instructions_4.frameNStart = frameN;  // exact frame index
      
      turtle_wedge_for_size_instructions_4.setAutoDraw(true);
    }
    
    
    // *turtle_wedge_boundary_for_instructions_4* updates
    if (t >= 0.0 && turtle_wedge_boundary_for_instructions_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      turtle_wedge_boundary_for_instructions_4.tStart = t;  // (not accounting for frame time here)
      turtle_wedge_boundary_for_instructions_4.frameNStart = frameN;  // exact frame index
      
      turtle_wedge_boundary_for_instructions_4.setAutoDraw(true);
    }
    
    
    // *avg_turtle_instr_5* updates
    if (t >= 0.0 && avg_turtle_instr_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      avg_turtle_instr_5.tStart = t;  // (not accounting for frame time here)
      avg_turtle_instr_5.frameNStart = frameN;  // exact frame index
      
      avg_turtle_instr_5.setAutoDraw(true);
    }
    
    
    // *key_resp_6* updates
    if (t >= 0.5 && key_resp_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_6.tStart = t;  // (not accounting for frame time here)
      key_resp_6.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_6.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_6.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_6.clearEvents(); });
    }
    
    if (key_resp_6.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_6.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_6_allKeys = _key_resp_6_allKeys.concat(theseKeys);
      if (_key_resp_6_allKeys.length > 0) {
        key_resp_6.keys = _key_resp_6_allKeys[_key_resp_6_allKeys.length - 1].name;  // just the last key pressed
        key_resp_6.rt = _key_resp_6_allKeys[_key_resp_6_allKeys.length - 1].rt;
        key_resp_6.duration = _key_resp_6_allKeys[_key_resp_6_allKeys.length - 1].duration;
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
    for (const thisComponent of size_judgment_instructions_p6Components)
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

function size_judgment_instructions_p6RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'size_judgment_instructions_p6' ---
    for (const thisComponent of size_judgment_instructions_p6Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('size_judgment_instructions_p6.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_6.corr, level);
    }
    psychoJS.experiment.addData('key_resp_6.keys', key_resp_6.keys);
    if (typeof key_resp_6.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_6.rt', key_resp_6.rt);
        psychoJS.experiment.addData('key_resp_6.duration', key_resp_6.duration);
        routineTimer.reset();
        }
    
    key_resp_6.stop();
    // the Routine "size_judgment_instructions_p6" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function size_judgment_paramsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'size_judgment_params' ---
    t = 0;
    size_judgment_paramsClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    size_judgment_paramsMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from get_turtle_params_for_size
    turtle_halfcircle_vertices = get_turtle_halfcircle_vertices(radius);
    turtle_wedge_vertices = get_turtle_wedge_vertices(angle);
    if ((area < avg_turtle_area)) {
        console.log("correct response is f");
        corr_resp_size_tmp = "f";
    } else {
        if ((area > avg_turtle_area)) {
            console.log("correct response is j");
            corr_resp_size_tmp = "j";
        }
    }
    
    psychoJS.experiment.addData('size_judgment_params.started', globalClock.getTime());
    size_judgment_paramsMaxDuration = null
    // keep track of which components have finished
    size_judgment_paramsComponents = [];
    
    for (const thisComponent of size_judgment_paramsComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function size_judgment_paramsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'size_judgment_params' ---
    // get current time
    t = size_judgment_paramsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of size_judgment_paramsComponents)
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

function size_judgment_paramsRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'size_judgment_params' ---
    for (const thisComponent of size_judgment_paramsComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('size_judgment_params.stopped', globalClock.getTime());
    // the Routine "size_judgment_params" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function size_judgment_responseRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'size_judgment_response' ---
    t = 0;
    size_judgment_responseClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    size_judgment_responseMaxDurationReached = false;
    // update component parameters for each repeat
    turtle_half_circle_for_size_judgment.setVertices(turtle_halfcircle_vertices);
    turtle_wedge_for_size_judgment.setVertices(turtle_wedge_vertices);
    key_resp_size_judgment.keys = undefined;
    key_resp_size_judgment.rt = undefined;
    _key_resp_size_judgment_allKeys = [];
    psychoJS.experiment.addData('size_judgment_response.started', globalClock.getTime());
    size_judgment_responseMaxDuration = null
    // keep track of which components have finished
    size_judgment_responseComponents = [];
    size_judgment_responseComponents.push(turtle_half_circle_for_size_judgment);
    size_judgment_responseComponents.push(turtle_wedge_for_size_judgment);
    size_judgment_responseComponents.push(turtle_boundary_for_size_judgment);
    size_judgment_responseComponents.push(size_judgment_prompt);
    size_judgment_responseComponents.push(key_resp_size_judgment);
    
    for (const thisComponent of size_judgment_responseComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function size_judgment_responseRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'size_judgment_response' ---
    // get current time
    t = size_judgment_responseClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *turtle_half_circle_for_size_judgment* updates
    if (t >= 0.0 && turtle_half_circle_for_size_judgment.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      turtle_half_circle_for_size_judgment.tStart = t;  // (not accounting for frame time here)
      turtle_half_circle_for_size_judgment.frameNStart = frameN;  // exact frame index
      
      turtle_half_circle_for_size_judgment.setAutoDraw(true);
    }
    
    
    // *turtle_wedge_for_size_judgment* updates
    if (t >= 0.0 && turtle_wedge_for_size_judgment.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      turtle_wedge_for_size_judgment.tStart = t;  // (not accounting for frame time here)
      turtle_wedge_for_size_judgment.frameNStart = frameN;  // exact frame index
      
      turtle_wedge_for_size_judgment.setAutoDraw(true);
    }
    
    
    // *turtle_boundary_for_size_judgment* updates
    if (t >= 0.0 && turtle_boundary_for_size_judgment.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      turtle_boundary_for_size_judgment.tStart = t;  // (not accounting for frame time here)
      turtle_boundary_for_size_judgment.frameNStart = frameN;  // exact frame index
      
      turtle_boundary_for_size_judgment.setAutoDraw(true);
    }
    
    
    // *size_judgment_prompt* updates
    if (t >= 0.0 && size_judgment_prompt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      size_judgment_prompt.tStart = t;  // (not accounting for frame time here)
      size_judgment_prompt.frameNStart = frameN;  // exact frame index
      
      size_judgment_prompt.setAutoDraw(true);
    }
    
    
    // *key_resp_size_judgment* updates
    if (t >= 0.0 && key_resp_size_judgment.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_size_judgment.tStart = t;  // (not accounting for frame time here)
      key_resp_size_judgment.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_size_judgment.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_size_judgment.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_size_judgment.clearEvents(); });
    }
    
    if (key_resp_size_judgment.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_size_judgment.getKeys({keyList: ['f', 'j'], waitRelease: false});
      _key_resp_size_judgment_allKeys = _key_resp_size_judgment_allKeys.concat(theseKeys);
      if (_key_resp_size_judgment_allKeys.length > 0) {
        key_resp_size_judgment.keys = _key_resp_size_judgment_allKeys[_key_resp_size_judgment_allKeys.length - 1].name;  // just the last key pressed
        key_resp_size_judgment.rt = _key_resp_size_judgment_allKeys[_key_resp_size_judgment_allKeys.length - 1].rt;
        key_resp_size_judgment.duration = _key_resp_size_judgment_allKeys[_key_resp_size_judgment_allKeys.length - 1].duration;
        // was this correct?
        if (key_resp_size_judgment.keys == corr_resp_size_tmp) {
            key_resp_size_judgment.corr = 1;
        } else {
            key_resp_size_judgment.corr = 0;
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
    for (const thisComponent of size_judgment_responseComponents)
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

function size_judgment_responseRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'size_judgment_response' ---
    for (const thisComponent of size_judgment_responseComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('size_judgment_response.stopped', globalClock.getTime());
    // was no response the correct answer?!
    if (key_resp_size_judgment.keys === undefined) {
      if (['None','none',undefined].includes(corr_resp_size_tmp)) {
         key_resp_size_judgment.corr = 1;  // correct non-response
      } else {
         key_resp_size_judgment.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_size_judgment.corr, level);
    }
    psychoJS.experiment.addData('key_resp_size_judgment.keys', key_resp_size_judgment.keys);
    psychoJS.experiment.addData('key_resp_size_judgment.corr', key_resp_size_judgment.corr);
    if (typeof key_resp_size_judgment.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_size_judgment.rt', key_resp_size_judgment.rt);
        psychoJS.experiment.addData('key_resp_size_judgment.duration', key_resp_size_judgment.duration);
        routineTimer.reset();
        }
    
    key_resp_size_judgment.stop();
    // the Routine "size_judgment_response" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function size_jugment_code_checkRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'size_jugment_code_check' ---
    t = 0;
    size_jugment_code_checkClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    size_jugment_code_checkMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from size_judgment_code_check
    if ((key_resp_size_judgment.corr === 1)) {
        size_feedback_dur = 1;
        size_feedback_col = "#008000";
        if ((corr_resp_size_tmp === "f")) {
            size_feedback_text = "You were correct! This turtle is smaller than the average turtle.";
        } else {
            if ((corr_resp_size_tmp === "j")) {
                size_feedback_text = "You were correct! This turtle is larger than the average turtle.";
            }
        }
    } else {
        if ((key_resp_size_judgment.corr === 0)) {
            size_feedback_dur = 2;
            size_feedback_col = "#FF0000";
            if ((corr_resp_size_tmp === "f")) {
                size_feedback_text = "You were incorrect. This turtle is smaller than the average turtle.";
            } else {
                if ((corr_resp_size_tmp === "j")) {
                    size_feedback_text = "You were incorrect. This turtle is larger than the average turtle.";
                }
            }
        }
    }
    
    psychoJS.experiment.addData('size_jugment_code_check.started', globalClock.getTime());
    size_jugment_code_checkMaxDuration = null
    // keep track of which components have finished
    size_jugment_code_checkComponents = [];
    
    for (const thisComponent of size_jugment_code_checkComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function size_jugment_code_checkRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'size_jugment_code_check' ---
    // get current time
    t = size_jugment_code_checkClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of size_jugment_code_checkComponents)
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

function size_jugment_code_checkRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'size_jugment_code_check' ---
    for (const thisComponent of size_jugment_code_checkComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('size_jugment_code_check.stopped', globalClock.getTime());
    // the Routine "size_jugment_code_check" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function size_judgment_feedbackRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'size_judgment_feedback' ---
    t = 0;
    size_judgment_feedbackClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    size_judgment_feedbackMaxDurationReached = false;
    // update component parameters for each repeat
    turtle_half_circle_for_size_judgment_feedback.setVertices(turtle_halfcircle_vertices);
    turtle_wedge_for_size_judgment_feedback.setVertices(turtle_wedge_vertices);
    size_feedback_text_display.setColor(new util.Color(size_feedback_col));
    size_feedback_text_display.setText(size_feedback_text);
    psychoJS.experiment.addData('size_judgment_feedback.started', globalClock.getTime());
    size_judgment_feedbackMaxDuration = null
    // keep track of which components have finished
    size_judgment_feedbackComponents = [];
    size_judgment_feedbackComponents.push(turtle_half_circle_for_size_judgment_feedback);
    size_judgment_feedbackComponents.push(turtle_wedge_for_size_judgment_feedback);
    size_judgment_feedbackComponents.push(turtle_boundary_for_size_judgment_feedback);
    size_judgment_feedbackComponents.push(size_feedback_text_display);
    
    for (const thisComponent of size_judgment_feedbackComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function size_judgment_feedbackRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'size_judgment_feedback' ---
    // get current time
    t = size_judgment_feedbackClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *turtle_half_circle_for_size_judgment_feedback* updates
    if (t >= 0.0 && turtle_half_circle_for_size_judgment_feedback.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      turtle_half_circle_for_size_judgment_feedback.tStart = t;  // (not accounting for frame time here)
      turtle_half_circle_for_size_judgment_feedback.frameNStart = frameN;  // exact frame index
      
      turtle_half_circle_for_size_judgment_feedback.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + size_feedback_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (turtle_half_circle_for_size_judgment_feedback.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      turtle_half_circle_for_size_judgment_feedback.setAutoDraw(false);
    }
    
    
    // *turtle_wedge_for_size_judgment_feedback* updates
    if (t >= 0.0 && turtle_wedge_for_size_judgment_feedback.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      turtle_wedge_for_size_judgment_feedback.tStart = t;  // (not accounting for frame time here)
      turtle_wedge_for_size_judgment_feedback.frameNStart = frameN;  // exact frame index
      
      turtle_wedge_for_size_judgment_feedback.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + size_feedback_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (turtle_wedge_for_size_judgment_feedback.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      turtle_wedge_for_size_judgment_feedback.setAutoDraw(false);
    }
    
    
    // *turtle_boundary_for_size_judgment_feedback* updates
    if (t >= 0.0 && turtle_boundary_for_size_judgment_feedback.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      turtle_boundary_for_size_judgment_feedback.tStart = t;  // (not accounting for frame time here)
      turtle_boundary_for_size_judgment_feedback.frameNStart = frameN;  // exact frame index
      
      turtle_boundary_for_size_judgment_feedback.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + size_feedback_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (turtle_boundary_for_size_judgment_feedback.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      turtle_boundary_for_size_judgment_feedback.setAutoDraw(false);
    }
    
    
    // *size_feedback_text_display* updates
    if (t >= 0.0 && size_feedback_text_display.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      size_feedback_text_display.tStart = t;  // (not accounting for frame time here)
      size_feedback_text_display.frameNStart = frameN;  // exact frame index
      
      size_feedback_text_display.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + size_feedback_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (size_feedback_text_display.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      size_feedback_text_display.setAutoDraw(false);
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
    for (const thisComponent of size_judgment_feedbackComponents)
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

function size_judgment_feedbackRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'size_judgment_feedback' ---
    for (const thisComponent of size_judgment_feedbackComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('size_judgment_feedback.stopped', globalClock.getTime());
    // the Routine "size_judgment_feedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function del_corr_size_resp_tmpRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'del_corr_size_resp_tmp' ---
    t = 0;
    del_corr_size_resp_tmpClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    del_corr_size_resp_tmpMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from del_corr_resp_size_tmp_code
    delete corr_resp_size_tmp;
    
    psychoJS.experiment.addData('del_corr_size_resp_tmp.started', globalClock.getTime());
    del_corr_size_resp_tmpMaxDuration = null
    // keep track of which components have finished
    del_corr_size_resp_tmpComponents = [];
    
    for (const thisComponent of del_corr_size_resp_tmpComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function del_corr_size_resp_tmpRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'del_corr_size_resp_tmp' ---
    // get current time
    t = del_corr_size_resp_tmpClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of del_corr_size_resp_tmpComponents)
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

function del_corr_size_resp_tmpRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'del_corr_size_resp_tmp' ---
    for (const thisComponent of del_corr_size_resp_tmpComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('del_corr_size_resp_tmp.stopped', globalClock.getTime());
    // the Routine "del_corr_size_resp_tmp" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function indexRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'index' ---
    t = 0;
    indexClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    indexMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from index_setup
    i = 0;
    
    psychoJS.experiment.addData('index.started', globalClock.getTime());
    indexMaxDuration = null
    // keep track of which components have finished
    indexComponents = [];
    
    for (const thisComponent of indexComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function indexRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'index' ---
    // get current time
    t = indexClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of indexComponents)
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

function indexRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'index' ---
    for (const thisComponent of indexComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('index.stopped', globalClock.getTime());
    // the Routine "index" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function transfer_loop_setupRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'transfer_loop_setup' ---
    t = 0;
    transfer_loop_setupClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    transfer_loop_setupMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from index_update
    if ((i === 0)) {
        if ((condition === "switch/standard")) {
            num_repeats_1 = 0;
            num_repeats_2 = num_transfer_blocks;
            do_standard_instructions = 0;
            do_switch_instructions = 1;
        } else {
            if ((condition === "standard/switch")) {
                num_repeats_1 = num_transfer_blocks;
                num_repeats_2 = 0;
                do_standard_instructions = 1;
                do_switch_instructions = 0;
            }
        }
    } else {
        if ((i === 1)) {
            if ((condition === "switch/standard")) {
                num_repeats_1 = num_transfer_blocks;
                num_repeats_2 = 0;
                do_standard_instructions = 1;
                do_switch_instructions = 0;
            } else {
                if ((condition === "standard/switch")) {
                    num_repeats_1 = 0;
                    num_repeats_2 = num_transfer_blocks;
                    do_standard_instructions = 0;
                    do_switch_instructions = 1;
                }
            }
        }
    }
    i = (i + 1);
    
    psychoJS.experiment.addData('transfer_loop_setup.started', globalClock.getTime());
    transfer_loop_setupMaxDuration = null
    // keep track of which components have finished
    transfer_loop_setupComponents = [];
    
    for (const thisComponent of transfer_loop_setupComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function transfer_loop_setupRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'transfer_loop_setup' ---
    // get current time
    t = transfer_loop_setupClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of transfer_loop_setupComponents)
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

function transfer_loop_setupRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'transfer_loop_setup' ---
    for (const thisComponent of transfer_loop_setupComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('transfer_loop_setup.stopped', globalClock.getTime());
    // the Routine "transfer_loop_setup" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function transfer_standard_instructions_p1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'transfer_standard_instructions_p1' ---
    t = 0;
    transfer_standard_instructions_p1Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    transfer_standard_instructions_p1MaxDurationReached = false;
    // update component parameters for each repeat
    space_8.keys = undefined;
    space_8.rt = undefined;
    _space_8_allKeys = [];
    psychoJS.experiment.addData('transfer_standard_instructions_p1.started', globalClock.getTime());
    transfer_standard_instructions_p1MaxDuration = null
    // keep track of which components have finished
    transfer_standard_instructions_p1Components = [];
    transfer_standard_instructions_p1Components.push(transfer_standard_instructions_text_1);
    transfer_standard_instructions_p1Components.push(space_7);
    transfer_standard_instructions_p1Components.push(space_8);
    
    for (const thisComponent of transfer_standard_instructions_p1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function transfer_standard_instructions_p1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'transfer_standard_instructions_p1' ---
    // get current time
    t = transfer_standard_instructions_p1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *transfer_standard_instructions_text_1* updates
    if (t >= 0.0 && transfer_standard_instructions_text_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      transfer_standard_instructions_text_1.tStart = t;  // (not accounting for frame time here)
      transfer_standard_instructions_text_1.frameNStart = frameN;  // exact frame index
      
      transfer_standard_instructions_text_1.setAutoDraw(true);
    }
    
    
    // *space_7* updates
    if (t >= 2 && space_7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      space_7.tStart = t;  // (not accounting for frame time here)
      space_7.frameNStart = frameN;  // exact frame index
      
      space_7.setAutoDraw(true);
    }
    
    
    // *space_8* updates
    if (t >= 2 && space_8.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      space_8.tStart = t;  // (not accounting for frame time here)
      space_8.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { space_8.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { space_8.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { space_8.clearEvents(); });
    }
    
    if (space_8.status === PsychoJS.Status.STARTED) {
      let theseKeys = space_8.getKeys({keyList: ['space'], waitRelease: false});
      _space_8_allKeys = _space_8_allKeys.concat(theseKeys);
      if (_space_8_allKeys.length > 0) {
        space_8.keys = _space_8_allKeys[_space_8_allKeys.length - 1].name;  // just the last key pressed
        space_8.rt = _space_8_allKeys[_space_8_allKeys.length - 1].rt;
        space_8.duration = _space_8_allKeys[_space_8_allKeys.length - 1].duration;
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
    for (const thisComponent of transfer_standard_instructions_p1Components)
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

function transfer_standard_instructions_p1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'transfer_standard_instructions_p1' ---
    for (const thisComponent of transfer_standard_instructions_p1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('transfer_standard_instructions_p1.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(space_8.corr, level);
    }
    psychoJS.experiment.addData('space_8.keys', space_8.keys);
    if (typeof space_8.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('space_8.rt', space_8.rt);
        psychoJS.experiment.addData('space_8.duration', space_8.duration);
        routineTimer.reset();
        }
    
    space_8.stop();
    // the Routine "transfer_standard_instructions_p1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function transfer_standard_instructions_p2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'transfer_standard_instructions_p2' ---
    t = 0;
    transfer_standard_instructions_p2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    transfer_standard_instructions_p2MaxDurationReached = false;
    // update component parameters for each repeat
    space_10.keys = undefined;
    space_10.rt = undefined;
    _space_10_allKeys = [];
    psychoJS.experiment.addData('transfer_standard_instructions_p2.started', globalClock.getTime());
    transfer_standard_instructions_p2MaxDuration = null
    // keep track of which components have finished
    transfer_standard_instructions_p2Components = [];
    transfer_standard_instructions_p2Components.push(transfer_standard_instructions_text);
    transfer_standard_instructions_p2Components.push(space_9);
    transfer_standard_instructions_p2Components.push(space_10);
    
    for (const thisComponent of transfer_standard_instructions_p2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function transfer_standard_instructions_p2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'transfer_standard_instructions_p2' ---
    // get current time
    t = transfer_standard_instructions_p2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *transfer_standard_instructions_text* updates
    if (t >= 0.0 && transfer_standard_instructions_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      transfer_standard_instructions_text.tStart = t;  // (not accounting for frame time here)
      transfer_standard_instructions_text.frameNStart = frameN;  // exact frame index
      
      transfer_standard_instructions_text.setAutoDraw(true);
    }
    
    
    // *space_9* updates
    if (t >= 2 && space_9.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      space_9.tStart = t;  // (not accounting for frame time here)
      space_9.frameNStart = frameN;  // exact frame index
      
      space_9.setAutoDraw(true);
    }
    
    
    // *space_10* updates
    if (t >= 2 && space_10.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      space_10.tStart = t;  // (not accounting for frame time here)
      space_10.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { space_10.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { space_10.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { space_10.clearEvents(); });
    }
    
    if (space_10.status === PsychoJS.Status.STARTED) {
      let theseKeys = space_10.getKeys({keyList: ['space'], waitRelease: false});
      _space_10_allKeys = _space_10_allKeys.concat(theseKeys);
      if (_space_10_allKeys.length > 0) {
        space_10.keys = _space_10_allKeys[_space_10_allKeys.length - 1].name;  // just the last key pressed
        space_10.rt = _space_10_allKeys[_space_10_allKeys.length - 1].rt;
        space_10.duration = _space_10_allKeys[_space_10_allKeys.length - 1].duration;
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
    for (const thisComponent of transfer_standard_instructions_p2Components)
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

function transfer_standard_instructions_p2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'transfer_standard_instructions_p2' ---
    for (const thisComponent of transfer_standard_instructions_p2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('transfer_standard_instructions_p2.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(space_10.corr, level);
    }
    psychoJS.experiment.addData('space_10.keys', space_10.keys);
    if (typeof space_10.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('space_10.rt', space_10.rt);
        psychoJS.experiment.addData('space_10.duration', space_10.duration);
        routineTimer.reset();
        }
    
    space_10.stop();
    // the Routine "transfer_standard_instructions_p2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function transfer_standard_instructions_p3RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'transfer_standard_instructions_p3' ---
    t = 0;
    transfer_standard_instructions_p3Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    transfer_standard_instructions_p3MaxDurationReached = false;
    // update component parameters for each repeat
    space_12.keys = undefined;
    space_12.rt = undefined;
    _space_12_allKeys = [];
    psychoJS.experiment.addData('transfer_standard_instructions_p3.started', globalClock.getTime());
    transfer_standard_instructions_p3MaxDuration = null
    // keep track of which components have finished
    transfer_standard_instructions_p3Components = [];
    transfer_standard_instructions_p3Components.push(transfer_standard_instructions_text_2);
    transfer_standard_instructions_p3Components.push(space_11);
    transfer_standard_instructions_p3Components.push(space_12);
    
    for (const thisComponent of transfer_standard_instructions_p3Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function transfer_standard_instructions_p3RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'transfer_standard_instructions_p3' ---
    // get current time
    t = transfer_standard_instructions_p3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *transfer_standard_instructions_text_2* updates
    if (t >= 0.0 && transfer_standard_instructions_text_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      transfer_standard_instructions_text_2.tStart = t;  // (not accounting for frame time here)
      transfer_standard_instructions_text_2.frameNStart = frameN;  // exact frame index
      
      transfer_standard_instructions_text_2.setAutoDraw(true);
    }
    
    
    // *space_11* updates
    if (t >= 2 && space_11.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      space_11.tStart = t;  // (not accounting for frame time here)
      space_11.frameNStart = frameN;  // exact frame index
      
      space_11.setAutoDraw(true);
    }
    
    
    // *space_12* updates
    if (t >= 2 && space_12.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      space_12.tStart = t;  // (not accounting for frame time here)
      space_12.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { space_12.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { space_12.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { space_12.clearEvents(); });
    }
    
    if (space_12.status === PsychoJS.Status.STARTED) {
      let theseKeys = space_12.getKeys({keyList: ['space'], waitRelease: false});
      _space_12_allKeys = _space_12_allKeys.concat(theseKeys);
      if (_space_12_allKeys.length > 0) {
        space_12.keys = _space_12_allKeys[_space_12_allKeys.length - 1].name;  // just the last key pressed
        space_12.rt = _space_12_allKeys[_space_12_allKeys.length - 1].rt;
        space_12.duration = _space_12_allKeys[_space_12_allKeys.length - 1].duration;
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
    for (const thisComponent of transfer_standard_instructions_p3Components)
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

function transfer_standard_instructions_p3RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'transfer_standard_instructions_p3' ---
    for (const thisComponent of transfer_standard_instructions_p3Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('transfer_standard_instructions_p3.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(space_12.corr, level);
    }
    psychoJS.experiment.addData('space_12.keys', space_12.keys);
    if (typeof space_12.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('space_12.rt', space_12.rt);
        psychoJS.experiment.addData('space_12.duration', space_12.duration);
        routineTimer.reset();
        }
    
    space_12.stop();
    // the Routine "transfer_standard_instructions_p3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function transfer_response_standardRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'transfer_response_standard' ---
    t = 0;
    transfer_response_standardClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    transfer_response_standardMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from get_turtle_params_transfer_standard
    turtle_halfcircle_vertices = get_turtle_halfcircle_vertices(radius);
    turtle_wedge_vertices = get_turtle_wedge_vertices(angle);
    
    transfer_prompt_standard_trials.setText('Is this turtle in Species F or Species J? \n\nF - Species F, J - Species J');
    key_resp_transfer_standard.keys = undefined;
    key_resp_transfer_standard.rt = undefined;
    _key_resp_transfer_standard_allKeys = [];
    turtle_halfcircle_standard.setVertices(turtle_halfcircle_vertices);
    turtle_wedge_standard.setVertices(turtle_wedge_vertices);
    psychoJS.experiment.addData('transfer_response_standard.started', globalClock.getTime());
    transfer_response_standardMaxDuration = null
    // keep track of which components have finished
    transfer_response_standardComponents = [];
    transfer_response_standardComponents.push(transfer_prompt_standard_trials);
    transfer_response_standardComponents.push(key_resp_transfer_standard);
    transfer_response_standardComponents.push(turtle_halfcircle_standard);
    transfer_response_standardComponents.push(turtle_wedge_standard);
    transfer_response_standardComponents.push(turtle_wedge_boundary_standard);
    
    for (const thisComponent of transfer_response_standardComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function transfer_response_standardRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'transfer_response_standard' ---
    // get current time
    t = transfer_response_standardClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *transfer_prompt_standard_trials* updates
    if (t >= 0.0 && transfer_prompt_standard_trials.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      transfer_prompt_standard_trials.tStart = t;  // (not accounting for frame time here)
      transfer_prompt_standard_trials.frameNStart = frameN;  // exact frame index
      
      transfer_prompt_standard_trials.setAutoDraw(true);
    }
    
    
    // *key_resp_transfer_standard* updates
    if (t >= 0.0 && key_resp_transfer_standard.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_transfer_standard.tStart = t;  // (not accounting for frame time here)
      key_resp_transfer_standard.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_transfer_standard.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_transfer_standard.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_transfer_standard.clearEvents(); });
    }
    
    if (key_resp_transfer_standard.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_transfer_standard.getKeys({keyList: ['f', 'j'], waitRelease: false});
      _key_resp_transfer_standard_allKeys = _key_resp_transfer_standard_allKeys.concat(theseKeys);
      if (_key_resp_transfer_standard_allKeys.length > 0) {
        key_resp_transfer_standard.keys = _key_resp_transfer_standard_allKeys[_key_resp_transfer_standard_allKeys.length - 1].name;  // just the last key pressed
        key_resp_transfer_standard.rt = _key_resp_transfer_standard_allKeys[_key_resp_transfer_standard_allKeys.length - 1].rt;
        key_resp_transfer_standard.duration = _key_resp_transfer_standard_allKeys[_key_resp_transfer_standard_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *turtle_halfcircle_standard* updates
    if (t >= 0.0 && turtle_halfcircle_standard.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      turtle_halfcircle_standard.tStart = t;  // (not accounting for frame time here)
      turtle_halfcircle_standard.frameNStart = frameN;  // exact frame index
      
      turtle_halfcircle_standard.setAutoDraw(true);
    }
    
    
    // *turtle_wedge_standard* updates
    if (t >= 0.0 && turtle_wedge_standard.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      turtle_wedge_standard.tStart = t;  // (not accounting for frame time here)
      turtle_wedge_standard.frameNStart = frameN;  // exact frame index
      
      turtle_wedge_standard.setAutoDraw(true);
    }
    
    
    // *turtle_wedge_boundary_standard* updates
    if (t >= 0.0 && turtle_wedge_boundary_standard.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      turtle_wedge_boundary_standard.tStart = t;  // (not accounting for frame time here)
      turtle_wedge_boundary_standard.frameNStart = frameN;  // exact frame index
      
      turtle_wedge_boundary_standard.setAutoDraw(true);
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
    for (const thisComponent of transfer_response_standardComponents)
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

function transfer_response_standardRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'transfer_response_standard' ---
    for (const thisComponent of transfer_response_standardComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('transfer_response_standard.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_transfer_standard.corr, level);
    }
    psychoJS.experiment.addData('key_resp_transfer_standard.keys', key_resp_transfer_standard.keys);
    if (typeof key_resp_transfer_standard.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_transfer_standard.rt', key_resp_transfer_standard.rt);
        psychoJS.experiment.addData('key_resp_transfer_standard.duration', key_resp_transfer_standard.duration);
        routineTimer.reset();
        }
    
    key_resp_transfer_standard.stop();
    // the Routine "transfer_response_standard" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function transfer_switch_instructions_p1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'transfer_switch_instructions_p1' ---
    t = 0;
    transfer_switch_instructions_p1Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    transfer_switch_instructions_p1MaxDurationReached = false;
    // update component parameters for each repeat
    space_14.keys = undefined;
    space_14.rt = undefined;
    _space_14_allKeys = [];
    psychoJS.experiment.addData('transfer_switch_instructions_p1.started', globalClock.getTime());
    transfer_switch_instructions_p1MaxDuration = null
    // keep track of which components have finished
    transfer_switch_instructions_p1Components = [];
    transfer_switch_instructions_p1Components.push(transfer_switch_instructions_text_1);
    transfer_switch_instructions_p1Components.push(space_13);
    transfer_switch_instructions_p1Components.push(space_14);
    
    for (const thisComponent of transfer_switch_instructions_p1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function transfer_switch_instructions_p1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'transfer_switch_instructions_p1' ---
    // get current time
    t = transfer_switch_instructions_p1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *transfer_switch_instructions_text_1* updates
    if (t >= 0.0 && transfer_switch_instructions_text_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      transfer_switch_instructions_text_1.tStart = t;  // (not accounting for frame time here)
      transfer_switch_instructions_text_1.frameNStart = frameN;  // exact frame index
      
      transfer_switch_instructions_text_1.setAutoDraw(true);
    }
    
    
    // *space_13* updates
    if (t >= 2 && space_13.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      space_13.tStart = t;  // (not accounting for frame time here)
      space_13.frameNStart = frameN;  // exact frame index
      
      space_13.setAutoDraw(true);
    }
    
    
    // *space_14* updates
    if (t >= 2 && space_14.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      space_14.tStart = t;  // (not accounting for frame time here)
      space_14.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { space_14.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { space_14.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { space_14.clearEvents(); });
    }
    
    if (space_14.status === PsychoJS.Status.STARTED) {
      let theseKeys = space_14.getKeys({keyList: ['space'], waitRelease: false});
      _space_14_allKeys = _space_14_allKeys.concat(theseKeys);
      if (_space_14_allKeys.length > 0) {
        space_14.keys = _space_14_allKeys[_space_14_allKeys.length - 1].name;  // just the last key pressed
        space_14.rt = _space_14_allKeys[_space_14_allKeys.length - 1].rt;
        space_14.duration = _space_14_allKeys[_space_14_allKeys.length - 1].duration;
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
    for (const thisComponent of transfer_switch_instructions_p1Components)
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

function transfer_switch_instructions_p1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'transfer_switch_instructions_p1' ---
    for (const thisComponent of transfer_switch_instructions_p1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('transfer_switch_instructions_p1.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(space_14.corr, level);
    }
    psychoJS.experiment.addData('space_14.keys', space_14.keys);
    if (typeof space_14.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('space_14.rt', space_14.rt);
        psychoJS.experiment.addData('space_14.duration', space_14.duration);
        routineTimer.reset();
        }
    
    space_14.stop();
    // the Routine "transfer_switch_instructions_p1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function transfer_switch_instructions_p2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'transfer_switch_instructions_p2' ---
    t = 0;
    transfer_switch_instructions_p2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    transfer_switch_instructions_p2MaxDurationReached = false;
    // update component parameters for each repeat
    space_16.keys = undefined;
    space_16.rt = undefined;
    _space_16_allKeys = [];
    psychoJS.experiment.addData('transfer_switch_instructions_p2.started', globalClock.getTime());
    transfer_switch_instructions_p2MaxDuration = null
    // keep track of which components have finished
    transfer_switch_instructions_p2Components = [];
    transfer_switch_instructions_p2Components.push(transfer_switch_instructions_text_2);
    transfer_switch_instructions_p2Components.push(space_15);
    transfer_switch_instructions_p2Components.push(space_16);
    
    for (const thisComponent of transfer_switch_instructions_p2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function transfer_switch_instructions_p2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'transfer_switch_instructions_p2' ---
    // get current time
    t = transfer_switch_instructions_p2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *transfer_switch_instructions_text_2* updates
    if (t >= 0.0 && transfer_switch_instructions_text_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      transfer_switch_instructions_text_2.tStart = t;  // (not accounting for frame time here)
      transfer_switch_instructions_text_2.frameNStart = frameN;  // exact frame index
      
      transfer_switch_instructions_text_2.setAutoDraw(true);
    }
    
    
    // *space_15* updates
    if (t >= 2 && space_15.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      space_15.tStart = t;  // (not accounting for frame time here)
      space_15.frameNStart = frameN;  // exact frame index
      
      space_15.setAutoDraw(true);
    }
    
    
    // *space_16* updates
    if (t >= 2 && space_16.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      space_16.tStart = t;  // (not accounting for frame time here)
      space_16.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { space_16.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { space_16.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { space_16.clearEvents(); });
    }
    
    if (space_16.status === PsychoJS.Status.STARTED) {
      let theseKeys = space_16.getKeys({keyList: ['space'], waitRelease: false});
      _space_16_allKeys = _space_16_allKeys.concat(theseKeys);
      if (_space_16_allKeys.length > 0) {
        space_16.keys = _space_16_allKeys[_space_16_allKeys.length - 1].name;  // just the last key pressed
        space_16.rt = _space_16_allKeys[_space_16_allKeys.length - 1].rt;
        space_16.duration = _space_16_allKeys[_space_16_allKeys.length - 1].duration;
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
    for (const thisComponent of transfer_switch_instructions_p2Components)
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

function transfer_switch_instructions_p2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'transfer_switch_instructions_p2' ---
    for (const thisComponent of transfer_switch_instructions_p2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('transfer_switch_instructions_p2.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(space_16.corr, level);
    }
    psychoJS.experiment.addData('space_16.keys', space_16.keys);
    if (typeof space_16.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('space_16.rt', space_16.rt);
        psychoJS.experiment.addData('space_16.duration', space_16.duration);
        routineTimer.reset();
        }
    
    space_16.stop();
    // the Routine "transfer_switch_instructions_p2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function transfer_switch_instructions_p3RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'transfer_switch_instructions_p3' ---
    t = 0;
    transfer_switch_instructions_p3Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    transfer_switch_instructions_p3MaxDurationReached = false;
    // update component parameters for each repeat
    space_18.keys = undefined;
    space_18.rt = undefined;
    _space_18_allKeys = [];
    psychoJS.experiment.addData('transfer_switch_instructions_p3.started', globalClock.getTime());
    transfer_switch_instructions_p3MaxDuration = null
    // keep track of which components have finished
    transfer_switch_instructions_p3Components = [];
    transfer_switch_instructions_p3Components.push(transfer_switch_instructions_text);
    transfer_switch_instructions_p3Components.push(space_17);
    transfer_switch_instructions_p3Components.push(space_18);
    
    for (const thisComponent of transfer_switch_instructions_p3Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function transfer_switch_instructions_p3RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'transfer_switch_instructions_p3' ---
    // get current time
    t = transfer_switch_instructions_p3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *transfer_switch_instructions_text* updates
    if (t >= 0.0 && transfer_switch_instructions_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      transfer_switch_instructions_text.tStart = t;  // (not accounting for frame time here)
      transfer_switch_instructions_text.frameNStart = frameN;  // exact frame index
      
      transfer_switch_instructions_text.setAutoDraw(true);
    }
    
    
    // *space_17* updates
    if (t >= 2 && space_17.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      space_17.tStart = t;  // (not accounting for frame time here)
      space_17.frameNStart = frameN;  // exact frame index
      
      space_17.setAutoDraw(true);
    }
    
    
    // *space_18* updates
    if (t >= 2 && space_18.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      space_18.tStart = t;  // (not accounting for frame time here)
      space_18.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { space_18.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { space_18.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { space_18.clearEvents(); });
    }
    
    if (space_18.status === PsychoJS.Status.STARTED) {
      let theseKeys = space_18.getKeys({keyList: ['space'], waitRelease: false});
      _space_18_allKeys = _space_18_allKeys.concat(theseKeys);
      if (_space_18_allKeys.length > 0) {
        space_18.keys = _space_18_allKeys[_space_18_allKeys.length - 1].name;  // just the last key pressed
        space_18.rt = _space_18_allKeys[_space_18_allKeys.length - 1].rt;
        space_18.duration = _space_18_allKeys[_space_18_allKeys.length - 1].duration;
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
    for (const thisComponent of transfer_switch_instructions_p3Components)
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

function transfer_switch_instructions_p3RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'transfer_switch_instructions_p3' ---
    for (const thisComponent of transfer_switch_instructions_p3Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('transfer_switch_instructions_p3.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(space_18.corr, level);
    }
    psychoJS.experiment.addData('space_18.keys', space_18.keys);
    if (typeof space_18.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('space_18.rt', space_18.rt);
        psychoJS.experiment.addData('space_18.duration', space_18.duration);
        routineTimer.reset();
        }
    
    space_18.stop();
    // the Routine "transfer_switch_instructions_p3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function transfer_switch_instructions_p4RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'transfer_switch_instructions_p4' ---
    t = 0;
    transfer_switch_instructions_p4Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    transfer_switch_instructions_p4MaxDurationReached = false;
    // update component parameters for each repeat
    space_to_begin_switch.keys = undefined;
    space_to_begin_switch.rt = undefined;
    _space_to_begin_switch_allKeys = [];
    psychoJS.experiment.addData('transfer_switch_instructions_p4.started', globalClock.getTime());
    transfer_switch_instructions_p4MaxDuration = null
    // keep track of which components have finished
    transfer_switch_instructions_p4Components = [];
    transfer_switch_instructions_p4Components.push(transfer_switch_instructions_text_3);
    transfer_switch_instructions_p4Components.push(space_to_begin_switch);
    
    for (const thisComponent of transfer_switch_instructions_p4Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function transfer_switch_instructions_p4RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'transfer_switch_instructions_p4' ---
    // get current time
    t = transfer_switch_instructions_p4Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *transfer_switch_instructions_text_3* updates
    if (t >= 0.0 && transfer_switch_instructions_text_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      transfer_switch_instructions_text_3.tStart = t;  // (not accounting for frame time here)
      transfer_switch_instructions_text_3.frameNStart = frameN;  // exact frame index
      
      transfer_switch_instructions_text_3.setAutoDraw(true);
    }
    
    
    // *space_to_begin_switch* updates
    if (t >= 0.0 && space_to_begin_switch.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      space_to_begin_switch.tStart = t;  // (not accounting for frame time here)
      space_to_begin_switch.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { space_to_begin_switch.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { space_to_begin_switch.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { space_to_begin_switch.clearEvents(); });
    }
    
    if (space_to_begin_switch.status === PsychoJS.Status.STARTED) {
      let theseKeys = space_to_begin_switch.getKeys({keyList: ['space'], waitRelease: false});
      _space_to_begin_switch_allKeys = _space_to_begin_switch_allKeys.concat(theseKeys);
      if (_space_to_begin_switch_allKeys.length > 0) {
        space_to_begin_switch.keys = _space_to_begin_switch_allKeys[_space_to_begin_switch_allKeys.length - 1].name;  // just the last key pressed
        space_to_begin_switch.rt = _space_to_begin_switch_allKeys[_space_to_begin_switch_allKeys.length - 1].rt;
        space_to_begin_switch.duration = _space_to_begin_switch_allKeys[_space_to_begin_switch_allKeys.length - 1].duration;
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
    for (const thisComponent of transfer_switch_instructions_p4Components)
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

function transfer_switch_instructions_p4RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'transfer_switch_instructions_p4' ---
    for (const thisComponent of transfer_switch_instructions_p4Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('transfer_switch_instructions_p4.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(space_to_begin_switch.corr, level);
    }
    psychoJS.experiment.addData('space_to_begin_switch.keys', space_to_begin_switch.keys);
    if (typeof space_to_begin_switch.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('space_to_begin_switch.rt', space_to_begin_switch.rt);
        psychoJS.experiment.addData('space_to_begin_switch.duration', space_to_begin_switch.duration);
        routineTimer.reset();
        }
    
    space_to_begin_switch.stop();
    // the Routine "transfer_switch_instructions_p4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function randomize_switch_trialsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'randomize_switch_trials' ---
    t = 0;
    randomize_switch_trialsClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    randomize_switch_trialsMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from randomize
    /* Syntax Error: Fix Python code */
    psychoJS.experiment.addData('randomize_switch_trials.started', globalClock.getTime());
    randomize_switch_trialsMaxDuration = null
    // keep track of which components have finished
    randomize_switch_trialsComponents = [];
    
    for (const thisComponent of randomize_switch_trialsComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function randomize_switch_trialsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'randomize_switch_trials' ---
    // get current time
    t = randomize_switch_trialsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of randomize_switch_trialsComponents)
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

function randomize_switch_trialsRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'randomize_switch_trials' ---
    for (const thisComponent of randomize_switch_trialsComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('randomize_switch_trials.stopped', globalClock.getTime());
    // the Routine "randomize_switch_trials" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function transfer_response_switchRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'transfer_response_switch' ---
    t = 0;
    transfer_response_switchClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    transfer_response_switchMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from get_turtle_params_transfer
    turtle_halfcircle_vertices = get_turtle_halfcircle_vertices(radius);
    turtle_wedge_vertices = get_turtle_wedge_vertices(angle);
    if ((trial_type === "standard")) {
        transfer_prompt_col = "#000000";
        transfer_prompt = "Is this turtle in Species F or Species J?\n\n F-Species F, J-Species J";
    } else {
        if ((trial_type === "switch")) {
            transfer_prompt_col = "#FF0000";
            transfer_prompt = "Is this turtle smaller or larger than the average turtle?\n\n F-smaller, J-larger";
        }
    }
    
    turtle_halfcircle_switch.setVertices(turtle_halfcircle_vertices);
    turtle_wedge_switch.setVertices(turtle_wedge_vertices);
    transfer_prompt_switch_trials.setColor(new util.Color(transfer_prompt_col));
    transfer_prompt_switch_trials.setText(transfer_prompt);
    key_resp_transfer_switch.keys = undefined;
    key_resp_transfer_switch.rt = undefined;
    _key_resp_transfer_switch_allKeys = [];
    psychoJS.experiment.addData('transfer_response_switch.started', globalClock.getTime());
    transfer_response_switchMaxDuration = null
    // keep track of which components have finished
    transfer_response_switchComponents = [];
    transfer_response_switchComponents.push(turtle_halfcircle_switch);
    transfer_response_switchComponents.push(turtle_wedge_switch);
    transfer_response_switchComponents.push(turtle_wedge_boundary_switch);
    transfer_response_switchComponents.push(transfer_prompt_switch_trials);
    transfer_response_switchComponents.push(key_resp_transfer_switch);
    
    for (const thisComponent of transfer_response_switchComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function transfer_response_switchRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'transfer_response_switch' ---
    // get current time
    t = transfer_response_switchClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *turtle_halfcircle_switch* updates
    if (t >= 0.0 && turtle_halfcircle_switch.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      turtle_halfcircle_switch.tStart = t;  // (not accounting for frame time here)
      turtle_halfcircle_switch.frameNStart = frameN;  // exact frame index
      
      turtle_halfcircle_switch.setAutoDraw(true);
    }
    
    
    // *turtle_wedge_switch* updates
    if (t >= 0.0 && turtle_wedge_switch.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      turtle_wedge_switch.tStart = t;  // (not accounting for frame time here)
      turtle_wedge_switch.frameNStart = frameN;  // exact frame index
      
      turtle_wedge_switch.setAutoDraw(true);
    }
    
    
    // *turtle_wedge_boundary_switch* updates
    if (t >= 0.0 && turtle_wedge_boundary_switch.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      turtle_wedge_boundary_switch.tStart = t;  // (not accounting for frame time here)
      turtle_wedge_boundary_switch.frameNStart = frameN;  // exact frame index
      
      turtle_wedge_boundary_switch.setAutoDraw(true);
    }
    
    
    // *transfer_prompt_switch_trials* updates
    if (t >= 0.0 && transfer_prompt_switch_trials.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      transfer_prompt_switch_trials.tStart = t;  // (not accounting for frame time here)
      transfer_prompt_switch_trials.frameNStart = frameN;  // exact frame index
      
      transfer_prompt_switch_trials.setAutoDraw(true);
    }
    
    
    // *key_resp_transfer_switch* updates
    if (t >= 0.0 && key_resp_transfer_switch.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_transfer_switch.tStart = t;  // (not accounting for frame time here)
      key_resp_transfer_switch.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_transfer_switch.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_transfer_switch.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_transfer_switch.clearEvents(); });
    }
    
    if (key_resp_transfer_switch.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_transfer_switch.getKeys({keyList: ['f', 'j'], waitRelease: false});
      _key_resp_transfer_switch_allKeys = _key_resp_transfer_switch_allKeys.concat(theseKeys);
      if (_key_resp_transfer_switch_allKeys.length > 0) {
        key_resp_transfer_switch.keys = _key_resp_transfer_switch_allKeys[_key_resp_transfer_switch_allKeys.length - 1].name;  // just the last key pressed
        key_resp_transfer_switch.rt = _key_resp_transfer_switch_allKeys[_key_resp_transfer_switch_allKeys.length - 1].rt;
        key_resp_transfer_switch.duration = _key_resp_transfer_switch_allKeys[_key_resp_transfer_switch_allKeys.length - 1].duration;
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
    for (const thisComponent of transfer_response_switchComponents)
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

function transfer_response_switchRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'transfer_response_switch' ---
    for (const thisComponent of transfer_response_switchComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('transfer_response_switch.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_transfer_switch.corr, level);
    }
    psychoJS.experiment.addData('key_resp_transfer_switch.keys', key_resp_transfer_switch.keys);
    if (typeof key_resp_transfer_switch.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_transfer_switch.rt', key_resp_transfer_switch.rt);
        psychoJS.experiment.addData('key_resp_transfer_switch.duration', key_resp_transfer_switch.duration);
        routineTimer.reset();
        }
    
    key_resp_transfer_switch.stop();
    // the Routine "transfer_response_switch" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function delete_switch_orderRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'delete_switch_order' ---
    t = 0;
    delete_switch_orderClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    delete_switch_orderMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from delete_switch_order_code
    os.remove("stim/stim_transfer_switch_random_tmp.csv");
    
    psychoJS.experiment.addData('delete_switch_order.started', globalClock.getTime());
    delete_switch_orderMaxDuration = null
    // keep track of which components have finished
    delete_switch_orderComponents = [];
    
    for (const thisComponent of delete_switch_orderComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function delete_switch_orderRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'delete_switch_order' ---
    // get current time
    t = delete_switch_orderClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of delete_switch_orderComponents)
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

function delete_switch_orderRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'delete_switch_order' ---
    for (const thisComponent of delete_switch_orderComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('delete_switch_order.stopped', globalClock.getTime());
    // the Routine "delete_switch_order" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function begin_debriefRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'begin_debrief' ---
    t = 0;
    begin_debriefClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    begin_debriefMaxDurationReached = false;
    // update component parameters for each repeat
    space_to_begin_debrief.keys = undefined;
    space_to_begin_debrief.rt = undefined;
    _space_to_begin_debrief_allKeys = [];
    psychoJS.experiment.addData('begin_debrief.started', globalClock.getTime());
    begin_debriefMaxDuration = null
    // keep track of which components have finished
    begin_debriefComponents = [];
    begin_debriefComponents.push(begin_debrief_text);
    begin_debriefComponents.push(space_20);
    begin_debriefComponents.push(space_to_begin_debrief);
    
    for (const thisComponent of begin_debriefComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function begin_debriefRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'begin_debrief' ---
    // get current time
    t = begin_debriefClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *begin_debrief_text* updates
    if (t >= 0.0 && begin_debrief_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      begin_debrief_text.tStart = t;  // (not accounting for frame time here)
      begin_debrief_text.frameNStart = frameN;  // exact frame index
      
      begin_debrief_text.setAutoDraw(true);
    }
    
    
    // *space_20* updates
    if (t >= 3 && space_20.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      space_20.tStart = t;  // (not accounting for frame time here)
      space_20.frameNStart = frameN;  // exact frame index
      
      space_20.setAutoDraw(true);
    }
    
    
    // *space_to_begin_debrief* updates
    if (t >= 3 && space_to_begin_debrief.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      space_to_begin_debrief.tStart = t;  // (not accounting for frame time here)
      space_to_begin_debrief.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { space_to_begin_debrief.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { space_to_begin_debrief.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { space_to_begin_debrief.clearEvents(); });
    }
    
    if (space_to_begin_debrief.status === PsychoJS.Status.STARTED) {
      let theseKeys = space_to_begin_debrief.getKeys({keyList: ['space'], waitRelease: false});
      _space_to_begin_debrief_allKeys = _space_to_begin_debrief_allKeys.concat(theseKeys);
      if (_space_to_begin_debrief_allKeys.length > 0) {
        space_to_begin_debrief.keys = _space_to_begin_debrief_allKeys[_space_to_begin_debrief_allKeys.length - 1].name;  // just the last key pressed
        space_to_begin_debrief.rt = _space_to_begin_debrief_allKeys[_space_to_begin_debrief_allKeys.length - 1].rt;
        space_to_begin_debrief.duration = _space_to_begin_debrief_allKeys[_space_to_begin_debrief_allKeys.length - 1].duration;
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
    for (const thisComponent of begin_debriefComponents)
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

function begin_debriefRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'begin_debrief' ---
    for (const thisComponent of begin_debriefComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('begin_debrief.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(space_to_begin_debrief.corr, level);
    }
    psychoJS.experiment.addData('space_to_begin_debrief.keys', space_to_begin_debrief.keys);
    if (typeof space_to_begin_debrief.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('space_to_begin_debrief.rt', space_to_begin_debrief.rt);
        psychoJS.experiment.addData('space_to_begin_debrief.duration', space_to_begin_debrief.duration);
        routineTimer.reset();
        }
    
    space_to_begin_debrief.stop();
    // the Routine "begin_debrief" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function debriefRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'debrief' ---
    t = 0;
    debriefClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    debriefMaxDurationReached = false;
    // update component parameters for each repeat
    space_to_end.keys = undefined;
    space_to_end.rt = undefined;
    _space_to_end_allKeys = [];
    psychoJS.experiment.addData('debrief.started', globalClock.getTime());
    debriefMaxDuration = null
    // keep track of which components have finished
    debriefComponents = [];
    debriefComponents.push(debrief_img);
    debriefComponents.push(space_to_end);
    
    for (const thisComponent of debriefComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function debriefRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'debrief' ---
    // get current time
    t = debriefClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *debrief_img* updates
    if (t >= 0.0 && debrief_img.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      debrief_img.tStart = t;  // (not accounting for frame time here)
      debrief_img.frameNStart = frameN;  // exact frame index
      
      debrief_img.setAutoDraw(true);
    }
    
    
    // *space_to_end* updates
    if (t >= 5 && space_to_end.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      space_to_end.tStart = t;  // (not accounting for frame time here)
      space_to_end.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { space_to_end.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { space_to_end.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { space_to_end.clearEvents(); });
    }
    
    if (space_to_end.status === PsychoJS.Status.STARTED) {
      let theseKeys = space_to_end.getKeys({keyList: ['space'], waitRelease: false});
      _space_to_end_allKeys = _space_to_end_allKeys.concat(theseKeys);
      if (_space_to_end_allKeys.length > 0) {
        space_to_end.keys = _space_to_end_allKeys[_space_to_end_allKeys.length - 1].name;  // just the last key pressed
        space_to_end.rt = _space_to_end_allKeys[_space_to_end_allKeys.length - 1].rt;
        space_to_end.duration = _space_to_end_allKeys[_space_to_end_allKeys.length - 1].duration;
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
    for (const thisComponent of debriefComponents)
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

function debriefRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'debrief' ---
    for (const thisComponent of debriefComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('debrief.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(space_to_end.corr, level);
    }
    psychoJS.experiment.addData('space_to_end.keys', space_to_end.keys);
    if (typeof space_to_end.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('space_to_end.rt', space_to_end.rt);
        psychoJS.experiment.addData('space_to_end.duration', space_to_end.duration);
        routineTimer.reset();
        }
    
    space_to_end.stop();
    // the Routine "debrief" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}

async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
