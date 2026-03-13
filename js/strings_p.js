// Kata: Longest Unique Characters
// Given two strings, combine all unique characters from both strings and return them sorted alphabetically.

function longest(s1, s2) {
  return [...new Set(s1 + s2)].sort().join("");
}

console.log(longest("asgfdbad", "dcwedasda"));
