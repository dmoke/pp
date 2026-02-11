/*

Create a function which compares two probabilities,
 returning true if the first one is most likely
  otherwise false.

For this exercise probability is expressed as
 two numbers separated by a colon e.g.
  a probability of 1 in 3 will be 1:3.

*/

let mostLikely = (prob1, prob2) =>
  Number(prob1.split(":")[0]) / Number(prob1.split(":")[1]) >
  Number(prob2.split(":")[0]) / Number(prob2.split(":")[1]);

console.log(mostLikely("2:8", "13:100"));

//mostLikely=(a,b,[c,d]=a.split`:`,[e,f]=b.split`:`)=>c/d>e/f
