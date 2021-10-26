


function hello(url,name){
    console.log(name);
    console.log(url);

    var data = {name : url};
    var dicString = JSON.stringify(data);
    var fs = require('fs');
    fs.writeFile("data.json", dicString);


};



/*
stream = ytdl(url)

proc = new ffmpeg({source:stream})
proc.setFfmpegPath('/Applications/ffmpeg')
proc.saveToFile(mp3, (stdout, stderr)->
            return console.log stderr if err?
            return console.log 'done'
        )



*/
