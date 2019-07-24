console.log("hello world");
var x = document.getElementById("dance");
var st =0;

function switchColor(){
  if (st==0){
      x.setAttribute("style", "color:grey");
      st = 1;
  }
  else {
    st=0;
      x.setAttribute("style", "color:white");
  }


}

  var image = document.getElementById('myImage');
  var images = ["cute.jpg", "badbunny.jpg", "facemask.jpg", "jerry.png", "rose.png", "seatbelt.jpg", "pic1.jpg", "selfie.jpg"]
  var num = 0
function changeImage() {
  image.src = images[num];
  num++
  if(num>=8){
    num=0
  }
}
var fonts = ["'Dancing Script', cursive", "'Bungee Outline', cursive", "'Fascinate', cursive", "'Butterfly Kids'", "'Londrina Shadow'", "'Source Code Pro', monospace"];
var posNum = 0;
var text = document.getElementById("dance");

function switchFont(){
  console.log("fdsf")
  text.style.fontFamily = fonts[posNum];
  posNum++;
  if(posNum>= fonts.length){
    posNum = 0;
  }
}






function zoomin(){
        var mouseImg = document.getElementById("mouse");
        var currWidth = mouseImg.clientWidth;
        console.log("HELP")
        if(currWidth >= 800){
          console.log("alert")
            alert("Maximum zoom-in level reached.");
        } else{
          console.log("add")
            mouseImg.style.width = (currWidth + 50) + "px";
        }
    }
    function zoomout(){
        var mouseImg = document.getElementById("mouse");
        var currWidth = mouseImg.clientWidth;
        if(currWidth <= 50){
          console.log("alert")
            alert("Maximum zoom-out level reached.");
        } else{
          console.log("sub")
            mouseImg.style.width = (currWidth - 50) + "px";
        }
    }
