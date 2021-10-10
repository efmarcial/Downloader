
window.onload = function() {
    function helloWorld(){
        console.log('Hello world from Java')
    };
    
    helloWorld();

    document.getElementById("demo").onclick = function() {HelloWorld()};
    function HelloWorld() {

        console.log("Downloading..........");
        var videourl = getElementById('video').href;
        console.log(videourl);
    };

    
}