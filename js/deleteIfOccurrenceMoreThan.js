function deleteNth(arr, n) {
  const seen = {};
  return arr.filter((x) => {
    seen[x] = (seen[x] || 0) + 1;
    return seen[x] <= n;
  });
}


console.log(deleteNth([20,37,20,21], 1));
