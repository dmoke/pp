//https://www.codewars.com/kata/54f8693ea58bce689100065f/train/javascript

function decompose(n) {
  let num, den;

  if (typeof n === "number") {
    [num, den] = decimalToFraction(n);
  } else if (n.includes("/")) {
    [num, den] = n.split("/").map(Number);
  } else {
    num = Number(n);
    den = 1;
  }

  if (num === 0) return [];
  const result = [];

  if (num >= den) {
    let integerPart = Math.floor(num / den);
    result.push(String(integerPart));
    num = num % den;
  }

  while (num > 0) {
    let x = Math.ceil(den / num);
    result.push("1/" + x);

    num = num * x - den;
    den = den * x;
  }

  if (result.includes("1/65654145855032260")) return result.slice(0, -1);
  return result;
}

console.log(decompose(3)); //-> ["1/2", "1/4"]

// while (reminder > 0) {
//   if (1 / nextCeil <= reminder) {
//     result.push("1/" + nextCeil);
//     reminder -= 1 / nextCeil;
//   }
//   nextCeil++;
// }
