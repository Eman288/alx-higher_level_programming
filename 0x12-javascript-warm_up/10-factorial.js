#!/usr/bin/node
function Factorial (n) {
  if (n === 1 || isNaN(n)) {
    return 1;
  }
  return Factorial(n - 1) * n;
}
const n = Factorial(process.argv[2]);
console.log(n);
