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
        setTab(false, 0, 10);
        setTabRT();
    }
}

//--------------------------- init --------------------------------

function init() {
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
