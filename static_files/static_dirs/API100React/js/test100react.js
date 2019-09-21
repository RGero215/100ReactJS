// test100react
var stopwatchInterval = 0;      // The interval for our loop.

var stopwatchClock = $(".container.stopwatch").find(".clock"),
    stopwatchDigits = stopwatchClock.find('span');

var username = stopwatchClock.find('.username')
var noOuts = stopwatchClock.find('.noOuts')
var inn = stopwatchClock.find('.innNo')
var emptyBases = stopwatchClock.find('.empty')
var run = stopwatchClock.find('.homeScore')
var awayScore = stopwatchClock.find('.awayScore')
var fastball = 10
var changeup = 100
var pitch = [fastball, changeup]
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
var manyTries = 0


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
        if(sign === 0){
            enable = false
        } 
    } else if (stopwatchClock.hasClass('inactive') && Number(localStorage.stopwatchRunningTime) > 0){
        resetStopwatch()
    }
    else{
        pauseStopwatch();
        stats[stopwatchDigits.text()] ? stats[stopwatchDigits.text()] += 1 : stats[stopwatchDigits.text()] = 1
        console.log(stats)
        if(manyTries >= 2){
            sign = 0
            // items = [0,1]
            // sign = Math.floor(Math.random()*items.length)
        }
        if(!enable){
            off = stopwatchDigits.text() - 100
            user['digit'] = stopwatchDigits.text()
            user['off'] = off
            displayModal(user)
            hideInputs()
        }
        create_stat(stats)
        outs(Number(stopwatchDigits.text()))
        runners(Number(stopwatchDigits.text()))
        
    }
});

function startStopwatch(){
    // Prevent multiple intervals going on at the same time.
    clearInterval(stopwatchInterval);
    manyTries += 1
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
            inningCounter = 1
            inn.text(`${inningCounter}`)
            emptyBases.attr('src', '/static/API100React/img/empty.png')
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
function displayModal(user) {
    if(Number(user['off']) >= 20){
        document.querySelector('.title').append('Did you fall asleep?')
    } else if (Number(user['off']) < 0){
        document.querySelector('.title').append('Too soon...')
    } else if (Number(user['off']) === 0) {
        document.querySelector('.title').append('Right on time')
    } else {
        document.querySelector('.title').append('Not bad')
    }
    // create_stat()
    document.querySelector('.bg-modal').style.display = 'flex';
    document.querySelector('.off').prepend(user['digit'])
    document.querySelector('.off').append(user['off'])
    
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
    // submit stats
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

function hideInputs(){
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
}

$(function() {
    // Handler for .ready() called.
    resetStopwatch()
    manyTries = 0
    sign = 1
});