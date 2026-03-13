// Kata: Series Slices
// Given a string of digits and a slice size n, extract all consecutive n-digit slices from the string.
// For example, the string "01234" with n=2 has the following slices: [0, 1], [1, 2], [2, 3], [3, 4]

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
