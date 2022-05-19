//-----------------------------------------------------------------
//------------------------ Role Display ---------------------------
//-----------------------------------------------------------------

function role_display(page) {
    //GLOBAL
    if (!document.right) {
        var buttonCalibrateType = document.getElementsByClassName("calibrationType");
        if(buttonCalibrateType) {
            for(let buttonX of buttonCalibrateType) {
                buttonX.style.display = "none";
            }
        }
    
        var buttonCalibrate = document.getElementById("calibrateButton");
        if(buttonCalibrate) {buttonCalibrate.style.display = "none"}

        var buttonAccount_param = document.getElementsByClassName("account_param");
        if(buttonAccount_param) {
            for(let i = 0; i<buttonAccount_param.length-1; i++) {
                buttonAccount_param[i].style.display = "none";
            }
        }
    } else {
        var buttonAccount_param = document.getElementsByClassName("account_param");
        if(buttonAccount_param) {buttonAccount_param[buttonAccount_param.length-1].style.display = "none"}
        //---------_DECONECTION À FAIRE-----------
    }

    //PAGE
    if (page == "RealTime" && !document.right) {
        var buttonLaunch = document.getElementById("GETRT");
        buttonLaunch.style.display = "none";

        var buttonLaunchOnce = document.getElementById("GETDATA");
        buttonLaunchOnce.style.display = "none";

    } else if (page == "Table" && !document.right) {


    } else if (page == "Stat" && !document.right) {

    } else if (page == "Camera" && !document.right) {
        var buttonCameraServo = document.getElementById("camera_controler");
        buttonCameraServo.style.display = "none";
    }
}