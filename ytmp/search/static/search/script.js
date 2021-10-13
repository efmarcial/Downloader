        // get all the class "btn..." in the DOM
        const div = document.getElementById("myDIV");
        var nodelist = div.getElementsByClassName("btn btn-sm btn-outline-secondary");
        
        var urls = [];
        var ids = [];
        var demoNum = 'demo';
        var ademo = document.getElementById('id');
        var atag = document.getElementById('video');


        // loop the lenght of all the classes "btn...." to get all <a>.
        
        for(var i=0; i < nodelist.length; i++) {
           
        console.log(nodelist[i]);
        var x = i + 1;
        
        if(ademo !==atag){
            
            ademo = ademo.setAttribute(demoNum);
            demoNum = demoNum+x.toString();
        }; 
         // console.log(nodelist[i]);
            // onClick Download btn to get url and pass it to js
          
          nodelist[i].onclick = function(){VideoURL()};
          function VideoURL(){
            console.log("clicked");
          console.log(ademo);
        };
          urls.push(nodelist[i][
            'title'
        ]);
        // append all id values in ids list
        ids.push(nodelist[i]['id']);

     
             
        };
        // Remove the empty " " index from the urls array
        urls = urls.filter(item => item);

        //log the arrays in the console
        console.log(urls);
        console.log(ids);
        
    

   

    



