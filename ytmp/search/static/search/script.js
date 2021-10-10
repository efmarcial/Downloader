
window.onload = function() {
    function helloWorld(){
        console.log('Hello world from Java')
    };
    
    helloWorld();

    document.getElementById("demo").onclick = function() {HelloWorld()};


function HelloWorld() {

    document.getElementById("demo").innerHTML = "You CLicked Me";
    console.log("Downloading..........");
};
    
}