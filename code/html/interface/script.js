var capteurValues = 0;

function init() {
    capteurValues = document.capteurValues;
    setTab();
    listener();
}

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



function checkChange() {
    if(capteurValues.length != document.capteurValues.length) {
        console.log("change");
        getChange();
        setChange();
    }
}

function getChange() {
    capteurValues = document.capteurValues;
    nbPoint = capteurValues.length;
}

function setChange() {
    var tbody = document.getElementById("capteurDonnee");
    let tr = document.createElement('tr');
    row = capteurValues[capteurValues.length-1];
    console.log(row);
    for (var i=0; i<=4;i++) {
        let td = document.createElement('td');
        td.innerHTML = row[i];
        tr.appendChild(td);
    }
    tbody.prepend(tr);
}


function listener() {
    var buttonSize = document.getElementById("graphInputSize");
    buttonSize.addEventListener("click", function() {showGraph()});
    
    var buttonLove = document.getElementById("love");
    buttonLove.addEventListener("click", function() {controlerDiv()});
}

function showGraph() {
    var graphPanel = document.getElementById("divGraph");
    var tableau = document.getElementById("tableau");
    var bouton = document.getElementById("graphInputSize");
    //-----------------------Cache----------------------------
    if (graphPanel.style.height != "0px") {
        graphPanel.animate([
            { height: '330px' },
            { height: '0px' },
        ], {
            duration: 300,
            iteration: 1
        });
        graphPanel.style.height = "0px";
        tableau.animate([
            { height: '40%' },
            { height: '70%' },
        ], {
            duration: 300,
            iteration: 1
        });
        tableau.style.height = "70%";
        bouton.innerHTML = "^"
    //-----------------------Affiche----------------------------
    } else {
        graphPanel.animate([
            { height: '0px' },
            { height: '330px' },
        ], {
            duration: 300,
            iteration: 1
        });
    graphPanel.style.height = "330px";
    tableau.animate([
        { height: '70%' },
        { height: '40%' },
    ], {
        duration: 300,
        iteration: 1
    });
    tableau.style.height = "40%";
    bouton.textContent = "v"
    }
}

function controlerDiv() {
    var div1 = document.getElementById("BDD");
    var div2 = document.getElementById("loveDiv");
    if (div1.style.display == "none") {
        div1.style.display = "block";
        div2.style.display = "none";
    } else {
        div1.style.display = "none";
        div2.style.display = "block";
    }
}


window.onload = function() {
  var div1 = document.getElementById("BDD");
  var div2 = document.getElementById("loveDiv");

  div1.style.display = "block";
  div2.style.display = "none";
}