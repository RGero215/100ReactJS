// pomodoro100react
var stopwatchInterval = 0;      // The interval for our loop.

var stopwatchClock = $(".container.stopwatch").find(".clock"),
    stopwatchDigits = stopwatchClock.find('span');
var userId = stopwatchClock.find('.userId')
var challengeId = stopwatchClock.find('.challengeId')
var username = stopwatchClock.find('.username')
var noOuts = stopwatchClock.find('.noOuts')
var inn = stopwatchClock.find('.innNo')
var emptyBases = stopwatchClock.find('.empty')
var run = stopwatchClock.find('.homeScore')
var awayScore = stopwatchClock.find('.awayScore')
var fastball = 10
var curveBall = 40
var pitch = [fastball, curveBall]
var sign = 1
var enable = true
var off = 0
var stats = {}
var user = {}
var lob = 0
var result = ''
var newInning = false
var risk = 0
var safe = 0
var grandSlam = 0

// Pomodoro variables
let pomodoroCountDown = 0; // variable to set/clear intervals
let pomodoroSeconds = 1500; // seconds left on the clock 
let workTime = 25;
let breakTime = 5;
let isBreak = true;
let isPaused = true;
const status = document.querySelector("#status");
const timerDisplay = document.querySelector(".timerDisplay");
const startBtn = document.querySelector("#start-btn");
const resetBtn = document.querySelector("#reset");
const workMin = document.querySelector("#work-min");
const breakMin = document.querySelector("#break-min");
const alarm = document.createElement('audio'); 
alarm.setAttribute("src", "https://www.soundjay.com/misc/sounds/bell-ringing-05.mp3");


/* EVENT LISTENERS FOR START AND RESET BUTTONS */
startBtn.addEventListener('click', () => {
    clearInterval(pomodoroCountDown);
    if (isPaused) {
      startCountdown();
      startBtn.textContent = "Pause";
      isPaused = false;
    } else {
      remaining = pomodoroSeconds;
      startBtn.textContent = "Cont.";
      isPaused = true;
    }
})

resetBtn.addEventListener('click', () => {
    clearInterval(pomodoroCountDown);
    pomodoroSeconds = workMin.textContent * 60;
    pomodoroCountDown = 0;
    remaining = 0;
    isPaused = true;
    isBreak = true;
    // calculate total work
    workTotal = totalWorkTime()
    // calculate total break
    breakTotal = totalBreakTime()
    status.textContent = "Keep Working";
    startBtn.textContent = "Start";
    displayTimeLeft(pomodoroSeconds);
    $("input[name='work_duration']").attr('value', parseInt($(workMin).text()))
    $("input[name='break_duration']").attr('value', parseInt($(breakMin).text()))
    $("input[name='workTotal']").attr('value',workTotal)
    $("input[name='breakTotal']").attr('value',breakTotal)
    document.querySelector('.settings').style.display = 'none';
})

/* MAIN FUNCTIONS - TIMER, START COUNTDOWN, & UPDATE DISPLAY */
isBreakPast30 = false;
roundsCounter = 0
function timer() {
    pomodoroSeconds --;
    playFor30sec = breakTime - 1;

    if($(timerDisplay).text() === String(playFor30sec) + ':30' && isBreakPast30){
        document.querySelector('.pomodoro-modal').style.display = 'flex';
        isBreakPast30 = false;
        pauseStopwatch()
    }

    if (pomodoroSeconds < 0) {
      clearInterval(pomodoroCountDown);
      alarm.currentTime = 0;
      alarm.play();
  
      if (isBreak) {
        roundsCounter += 1
        $("input[name='rounds']").attr('value', roundsCounter)
        if(roundsCounter == 4){
            document.querySelector('.pomodoro-form').style.display = 'flex';
            document.querySelector('#pomodoro').style.display = 'none';
            startBtn.click()
            displayModal()
            hideInputs()
            // Donate if didn't Win
            if($("input[name='result']").val() === 'L'){
                console.log(`Thanks for your $${$("input[name='donation']").val()}` )
            }

        }
        document.querySelector('.pomodoro-modal').style.display = 'none';
        pomodoroSeconds = breakMin.textContent * 60;
        status.textContent = "Take a Break!";
        isBreak = false;
        isBreakPast30 = true;
      } else {
        pomodoroSeconds = workMin.textContent * 60;
        status.textContent = "Keep Working";
        isBreak = true;
      }
      pomodoroCountDown = setInterval(timer, 1000);
      return;
    }
    displayTimeLeft(pomodoroSeconds); // Keep updating display
}
  
