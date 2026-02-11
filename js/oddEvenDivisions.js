const oddity = (n) =>
  Array.from({ length: Math.floor(n / 2) }, (_, i) => i + 1)
    .concat(n)
    .filter((e) => n % e === 0).length %
    2 ===
  0
    ? "even"
    : "odd";

console.log(oddity(120000001));



//const oddity = (n) =>
//  Number.isInteger(Math.sqrt(n)) ? "odd" : "even";
