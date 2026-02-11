const alphabet: any = {
  I: 1,
  IV: 4,
  V: 5,
  VI: 6,
  VII: 7,
  VIII: 8,
  IX: 9,
  X: 10,
  L: 50,
  C: 100,
  D: 500,
  M: 1000,
};

export function solution(roman: string): number {
  let array: any = [...roman];

  array = array.map((element: any, index: any, arr: any) => {
    if (Object.keys(alphabet).includes(element + arr[index + 1])) {
      let tmp = arr[index + 1];
      arr.splice(index + 1, 1);
      return element + tmp;
    } else return element;
  });

  return array.reduce((acc: any, next: any) => {
    return acc + alphabet[next];
  }, 0);
}

console.log(solution("MDCLXVI"));
