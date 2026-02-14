function deleteNth(arr, n) {
  [...new Set(arr)].forEach((e) => {
    let occurrences = arr
      .sort((a, b) => a - b)
      .reduce((acc, next) => (next === e ? acc + 1 : acc), 0);

    if (n < occurrences)
      arr = arr
        .join(",")
        .replace(
          new Array(occurrences).fill(e).join(","),
          new Array(n).fill(e).join(","),
        )
        .split(",")
        .map(Number);
  });
  return arr;
}

console.log(deleteNth([20,37,20,21], 1));
