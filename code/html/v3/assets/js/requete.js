//-----------------------------------------------------------------
//------------------------ REQUETE BDD ----------------------------
//-----------------------------------------------------------------

var httpRequest;

function getValue() {
    httpRequest = new XMLHttpRequest();
    if (!httpRequest) {
        alert('erreur Requette');
    }
    httpRequest.responseType = "json";
    httpRequest.open('GET', 'assets/php/getData.php');
    httpRequest.send();
    httpRequest.onload = function() {
        if(httpRequest.readyState == 4 && httpRequest.status == 200) {
            console.log(httpRequest.response);
            //document.capteurValues = httpRequest.response;
            //document.lastCaptureValues = document.capteurValues[0];
            document.backupValues = [];
            for (i=1; i<=200; i++) {
                document.backupValues.unshift({0:i, 1:"13/12/07 18:19:11", 2:7.1, 3: 1.2, 4: 3.1, 5: null, id:i, date:"13/12/07 18:19:11", pH:7.1, oxygen: 1.2, conductivity: 3.1, turbidifty: null});
            }
            document.lastCaptureValues = document.backupValues[0];
            document.capteurValues = document.backupValues;
            checkValue();
        }
        
    }
}

function getLastValue() {
    httpRequest2 = new XMLHttpRequest();
    if (!httpRequest2) {
        alert('erreur Requette');
    }
    httpRequest2.responseType = "json";
    httpRequest2.open('GET', 'assets/php/getLastData.php');
    httpRequest2.send();
    httpRequest2.onload = function() {
        if(httpRequest2.readyState == 4 && httpRequest2.status == 200) {
            //document.newLastCapteurValues = httpRequest2.response[0];
            document.newLastCapteurValues = {0:"201", 1:"13/12/07 18:19:11", 2:7.1, 3: 1.2, 4: 3.1, 5: null, id:"1", date:"13/12/07 18:19:11", pH:7.1, oxygen: 1.2, conductivity: 3.1, turbidifty: null};
            checkChange();
        }
        
    }
}

function launchPy(type, action) {
    httpRequest3 = new XMLHttpRequest();
    if (!httpRequest3) {
        alert('erreur Requette');
    }
    httpRequest3.responseType = "json";
    httpRequest3.open('POST', 'assets/php/launchPy.php');
    httpRequest3.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    httpRequest3.send("type="+type+"&action="+action);
    httpRequest3.onload = function() {
        if(httpRequest3.readyState == 4 && httpRequest3.status == 200) {
            sortie = httpRequest3.response;
            console.log(sortie);
        }
        
    }
}
