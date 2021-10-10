
window.onload = function() {
    function helloWorld(){
        console.log('Hello world from Java')
    };
    
    helloWorld();

    document.getElementById("demo").onclick = function() {HelloWorld()};
    document.getElementsByName('video').onclick = function() {VideoURL()};
    function HelloWorld() {

        console.log("Downloading..........");
        
    };

    function VideoURL(){
        var value = document.getElementById('video').href;
        console.log(value); 
    }
    
}