function startCountdown() {
    if (remaining != 0) {
        pomodoroSeconds = remaining;
    } else {
        pomodoroSeconds = workMin.textContent * 60;
        status.textContent = "Keep Working";
    }
    pomodoroCountDown = setInterval(timer, 1000);
}
  
function displayTimeLeft(pomodoroSeconds) {
    const minutes = Math.floor(pomodoroSeconds / 60);
    const remainderSeconds = pomodoroSeconds % 60;
    timerDisplay.textContent = `${minutes}:${remainderSeconds < 10 ? '0' : ''}${remainderSeconds}`;
}
  
/* UPDATE WORK AND BREAK TIMES */
const workPlus = document.querySelector("#work-plus");
const workMinus = document.querySelector("#work-minus");
const breakPlus = document.querySelector("#break-plus");
const breakMinus = document.querySelector("#break-minus");
  
workPlus.addEventListener('click', () => {
    let x = parseInt(workMin.textContent);          
    if (x < 60) {
      workMin.textContent = x+5;
    }                       
})
  
workMinus.addEventListener('click', () => {
    let x = parseInt(workMin.textContent);          
    if (x > 5) {
      workMin.textContent = x-5;
    }                       
})
  
breakPlus.addEventListener('click', () => {
    let x = parseInt(breakMin.textContent);          
    if (x < 60) {
      breakMin.textContent = x+5;
    }                       
})
  
breakMinus.addEventListener('click', () => {
    let x = parseInt(breakMin.textContent);          
    if (x > 5) {
      breakMin.textContent = x-5;
    }                       
}) 

// Checks if the previous session was ended while the stopwatch was running.
// If so start it again with according time.
if(Number(localStorage.stopwatchBeginingTimestamp) && Number(localStorage.stopwatchRunningTime)){

    var runningTime = Number(localStorage.stopwatchRunningTime) + new Date().getTime() - Number(localStorage.stopwatchBeginingTimestamp);

    localStorage.stopwatchRunningTime = runningTime;

    startStopwatch();
}

// If there is any running time form previous session, write it on the clock.
// If there isn't initialise to 0.
if(localStorage.stopwatchRunningTime){
    stopwatchDigits.text(returnFormattedToMilliseconds(Number(localStorage.stopwatchRunningTime)));
}
else{
    localStorage.stopwatchRunningTime = 0;
}

$('#stopwatch-btn-start').on('click',function(){
    if(stopwatchClock.hasClass('inactive')){
        startStopwatch()
    }
});

$('#stopwatch-btn-pause').on('click',function(){
    pauseStopwatch();
});

$('#stopwatch-btn-reset').on('click',function(){
    resetStopwatch();
});

// Pressing the clock will pause/unpause the stopwatch.
stopwatchClock.on('click',function(){
    if(stopwatchClock.hasClass('inactive') && Number(localStorage.stopwatchRunningTime) === 0){
        if(enable){
            startStopwatch()
        } 
        // Game Finish
        if(inningCounter > 9){
            enable = false
        } 
    } else if (stopwatchClock.hasClass('inactive') && Number(localStorage.stopwatchRunningTime) > 0){
        resetStopwatch()
    }
    else{
        pauseStopwatch();
        stats[stopwatchDigits.text()] ? stats[stopwatchDigits.text()] += 1 : stats[stopwatchDigits.text()] = 1
        console.log(stats)
        
        // Different Pitch
        items = [0,1]
        sign = Math.floor(Math.random()*items.length)

        outs(Number(stopwatchDigits.text()))
        runners(Number(stopwatchDigits.text()))
        create_stat(stats)
        
    }
});

