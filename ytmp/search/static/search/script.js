

    document.getElementsId('demo').onclick = function() {videoURL()};
    function videoURL() {
        var id = document.getElementsId("demo");
        var videourl = document.getElementById('demo').getAttribute('title');

        console.log("Downloading..........");
        console.log(videourl);
    };

    
