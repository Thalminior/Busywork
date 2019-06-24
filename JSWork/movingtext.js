/*
Write a JavaScript program to scroll/rotate a string
 in direction by periodically removing one letter from the end of the string and attaching it to the other
idea taken from w3scools
*/
window.onload = MAIN


// variables


// TODO build button to make text scroll

function scroll(target)
{
        textIn = document.getElementById(target).innerHTML;
        var newText = textIn.concat(" ") // add space at end of line

    setInterval(function(){

        
        newText = newText[textIn.length - 1] + newText.substring(0, newText.length - 1);
        // console.log(newText);
        document.getElementById(target).innerHTML = newText;
    
    },175);
    
}




// this is where it all runs from
function MAIN(){
    

    scroll("scrollLeft")
    
}