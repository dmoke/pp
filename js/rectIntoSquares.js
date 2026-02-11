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



console.log(sqInRect(20,14));