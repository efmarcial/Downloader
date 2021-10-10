

    var demo =document.getElementById('demo');
    demo.onclick = function(){videoURL()};
    function videoURL(){
        console.log("Clicked");
    };

   
    var myForm = document.form1;

    function btnCheckFormClick(e) {
        console.log("Clicked Button");
    };

    myForm.myButton.addEventListener("click", btnCheckFormClick);



