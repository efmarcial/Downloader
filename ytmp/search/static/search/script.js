

function helloWorld(){
    console.log('Hello world from Java')
};

helloWorld();

document.getElementById("demo").onclick = function() {helloWorld()};


function helloWorld() {

    document.getElementById("demo").innerHTML = "You CLicked Me";
    console.log("Downloading..........");
};