function startStopwatch(){
    // Prevent multiple intervals going on at the same time.
    clearInterval(stopwatchInterval);

    var startTimestamp = new Date().getTime(),
        runningTime = 0;

    localStorage.stopwatchBeginingTimestamp = startTimestamp;

    // The app remembers for how long the previous session was running.
    if(Number(localStorage.stopwatchRunningTime)){
        runningTime = Number(localStorage.stopwatchRunningTime);
    }
    else{
        localStorage.stopwatchRunningTime = 1;
    }

    // Every 100ms recalculate the running time, the formula is:
    // time = now - when you last started the clock + the previous running time

    stopwatchInterval = setInterval(function () {
        var stopwatchTime = (new Date().getTime() - startTimestamp + runningTime);

        stopwatchDigits.text(returnFormattedToMilliseconds(stopwatchTime));
    }, 100);

    stopwatchClock.removeClass('inactive');
}

function pauseStopwatch(){
    // Stop the interval.
    clearInterval(stopwatchInterval);

    if(Number(localStorage.stopwatchBeginingTimestamp)){

        // On pause recalculate the running time.
        // new running time = previous running time + now - the last time we started the clock.
        var runningTime = Number(localStorage.stopwatchRunningTime) + new Date().getTime() - Number(localStorage.stopwatchBeginingTimestamp);

        localStorage.stopwatchBeginingTimestamp = 0;
        localStorage.stopwatchRunningTime = runningTime;

        stopwatchClock.addClass('inactive');
    }
}

// Reset everything.
function resetStopwatch(){
    clearInterval(stopwatchInterval);

    stopwatchDigits.text(returnFormattedToMilliseconds(0));
    localStorage.stopwatchBeginingTimestamp = 0;
    localStorage.stopwatchRunningTime = 0;

    stopwatchClock.addClass('inactive');
}


function returnFormattedToMilliseconds(time){
    var seconds = Math.floor((time/pitch[sign])),

    seconds = seconds < 0 ? '0' + seconds : seconds;
    return seconds ;
}

// Outs
var inningCounter = 1
function outs(runningTime){
    if((noOuts.attr('src') === "/static/API100React/img/noOuts.png") && (runningTime < 97 || runningTime > 100)){
        noOuts.attr('src', "/static/API100React/img/oneOut.png")
        newInning = false
    } else if ((noOuts.attr('src') === "/static/API100React/img/oneOut.png") && (runningTime < 97 || runningTime > 100)) {
        noOuts.attr('src', "/static/API100React/img/twoOuts.png")
        newInning = false    
    } else if ((noOuts.attr('src') === "/static/API100React/img/twoOuts.png") && (runningTime < 97 || runningTime > 100)) {
        noOuts.attr('src', "/static/API100React/img/noOuts.png")
        inningCounter += 1
        newInning = true
        leftOnBases()
        if(inningCounter < 10){
            inn.text(`${inningCounter}`)
            emptyBases.attr('src', '/static/API100React/img/empty.png')
        } else {
            enable = false
            // off = stopwatchDigits.text() - 100
            user['digit'] = stopwatchDigits.text()
            user['off'] = off
            $("input[name='final']").prop( "checked", true )
            // displayModal()
            hideInputs()
            inningCounter = 1
            inn.text(`${inningCounter}`)
            emptyBases.attr('src', '/static/API100React/img/empty.png')
            resetStopwatch()
        }
    }
}

