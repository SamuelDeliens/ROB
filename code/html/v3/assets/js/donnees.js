//-----------------------------------------------------------------
//------------------------ TABLEAU -------------------------------
//-----------------------------------------------------------------

// ----------------------- Define Tableau ----------------------

function initTab() {
    var tbody = document.getElementById("capteurDonnee");
    length = tbody.children.length;
    for(i=0; i<length; i++) {
        tbody.removeChild(tbody.children[0]);
    }
}

function setTabRT() {
    tabRT = document.getElementsByClassName("tabRT");
    for(i=0; i<tabRT.length; i++) {
        tabRT[i].innerHTML = document.lastCaptureValues[i+1];
    }
}

function setTab(offset, show) {
    var tbody = document.getElementById("capteurDonnee");
    for(i=offset; i<(offset+show); i++) {
        if (document.capteurValues[i]) {
            let tr = document.createElement('tr');
<<<<<<< HEAD
            let icon = document.createElement('i');
            icon.classList.add("fas");
            icon.classList.add("fa-times");
            tr.appendChild(icon);
            tr.value=i;
            for (var j=0; j<=5;j++) {
=======
            tr.value=i;
            for (var j=0; j<=4;j++) {
>>>>>>> 60a210487000a1330e36e2510a31655e59970c25
                let td = document.createElement('td');
                td.innerHTML = document.capteurValues[i][j];
                tr.appendChild(td);
            }
            tbody.append(tr);
        }
    }
}

function refreshTab(offset, show) {
    console.log("refresh");
    initTab();
    setTab(offset, show);
}

//-----------------------------------------------------------------
//------------------------ Loop Données ---------------------------
//-----------------------------------------------------------------

function actuDonnees() {
    document.lastCaptureValues = document.newLastCapteurValues;
}

function changeTab() {
    var tbody = document.getElementById("capteurDonnee");
    tbody.removeChild(tbody.lastChild);
    let tr = document.createElement('tr');
    for (var j=0; j<=4;j++) {
        let td = document.createElement('td');
        td.innerHTML = document.lastCaptureValues[j];
        tr.appendChild(td);
    }
    tbody.prepend(tr);
}