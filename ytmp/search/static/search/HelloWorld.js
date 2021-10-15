

import ytdl from "ytdl-core";
import ffmpeg from "ffmpeg";
import { stderr } from "process";

function hello(url,name){
    var url = url;
    ytdl(url);
    var name = name;
    console.log(name);
    console.log(url);
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

function convert(url){
    var stream = ytdl(url);

    var proc = new ffmpeg({source:stream});
proc.setFfmpegPath('/Applications/ffmpeg');
proc.saveToFile(mp3, (stdout, stderr)
    );
        

}