function runners(runningTime) {
    // Single with empty bases
    if(emptyBases.attr('src') === '/static/API100React/img/empty.png' && runningTime === 97)  {
        emptyBases.attr('src', '/static/API100React/img/manOnFirst.png')
    // Double with empty bases
    } else if (emptyBases.attr('src') === '/static/API100React/img/empty.png' && runningTime === 98) {
        emptyBases.attr('src', '/static/API100React/img/manOnSecond.png')
    // Triple with empty bases
    } else if (emptyBases.attr('src') === '/static/API100React/img/empty.png' && runningTime === 99) {
        emptyBases.attr('src', '/static/API100React/img/manOnThird.png')
    // HR with empty bases
    }  else if (emptyBases.attr('src') === '/static/API100React/img/empty.png' && runningTime === 100) {
        emptyBases.attr('src', '/static/API100React/img/empty.png')
        runs(1)
    // Single with Man on First
    } else if (emptyBases.attr('src') === '/static/API100React/img/manOnFirst.png' && runningTime === 97) {
        emptyBases.attr('src', '/static/API100React/img/firstAndSecond.png')
    // Single with Man on Second
    } else if (emptyBases.attr('src') === '/static/API100React/img/manOnSecond.png' && runningTime === 97) {
        emptyBases.attr('src', '/static/API100React/img/firstAndThird.png')
    // Single with Man on Third
    } else if (emptyBases.attr('src') === '/static/API100React/img/manOnThird.png' && runningTime === 97) {
        emptyBases.attr('src', '/static/API100React/img/manOnFirst.png')
        runs(1)
    // Single with First and Second
    } else if (emptyBases.attr('src') === '/static/API100React/img/firstAndSecond.png' && runningTime === 97) {
        emptyBases.attr('src', '/static/API100React/img/basesLoaded.png')
    // Single with First and Third
    } else if (emptyBases.attr('src') === '/static/API100React/img/firstAndThird.png' && runningTime === 97) {
        emptyBases.attr('src', '/static/API100React/img/firstAndSecond.png')
        runs(1)
    // Single with Second and Third
    } else if (emptyBases.attr('src') === '/static/API100React/img/secondAndThird.png' && runningTime === 97) {
        emptyBases.attr('src', '/static/API100React/img/firstAndThird.png')
        runs(1)
    // Single with Bases Loaded
    } else if (emptyBases.attr('src') === '/static/API100React/img/basesLoaded.png' && runningTime === 97) {
        emptyBases.attr('src', '/static/API100React/img/basesLoaded.png')
        runs(1)
    // Double with Man on First
    }else if (emptyBases.attr('src') === '/static/API100React/img/manOnFirst.png' && runningTime === 98) {
        emptyBases.attr('src', '/static/API100React/img/secondAndThird.png')
    // Double with Man on Second
    } else if (emptyBases.attr('src') === '/static/API100React/img/manOnSecond.png' && runningTime === 98) {
        emptyBases.attr('src', '/static/API100React/img/manOnSecond.png')
        runs(1)
    // Double with Man on Third
    } else if (emptyBases.attr('src') === '/static/API100React/img/manOnThird.png' && runningTime === 98) {
        emptyBases.attr('src', '/static/API100React/img/manOnSecond.png')
        runs(1)
    // Double with First and Second 
    } else if (emptyBases.attr('src') === '/static/API100React/img/firstAndSecond.png' && runningTime === 98) {
        emptyBases.attr('src', '/static/API100React/img/secondAndThird.png')
        runs(1)
    // Double with First and Third 
    } else if (emptyBases.attr('src') === '/static/API100React/img/firstAndThird.png' && runningTime === 98) {
        emptyBases.attr('src', '/static/API100React/img/secondAndThird.png')
        runs(1)
    // Double with Second and Third
    } else if (emptyBases.attr('src') === '/static/API100React/img/secondAndThird.png' && runningTime === 98) {
        emptyBases.attr('src', '/static/API100React/img/manOnSecond.png')
        runs(2)
    // Double with Bases Loaded
    } else if (emptyBases.attr('src') === '/static/API100React/img/basesLoaded.png' && runningTime === 98) {
        emptyBases.attr('src', '/static/API100React/img/secondAndThird.png')
        runs(2)
    // Triple with Man on First
    } else if (emptyBases.attr('src') === '/static/API100React/img/manOnFirst.png' && runningTime === 99) {
        emptyBases.attr('src', '/static/API100React/img/manOnThird.png')
        runs(1)
    // Triple with Man on Second
    } else if (emptyBases.attr('src') === '/static/API100React/img/manOnSecond.png' && runningTime === 99) {
        emptyBases.attr('src', '/static/API100React/img/manOnThird.png')
        runs(1)
    // Triple with Man on Third
    } else if (emptyBases.attr('src') === '/static/API100React/img/manOnThird.png' && runningTime === 99) {
        emptyBases.attr('src', '/static/API100React/img/manOnThird.png')
        runs(1)
    // Triple with First and Second
    } else if (emptyBases.attr('src') === '/static/API100React/img/firstAndSecond.png' && runningTime === 99) {
        emptyBases.attr('src', '/static/API100React/img/manOnThird.png')
        runs(2)
    // Triple with First and Third
    } else if (emptyBases.attr('src') === '/static/API100React/img/firstAndThird.png' && runningTime === 99) {
        emptyBases.attr('src', '/static/API100React/img/manOnThird.png')
        runs(2)
    // Triple with Second and Third
    } else if (emptyBases.attr('src') === '/static/API100React/img/secondAndThird.png' && runningTime === 99) {
        emptyBases.attr('src', '/static/API100React/img/manOnThird.png')
        runs(2)
    // Triple with Bases Loaded
    } else if (emptyBases.attr('src') === '/static/API100React/img/basesLoaded.png' && runningTime === 99) {
        emptyBases.attr('src', '/static/API100React/img/manOnThird.png')
        runs(3)
    // HR with Man on First
    } else if (emptyBases.attr('src') === '/static/API100React/img/manOnFirst.png' && runningTime === 100) {
        emptyBases.attr('src', '/static/API100React/img/empty.png')
        runs(2)
    // HR with Man on Second
    } else if (emptyBases.attr('src') === '/static/API100React/img/manOnSecond.png' && runningTime === 100) {
        emptyBases.attr('src', '/static/API100React/img/empty.png')
        runs(2)
    // HR with Man on Third
    } else if (emptyBases.attr('src') === '/static/API100React/img/manOnThird.png' && runningTime === 100) {
        emptyBases.attr('src', '/static/API100React/img/empty.png')
        runs(2)
    // HR with First and Second
    }  else if (emptyBases.attr('src') === '/static/API100React/img/firstAndSecond.png' && runningTime === 100) {
        emptyBases.attr('src', '/static/API100React/img/empty.png')
        runs(3)
    // HR with First and Third
    }else if (emptyBases.attr('src') === '/static/API100React/img/firstAndThird.png' && runningTime === 100) {
        emptyBases.attr('src', '/static/API100React/img/empty.png')
        runs(3)
    // HR with Second and Third
    } else if (emptyBases.attr('src') === '/static/API100React/img/secondAndThird.png' && runningTime === 100) {
        emptyBases.attr('src', '/static/API100React/img/empty.png')
        runs(3)
    // HR with Bases Loaded GRANSLAM
    } else if (emptyBases.attr('src') === '/static/API100React/img/basesLoaded.png' && runningTime === 100) {
        emptyBases.attr('src', '/static/API100React/img/empty.png')
        runs(4)
        grandSlam += 1
    }  
}

