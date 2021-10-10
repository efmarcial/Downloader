

    var demo =document.getElementById('demo');
    demo.onclick = function(){videoURL()};
    function videoURL(){
        console.log("Clicked");
    };

    var mybutton = document.form1.myButton;
    var numberClicked = 0;

    function myButtonClicked() {
        console.log("Clicked button")
    };

    mybutton.addEventListener("'click", myButtonClicked);



