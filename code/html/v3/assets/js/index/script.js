//-----------------------------------------------------------------
//--------------------------- GLOBALE -----------------------------
//-----------------------------------------------------------------

//Verif changement (donnees + graph)
function checkChange() {
    if(!document.lastCaptureValues || document.newLastCapteurValues.id != document.lastCaptureValues.id) {
        console.log("change");
        actuDonnees();
        setTabRT();
        changeTab();
    }
}

function checkValue() {
    if(document.capteurValues) {
        console.log("init");
        initTab();
        setTab(0, 10, false);
        setTabRT();
    }
}

//--------------------------- init --------------------------------

function init() {
    checkPrivileges();
    role_display("RealTime");
    listener("RealTime");
    getValue();
}

function getLoop() {
    console.log("recherche");
    getLastValue();
    setTimeout(function() {getLoop()}, 500);
}    

//-----------------------------------------------------------------
//--------------------------- SCRIPT ------------------------------
//-----------------------------------------------------------------

init();
setTimeout(function() {getLoop()}, 1000);
