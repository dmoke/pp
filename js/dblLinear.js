//https://www.codewars.com/kata/5672682212c8ecf83e000050
function dblLinear(n) {
  let list = [1];
  let indexX = 0;
  let indexY = 0;

  while (list.length <= n) {
    let x = 2 * list[indexX] + 1;
    let y = 3 * list[indexY] + 1;

    let next = Math.min(x, y);
    list.push(next);

    if (next === x) indexX++;
    if (next === y) indexY++;
  }

  return list;
}


console.log(dblLinear(10));
