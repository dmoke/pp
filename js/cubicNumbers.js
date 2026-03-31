//https://www.codewars.com/kata/55031bba8cba40ada90011c4/solutions/javascript?filter=all&sort=newest&invalids=false
function isSumOfCubes(s) {
  let groups = [];
  for (let i = 0; i < s.length; ) {
    if (/\d/.test(s[i])) {
      let group = [];
      while (/\d/.test(s[i])) {
        group.push(s[i]);
        i++;
      }
      while (group.length > 0) {
        groups.push(group.splice(0, 3));
      }
    } else {
      i++;
    }
  }

  let result = groups.filter((group) => {
    let nums = group.map(Number);
    return nums.join("") == nums.reduce((acc, next) => acc + next ** 3, 0);
  });

  let sum = result.reduce((acc, arr) => acc + Number(arr.join("")), 0);

  return result.length > 0
    ? result
        .map((group) => Number(group.join("")))
        .concat(sum)
        .concat("Lucky")
        .join(" ")
    : "Unlucky";
}

let s =
  "153000153407000407";

console.log(isSumOfCubes(s));