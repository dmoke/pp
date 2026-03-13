/*
 * This is a basic Kata about how to delete an element from an array if its occurrence is more than a specified limit.
 * The name of the Kata is “deleteNth”.
 * The purpose of this Kata is to learn how to manipulate arrays in JavaScript.
 *
 */

function deleteNth(arr, n) {
  const seen = {};
  return arr.filter((x) => {
    seen[x] = (seen[x] || 0) + 1;
    return seen[x] <= n;
  });
}

// Example usage:
console.log(deleteNth([20, 37, 20, 21], 1)); // returns [20, 37, 21]
