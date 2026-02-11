/*

Create a function to determine whether or not two circles are colliding.
You will be given the position of both circles in addition to their radii:

*/

export function collision(
  x1: number,
  y1: number,
  r1: number,
  x2: number,
  y2: number,
  r2: number,
): boolean {
  const hypotenuse: number = Math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2);
  return hypotenuse > r1 + r2;
}

console.log(collision(-1, 1, 6, -10.1, 1.1, 1));
