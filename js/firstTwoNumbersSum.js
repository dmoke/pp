/**
 * This JavaScript function is an implementation of the "Two Sum" problem from the LeetCode platform.
 *
 * The Two Sum problem is a common coding interview question. The problem is as follows:
 *
 * Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
 *
 * You may assume that each input would have exactly one solution, and you may not use the same element twice.
 *
 * Here's a function named `sumPairs` that solves this problem. Given an array of integers `ints` and a target sum `s`,
 * it returns an array of two integers that add up to `s`. If no such pair exists, the function returns `undefined`.
 *
 * This function uses a brute-force approach, where it iterates through all possible pairs of numbers in the array.
 * For each pair, it checks if the sum of the two numbers equals `s`. If it does, it checks if the pair is the first
 * one to sum up to `s` or if it is an earlier pair that had a later index in the array.
 *
 * The function returns the first pair of numbers that sum up to `s` it finds.
 */

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
