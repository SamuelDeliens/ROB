function startCalibration() {
    document.isLaunch = true;
    displayCalibration(document.isLaunch);
    console.log(document.pinSensor)
    console.log(document.stepCALIB)
    calibrate("CALIBRATE", document.pinSensor,  document.stepCALIB ? 1 : 0);
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
    var indicationLabel = [["7.0 pH", "4.0 pH"], ["5°C", "25°C"], ["1413 uS", "12.88 mS"]];

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
    console.log(document.pinSensor);
    console.log(indicationLabel[document.pinSensor][document.stepCALIB ? 1 : 0]);
    indicCalibButton.innerHTML = "Please put the sensor in the "+indicationLabel[document.pinSensor][document.stepCALIB ? 1 : 0]+" solution";
}