function leftOnBases() {
    // Out with Man on First
    if(emptyBases.attr('src') === '/static/API100React/img/manOnFirst.png' && newInning) {
        lob += 1
    // Out with Man on Second
    } else if (emptyBases.attr('src') === '/static/API100React/img/manOnSecond.png' && newInning ) {
        lob += 1
    // Out with Man on Third
    } else if (emptyBases.attr('src') === '/static/API100React/img/manOnThird.png' && newInning ) {
        lob += 1
    // Out with First and Second
    } else if (emptyBases.attr('src') === '/static/API100React/img/firstAndSecond.png' && newInning ) {
        lob += 2
    // Out with First and Third
    } else if (emptyBases.attr('src') === '/static/API100React/img/firstAndThird.png' && newInning ) {
        lob += 2
    // Out with Second and Third
    } else if (emptyBases.attr('src') === '/static/API100React/img/secondAndThird.png' && newInning) {
        lob += 2
    // Out with Bases Loaded
    } else if (emptyBases.attr('src') === '/static/API100React/img/basesLoaded.png' && newInning ) {
        lob += 3
    }

    console.log('LOB: ', lob)
}

var run_counter = 0
function runs(score){
    run_counter += score
    if(inningCounter < 10){
        run.text(`${run_counter}`)
    } else {
        run_counter = 0
    }
    
}

