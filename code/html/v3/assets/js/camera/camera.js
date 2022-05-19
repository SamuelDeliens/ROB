function setControlerCamera() {
    //CHANGE ANGLE DIRECT
    var buttonsCamera = document.getElementsByClassName("buttonCameraServoDirect");
    buttonsCamera[0].value = 180;
    buttonsCamera[1].value = 90;
    buttonsCamera[2].value = 0;
    //CHANGE ANGLE STEP BY STEP --> SLOW
    var buttonsCamera2 = document.getElementsByClassName("buttonCameraServoSlow");
    buttonsCamera2[0].value = 1;
    buttonsCamera2[1].value = -1;
}

function controlCameraServo(type, angle) {
    launchPy("SERVO", type, angle);
}