


var aElement = document.getElementsByTagName('a');
var lenght = aElement.length;

for (var i=0; i < lenght; i++){
    //console.log(aElement[i]);
}



//Psuedo Code:
//TODO: get all <a> tags and count them using lenght()
const aElem = document.getElementsByTagName('a');
var lenght = aElem.length;

/*
TODO: for loop all the 'a' tags to change the
        id's of all the tags.
*/

for (i=0; i < lenght; i++){
    aElem.id = 'demo'+i;
}

for(i=0; i < length; i++){
    console.log(aElem[i]);
}