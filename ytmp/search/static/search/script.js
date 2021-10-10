
function load(){


        document.getElementById('demo').onclick = function() {videoURL()};
        function videoURL() {
            var videourl = document.getElementById('demo').getAttribute('title');

            console.log("Downloading..........");
            console.log(videourl);
        

        };
};
window.onload = load;


