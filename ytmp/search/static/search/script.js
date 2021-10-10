
function load(){

    for(var counter =0; counter > 10; counter++){

        document.getElementById('demo').onclick = function() {videoURL()};
        function videoURL() {
            var videourl = document.getElementById('demo').getAttribute('title');

            console.log("Downloading..........");
            console.log(videourl);
        

        };
    };
};
window.onload = load;


