//https://www.codewars.com/kata/5868b2de442e3fb2bb000119

function closest(strng) {
  if (strng === "") return [];
  let weights = strng
    .split(" ")
    .map((w) => w.split("").reduce((acc, nxt) => acc + Number(nxt), 0));
  let nums = strng.split(" ").map(Number);

  let relations = {};
  for (let i = 0; i < weights.length; i++) {
    for (let j = i + 1; j < weights.length; j++) {
      let diff = Math.abs(weights[i] - weights[j]);
      if (
        !relations[diff] ||
        (weights[relations[diff][0]] > weights[i] &&
          weights[relations[diff][1]] >= weights[j]) ||
        (weights[relations[diff][0]] >= weights[i] &&
          weights[relations[diff][1]] > weights[j])
      ) {
        relations[diff] = [i, j];
      }
    }
  }
  let r = relations[Object.keys(relations)[0]];

  let minWaight = Math.min(weights[r[0]], weights[r[1]]);
  let minWaightIndex = weights.indexOf(minWaight);
  let minWaightValue = nums[minWaightIndex];

  let maxWaight = Math.max(weights[r[0]], weights[r[1]]);

  let maxWaightIndex = weights.indexOf(maxWaight);
  if (minWaight === maxWaight) maxWaightIndex = r[1];
  let maxWaightValue = nums[maxWaightIndex];

  return [
    [minWaight, minWaightIndex, minWaightValue],
    [maxWaight, maxWaightIndex, maxWaightValue],
  ];
}

// by their indexes in the string if they have the same weights

let strng = "239382 162 254765 182 485944 134 468751 62 49780 108 54";

console.log(closest(strng));

/*

const closest = strng => {
  if (!strng) return [];
  
  const getNumWeight = num => [...`${num}`].reduce((acc, dgt) => acc + +dgt, 0);
  
  const nums = strng.split(/\s/).map(Number);
  const weights = nums.map(getNumWeight);
  
  let [a, b, diff] = [null, null, Infinity];
  
  for (let i = 0, len = weights.length; i < len - 1; i++) {
    for (let j = i + 1; j < len; j++) {
       const [wi, wj] = [weights[i], weights[j]];
       const d = Math.abs(wi - wj);
      
       if (d < diff || d === diff && Math.min(wi, wj) < a[0]) {
         [a, b, diff] = [[wi, i, nums[i]], [wj, j, nums[j]], d];
         b[0] < a[0] && ([a, b] = [b, a]);
       }
    }
  }
    
  return [a, b];
}

*/
