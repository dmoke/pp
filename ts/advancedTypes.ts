//https://www.codewars.com/kata/5916c87540ef95d8e1000007/solutions/typescript?filter=all&sort=best_practice&invalids=false
export function intersect<T extends Object, U extends Object>(
  first: T,
  second: U,
): T & U {
  let result = <T & U>{};
  let fset = new Set(Object.keys(<any>first));
  let sset = new Set(Object.keys(<any>second));
  const intersection = new Set([...fset].filter((x) => sset.has(x)));

  for (let same of [...intersection]) {
    (<any>result)[same] = (<any>first)[same];
  }

  return result;
}

var obj1 = { a: 1 };
var obj2 = { a: 2, b: 2 };
var intersection = intersect(obj1, obj2);

console.log(intersection);



// export function intersect<T extends Object, U extends Object>(first: T, second: U): T & U {
//   let result = <T & U>{}

//   for (let [key, value] of Object.entries(first)) {
//     if (key in second) Object.assign(result, { [key]: value })
//   }

//   return result
// }



// export function intersect<T, U>(first: T, second: U): T & U {
//     let result = <T & U>{};
    
//     for (let key in first) {
//       if(second.hasOwnProperty(key)) {
//         (<any>result)[key] = (<any>first)[key];
//       }
//     }
    
//     return result;
// }