// Write a function that will accept a jumble of letters as well as a dictionary,
//  and output a list of words that the pirate might have meant.

// For example:

// grabscrab( "ortsp", ["sport", "parrot", "ports", "matey"] )
// Should return ["sport", "ports"].

// Return matches in the same order as in the dictionary. Return an empty array if there are no matches.

function grabscrab(anagram, dictionary) {
  return dictionary.filter(
    (word) => [...word].sort().join() === [...anagram].sort().join(),
  );
}

let res = grabscrab("ainstuomn", ["mountains", "hills", "mesa"]);

console.log(res);
