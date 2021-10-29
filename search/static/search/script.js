
       
       
       // get all the class "btn..." in the DOM
        const div = document.getElementById("myDIV");
        var nodelist = div.getElementsByTagName('button');
        var urls = [];
        var ids = [];
        var demoNum = 'demo';
        
        
        // loop the lenght of all the classes "btn...." to get all <a>.
        
        for(var i=0; i < nodelist.length; i++) {
           
        console.log(nodelist[i]);
        
        
          console.log(nodelist[i]);



        function setAttr(){
            var x = i + 1;
            demoNum = demoNum+x.toString();
            list = console.log(demoNum);

        };

            // onClick Download btn to get url and pass it to js
          
          nodelist[i].onclick = function(){Clicked()};
          function Clicked(){
            console.log("clicked");
            setAttr();
        };




          urls.push(nodelist[i]['title']);
        // append all id values in ids list
        ids.push(nodelist[i]['id']);
             
        };
        // Remove the empty " " index from the urls array
        //ids = ids.filter(item => item);

        //log the arrays in the console
        console.log(urls);
        console.log(ids);
        
    

   

    



