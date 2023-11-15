#!/usr/bin/node
if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
  console.log('Missing number of occurrences');
} else {
  let n = process.argv[2];
  while (n > 0) {
    console.log('C is fun');
    n -= 1;
  }
}
