        // get all the class "btn..." in the DOM
        const div = document.getElementById("myDIV");
        var nodelist = div.getElementsByClassName("btn btn-sm btn-outline-secondary");
        
        var urls = [];
        var ids = [];

        var ademo = document.getElementById('demo');

        for(var x=0; x < 9; x++){
            demoNum = 'demo'+x.toString();
            ademo.setAttribute('id', demoNum);
        };

        // loop the lenght of all the classes "btn...." to get all <a>.
        
        for(var i=0; i < nodelist.length; i++) {
           
        console.log(nodelist[i]);
        
        
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
        ids = ids.filter(item => item);

        //log the arrays in the console
        console.log(urls);
        console.log(ids);
        
    

   

    



