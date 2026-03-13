// Kata: Rectangle into Squares
// Given dimensions of a rectangle (length and width), decompose it into the smallest possible squares
// by recursively cutting off the largest square that fits until the rectangle is completely divided.
// Returns the list of square sizes, or null if the rectangle is already a square.

function sqInRect(lng, width) {
  if (lng === width) return null;

  let squares = [];
  while (lng > 0 && width > 0) {
    if (lng > width) {
      squares.push(width);
      lng -= width;
    } else {
      squares.push(lng);
      width -= lng;
    }
  }
  return squares;
}

console.log(sqInRect(20, 14));
