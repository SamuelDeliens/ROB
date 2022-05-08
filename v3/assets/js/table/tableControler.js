//-----------------------------------------------------------------
//------------------------ Display Table --------------------------
//-----------------------------------------------------------------

function updateTable() {
    refreshTab(document.tableOffset, document.tableShowNb);
    setDisplayTable();
}

function setDisplayTable() {
    setTabInfo();
    setPosControler();
}

// ----------------------- Parameter Table ------------------------

function initVarTable() {
    document.tableShowNb = 10;
    document.tablePosition = 1;
    document.tableOffset = 0;
    document.maxPos = 3;
    document.filterName = "date";
}

function setVarTable(show, pos) {
    document.tableShowNb = show;
    document.tablePosition = pos;
    document.tableOffset =  (document.tablePosition-1) * document.tableShowNb;
    document.maxPos = Math.ceil(document.capteurValues.length / document.tableShowNb);
}

function foundNewPos(newShowNb) {
    startPos = document.getElementById("capteurDonnee").children[0].value;
    i=0;
    notFound = false;
    while (notFound == false) {
        if(startPos >= i*newShowNb && startPos < (i+1)*newShowNb) {
            notFound = true;
        }
        i++;
    }
    return i;
}

// ----------------------- Controler Table ------------------------

function changeNumberShow() {
    newShowNb = parseInt(document.getElementById("showNumber").value);
    setVarTable(newShowNb, foundNewPos(newShowNb));
    document.maxPos = Math.ceil(document.capteurValues.length / document.tableShowNb);
    updateTable();
}

function changePos(posButton) {
    document.tablePosition = posButton.value;
    document.tableOffset =  (document.tablePosition-1) * document.tableShowNb;
    updateTable();
}


// ----------------------- Controler Filter ------------------------

function changeNameFilter() {
    nameFilterButton = document.getElementById("filterName");
    document.filterName = nameFilterButton.value;
    filterValue();
}

function filterValue() {
    console.log("filtering");
    sheachValue = document.getElementById("filterValue").value.toString().toLowerCase();
    if(sheachValue != "") {
        document.capteurValues = [];
        for(i=0; i<document.backupValues.length; i++) {
            if(document.backupValues[i][document.filterName].toString().toLowerCase().includes(sheachValue)) {
                document.capteurValues.push(document.backupValues[i]);
            }
        }
    } else {
        document.capteurValues = document.backupValues;
    }
    setVarTable(document.tableShowNb, 1);
    updateTable();
}

// ----------------------- Controler Data -------------------------

//Définie les parametres valeur des boutons controler de la position
function setPosControler() {
    posButton = document.getElementsByClassName("posButton");
    posButton[0].value = 1;
    for(i=1; i<posButton.length-1; i++) {
        posButton[i].value = document.tablePosition + i - 2;
        displayPosButton(posButton[i]);
    }
    posButton[4].value = Math.ceil(document.capteurValues.length / document.tableShowNb);    
}

// ----------------------- Display Table ------------------------

function setTabInfo() {
    if(document.getElementById("capteurDonnee").children[0]) {
        firstID = document.getElementById("capteurDonnee").children[0].firstChild.innerHTML;
        lastID = document.getElementById("capteurDonnee").lastChild.firstChild.innerHTML;
        document.getElementById("dataTable_info").innerHTML = "Showing "+ lastID +" to "+ firstID +" of "+document.capteurValues.length;       
    } else {
        document.getElementById("dataTable_info").innerHTML = "No data found";       
    }
}

function displayPosButton(button) {
    button.innerHTML =  button.value;
    if(button.value < 1 || button.value > Math.ceil(document.capteurValues.length / document.tableShowNb)) {
        button.parentNode.style.display = "none";
    } else {
        button.parentNode.style.display = "";
    }
}
