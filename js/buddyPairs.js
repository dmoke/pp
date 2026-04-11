//https://www.codewars.com/kata/59ccf051dcc4050f7800008f/train/javascript

function buddy(start, limit) {
  function sumDivisors(num) {
    let sum = 1;

    for (let i = 2; i * i <= num; i++) {
      if (num % i === 0) {
        sum += i;
        if (i !== num / i) sum += num / i;
      }
    }

    return num > 1 ? sum : 0;
  }

  for (let i = start; i <= limit; i++) {
    let m = sumDivisors(i) - 1;

    if (m <= i) continue;

    if (sumDivisors(m) === i + 1) {
      return [i, m];
    }
  }

  return "Nothing";
}


console.log(buddy(310, 2755));

// function buddy(start, limit) {
//   for (let i = start; i <= limit; i++) {
//     let s = (arr) => arr.reduce((a, n) => a + n, 0);

//     let startDivisors = [...Array(i)]
//       .map((_, idx) => idx)
//       .filter((e) => e !== 0 && e !== i && i % e === 0);

//     let m = s(startDivisors) - 1;

//     if (m <= i) continue;

//     let mDivisors = [...Array(m)]
//       .map((_, idx) => idx)
//       .filter((e) => e !== 0 && e !== m && m % e === 0);

//     if (s(mDivisors) === i + 1) {
//       return [i, m];
//     }
//   }

//   return "Nothing";
// }
