function series_slices(digits, n) {
  let arr = digits.split("").map(Number);
  let result = [];
  for (let i = 0; i < arr.length; i += 1) {
    result.push(arr.slice(i, i + n));
    if (i + n == arr.length) break;
  }

  return result;
}

console.log(series_slices("01234", 2));
