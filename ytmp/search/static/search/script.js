
function load(){

    document.getElementById('demo').onclick = function(){videoURL};
    function videoURL(){
        console.log("Clicked");
    };

};
window.onload = load;


