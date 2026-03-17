// function accepts two integer arrays of equal length
// compares the value each member in one array to the corresponding member in the other
// squares the absolute value difference between those two values
// and returns the average of those squared absolute value difference between each member pair.
const solution = function (firstArray, secondArray) {
  return (
    firstArray
      .map((val, index) => Math.abs(secondArray[index] - val) ** 2)
      .reduce((p, n) => p + n) / firstArray.length
  );
};

console.log(solution([1, 2, 3], [4, 5, 6]));
Math.pow



//const solution = (first, sec) => first.reduce((a, el, i) => a + Math.abs(el - sec[i])**2, 0)/first.length;
