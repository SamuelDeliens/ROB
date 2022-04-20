//-----------------------------------------------------------------
//------------------------ Listener -------------------------------
//-----------------------------------------------------------------

function listener() {
    var buttonSize = document.getElementById("graphInputSize");
    buttonSize.addEventListener("click", function() {showGraph()});
    
    var buttonLove = document.getElementById("love");
    buttonLove.addEventListener("click", function() {controlerDiv()});
    
    var buttonLaunch = document.getElementById("launchPy");
    buttonLaunch.addEventListener("click", function() {launchPy()});
    
    var firstChart = document.getElementById("firstChartO");
    firstChart.addEventListener("change", function() { changeChart("firstChart", 0, "firstChartO"); });
    
    var secondChart = document.getElementById("secondChartO");
    secondChart.addEventListener("change", function() { changeChart("secondChart", 1, "secondChartO"); });
}

//-----------------Graph------------------

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

//-----------------Page------------------

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