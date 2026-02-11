/*all the ways to populate array*/

let array1 = [1, 2, 3];
console.log("array literal:", array1);

let array2 = new Array(10).fill(2, 4, 5);
console.log("new Array pre-filled:", array2);

let array3 = new Array(1, 2, 3);
console.log("new Array with elements:", array3);

let array35 = Array.from(new Set([12, 2, 3, 3, 2, 2, 2]));
console.log("35 new Array from set:", array35);

let array4 = Array.from(["2"]);
console.log("Array.from from iterable:", array4);

let array5 = Array.from({ length: 12 }, (element, index) => index / 2);
console.log("Array.from generated:", array5);

let array51 = Array.from([4, 5, 6, 7, 7], (element, index) => element * 2);
console.log("51 Array.from g*2:", array51);

let array6 = Array.of(5);
console.log("Array.of single element:", array6);

let array7 = Array.of(1, 2, 3);
console.log("Array.of multiple elements:", array7);

let array8 = [...array1];
console.log("Spread from array:", array8);

let array9 = [..."abc"];
console.log("Spread from string:", array9);
let number = 10;
let array91 = [...new Array(number).keys()];
console.log("91Spread from string:", array91);

let array10 = [];
array10.push(1, 2, 3);
console.log("Push dynamically:", array10);

let array11 = [];
for (let i = 0; i < 5; i++) {
  array11.push(i);
}
console.log("Loop-based population:", array11);

let array12 = [...Array(5)].map((_, i) =>_);
console.log("Map on placeholder array:", array12);

let array122 = Array(5).map((_, i) => i * 2);
console.log("122 Map on placeholder array:", array122);

let array13 = new Uint8Array([1, 2, 3, 4]);
console.log("Typed array:", array13);

let array14 = [1, [2, 3], [4, [5]]].flat(Infinity);
console.log("Flatten nested arrays:", array14);
