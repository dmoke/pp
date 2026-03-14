// # everytime you press the button it sends you an array of one-letter strings representing directions
// # to walk (eg. ['n', 's', 'w', 'e']). You always walk only a single block for each letter (direction)
// # and you know it takes you one minute to traverse one city block, so create a function that will return
// # true if the walk the app gives you will take you exactly ten minutes
// # and will, of course, return you to your starting point

let isValidWalk = (walk) =>
  walk.length == 10 &&
  walk.filter((e) => e == "n").length == walk.filter((e) => e == "s").length &&
  walk.filter((e) => e == "e").length == walk.filter((e) => e == "w").length;

console.log(isValidWalk(["n", "s", "n", "s", "n", "s", "n", "s", "n", "s"]));

