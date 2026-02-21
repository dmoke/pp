// function partsSums(ls) {
//   if (ls.length === 0) return [0];
//   ls.push(0);
//   return ls.map((_, index, array) =>
//     array.slice(index).reduce((p, n) => (p += n)),
//   );
// }

function partsSums(ls) {
  const result = new Array(ls.length + 1);
  let total = 0;

  for (let i = 0; i < ls.length; i++) {
    total += ls[i];
  }

  for (let i = 0; i < ls.length; i++) {
    result[i] = total;
    total -= ls[i];
  }

  result[ls.length] = 0;
  return result;
}

console.log(partsSums([0, 1, 3, 6, 10]));
