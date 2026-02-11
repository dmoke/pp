/*
Given an array of integers, find the minimum number of elements to remove from the array so
that the square root of the largest integer in the array is less or equal to the smallest number in the same array.

x = smallest integer in the array

y = largest integer in the array

Find the minimum number of elements to remove so, √y ≤ x.
*/

function minRemovals(arr) {
  arr.sort((a, b) => a - b);
  let left = 0;
  let right = 0;
  let keep = 0;
  for (right; right < arr.length; right++) {
    while (arr[left] ** 2 < arr[right]) {
      left++;
    }
    keep = Math.max(keep, right - left + 1);

    console.log({
      "arr[left]": arr[left],
      "arr[right]": arr[right],
      "length-(right-left+1)":  arr.length - keep,
    });
  }
  return arr.length - keep;
}

const arr = [1,2,3,4,5];

console.log(minRemovals(arr));
