console.log("hello world");


var goals = ["eat","sleep","dance","repeat"];
var pos = 0;
var loc = document.getElementById("lifeGoal");
function changegoal() {
  loc.innerHTML = goals[pos];
  pos++;
  if (pos >= goals.length){
    pos=0;
  }
}
