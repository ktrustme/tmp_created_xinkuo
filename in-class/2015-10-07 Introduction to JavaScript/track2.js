var main = function(){
    var interval


    var timeDisplay = document.getElementById("timeElapsed");
    timeDisplay.innerText = "0";
    var currentTime = 0; 

    var update = function(){
       currentTime = currentTime + 1;          
       timeDisplay.innerText = currentTime + "";
    }

    var startButton = document.getElementById("startBtn");
    var start = function() {
        if(!interval)
            interval = setInterval(update,1000);
    }

    startButton.onclick=start;

    var stopButton = document.getElementById("stopBtn");
    var stop = function() {
        clearInterval(interval);
        interval = null;
    }
    stopButton.onclick = stop;

    var resetButton = document.getElementById("resetBtn");
    var reset = function() {
        currentTime = 0;
        clearInterval(interval);
        timeDisplay.innerText = currentTime + "";
        interval = null;
    }
    resetButton.onclick = reset;



    //alert("finished");
}

document.addEventListener("DOMContentLoaded", main)
