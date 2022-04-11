//-----------------------------------------------------------------
//--------------------------- GLOBALE -----------------------------
//-----------------------------------------------------------------

//Verif changement (donnees + graph)
function checkChange() {
    if(document.newCapteurValues) {
        if(document.newCapteurValues.length != document.capteurValues.length) {
            console.log("change");
            actuDonnees();
            //actuGraph();
        }
    } else {
        console.log(document.capteurValues);
        defDonnees();
        setGraph();
    }
}

//--------------------------- init --------------------------------

function init() {
    listener();
    getValue();
}

function getLoop() {
    console.log("recherche");
    getValue();
    setTimeout(function() {getLoop()}, 5000);
}    

//-----------------------------------------------------------------
//--------------------------- SCRIPT ------------------------------
//-----------------------------------------------------------------

init();
getLoop();