// display modal
function displayModal() {
    console.log("Working Modal")
    var final = result === 'W' ? 'You won' : 'You loss'
    if(inningCounter > 9){
        document.querySelector('.title').append('GAME OVER')
    }
    document.querySelector('.result').append(`To compleate your donation of $${$("input[name='donation']").val()} please enter your credit card information.`)
    $('.legend').text('Save Pomodoro')
    $('.save').text('Save')
    $("input[name='final']").prop( "checked", true )
}


function create_stat(stats) {
    var atBats = 0
    var hits = 0
    var avg = 0
    var slg = 0
    var points = 0
    result = Number(run.text()) > Number(awayScore.text()) ? 'W' : 'L'
    // Calculate at bats
    for(atBat in stats){
        atBats += stats[atBat]
    }
    // Calculate hits
    hits = hitsCal(stats)
    // Calculate avg
    avg = Math.floor((hits / atBats) * 1000)
    // Calculate slg
    slg = slgCal(stats, atBats)
    // Calculate points
    points = pointsCal(stats, avg, slg, lob)
    // Calculate risk
    risk = riskCal(stats)
    // Calculate safe
    safe = safeCal(stats)
    // Calculate off
    off = offCal(stats)
    // submit stats
    $("#id_four option[value='']").attr('value', challengeId.val()).attr('selected', 'selected')
    $("#id_player option[value='']").attr('value', userId.val()).attr('selected', 'selected')
    $("input[name='singles']").attr('value',stats[97])
    $("input[name='doubles']").attr('value',stats[98])
    $("input[name='triples']").attr('value',stats[99])
    $("input[name='homeRuns']").attr('value',stats[100])
    $("input[name='atBats']").attr('value', atBats)
    $("input[name='hits']").attr('value',hits)
    $("input[name='avg']").attr('value',avg)
    $("input[name='slg']").attr('value',slg)
    $("input[name='lob']").attr('value',lob)
    $("input[name='rbi']").attr('value',Number(run.text()))
    $("input[name='runs']").attr('value',Number(run.text()))
    $("input[name='home']").attr('value',Number(run.text()))
    $("input[name='away']").attr('value',Number(awayScore.text()))
    $("input[name='result']").attr('value',result)
    $("input[name='points']").attr('value',points)
    $("input[name='grandSlam']").attr('value', grandSlam)
    $("input[name='risk']").attr('value',risk)
    $("input[name='safe']").attr('value',safe)
    $("input[name='off']").attr('value', off)
    $("input[name='stop']").attr('value',Number(stopwatchDigits.text()))
    firstPointsAndFirstHomeCal(points)
    
}

function hitsCal(stats) {
    var hits = 0
    for(key in stats){
        if(parseInt(key) === 97 || parseInt(key) === 98 || parseInt(key) === 99 || parseInt(key) === 100){
           hits += stats[key] 
        }
    }
    return hits
}

function slgCal(stats, atBats) {
    var slg = 0
    var singles = 0
    var doubles = 0
    var triples = 0
    var hr = 0
    for(key in stats){
        if(parseInt(key) === 97){
           singles += stats[key] 
        } else if (parseInt(key) === 98){
            doubles += stats[key]
        } else if (parseInt(key) === 99){
            triples += stats[key]
        } else if (parseInt(key) === 100) {
            hr += stats[key]
        }
    }
    slg = (singles + (2 * doubles) + (3 * triples) + (4 * hr)) / atBats * 1000
    return Math.floor(slg)
}

