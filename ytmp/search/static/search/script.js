
function load(){

    document.getElementById('divBtn').onclick = function() {videoURL()};
    function videoURL() {
        var id = document.getElementById("demo");
        var videourl = document.getElementById('demo').getAttribute('title');

        console.log("Downloading..........");
        console.log(videourl);


    };
};
window.onload = load;


