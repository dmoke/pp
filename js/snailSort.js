function snail(arr) {
  if (!arr || arr.length === 0 || arr[0].length === 0) return [];

  const n = arr.length;
  let result = [];


  let row = 0;
  let col = 0;

  let top = 0,
      bottom = n - 1,
      left = 0,
      right = n - 1;

  let direction = "right";

  let total = n * n;
  for (let i = 0; i < total; i++) {
    result.push(arr[row][col]);

    if (direction === "right") {
      if (col < right) col++;
      else {
        direction = "down";
        top++;
        row++;
      }
    } else if (direction === "down") {
      if (row < bottom) row++;
      else {
        direction = "left";
        right--;
        col--;
      }
    } else if (direction === "left") {
      if (col > left) col--;
      else {
        direction = "up";
        bottom--;
        row--;
      }
    } else if (direction === "up") {
      if (row > top) row--;
      else {
        direction = "right";
        left++;
        col++;
      }
    }
  }

  return result;
}
let arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]];

console.log(snail(arr));


//const snail = array => array.length ? array.shift().concat(array.map(x => x.pop()), snail(array.reverse().map(x => x.reverse()))) : array
