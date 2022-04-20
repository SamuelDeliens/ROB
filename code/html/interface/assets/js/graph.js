//-----------------------------------------------------------------
//------------------------ GRAPHIQUE ------------------------------
//-----------------------------------------------------------------

const pHlabel = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14];
const graph = {"firstChart": 0, "secondChart": 0};

var graphVar = {
    0: [], //date
    1: [], //pH
    2: [], //oxy
    3: [], //conduct
    4: [0,0,0,0,0,0,0,0,0,0,0,0,0,0], //nb
};

//Fonction globale
function setGraph() {
    setVar();
    setNbVar(1);
    defineGraphe("firstChart", graphVar[0], graphVar[1], {type:"line",option:{scales:{x:{title :{display:false}}}} });
    defineGraphe("secondChart", pHlabel, graphVar[4], {type: 'bar', options: {scales:{y:{beginAtZero:true}}} });
}


//---------------Fonction initialisation-----------------

function initVar() {
    graphVar = {
        0: [], //date
        1: [], //pH
        2: [], //oxy
        3: [], //conduct
        4: [0,0,0,0,0,0,0,0,0,0,0,0,0,0], //nb
    };
}

//---------------Fonction set-------------------------

function setVar() {
    for (var i=0; i<document.capteurValues.length; i++) {
        for(var j=0; j<4; j++) {
            graphVar[j][i] = document.capteurValues[i][j+1];
        }
    }
}

//Definie le nb de fois que l'on a la variable choisis (nb de pH 1, 2)
function setNbVar(type) {
    for(var i=0; i<graphVar[type].length; i++) {
        graphVar[4][Math.round(graphVar[type][i])]++;
    }
}

//---------------Fonction graphe-------------------------

function changeChart(idChart, idName, idButton) {
    initVar();
    setVar();
    var button = document.getElementById(idButton);
    initChart(idChart, idName);
        value = choosenValue(button.value);
    if (idName == 0) {
        defineGraphe(idChart, graphVar[0], graphVar[value], {type:"line",option:{scales:{x:{title :{display:false}}}}});
    } else {
        graphVar[4] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0];
        setNbVar(value);
            defineGraphe(idChart, pHlabel, graphVar[4], {type: 'bar', options: {scales:{y:{beginAtZero:true}}} });
    }
}

function initChart(idChart, idName) {
    graph.firstChart = null;
    canvas = document.createElement("canvas");
    canvas.id=idChart;
    document.getElementsByClassName("graphique")[idName].replaceChild(canvas, document.getElementById(idChart));
}

function choosenValue(value) {
    switch (value) {
        case 'pH':
            return 1;
            break;
        case 'oxygen':
            return 2;
            break;
        case 'conductivity':
            return 3;
            break;
    }
}

function defineGraphe(id, label, valeur, config) {
    const data = {
        labels:label,
        datasets: [{
            label: 'graph',
            backgroundColor: 'rgb(248, 68, 68)',
            borderColor: 'rgb(248, 68, 68)',
            data: valeur,
        }]
       };
       
    config.data = data;   

    graph[id] = new Chart(
        document.getElementById(id),
        config
    );
}