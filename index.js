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
