//-----------------------------------------------------------------
//------------------------ TABLEAU -------------------------------
//-----------------------------------------------------------------

// ----------------------- Define Tableau ----------------------

function setTab() {
    var tbody = document.getElementById("capteurDonnee");
    for(row of document.capteurValues) {
        let tr = document.createElement('tr');
        for (var i=0; i<=4;i++) {
            let td = document.createElement('td');
            td.innerHTML = row[i];
            tr.appendChild(td);
        }
        tbody.prepend(tr);
    }
}

//-----------------------------------------------------------------
//------------------------ Loop Données ---------------------------
//-----------------------------------------------------------------

function defDonnees() {
    getChange();
    setTab();
}

function actuDonnees() {
    getChange();
    setChange();
}

function getChange() {
    document.newCapteurValues = document.capteurValues;
    nbPoint = document.newCapteurValues.length;
}

function setChange() {
    var tbody = document.getElementById("capteurDonnee");
    let tr = document.createElement('tr');
    row = document.newCapteurValues[document.newCapteurValues.length-1];
    console.log(row);
    for (var i=0; i<=4;i++) {
        let td = document.createElement('td');
        td.innerHTML = row[i];
        tr.appendChild(td);
    }
    tbody.prepend(tr);
}
