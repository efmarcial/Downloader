
        const div = document.getElementById("myDIV");
        var nodelist = div.getElementsByClassName("btn btn-sm btn-outline-secondary");
        
        var urls = [];

        var i;
        for(i=0; i < nodelist.length; i++) {

         // console.log(nodelist[i]);

          var tagId = document.getElementById("demo");
          nodelist[i].onclick = function(){VideoURL()};
          urls.push(nodelist[i]['id','href','title']);

          function VideoURL(){

              console.log("clicked");
            console.log(tagId);
          };
          
        };

        console.log(urls)
        
    

   

    



