


function hello(url,name){
    console.log(name);
    console.log(url);

    var data = {name : url};
    $.ajax({
        url: 'ajax/foo',
        data : {
          'url': url,
          'name':name
        },
        success: function(data){
          console.log("everything checks out!!")
        }
      });

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
