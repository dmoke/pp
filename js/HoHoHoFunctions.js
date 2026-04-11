//https://www.codewars.com/kata/52af1f150fcae8d33d0009bc/solutions/java
function ho(func="") {
  return func =="" ? "Ho!"+ func : "Ho "+ func;
}

let result = ho(ho(ho()));
console.log(result);
