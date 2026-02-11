// TODO: In how many different ways can this array be arranged?

/*
findCombos([[1, 2], [3]]); 
// 6 -> [[1, 2], [3]], [[1, 3], [2]], 
//      [[2, 1], [3]], [[2, 3], [1]],
//      [[3, 1], [2]], [[3, 2], [1]]
*/

function findCombos(array) {
  const flat = array.flat(Infinity);
  const factorial = n => (n <= 1 ? 1 : n * factorial(n - 1));
  const freq = flat.reduce((m, v) => {
    m[v] = (m[v] || 0) + 1;
    return m;
  }, {});
  let denominator = 1;
  for (const count of Object.values(freq)) {
    denominator *= factorial(count);
  }
  return factorial(flat.length) / denominator;
}

let a = [1, 2, 2];
console.log(findCombos(a));
