function deleteNth(arr, n) {
  [...new Set(arr)].forEach((e) => {
    let occurrences = arr.reduce((acc, next) => (next === e ? acc + 1 : acc));
    if (n < occurrences) arr = arr
        .join("")
        .replace(new Array(occurrences).fill(e), new Array(n).fill(e))
        .split("");
  });
  return arr;
}

console.log(deleteNth([1, 1, 3, 3, 7, 2, 2, 2, 2], 1));
