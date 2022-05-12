//-----------------------------------------------------------------
//------------------------ Listener -------------------------------
//-----------------------------------------------------------------

function listener(page) {
    var buttonLove = document.getElementById("love");
    if(buttonLove) {buttonLove.addEventListener("click", function() {controlerDiv()}); }

    var buttonCalibrateType = document.getElementsByClassName("calibrationType");
    if(buttonCalibrateType) {
        let i = 0;
        for(let buttonX of buttonCalibrateType) {
            buttonX.value = i;
            buttonX.addEventListener("click", function() {controlerPythonCALIB(buttonX.value)});
        }
    }

    var buttonCalibrate = document.getElementById("calibrateButton");
    if(buttonCalibrate) {buttonCalibrate.addEventListener("click", function() {startCalibration()}); }

    if (page == "RealTime") {     
        var buttonLaunch = document.getElementById("GETRT");
        buttonLaunch.addEventListener("click", function() {controlerPythonRT()});

        var buttonLaunchOnce = document.getElementById("GETDATA");
        buttonLaunchOnce.addEventListener("click", function() {launchPy("GETDATA")});

        var buttonRefresh = document.getElementById("Refresh");
        buttonRefresh.addEventListener("click", function() {refreshTab(0, 10)});
    } 
    else if (page == "Table") {
        var showButton = document.getElementById("showNumber");
        showButton.addEventListener("change", function() {changeNumberShow()});

        var posButton = document.getElementsByClassName("posButton");
        for(let posButtonX of posButton) {
            posButtonX.addEventListener("click", function() {changePos(posButtonX)});
        }

        var nameFilterButton = document.getElementById("filterName");
        nameFilterButton.addEventListener("change", function() {changeNameFilter()});

        var sheachButton = document.getElementById("filterValue");
        sheachButton.addEventListener("keypress", function() {filterValue()});
    } 
    else if (page == "stat") {
        var firstChart = document.getElementById("firstChartO");
        firstChart.addEventListener("change", function() { changeChart("firstChart", 0, "firstChartO"); });
    
        var secondChart = document.getElementById("secondChartO");
        secondChart.addEventListener("change", function() { changeChart("secondChart", 1, "secondChartO"); });
    }
}

//-----------------Page------------------

function controlerDiv() {
    var div1 = document.getElementById("BDD");
    var div2 = document.getElementById("loveDiv");
    if (div1.style.display == "none") {
        div1.style.display = "block";
        div2.style.display = "none";
    } else {
        div1.style.display = "none";
        div2.style.display = "block";
    }
}

function controlerPythonRT() {
    button = document.getElementById("GETRT");
    if(button.innerHTML == "GETRT") {
        button.innerHTML = "stop"
        launchPy("GETRT", "launch");
    } else {
        button.innerHTML = "GETRT";
        launchPy("GETRT", "stop");
    }
}

function controlerPythonCALIB(pinSensor) {
    document.pinSensor = pinSensor;
    if(document.stepCALIB == undefined) {document.stepCALIB = 0}
    if(document.isLaunch == undefined) {document.isLaunch = false}
    displayCalibration(document.stepCALIB);
}