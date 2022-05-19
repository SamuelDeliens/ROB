function startCalibration() {
    document.isLaunch = true;
    displayCalibration(document.isLaunch);
    calibrate("CALIBRATE", document.pinSensor,  document.stepCALIB);
}

function endCalibration() {
    document.stepCALIB = !document.stepCALIB;
    document.isLaunch = false;
    displayCalibration(document.isLaunch);
}

function  displayCalibration(isLaunch){
    var buttonCalibrate = document.getElementById("calibrateButton");
    var iconCalibrate = document.getElementById("iconCalibrate");
    var endCalibrate = document.getElementById("endCalibration");
    var indicCalibButton = document.getElementById("indicCalibButton");
    var indicationLabel = [["7.0 pH", "4.0 pH"], ["14.22 mS", "12.80 mS"], ["5°C", "25°C"]];

    if (isLaunch) {
        iconCalibrate.style.display = "";
        buttonCalibrate.classList.add("disabled");
        endCalibrate.classList.add("disabled");
    } else {
        iconCalibrate.style.display = "none";
        buttonCalibrate.classList.remove("disabled");
    }
    if(document.stepCALIB) {
        endCalibrate.classList.remove("disabled");
    }

    indicCalibButton.innerHTML = "Please put the sensor in the "+indicationLabel[document.pinSensor][document.stepCALIB ? 1 : 0]+" solution";
}