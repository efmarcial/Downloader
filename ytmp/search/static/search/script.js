

    document.getElementById("demo").onclick = function() {videoURL()};
    function videoURL() {
        var videourl = document.getElementsByTagName('a')[0].getAttribute('title');

        console.log("Downloading..........");
        console.log(videourl);
    };

    
