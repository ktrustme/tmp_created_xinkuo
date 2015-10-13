var req;

function getFortune() {

    req = new XMLHttpRequest();
    req.onreadystatechange = handleResponse;
    req.open("GET", "http://garrod.isri.cmu.edu/webapps/fortune");
    req.send(); 
}

function handleResponse(){
    if(req.readyState != 4 || req.status != 200){
        return;     
    }
    var content = document.getElementById("content");
    var fortune = JSON.parse(req.responseText);
    content.innerHTML=fortune["fortune"];
}

