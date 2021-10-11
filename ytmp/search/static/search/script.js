

  
        const div = document.getElementById("myDIV");
        var nodelist = div.getElementsByClassName("btn btn-sm btn-outline-secondary");
        
      
        var i;
        for(i=0; i < nodelist.length; i++) {
          console.log(nodelist[i]);
            var url = nodelist[i].getAttribute('title');

          nodelist[i].onclick = function(){VideoURL()};
          function VideoURL(){



              console.log("clicked");
            console.log(url);
          };

        };

    

   

    