function pointsCal(stats, avg, slg, lob) {
    var points = 0
    var singles = 0
    var doubles = 0
    var triples = 0
    var hr = 0
    for(key in stats){
        if(parseInt(key) === 97){
           singles += stats[key] 
        } else if (parseInt(key) === 98){
            doubles += stats[key]
        } else if (parseInt(key) === 99){
            triples += stats[key]
        } else if (parseInt(key) === 100) {
            hr += stats[key]
        }
    }
    
    points = ((10 * singles) + (20 * doubles) + (30 * triples) + (40 * hr) + avg + slg - (10 * lob)) / 7
    return Math.floor(points)
}

function riskCal(stats){
    var risk = 0
    for(key in stats){
        if(parseInt(key) === 97){
           risk += 1 
        } else if (parseInt(key) === 98){
            risk += 2
        } else if (parseInt(key) === 99){
            risk += 3
        } else if (parseInt(key) === 100) {
            risk += 4
        } else if (parseInt(key) === 101) {
            risk += 3
        } else if (parseInt(key) === 102) {
            risk += 2
        } else if (parseInt(key) === 103) {
            risk += 1
        }
    }
    return risk
}

function safeCal(stats){
    var safe = 0
    for(key in stats){
        if(parseInt(key) === 100){
           safe += 1 
        } else if (parseInt(key) === 99){
            safe += 2
        } else if (parseInt(key) === 98){
            safe += 3
        } else if (parseInt(key) === 97) {
            safe += 4
        } else if (parseInt(key) === 96) {
            safe += 3
        } else if (parseInt(key) === 95) {
            safe += 2
        } else if (parseInt(key) === 94) {
            safe += 1
        }
    }
    return safe
}

function offCal(stats){
    var off = 0
    for(key in stats){
        off += parseInt(key)
    }
    off = off / Object.keys(stats).length
    return Math.floor(off) - 100
}

$(function() {
    // Handler for .ready() called.
    resetStopwatch()
    $('.pomodoro-form').hide()
});

function hideInputs(){
    $("#div_id_four").hide()
    $("#div_id_player").hide()
    $("#div_id_singles").hide()
    $("#div_id_doubles").hide()
    $("#div_id_triples").hide()
    $("#div_id_homeRuns").hide()
    $("#div_id_atBats").hide()
    $("#div_id_hits").hide()
    $("#div_id_avg").hide()
    $("#div_id_slg").hide()
    $("#div_id_lob").hide()
    $("#div_id_rbi").hide()
    $("#div_id_runs").hide()
    $("#div_id_home").hide()
    $("#div_id_away").hide()
    $("#div_id_result").hide()
    $("#div_id_points").hide()
    $("#div_id_createdAt").hide()
    $("#div_id_grandSlam").hide()
    $("#div_id_risk").hide()
    $("#div_id_safe").hide()
    $("#div_id_off").hide()
    $("#div_id_stop").hide()
    $('#div_id_level').hide()
    $('#div_id_final').hide()
    $("#div_id_task_one").hide()
    $("#div_id_task_two").hide()
    $("#div_id_task_three").hide()
    $("#div_id_task_four").hide()
    $("#div_id_work_duration").hide()
    $("#div_id_break_duration").hide()
    $("#div_id_donation").hide()
    $("#div_id_workTotal").hide()
    $("#div_id_breakTotal").hide()
    $("#div_id_firstHome").hide()
    $("#div_id_firstPoints").hide()
    $("#div_id_title").hide()
}

function totalWorkTime(){
    var decimal = parseInt($(workMin).text()) * 4
    var min = decimal % 60
    var hours = Math.floor(decimal / 60)
    return `${hours}:${min}` 
}

function totalBreakTime(){
    var decimal = parseInt($(breakMin).text()) * 4
    var min = decimal % 60
    var hours = Math.floor(decimal / 60)
    return `${hours}:${min}` 
}

function firstPointsAndFirstHomeCal(points) {
    if(inningCounter === 5){
        $("input[name='firstHome']").attr('value',Number(run.text()))
        $("input[name='firstPoints']").attr('value',points)
    }
}