//-----------------------------------------------------------------
//--------------------------- GLOBALE -----------------------------
//-----------------------------------------------------------------

//Verif changement (donnees + graph)
function checkValue() {
    if(document.capteurValues) {
        console.log("init");
        setTab(document.tableOffset, document.tableShowNb, true);
        setDisplayTable();
    }
}

//--------------------------- init --------------------------------

function init() {
    checkPrivileges();
    role_display("Table");
    listener("Table");
    initVarTable();
    getValue();
}

//-----------------------------------------------------------------
//--------------------------- SCRIPT ------------------------------
//-----------------------------------------------------------------

init();
