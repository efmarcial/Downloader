

    var demo =document.getElementById('demo');
    demo.onclick = function(){videoURL()};
    function videoURL(){
        console.log("Clicked");
    };

        var div = document.getElementById("myDIV");
        var nodelist = div.getElementsByClassName("btn btn-sm btn-outline-secondary");

        var i;
        for(i=0; i < nodelist.length; i++) {
          console.log(nodelist[i]);

          nodelist[i].onclick = function(){VideoURL()};
          function VideoURL(){
              console.log("clicked");
          };


        };

    

   

    



