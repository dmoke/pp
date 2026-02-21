function sumPairs(ints, s) {
  let rightBound = ints.length;
  let earliestSecond = null;
  let result;

  for (let first = 0, len = ints.length; first < len; first++) {
    for (let second = first + 1; second < rightBound; second++) {
      if (ints[first] + ints[second] === s) {
        if (earliestSecond === null || second < earliestSecond) {
          earliestSecond = second;
          rightBound = second;
          result = [ints[first], ints[second]];
        }
      }
    }
  }

  return result;
}


console.log(sumPairs([1, 4, 8, 7, 3, 15], 8));
