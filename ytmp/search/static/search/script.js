

  
        var div = document.getElementById("myDIV");
        var nodelist = div.getElementsByClassName("btn btn-sm btn-outline-secondary");
        const url = nodelist;
        var i;
        for(i=0; i < nodelist.length; i++) {
          console.log(nodelist[i]);

          nodelist[i].onclick = function(){VideoURL()};
          function VideoURL(){

            var vdurl = url.getAttribute("title");


              console.log("clicked");
              console.log(vdurl);

          };

        };

    

   

    



