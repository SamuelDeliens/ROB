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
    httpRequest.open('GET', 'assets/php/refresh.php');
    httpRequest.send();
    httpRequest.onload = function() {
        if(httpRequest.readyState == 4 && httpRequest.status == 200) {
            document.capteurValues = httpRequest.response;
            checkChange();
        }
        
    }
}

function launchPy() {
    httpRequest2 = new XMLHttpRequest();
    if (!httpRequest2) {
        alert('erreur Requette');
    }
    httpRequest2.responseType = "json";
    httpRequest2.open('GET', 'assets/php/launchPy.php');
    httpRequest2.send();
    httpRequest2.onload = function() {
        if(httpRequest2.readyState == 4 && httpRequest2.status == 200) {
            sortie = httpRequest2.response;
            console.log(sortie);
        }
        
    }
}