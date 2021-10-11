

  
        var div = document.getElementById("myDIV");
        var nodelist = div.getElementsByClassName("btn btn-sm btn-outline-secondary");

        var i;
        for(i=0; i < nodelist.length; i++) {
          console.log(nodelist[i]);

          nodelist[i].onclick = function(){VideoURL()};
          function VideoURL(){
              var url = nodelist[i].getAttribute("title");
              console.log("clicked");
              console.log(url);
          };
          document.getElementById("myAnchor").getAttribute("target");

        };

    

   

    



