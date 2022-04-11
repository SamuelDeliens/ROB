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
    httpRequest.open('GET', 'requete.php');
    httpRequest.send();
    httpRequest.onload = function() {
        if(httpRequest.readyState == 4 && httpRequest.status == 200) {
            document.capteurValues = httpRequest.response;
            checkChange();
        }
        
    }
}