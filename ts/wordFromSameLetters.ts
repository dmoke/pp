export const grabscrab = (anagram: string, dictionary: string[]) =>
  dictionary.filter(
    (w) => [...w].sort().join("") === [...anagram].sort().join(""),
  );

console.log(grabscrab("oolp", ["donkey", "pool", "horse", "loop"]));
