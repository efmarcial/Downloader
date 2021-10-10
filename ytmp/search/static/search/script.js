
window.onload = function() {
    
    document.getElementById("demo").onclick = function() {videoURL()};
    function videoURL() {
        
        var videourl = document.getElementById('video').getAttribute('href');

        console.log("Downloading..........");
        console.log(videourl);
    };

    
}