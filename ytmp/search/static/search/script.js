        // get all the class "btn..." in the DOM
        const div = document.getElementById("myDIV");
        var nodelist = div.getElementsByClassName("btn btn-sm btn-outline-secondary");
        
        var urls = [];
        var ids = [];
        // loop the lenght of all the classes "btn...." to get all <a>.
        var i;
        for(i=0; i < nodelist.length; i++) {

         // console.log(nodelist[i]);
            // onClick Download btn to get url and pass it to js
          
          nodelist[i].onclick = function(){VideoURL()};
          var tagId = document.getElementById('demo');
          function VideoURL(){

            console.log("clicked");
          console.log(tagId);
        };

          var x = i + 1
          var demoNum = 'demo'+x.toString();
          nodelist[i].setAttribute('id', demoNum);

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
        
    

   

    



