

  
        var div = document.getElementById("myDIV");
        var nodelist = div.getElementsByClassName("btn btn-sm btn-outline-secondary");
        var url = nodelist;
        var i;
        for(i=0; i < nodelist.length; i++) {
          console.log(nodelist[i]);

          nodelist[i].onclick = function(){VideoURL()};
          function VideoURL(){
              var vidurl = url.getAttribute("title");
              console.log("clicked");
              console.log(vidurl);
          };

        };

    

   

    



