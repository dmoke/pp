//https://www.codewars.com/kata/56f78a42f749ba513b00037f/solutions/javascript
function rolldiceSumProb(sum, dice) {
  function ways(remainingSum, remainingDice) {
    if (remainingDice === 0 && remainingSum === 0) {
      return 1;
    }

    if (remainingSum < 0 || remainingDice === 0) {
      return 0;
    }

    let count = 0;

    for (let i = 1; i <= 6; i++) {
      count += ways(remainingSum - i, remainingDice - 1);
    }

    return count;
  }

  const successfulWays = ways(sum, dice);
  const totalWays = 6 ** dice;

  return successfulWays / totalWays;
}
console.log(rolldiceSumProb(8, 2));



// function rolldiceSumProb(arr, totalSides){
//     if (arr<totalSides || arr>totalSides*6) return 0;
//     if (totalSides===0) return 1;
//     let p = 0;
//     for (let i=1; i<=6; i++) p += rolldiceSumProb(arr-i, totalSides-1);
//     return p/6;
// }